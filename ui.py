## Interface
from tkinter import *
from numButtons import *
from calcLogic import *

master = Tk()
master.title("Calculator")
canvas_width = 340
canvas_height = 600

w = Canvas(master, width=canvas_width, height=canvas_height, bg="#000000")

w.pack()

def display():
    variable = 0
    varChoice = 0
    var = 0
    a = 0
    b = 0
    f = 0
    i = 0
    varList = []
    running = True

    ## operation states
    operationValueState = 0
    
    displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))
        
    
    ## operation button click functions 
    def additionClicked(*args):
        nonlocal operationValueState
        nonlocal a
        nonlocal variable
        nonlocal varList
        nonlocal displayNum
        a = variable
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))
        operationValueState = 1
    
    def subtractionClicked(*args):
        nonlocal operationValueState
        nonlocal a
        nonlocal variable
        nonlocal varList
        nonlocal displayNum
        a = variable
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))
        operationValueState = 2

    def multipleClicked(*args):
        nonlocal operationValueState
        nonlocal a
        nonlocal variable
        nonlocal varList
        nonlocal displayNum
        a = variable
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))
        operationValueState = 3

    def divideClicked(*args):
        nonlocal operationValueState
        nonlocal a
        nonlocal variable
        nonlocal varList
        nonlocal displayNum
        a = variable
        operationValueState = 4
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))
    
    def equalsClicked(*args):
        nonlocal operationValueState
        nonlocal variable
        nonlocal displayNum
        nonlocal f
        nonlocal a
        nonlocal b
        b = variable
        match operationValueState:
            case 0:
                f = 0
            case 1:
                f = addition(a, b)
            case 2:
                f = subtraction(a, b)
            case 3:
                f = multiplication(a, b)
            case 4:
                f = division(a, b)
        variable = 0
        operationValueState = 0
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=f, tag="display_num", font=("Helvetica", 26))
    
    def calculateClicked(*args):
        nonlocal variable
        nonlocal operationValueState
        nonlocal displayNum
        nonlocal varList
        variable = 0
        operationValueState = 0
        w.delete(displayNum)
        varList.clear()
        displayNum = w.create_text(170, 45, text=variable, tag="display_num", font=("Helvetica", 26))

    def positiveNegative(*args):
        nonlocal variable
        nonlocal displayNum
        variable = variable * -1
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable

    ## number button
    def zeroClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('0')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def pointClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('.')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable


        
    def oneClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('1')
        variable = listToFloat(varList)
        ## new display
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def twoClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('2')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def threeClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('3')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    
    def fourClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('4')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def fiveClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('5')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def sixClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('6')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
        
    def sevenClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('7')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def eightClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('8')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable
    def nineClicked(*args):
        nonlocal displayNum
        nonlocal variable
        varList.append('9')
        variable = listToFloat(varList)
        w.delete(displayNum)
        displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
        return variable


    #### OPERATION BUTTONS
    ## calculate button
    w.create_rectangle(15, 100, 75, 175, outline="#555559", fill="#555559", tag="calculateButton")
    w.create_text(45, 137, text="C", font=("Helvetica", 26), tags="calculateButton")    
    ## equals
    w.create_rectangle(100, 100, 245, 175, outline="#555559", fill="#555559", tag="equalsButton")
    w.create_text(172, 137, text="=", font=("Helvetica", 26), tags="equalsButton")
    ## positive or negative
    w.create_rectangle(270, 100, 330, 175, outline="#555559", fill="#555559", tag="positiveNegative")
    w.create_text(300, 137, text="+/-", font=("Helvetica", 26), tags="positiveNegative")
    
    ## plus button
    w.create_rectangle(270, 500, 330, 575, outline="#ce9932", fill="#ce9932", tag="plusButton")
    w.create_text(302, 535, text="+", font=("Helvetica", 26), tags="plusButton")
    ## minus button
    w.create_rectangle(270, 400, 330, 475, outline="#ce9932", fill="#ce9932", tag="minusButton")
    w.create_text(302, 435, text="-", font=("Helvetica", 26), tags="minusButton")
    ## multiple button
    w.create_rectangle(270, 300, 330, 375, outline="#ce9932", fill="#ce9932", tag="multButton")
    w.create_text(302, 335, text="x", font=("Helvetica", 26), tags="multButton")
    ## divide button
    w.create_rectangle(270, 200, 330, 275, outline="#ce9932", fill="#ce9932", tag="divideButton")
    w.create_text(302, 235, text="/", font=("Helvetica", 26), tags="divideButton")



    #### NUMERICAL BUTTONS
    ## zero
    w.create_rectangle(15, 500, 160, 575, outline="#36373b", fill="#36373b", tag="zeroButton")
    w.create_text(45, 537, text="0", font=("Helvetica", 26), tags="zeroButton")
    ## point
    w.create_rectangle(185, 500, 245, 575, outline="#36373b", fill="#36373b", tag="pointButton")
    w.create_text(215, 537, text=".", font=("Helvetica", 26), tags="pointButton")
    
    ## one
    w.create_rectangle(15, 400, 75, 475, outline="#36373b", fill="#36373b", tag="oneButton")
    w.create_text(45, 437, text="1", font=("Helvetica", 26), tags="oneButton")
    ## two
    w.create_rectangle(100, 400, 160, 475, outline="#36373b", fill="#36373b", tag="twoButton")
    w.create_text(130, 437, text="2", font=("Helvetica", 26), tags="twoButton")
    ## three
    w.create_rectangle(185, 400, 245, 475, outline="#36373b", fill="#36373b", tag="threeButton")
    w.create_text(215, 437, text="3", font=("Helvetica", 26), tags="threeButton")

    ####
    ## four
    w.create_rectangle(15, 300, 75, 375, outline="#36373b", fill="#36373b", tag="fourButton")
    w.create_text(45, 337, text="4", font=("Helvetica", 26), tags="fourButton")
    ## five
    w.create_rectangle(100, 300, 160, 375, outline="#36373b", fill="#36373b", tag="fiveButton")
    w.create_text(130, 337, text="5", font=("Helvetica", 26), tags="fiveButton")
    ## six
    w.create_rectangle(185, 300, 245, 375, outline="#36373b", fill="#36373b", tag="sixButton")
    w.create_text(215, 337, text="6", font=("Helvetica", 26), tags="sixButton")
    
    ####
    ## seven
    w.create_rectangle(15, 200, 75, 275, outline="#36373b", fill="#36373b", tag="sevenButton")
    w.create_text(45, 237, text="7", font=("Helvetica", 26), tags="sevenButton")
    ## eight
    w.create_rectangle(100, 200, 160, 275, outline="#36373b", fill="#36373b", tag="eightButton")
    w.create_text(130, 237, text="8", font=("Helvetica", 26), tags="eightButton")
    ## nine
    w.create_rectangle(185, 200, 245, 275, outline="#36373b", fill="#36373b", tag="nineButton")
    w.create_text(215, 237, text="9", font=("Helvetica", 26), tags="nineButton")


    
    ## Operation Button Utility
    w.tag_bind("plusButton","<Button-1>",additionClicked)
    w.tag_bind("minusButton","<Button-1>",subtractionClicked)
    w.tag_bind("multButton","<Button-1>",multipleClicked)
    w.tag_bind("divideButton","<Button-1>",divideClicked)

    w.tag_bind("equalsButton","<Button-1>",equalsClicked)
    w.tag_bind("calculateButton","<Button-1>",calculateClicked)
    w.tag_bind("positiveNegative","<Button-1>",positiveNegative)

    ## number utility
    w.tag_bind("zeroButton","<Button-1>",zeroClicked)
    w.tag_bind("pointButton","<Button-1>",pointClicked)
    
    w.tag_bind("oneButton","<Button-1>",oneClicked)
    w.tag_bind("twoButton","<Button-1>",twoClicked)
    w.tag_bind("threeButton","<Button-1>",threeClicked)
    
    w.tag_bind("fourButton","<Button-1>",fourClicked)
    w.tag_bind("fiveButton","<Button-1>",fiveClicked)
    w.tag_bind("sixButton","<Button-1>",sixClicked)
    
    w.tag_bind("sevenButton","<Button-1>",sevenClicked)
    w.tag_bind("eightButton","<Button-1>",eightClicked)
    w.tag_bind("nineButton","<Button-1>",nineClicked)


            







        
