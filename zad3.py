import matplotlib.pyplot as plt

def bayes(pc,pcl,pl):
    return (pc*pcl)/pl


pc = [0.01, 0.03, 0.04, 0.1]
pl = [0.06, 0.03, 0.020, 0.050]
pcl = [0.004, 0.003, 0.002, 0.001]



plt.figure()
plt.title('P(l) = 0.001, P(l|c) = 0.01')
plt.ylabel('P(c|l)')
plt.xlabel('P(c)')

for i in pc:
    plt.plot([i,i],[0,bayes(i,0.001,0.01)])


plt.figure()
plt.title('P(c) = 0.1, P(l|c) = 0.01')
plt.ylabel('P(c|l)')
plt.xlabel('P(l)')
for i in pcl:
    plt.plot([i,i],[0,bayes(0.1,i,0.01)])

plt.figure()
plt.title('P(c) = 0.1, P(l) = 0.001')
plt.ylabel('P(c|l)')
plt.xlabel('P(l|c)')

for i in pcl:
    plt.plot([i,i],[0,bayes(0.1,0.001,i)])

plt.show()

#ponieważ licznik musi byc mniejszy od mianownika w równaniu bayesa
#czyli (p(c|l)*p(c)> p(l))) inaczej prawdopodobienstwo wychodzi >=1