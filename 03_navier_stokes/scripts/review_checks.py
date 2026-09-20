"""Reproduce sensitivity summaries from the bundled CSV files."""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import binomtest, fisher_exact

ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'data'
ls=pd.read_csv(D/'phase4_lowest_states.csv')
k=pd.read_csv(D/'phase5_kappa_interval_means.csv')
st={(int(r.id), round(float(r.time),3)):r for r in ls.itertuples()}
print('kappa endpoint slopes:')
for r in k.itertuples():
    s1=st.get((int(r.id),round(float(r.t_start),3)))
    s2=st.get((int(r.id),round(float(r.t_end),3)))
    if s1 is not None and s2 is not None:
        k5=(s2.rho5-s1.rho5)/(2*np.log(r.q_end/r.q_start))
    else: k5=np.nan
    print(r.id, r.t_start, r.t_end, f'k7={r.kappa_bar_G:+.3f}', f'k5={k5:+.3f}')

ep=pd.read_csv(D/'phase4_episodes.csv')
err=(ep.G_int_a_dt-ep.log_q_ratio)/ep.log_q_ratio
print('relative integral-vs-endpoint errors:', np.round(err.values,3))
for lab,N,n in [('99-99.5',205,1),('99.5-99.9',185,0),('99.9-100',47,2)]:
    ci=binomtest(n,N).proportion_ci(method='wilson')
    print(lab, n, '/', N, 'Wilson95=', (ci.low,ci.high))
print('Fisher p:', fisher_exact([[2,45],[9,381]])[1])
