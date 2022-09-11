import numpy.random as np
import seaborn as sns
import matplotlib.pyplot as plt


population_size = 1000000
population = np.randint(1,10000,1000000)

number_of_samples = 10000
sample_means = np.randint(1,10000,number_of_samples)
sample_size = 31

c = np.randint(1,10000,number_of_samples)

for i in range(0,number_of_samples):
    c = np.randint(1,population_size,sample_size)
    sample_means[i] = population[c].mean()



plt.subplot(1,2,1)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,bins=int(180/5),hist = True,kde = False)
plt.title('Histogram of Sample mean',fontsize=20)
plt.xlabel('Sample mean',fontsize=20)
plt.ylabel('Count',fontsize=20)
plt.show()

plt.subplot(1,2,2)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,hist = False,kde = True)
plt.title('Density of Sample mean',fontsize=20)
plt.xlabel('Sample mean',fontsize=20)
plt.ylabel('Density',fontsize=20)
# plt.subplots_adjust(bottom=0.1, right=2, top=0.9)
plt.show()

