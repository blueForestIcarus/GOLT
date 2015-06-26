#!/usr/bin/env python3

from os import system
import termbox
import random
import time
import os
import math


INITIAL_TEXT = """  
    display = Display()
    cols, rows = display.setup()
    

   
            display.refresh()
            pass

        time.sleep(DELAY)
    pass

def stop():
    curses.endwin()


class Simulator:
    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2
    
    display.inputText(INITIAL_TEXT)
    display.insertChar(176,47,chr(2))


class Simulator:
    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2
    
    display.inputText(INITIAL_TEXT)
    display.insertChar(176,47,chr(2))
    display.insertChar(176,48,chr(23))
    sim = Simulator(cols,rows)

    sim.thisGen = display.getBoolArray(display.text)

    display.refresh()
     
def start():
    global sim, display, running, paused, wait, DELAY

    while running:
        if not paused and not wait:
            sim.step()
            display.update(sim.getArray())
            display.refresh()
            pass

        time.sleep(DELAY)
    pass

def stop():
    curses.endwin()


class Simulator:
class Simulator:      
"""
#---------------------------------------------------------------------------
DELAY = 0 

running = True
paused = False
wait = False

ENDIAN='little'#this does nothing

sim = None
display = None
array = None

def init():
    global sim, display,array
    
    display = Display()
    cols, rows, array= display.setup()
    cols *= 2
    rows *= 4
    
    sim = Simulator(cols,rows)    

    rice()

def start():
    global sim, display, running, paused, wait, DELAY

    while running:
        if not paused and not wait:
            sim.step()
            display.refresh(sim.getArray())

        event = display.box.peek_event(timeout=30)
        if event:
            (typee, char, key, mod, width, height, mousex, mousey) = event
            if typee == termbox.EVENT_KEY and key == termbox.KEY_ESC:
                display.box.close()
                exit()
        #time.sleep(DELAY)
    pass

def stop():
    curses.endwin()
    
def rice():
    global sim, display

    display.inputText(INITIAL_TEXT, array)
    display.insertChar(10,5,2,array)
    display.insertChar(10,6,23,array)

    sim.thisGen = display.getBoolArray(array)
    sim.glider(60,70)
    display.refresh(sim.getArray())
    
class Simulator:
    rows = None
    cols = None

    thisGen = []
    nextGen = []

    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        self.thisGen = self.initGrid(cols,rows)
        self.nextGen = self.initGrid(cols,rows)

    def initGrid(self, cols, rows):
        array=[]
        for col in range(cols):
            arrayCol = []
            for row in range(rows):
                arrayCol += [False]

            array += [arrayCol]

        return array

    def step(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.nextGen[col][row] = self.checkCell(col, row)
                
        #Alex Martelli's opinion (at least back in 2007) about this is, that it is a weird syntax and it does not make sense to use it ever.
        self.thisGen = [col[:] for col in self.nextGen]
        
    def checkCell(self, x, y):
        living = 0 #number of living neighboring cells
        for x1 in [-1, 0, 1]:
            for y1 in [-1, 0, 1]:
                if not(x1 == y1 == 0):
                    col=(x1+x)%self.cols 
                    row=(y1+y)%self.rows         
                    if self.thisGen[col][row]:                           
                        living += 1

        if self.thisGen[x][y] == True and living < 2:
            return False
        elif self.thisGen[x][y] == True and living > 3:
            return False
        elif self.thisGen[x][y] == False and living == 3:
            return True
        else:
            return self.thisGen[x][y]
            
    def getArray(self): 
        return self.thisGen[:]

    def setCell(self,x,y,bool):
        x%=self.cols
        y%=self.rows
        self.thisGen[x][y] = bool

    def glider(self,x,y):
        self.setCell(x,y,True)
        self.setCell(x-1,y,True)
        self.setCell(x-2,y,True)
        self.setCell(x,y-1,True)
        self.setCell(x-1,y-2,True)


class Display:  
    box = None
    rows = 0
    cols = 0
    #modified=False
    #needsRefresh=False
    
    def __init__(self):
        self.box = termbox.Termbox()
        self.box.clear()
        self.box.present()
        pass
                
    def getText(self):
        text = ""
        for row in range(self.rows):
            for col in range(self.cols):
                text += self.text[col][row]
        return text
            
    def inputText(self, text, array):
        for row in range(self.rows):
            for col in range(self.cols):
                try:
                    array[col][row]=ord(text[col+(row*self.cols)])
                except:
                    array[col][row]=0
        return array

    def getBinaryChar(self, char):
        charCode = char 
        binary = []

        try:
            while charCode != 0:
                bit = charCode % 2 == 1
                binary.insert(0, bit)
                charCode = math.floor(charCode / 2)

            while len(binary)<8:
                binary.insert(0, False)
        except:
            self.box.close()
            print(charCode.__class__)
            print(char)
            raise

        return binary

    
    def getBoolArray(self, array):
        cols = len(array)
        rows = len(array[0])
        boolArray = Simulator.initGrid(None, cols*2,rows*4)
        
        for col in range(cols):
            for row in range(rows):
                binary = self.getBinaryChar(array[col][row])
                for x in range(2):
                     for y in range(4):
                          boolArray[col*2 + x][row*4 + y] = binary[x*2 + y]
                            
        return boolArray

    def setup(self):
        self.cols =  self.box.width()
        self.rows =  self.box.height()
        array=[]
        for col in range(self.cols):
            arrayCol = []
            for row in range(self.rows):
                arrayCol += [0]
            array += [arrayCol]

        return self.cols , self.rows, array
        
    def refresh(self, array):
        self.box.clear()

        for col in range(self.cols):
            for row in range(self.rows):
                
                char = 0
                for x in range(2):
                    for y in range(4):
                        char *= 2
                        char += 1 if array[col*2 + x][row*4 + y] else 0
                
                fg = termbox.BLACK
                if char == 0:
                    char = ord(" ")
                    bg = termbox.BLACK
                elif char < 32 or char == 127:
                    char = ord(" ")
                    bg = termbox.WHITE
                else:
                    char = char
                    bg = termbox.WHITE
                
                self.box.change_cell(col, row, char, fg, bg)


        #print(self.text)
        self.box.present()
        
    def insertChar(self, col, row, char, array):
        col%=self.cols
        row%=self.rows
        array[col][row] = char
        return array
    
    def getSimGrid(self):
        return self.getBoolArray(self.text)
    
init()
start()
stop()


