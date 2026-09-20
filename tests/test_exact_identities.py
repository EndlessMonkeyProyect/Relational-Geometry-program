import numpy as np


def test_order_four_J():
    J=np.array([[0.,-1.],[1.,0.]])
    I=np.eye(2)
    assert np.allclose(J@J,-I)
    assert np.allclose(np.linalg.matrix_power(J,4),I)


def test_ns_material_split():
    w=np.array([1.2,-0.7,2.3])
    dw=np.array([0.4,1.1,-0.2])
    q=np.linalg.norm(w); xi=w/q; v=dw/q
    a=xi@v; b=v-a*xi
    assert abs(xi@b)<1e-14
    assert np.allclose(v,a*xi+b)
    assert np.allclose(v@v,a*a+b@b)


def test_transverse_evolution_identity_finite_vectors():
    # Algebraic consistency at one generic instant using an orthonormal xi,b.
    xi=np.array([1.,0.,0.]); b=np.array([0.,0.3,-0.2]); a=1.4
    Y=np.array([0.7,-0.1,0.8])
    B=b@b
    Da=B+xi@Y
    Db=Y-Da*xi-a*b
    P=np.eye(3)-np.outer(xi,xi)
    assert np.allclose(P@Db,P@Y-a*b)


def test_binary_first_heritage_novelty_is_four():
    seen=set()
    first=None
    for e in range(1,15):
        n=2**e-1
        primes=set(); d=2; m=n
        while d*d<=m:
            while m%d==0:
                primes.add(d); m//=d
            d+=1
        if m>1: primes.add(m)
        if primes & seen and primes-seen and first is None:
            first=e
        seen |= primes
    assert first==4
