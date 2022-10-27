import arviz as az
import pymc3 as pm
import numpy as np

ones = np.ones(7)
zeros = np.zeros(3)
occurrences1 = np.concatenate((ones, zeros))

ones = np.ones(70)
zeros = np.zeros(30)
occurrences10 = np.concatenate((ones, zeros))

ones = np.ones(700)
zeros = np.zeros(300)
occurrences100 = np.concatenate((ones, zeros))

if __name__ == '__main__':
    with pm.Model() as model:
        p1 = pm.Uniform("p1", lower=0, upper=1)
        obs1 = pm.Bernoulli("obs1", p1, observed=occurrences1)

        p10 = pm.Uniform("p10", lower=0, upper=1)
        obs10 = pm.Bernoulli("obs10", p10, observed=occurrences10)

        p100 = pm.Uniform("p100", lower=0, upper=1)
        obs100 = pm.Bernoulli("obs100", p100, observed=occurrences100)

        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)
