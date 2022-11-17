# zad 8 punkt a generuje za pomoca randomchose 100 probek dla ktorych mamy szanse na tak 0,1 lub 0,5 lub 0.9 i sprawdzam
# w wygenerowanej tablicy ile wygenerowało sie danych przykładów

# pkt b to samo co w a tylko dla sznsy = 0.1 i robie to 50 razy zliczajac ile w każdym razie było yesów
import numpy as np
import random
import matplotlib.pyplot as plt

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



x_10 = []
x_50 = []
x_90 = []

for a in range(100):
    x_10.append(random.choice(occurrences_10))
    x_50.append(random.choice(occurrences_50))
    x_90.append(random.choice(occurrences_90))

print(x_90)
print('ilość wartości 1 po 100 losowaniach dla sznsy wylosowania 1 równej 90% :',sum(x_90))
print(x_50)
print('ilość wartości 1 po 100 losowaniach dla sznsy wylosowania 1 równej 50% :',sum(x_50))
print(x_10)
print('ilość wartości 1 po 100 losowaniach dla sznsy wylosowania 1 równej 10% :',sum(x_10))



#pkt 2
x_10 = []
x_10_2 = []
for b in range(50):
    for a in range(100):
        x_10.append(random.choice(occurrences_10))
    x_10_2.append(x_10)
    x_10 = []
x_10_2 = np.array(x_10_2)

print('\n ilość wartości 1 po 100 losowaniach dla sznsy wylosowania 1 równej 10% (powtórzone 50 razy): \n',np.sum(x_10_2,axis=1))
print(max(np.sum(x_10_2,axis=1)))
plt.hist(np.sum(x_10_2,axis=1), bins=30)
plt.xticks([a for a in range(int(min(np.sum(x_10_2,axis=1))),int(max(np.sum(x_10_2,axis=1))))])
plt.xlabel('ilość wartosci jeden przy 100 losach')
plt.ylabel('ilość powtórzeń danej wartości')
plt.show()
