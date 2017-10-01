import numpy as np
import copy
import matplotlib.pyplot as plt


x=[]
y=[]
k=3

centroids=[]
prevCendroids=[]

cluster0=[]
cluster1=[]
cluster2=[]



try:
    f=open("clusters.txt","r")
    for i in range(0,150):
        data = f.readline().split(",")

        x.append(float(data[0]))
        y.append(float(data[1]))
    #print(x)
    #print(y)

finally:
    if f:
        f.close()




def init():
    global centroids
    index0=-1
    index1=-1
    index2=-1

    while(index1==index0 or index1==index2 or index0==index2):
        index0 = np.random.randint(0, 150)
        index1 = np.random.randint(0, 150)
        index2 = np.random.randint(0, 150)

    centroids.append([x[index0], y[index0]])
    centroids.append([x[index1], y[index1]])
    centroids.append([x[index2], y[index2]])



    #centroids.append([float(np.random.randint(-4, 8)), float(np.random.randint(-4, 8))])
    #centroids.append([float(np.random.randint(-4, 8)), float(np.random.randint(-4, 8))])
    #centroids.append([float(np.random.randint(-4, 8)), float(np.random.randint(-4, 8))])

    #print(centroids)



def findDistance(x, y):
    global cluster0,cluster1,cluster2,centroids
    distance = 10000000
    for i in range(0,3):
        current = np.sqrt((x - centroids[i][0]) ** 2 + (y - centroids[i][1]) ** 2)
        #print(current)
        if distance > current:
            distance = current
            clu = i
    #print(distance)
    #print(clu)


    if clu==0:
        cluster0.append([x,y])
    elif clu==1:
        cluster1.append([x,y])
    elif clu==2:
        cluster2.append([x, y])



def updateCentroids():
    global centroids,cluster0,cluster1,cluster2
    cluArray0 = np.array(cluster0)
    cluArray1 = np.array(cluster1)
    cluArray2 = np.array(cluster2)
    #for i in range(0,3):
    centroids[0][0] = cluArray0[:, 0].mean()
    centroids[0][1] = cluArray0[:, 1].mean()
    centroids[1][0] = cluArray1[:, 0].mean()
    centroids[1][1] = cluArray1[:, 1].mean()
    centroids[2][0] = cluArray2[:, 0].mean()
    centroids[2][1] = cluArray2[:, 1].mean()


    #print(centroids)




init()
while (prevCendroids != centroids):
    prevCendroids = copy.deepcopy(centroids)
    cluster0 = []
    cluster1 = []
    cluster2 = []

    for i in range(0, 150):
        findDistance(x[i], y[i])

    updateCentroids()

print centroids



xx=[]
yy=[]
colors = []
for i in range(0, len(cluster0)):
    xx.append(cluster0[i][0])
    yy.append(cluster0[i][1])
    colors.append('r')

for i in range(0, len(cluster1)):
    xx.append(cluster1[i][0])
    yy.append(cluster1[i][1])
    colors.append('g')

for i in range(0, len(cluster2)):
    xx.append(cluster2[i][0])
    yy.append(cluster2[i][1])
    colors.append('b')





area = 4**2  

plt.scatter(xx, yy, s=area, c=colors, alpha=0.5)

plt.show()
