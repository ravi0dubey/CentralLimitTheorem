import numpy
import numpy.random as np
import seaborn as sns
import matplotlib.pyplot as plt


population_size = 1000000
#Population Array is created with values from range 1 to 10k  having 1 million elements in it
population = np.randint(1,10000,population_size)

#for population size of 1 Million we will create sample of 10k
number_of_samples = 10000

#Sample Size is 31 as we know samplesize greater than equal to 30 will make sense to have

sample_enter = True
while(sample_enter):
    sample_size = int(input("Enter Sample Size>=30 "))
    if sample_size < 30:
        print("Entered Sample Size is < 30")
    else:
        sample_enter= False

#Create Blank list of Sample Means
sample_means=[]


for i in range(0,number_of_samples):
    sample_means.append(0) #Keep on initializing sample means with 0 before it gets filled with actual sample means
    c = np.randint(1,population_size,sample_size) #Create array from Population data for sample size entered
    sample_means[i] = numpy.mean(c)  # Store means of sample picked from

#Plot Histogram  of Sample Means
plt.subplot(1,2,1)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,bins=int(180/5),hist = True,kde = False)
plt.title('Histogram of Sample mean',fontsize=20)
plt.xlabel('Sample mean',fontsize=20)
plt.ylabel('Count',fontsize=20)
plt.show()

#Plot BellCure of Sample Means based on Histogram plotted
plt.subplot(1,2,2)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
sns.distplot(sample_means,hist = False,kde = True)
plt.title('Density of Sample mean',fontsize=20)
plt.xlabel('Sample mean',fontsize=20)
plt.ylabel('Density',fontsize=20)
# plt.subplots_adjust(bottom=0.1, right=2, top=0.9)
plt.show()

