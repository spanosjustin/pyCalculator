## Operation Logic for py calc
from tkinter import *

input1 = float
input2 = float
ans = float
equals = False
myList = []

## Math logic
def addition(input1, input2,):
    ans = input1 + input2
    return ans
  
def subtraction(input1, input2,):
    ans = input1 - input2
    return ans
    
def multiplication(input1, input2,):
    ans = input1 * input2
    return ans
    
def division(input1, input2,):
    ans = input1 / input2
    return ans
    

## Function that combines list into one float variable
def listToFloat(myList):
    myString = ''.join(myList)
    variable = float(myString)
    return variable


    




