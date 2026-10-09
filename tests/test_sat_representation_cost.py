"""Finite positive controls for CNF interfaces and complete dense elimination.

The tiny canonicalizer searches a declared finite pool; it is not a general
polynomial-time canonicalizer. Dense elimination preserves every declared scope.
"""

import itertools
import unittest


def evaluate_cnf(clauses, assignment):
    return all(any(assignment[abs(literal)] if literal > 0
                   else not assignment[abs(literal)] for literal in clause)
               for clause in clauses)


def satisfiable(clauses, variables):
    return any(evaluate_cnf(clauses, dict(zip(variables, bits)))
               for bits in itertools.product((False, True), repeat=len(variables)))


def residual_table(clauses, internal, boundary):
    return tuple(any(evaluate_cnf(clauses, dict(zip(boundary + internal, outer + inner)))
                     for inner in itertools.product((False, True), repeat=len(internal)))
                 for outer in itertools.product((False, True), repeat=len(boundary)))


def normalized_formula(clauses):
    return tuple(sorted(set(tuple(sorted(set(clause))) for clause in clauses)))


def encode_formula(clauses, boundary):
    return repr((tuple(boundary), normalized_formula(clauses)))


def all_small_formulas():
    """All subsets of the 9 non-tautological clauses over two variables."""
    clauses = tuple(tuple(sign * variable for variable, sign in enumerate(signs, 1) if sign)
                    for signs in itertools.product((-1, 0, 1), repeat=2))
    return tuple(normalized_formula(clause for index, clause in enumerate(clauses)
                                    if mask & (1 << index))
                 for mask in range(1 << len(clauses)))


def canonical_representatives(pool, internal, boundary):
    representatives = {}
    for formula in pool:
        signature = residual_table(formula, internal, boundary)
        code = encode_formula(formula, boundary)
        key = (len(code), code)
        if signature not in representatives or key < representatives[signature][0]:
            representatives[signature] = (key, formula)
    return {signature: item[1] for signature, item in representatives.items()}


def table_index(scope, assignment):
    index = 0
    for variable in scope:
        index = 2 * index + int(assignment[variable])
    return index


def dense_clause(clause):
    scope = tuple(sorted({abs(literal) for literal in clause}))
    values = tuple(evaluate_cnf((clause,), dict(zip(scope, bits)))
                   for bits in itertools.product((False, True), repeat=len(scope)))
    return scope, values


def complete_dense_elimination(clauses, variables, order):
    """Materialize all union/message tables, retaining scopes and every step."""
    if len(set(variables)) != len(variables):
        raise ValueError("Variables must be distinct")
    if len(order) != len(variables) or set(order) != set(variables):
        raise ValueError("The order must eliminate every variable exactly once")
    if any(literal == 0 or abs(literal) not in variables
           for clause in clauses for literal in clause):
        raise ValueError("Every literal must use a declared variable")
    factors = [dense_clause(clause) for clause in clauses]
    records = []
    for variable in order:
        bucket = [factor for factor in factors if variable in factor[0]]
        factors = [factor for factor in factors if variable not in factor[0]]
        union_scope = tuple(sorted({variable}.union(*(set(scope) for scope, _ in bucket))))
        message_scope = tuple(v for v in union_scope if v != variable)
        union_values = []
        for bits in itertools.product((False, True), repeat=len(union_scope)):
            assignment = dict(zip(union_scope, bits))
            union_values.append(all(values[table_index(scope, assignment)]
                                    for scope, values in bucket))
        message_values = []
        for bits in itertools.product((False, True), repeat=len(message_scope)):
            assignment = dict(zip(message_scope, bits))
            alternatives = []
            for value in (False, True):
                assignment[variable] = value
                alternatives.append(union_values[table_index(union_scope, assignment)])
            message_values.append(any(alternatives))
        factors.append((message_scope, tuple(message_values)))
        records.append({"variable": variable, "union_scope": union_scope,
                        "message_scope": message_scope,
                        "union_values": tuple(union_values),
                        "message_values": tuple(message_values)})
    assert all(not scope for scope, _ in factors)
    return all(values[0] for _, values in factors), records


def primal_graph(clauses, variables):
    graph = {variable: set() for variable in variables}
    for clause in clauses:
        scope = {abs(literal) for literal in clause}
        for variable in scope:
            graph[variable].update(scope - {variable})
    return graph


def induced_neighborhoods(graph, order):
    graph = {v: set(neighbors) for v, neighbors in graph.items()}
    active = set(graph)
    result = []
    for variable in order:
        neighbors = graph[variable] & active
        result.append(tuple(sorted(neighbors)))
        for neighbor in neighbors:
            graph[neighbor].update(neighbors - {neighbor})
        active.remove(variable)
    return result


def induced_width(graph, order):
    return max(map(len, induced_neighborhoods(graph, order)), default=0)


class SatRepresentationCostTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pool = all_small_formulas()
        cls.internal, cls.boundary = (1,), (2,)
        cls.representatives = canonical_representatives(cls.pool, cls.internal, cls.boundary)

    def test_presentation_read_and_contextual_update(self):
        continuations = ((), ((2,),), ((-2,),), ((2,), (-2,)))
        for formula in self.pool:
            residual = residual_table(formula, self.internal, self.boundary)
            self.assertEqual(any(residual), satisfiable(formula, (1, 2)))
            for continuation in continuations:
                context = residual_table(continuation, (), self.boundary)
                updated = tuple(a and b for a, b in zip(residual, context))
                self.assertEqual(residual_table(formula + continuation,
                                                self.internal, self.boundary), updated)
                self.assertEqual(satisfiable(formula + continuation, (1, 2)), any(updated))

    def test_finite_pool_canonicalizer_is_length_lex_and_class_injective(self):
        self.assertEqual(len(self.pool), 512)
        self.assertEqual(len(self.representatives), 4)
        codes = {encode_formula(formula, self.boundary)
                 for formula in self.representatives.values()}
        self.assertEqual(len(codes), 4)
        for formula in self.pool:
            residual = residual_table(formula, self.internal, self.boundary)
            canonical = self.representatives[residual]
            code = encode_formula(formula, self.boundary)
            canonical_code = encode_formula(canonical, self.boundary)
            self.assertLessEqual((len(canonical_code), canonical_code), (len(code), code))
            self.assertEqual(residual_table(canonical, self.internal, self.boundary), residual)

    def test_finite_canonical_update_build_read_diagram(self):
        continuations = ((), ((2,),), ((-2,),), ((2,), (-2,)))
        for formula in self.pool:
            canonical = self.representatives[residual_table(formula, (1,), (2,))]
            for continuation in continuations:
                after_build = self.representatives[residual_table(formula + continuation, (1,), (2,))]
                after_update = self.representatives[residual_table(canonical + continuation, (1,), (2,))]
                self.assertEqual(after_build, after_update)
                self.assertEqual(satisfiable(after_update, (1, 2)),
                                 satisfiable(formula + continuation, (1, 2)))

    def test_named_boundary_is_part_of_the_code(self):
        self.assertNotEqual(encode_formula((), (2,)), encode_formula((), (3,)))
        self.assertNotEqual(encode_formula((), (2, 3)), encode_formula((), (3, 2)))

    def test_complete_dense_elimination_matches_all_small_cnf(self):
        for formula in self.pool:
            for order in ((1, 2), (2, 1)):
                answer, records = complete_dense_elimination(formula, (1, 2), order)
                self.assertEqual(answer, satisfiable(formula, (1, 2)))
                self.assertEqual(len(records), 2)
                graph = primal_graph(formula, (1, 2))
                scopes = induced_neighborhoods(graph, order)
                for record, scope in zip(records, scopes):
                    self.assertEqual(record["message_scope"], scope)
                    self.assertEqual(len(record["message_values"]), 2 ** len(scope))
                    self.assertEqual(len(record["union_values"]), 2 ** (len(scope) + 1))

    def test_all_four_vertex_graphs_match_full_message_and_union_sizes(self):
        variables = (1, 2, 3, 4)
        edges = tuple(itertools.combinations(variables, 2))
        for mask in range(1 << len(edges)):
            # Unary tautologies explicitly retain each isolated variable.
            clauses = tuple((v, -v) for v in variables) + tuple(
                edge for index, edge in enumerate(edges) if mask & (1 << index))
            graph = primal_graph(clauses, variables)
            for order in itertools.permutations(variables):
                answer, records = complete_dense_elimination(clauses, variables, order)
                width = induced_width(graph, order)
                self.assertTrue(answer)
                self.assertEqual(max(len(r["message_values"]) for r in records), 2 ** width)
                self.assertEqual(max(len(r["union_values"]) for r in records), 2 ** (width + 1))

    def test_optimal_width_for_small_paths_cycles_and_cliques(self):
        for size in range(3, 6):
            vertices = tuple(range(1, size + 1))
            path = tuple((v, v + 1) for v in range(1, size))
            cycle = path + ((1, size),)
            clique = tuple(itertools.combinations(vertices, 2))
            for edges, expected in ((path, 1), (cycle, 2), (clique, size - 1)):
                graph = primal_graph(edges, vertices)
                best = min(induced_width(graph, order)
                           for order in itertools.permutations(vertices))
                self.assertEqual(best, expected)
                self.assertEqual(min(2 ** induced_width(graph, order)
                                     for order in itertools.permutations(vertices)),
                                 2 ** expected)

    def test_logarithmic_width_has_polynomial_table_capacity(self):
        for exponent in range(1, 11):
            input_size = 2 ** exponent
            for coefficient in (1, 2, 3):
                width = coefficient * exponent
                self.assertEqual(2 ** width, input_size ** coefficient)
                self.assertEqual(2 ** (width + 1), 2 * input_size ** coefficient)

    def test_explicit_variable_and_order_contract(self):
        with self.assertRaises(ValueError):
            complete_dense_elimination(((1,),), (1, 2), (1, 1))
        with self.assertRaises(ValueError):
            complete_dense_elimination(((3,),), (1, 2), (1, 2))
        with self.assertRaises(ValueError):
            complete_dense_elimination(((0,),), (1,), (1,))


if __name__ == "__main__":
    unittest.main()
