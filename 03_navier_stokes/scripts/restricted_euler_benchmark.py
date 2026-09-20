"""Restricted-Euler benchmark used by the public repository.

Requires numpy and scipy.  This is a model-system computation, not a
Navier–Stokes blowup claim.
"""
import argparse
import numpy as np
from scipy.integrate import solve_ivp


def rhs(_, y):
    A = y.reshape(3, 3)
    A2 = A @ A
    return (-A2 + np.trace(A2) / 3 * np.eye(3)).ravel()


def obs(A):
    S = 0.5 * (A + A.T)
    w = np.array([A[2,1]-A[1,2], A[0,2]-A[2,0], A[1,0]-A[0,1]])
    q = np.linalg.norm(w)
    if q == 0:
        return np.nan, np.nan, np.nan, np.nan
    xi = w/q
    alpha = xi @ S @ xi
    tau = S @ xi - alpha*xi
    P = -np.trace(A @ A)/3*np.eye(3)
    beta = np.linalg.norm(tau)/alpha
    alpha_p = (xi @ P @ xi)/alpha**2
    return q, alpha, beta, alpha_p


def event(_, y):
    return np.linalg.norm(y) - 1e6

event.terminal = True

parser=argparse.ArgumentParser()
parser.add_argument('--full', action='store_true', help='run the documented 200-trajectory benchmark; default is a quick 12-trajectory smoke test')
args=parser.parse_args()
N=200 if args.full else 12

rng = np.random.default_rng(7)
rhos=[]; n=0
for _ in range(N):
    A0=rng.normal(size=(3,3)); A0-=np.trace(A0)/3*np.eye(3)
    sol=solve_ivp(rhs,(0,50),A0.ravel(),events=event,rtol=1e-10,atol=1e-12,dense_output=True,method='DOP853')
    if sol.status!=1:
        continue
    n+=1; T=sol.t_events[0][0]
    q,a,beta,ap=obs(sol.sol(T*(1-1e-4)).reshape(3,3))
    rhos.append(beta**2/(1+beta**2))

print(f"event reached in {n}/{N} trajectories")
print(f"median rho_perp at t=T(1-1e-4): {np.median(rhos):.6e}")

rng=np.random.default_rng(11)
A0=rng.normal(size=(3,3)); A0-=np.trace(A0)/3*np.eye(3)
sol=solve_ivp(rhs,(0,50),A0.ravel(),events=event,rtol=1e-11,atol=1e-13,dense_output=True,method='DOP853')
T=sol.t_events[0][0]
for frac in (0.7,0.9):
    h=1e-6*T
    q1,_,b1,_=obs(sol.sol(frac*T-h).reshape(3,3))
    q2,_,b2,_=obs(sol.sol(frac*T+h).reshape(3,3))
    _,a,b0,ap=obs(sol.sol(frac*T).reshape(3,3))
    num=np.log(b2/b1)/np.log(q2/q1)
    pred=-(1+b0*b0-ap)
    print(f"t/T={frac}: numeric={num:+.6f} predicted={pred:+.6f}")
