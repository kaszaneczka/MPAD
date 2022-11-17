import warnings

import arviz as az
import pymc3 as pm
import numpy as np
import warnings

warnings.filterwarnings('ignore')





if __name__ == '__main__':
    # pkt 1
    with pm.Model() as model:
        p_d = pm.Uniform("p_d", 0, 1)
        p_observed = pm.Deterministic("p_observed", 0.25 + 0.5 * p_d)
        # answers = pm.Bernoulli("answers", p_observed, observed=occurrences)
        yes_count = 70
        answers1 = pm.Binomial("answers1", 100, p_observed, observed=yes_count)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)

    with pm.Model() as model:
        p_d = pm.Uniform("p_d", 0, 1)
        p_observed = pm.Deterministic("p_observed", 0.25 + 0.5 * p_d)
        # answers = pm.Bernoulli("answers", p_observed, observed=occurrences)
        yes_count = 20
        answers1 = pm.Binomial("answers1", 100, p_observed, observed=yes_count)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)



    with pm.Model() as model:
        p_d = pm.Uniform("p_d", 0, 1)
        p_observed = pm.Deterministic("p_observed", 0.25 + 0.5 * p_d)
        # answers = pm.Bernoulli("answers", p_observed, observed=occurrences)
        yes_count = 10
        answers1 = pm.Binomial("answers1", 100, p_observed, observed=yes_count)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)

    with pm.Model() as model:
        p_d = pm.Uniform("p_d", 0, 1)
        p_observed = pm.Deterministic("p_observed", 0.25 + 0.5 * p_d)
        # answers = pm.Bernoulli("answers", p_observed, observed=occurrences)
        yes_count = 5
        answers1 = pm.Binomial("answers1", 100, p_observed, observed=yes_count)
        idata = pm.sample(2000, tune=2500)
    az.plot_trace(idata, show=True)

# dla danych w ktorych ilosc yes przyjmuje wartosci z zakresu 20 10 i 5  otrzymujemy prawdopodbienstwo w okolicy 25 procent
# oznacza to ze wspolczynnik pd nie miał dużego wplywu na obliczenia, co przekłada sie an to ze studenci musieli podawac fałszywe informacje
# albo niemalże nikt nie bierze narkotyków





    #zad 8 punkt a generuje za pomoca randomchose 100 probek dla ktorych mamy szanse na tak 0,1 lub 0,5 lub 0.9 i sprawdzam
    #w wygenerowanej tablicy ile wygenerowało sie danych przykładów

    #pkt b to samo co w a tylko dla sznsy = 0.1 i robie to 50 razy zliczajac ile w każdym razie było yesów