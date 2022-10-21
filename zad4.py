import matplotlib.pyplot as plt

class bayes_extended():
    def bayes1(self,co_poczym:str,sprawdzenie_pies:str,sprawdzenie_alarm:str ,p_alarm:float=0.0,p_pies:float=0.0,
               p_alarm_wlamanie:float=0.0,p_pies_wlamanie:float=0.0,
               p_wlamania:float=0.0):
        self.wyjscie1 = 0
        self.wyjscie2 = 0
        self.wyjscie3 = 0

        if sprawdzenie_alarm== 'tak':
            self.wyjscie1 = (p_wlamania*p_alarm_wlamanie)/p_alarm
        elif sprawdzenie_alarm == 'nie':
            self.wyjscie1 = (p_wlamania*(1-p_alarm_wlamanie))/(1-p_alarm)
        elif sprawdzenie_alarm == 'brak':
            self.wyjscie1 = None


        if sprawdzenie_pies == 'tak':
            self.wyjscie2 = (p_wlamania * p_pies_wlamanie) / p_pies
        elif sprawdzenie_pies  == 'nie':
            self.wyjscie2 = (p_wlamania * (1 - p_pies_wlamanie)) / (1 - p_pies)
        elif sprawdzenie_pies  == 'brak':
            self.wyjscie2 = None

        if co_poczym == 'piesalarm':
            if sprawdzenie_alarm == 'tak' and sprawdzenie_pies == 'tak':
                self.wyjscie3 = (self.wyjscie2 * p_alarm_wlamanie) / p_alarm
            elif sprawdzenie_alarm == 'tak' and sprawdzenie_pies == 'nie':
                self.wyjscie3 = (self.wyjscie2 * (1 - p_alarm_wlamanie)) / (1 - p_alarm)
            elif sprawdzenie_alarm == 'nie' and sprawdzenie_pies == 'tak':
                self.wyjscie3 = (self.wyjscie2 * p_alarm_wlamanie) / p_alarm
            elif sprawdzenie_alarm == 'nie' and sprawdzenie_pies == 'nie':
                self.wyjscie3 = (self.wyjscie2 * (1 - p_alarm_wlamanie)) / (1 - p_alarm)

        elif co_poczym == 'alarmpies':
            if sprawdzenie_alarm == 'tak' and sprawdzenie_pies  == 'tak':
                self.wyjscie3 = (self.wyjscie1 * p_pies_wlamanie) / p_pies
            elif sprawdzenie_alarm == 'tak' and sprawdzenie_pies  == 'nie':
                self.wyjscie3 = (self.wyjscie1 * (1 - p_pies_wlamanie)) / (1 - p_pies)
            elif sprawdzenie_alarm == 'nie' and sprawdzenie_pies == 'tak':
                self.wyjscie3 = (self.wyjscie1 * p_pies_wlamanie) / p_pies
            elif sprawdzenie_alarm == 'nie' and sprawdzenie_pies == 'nie':
                self.wyjscie3 = (self.wyjscie1 * (1 - p_pies_wlamanie)) / (1 - p_pies)

        if sprawdzenie_alarm  == 'brak' and sprawdzenie_pies  == 'brak':
            self.wyjscie3 = p_wlamania
        elif sprawdzenie_alarm  == 'tak' and sprawdzenie_pies  == 'brak':
            self.wyjscie3 = self.wyjscie1
        elif sprawdzenie_alarm  == 'brak' and sprawdzenie_pies  == 'tak':
            self.wyjscie3 = self.wyjscie2
        elif sprawdzenie_alarm  == 'nie' and sprawdzenie_pies  == 'brak':
            self.wyjscie3 = self.wyjscie1
        elif sprawdzenie_alarm  == 'brak' and sprawdzenie_pies  == 'nie':
            self.wyjscie3 = self.wyjscie2


lista = ['tak','nie','brak']
zad4 = bayes_extended()
zad4.bayes1('alarmpies','tak','tak',0.01,0.5,0.8,0.98,0.002)

x = []
tab_pomoc = ['a-tak,p-tak','a-tak,p-nie','a-tak,p-brak','a-nie,p-tak','a-nie,p-nie','a-nie,a-brak',
             'a-brak,p-tak','a-brak,p-nie','a-brak,p-brak']
plt.figure()
for a in lista:
    for b in lista:
        zad4.bayes1('alarmpies', a, b, 0.01, 0.5, 0.8, 0.98, 0.002)
        x.append(zad4.wyjscie3)

for a in range(len(x)):
    plt.plot([tab_pomoc[a], tab_pomoc[a]], [0, x[a]], )

plt.xticks(rotation=20)
print(x)

x = []
plt.figure()
for a in lista:
    for b in lista:
        zad4.bayes1('piesalarm', a, b, 0.01, 0.5, 0.8, 0.98, 0.002)
        x.append(zad4.wyjscie3)

for a in range(len(x)):
    plt.plot([tab_pomoc[a], tab_pomoc[a]], [0, x[a]])

plt.xticks(rotation=20)
print(x)

plt.show()


# zmienne przestają być niezależne więc zmienią się
# możliwości w drugim etapie obliczeń, będzie trzeba uwzględnić
# prawdopodobienstwo szczekania psa pod wpływem alarmu i w drugą stronę
