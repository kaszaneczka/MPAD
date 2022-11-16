# zad 8 punkt a generuje za pomoca randomchose 100 probek dla ktorych mamy szanse na tak 0,1 lub 0,5 lub 0.9 i sprawdzam
# w wygenerowanej tablicy ile wygenerowało sie danych przykładów

# pkt b to samo co w a tylko dla sznsy = 0.1 i robie to 50 razy zliczajac ile w każdym razie było yesów
import numpy as np
import random

#pkt 1

ones = np.ones(90)
zeros = np.zeros(10)
occurrences_90 = np.concatenate((ones, zeros))
ones = np.ones(50)
zeros = np.zeros(50)
occurrences_50 = np.concatenate((ones, zeros))
ones = np.ones(10)
zeros = np.zeros(90)
occurrences_10 = np.concatenate((ones, zeros))

print(occurrences_90)

x_10 = []
x_50 = []
x_90 = []

for a in range(100):
    x_10.append(random.choice(occurrences_10))
    x_50.append(random.choice(occurrences_50))
    x_90.append(random.choice(occurrences_90))

print(x_90)
print(sum(x_90))

#pkt 2
x_10 = []
x_10_2 = []
for b in range(50):
    for a in range(100):
        x_10.append(random.choice(occurrences_10))
    x_10_2.append(x_10)
    x_10 = []
x_10_2 = np.array(x_10_2)

print(np.sum(x_10_2,axis=1))


