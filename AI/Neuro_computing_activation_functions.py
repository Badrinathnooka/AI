import math
import numpy

def Linear(z):
    print("Activation value is ",z)
def Threshold(z):
    if(z>=0):
        print("Activation value is ",1)
    else:
        print("Activation value is ",0)
def Sigmoid(z):
    k = 1/(1+math.pow(2.17,-z))
    print("Activation value is ",k)
def Tanh(z):
    print("Activation value is ",math.tanh(z))
    
def PiecewiseLF(z):
    if(z<=-0.5):
        print("Activation value is ",-0.5)
    elif(z<0.5 and z>-0.5):
        print("Activation value is ",z)
    else:
        print("Activation value is ",0.5)
        
def Relu(z):
    if(z<0):
        print("Activation value is ",0)
    else:
        print("Activation value is ",1)


def Softmax(z):
    print("DOnt know to solve :")
    
def Signum(z):
    if(z<0):
        print("Activation value is ",-1)
    elif(z==0):
        print("Activation value is ",z)
    else:
        print("Activation value is ",1)

def Arctan(z):
    print("Activation value is ",math.atanh(z))
    
    
b = 1
wb = float(input("Enter bias weight :"))
n = int(input("number of inputs"))
z = b*wb
for i in range(n):
    I = float(input("Enter input :"))
    w = float(input("Enter weight :"))
    z = z + I*w
op = int(input("Enter 1-Linear :"))
print("summation value is ",z)
if(op==1):
    Linear(z)
elif(op==2):
    Threshold(z)
elif(op==3):
    Sigmoid(z)
elif(op==4):
    Tanh(z)
elif(op==5):
    PiecewiseLF(z)
elif(op==6):
    Relu(z)
elif(op==7):
    Softmax(z)
elif(op==8):
    Signum(z)
elif(op==9):
    Arctan(z)
else:
    print("Invalid input")