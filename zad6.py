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

ones = np.ones(5)
zeros = np.zeros(5)
placebo1 = np.concatenate((ones, zeros))


ones = np.ones(50)
zeros = np.zeros(50)
placebo10 = np.concatenate((ones, zeros))


ones = np.ones(500)
zeros = np.zeros(500)
placebo100 = np.concatenate((ones, zeros))

if __name__ == '__main__':
    with pm.Model() as model:
        p1 = pm.Uniform("p1", lower=0, upper=1)
        obs1 = pm.Bernoulli("obs1", p1, observed=occurrences1)
        p2 = pm.Uniform("p2", lower=0, upper=1)
        obs2 = pm.Bernoulli("obs2", p2, observed=placebo1)
        p_observed1 = pm.Deterministic("p_observed1", p1-p2)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)

    with pm.Model() as model:
        p10 = pm.Uniform("p10", lower=0, upper=1)
        obs10 = pm.Bernoulli("obs10", p10, observed=occurrences10)
        p20 = pm.Uniform("p20", lower=0, upper=1)
        obs20 = pm.Bernoulli("obs20", p20, observed=placebo10)
        p_observed10 = pm.Deterministic("p_observed10", p10 - p20)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)

    with pm.Model() as model:
        p100 = pm.Uniform("p100", lower=0, upper=1)
        obs100 = pm.Bernoulli("obs100", p100, observed=occurrences100)
        p200 = pm.Uniform("p200", lower=0, upper=1)
        obs200 = pm.Bernoulli("obs200", p200, observed=placebo100)
        p_observed100 = pm.Deterministic("p_observed100", p100 - p200)

        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)
