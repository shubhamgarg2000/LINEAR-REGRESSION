
dataset=[[1,2],[2,4],[3,6],[5,10],[6,12]]
x=[i[0] for i in dataset]
y=[i[1] for i in dataset]

def train_test(x,y,train_size=0.8):
    a=int(train_size*len(x))
    x_train,x_test,y_train,y_test=x[:a],x[a:],y[:a],y[a:]
    return x_train,x_test,y_train,y_test
x_train,x_test,y_train,y_test=train_test(x,y)

def mean(a):
    sum=0
    for i in a:
        sum+=i
    return sum/len(a)
mean(x)         
def variance(a):
    sum=0
    for i in a:
        sum+=(i-a.mean())**2
    return sum/len(x)

def co_variance(x,y):
    print(x)
    sum=0
    for i in range(len(x)):
        sum+=((x[i]-mean(x)))*(y[i]-mean(y))
    return sum/(len(x)-1)

co_variance(x,y)

def coeff_consta(x,y):
    coeff=0
    print(x)
    print(y)
    for i in range(len(x)):
        print(x[i],y[i])
        print(mean(x),mean(y))
        coeff+=(x[i]-mean(x))*(y[i]-mean(y))/((x[i]-mean(x))**2)
    cons=mean(y)-coeff*mean(x)
    return coeff,cons
coeff_consta(x_train,y_train)

def simple_linear(test):
    y_list=[]
    b1,b0=0,12
    for i in range(len(test)):
        b=b0+b1*i
        y_list.append(b)
    return y_list
y_pred=simple_linear(x_test)
return y_pred

import math

def rmse(actual,pred):
    sum=0
    for i in range(0,len(actual)):
        sum+=actual[i]-pred[i]
    s_mean=sum**2/len(actual)
    print(s_mean)
    rm=math.sqrt(s_mean)
    return rm

rmse(y_test,y_pred)

import matplotlib.pyplot as plt
plt.plot(0,15)
plt.scatter(x_test,y_test)
plt.scatter(x_train,y_train)
plt.scatter(x_test,y_pred)
plt.show()
