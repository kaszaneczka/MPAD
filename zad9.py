import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import arviz as az
import pymc3 as pm

if __name__ == '__main__':
    data = pd.read_excel('data.xlsx')
    data = data.drop(columns ='Unnamed: 0' )
    data = np.array(data)
    mini = []
    beta, alfa, r, p, se = stats.linregress(data[:,0], data[:,1])
    mini.append(min(data[:,0]))
    mini.append(max(data[:,0]))
    print(beta,alfa)



    with pm.Model() as model:
        std = pm.Uniform("std", 0, 100)
        beta = pm.Normal("beta", mu=0, sd=100)
        alpha = pm.Normal("alpha", mu=0, sd=100)
        mean = pm.Deterministic("mean", alpha + beta * data[:,0])
        obs = pm.Normal("obs", mu=mean, sd=std, observed=data[:,1])
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)



    # plt.scatter(data[:,0],data[:,1])
    # plt.plot(mini,[slope*mini[0] + intercept ,slope*mini[1] + intercept] )
    # plt.show()

    #scipy.stats.linregress(x, y=None, alternative='two-sided')[source]

    #print(data[:,1])


