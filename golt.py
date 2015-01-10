#!/usr/bin/env python3

from os import system
import curses
import random
import time
import os


start = "this is a test text and is the pon t of this all this is to be a test and i have o add all this text because i need source for the simulator asefihsakdfhbasdljgbasfbvkudhbfvksbdfasdhbfjkbsdfkjsdafjbsdajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjfksdgfpviasdbvpibasdojvbasdpjvbpa"
#---------------------------------------------------------------------------
DELAY = 0.5

running = True
paused = False
wait = False

ENDIAN='little'

sim = null
display = null

def init():
    display = Display()
    cols, rows = display.setup()
    cols *= 4
    rows *= 2
    
    display.inputText(start)
    sim = Simulator(cols,rows)
    
    sim.thisGen = display.getBoolArray(display.text)
     
def start():
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
    rows = null
    cols = null

    thisGen = []
    nextGen = []

    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        thisGen = self.initGrid(cols,rows)
        nextGen = self.initGrid(cols,rows)

    def initGrid(self, cols, rows):
        for i in range(rows):
            arrayRow = []
            for j in range(cols):
                arrayRow += [False]

            array += [arrayRow]

        return array

    def step(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.nextGen[i][j] = checkCell(i, j)
                
        #Alex Martelli's opinion (at least back in 2007) about this is, that it is a weird syntax and it does not make sense to use it ever.
        self.thisGen = self.nextGen[:] 
        
    def checkCell(self, x, y):
        living = 0 #number of living neighboring cells
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if not(i == x and j == y):
                    if(i >= self.cols):
                        i=0   
                    if(j >= self.rows):
                        j=0                                       
                    living += self.thisGen[i][j]

        if self.thisGen[x][y] == True and living < 2:
            return False
        if self.thisGen[x][y] == True and living > 3:
            return False
        if self.thisGen[x][y] == False and living == 3:
            return True
        else:
            return self.thisGen[x][y]
            
    def getArray(): 
        return thisGen[:]

class Display:  
    screen = null
    text = null
    rows = 0
    cols = 0
    modified=false
    needsRefresh=false
    
    def __init__(self):
        screen = curses.initscr()

    def getCharArray(self, array):
        text=[]
        if(array.length%4 == 0 and array[0].length%2 == 0):
            cols = array.length/4
            rows = array.length/2
            for row in range(rows):
                textRow = []
                for col in range(cols):
                    binary = []
                    for y in range(2):
                        for x in range(4):
                            binary += [array[col + x][row + y]]
                    textRow += [self.getChar(binary)]
                text += [textRow]
        else:
            text += [-1]
        
        return text
        
    def getText(self, array):
        text = ""
        for char in row in array:
            text += char
            
    def inputText(self, string):
        for row in range(self.rows):
            for col in range(self.cols):
                try:
                    this.text[col][row]= string[col+row*this.cols]
                except:
                    this.text[col][row]=" "
    
    def getChar(self, array):
        return bitarray(array, endian=ENDIAN).tobytes()#.toString()
    
    def getBoolArray(self, array):
        cols = array[0].length()
        rows = array.length()
        boolArray = Simulator.initGrid(cols,rows)
        
        for row in range(rows):
            for col in range(cols):
                binary = getBinaryChar(array[col][row])
                for y in range(2):
                        for x in range(4):
                            boolArray[col + x][row + y] = binary[x + 4*y]
                            
        return boolArray

    
    def getBinaryChar(self, char):
        return bitarray(endian=ENDIAN).frombytes(char).tolist()###what does this return

    def setup(self):
        self.cols = screen.getmaxyx()[1]
        self.rows = screen.getmaxyx()[0]
        for i in range(self.rows):
            arrayRow = []
            for j in range(self.cols):
                arrayRow += ["0"]
            array += [arrayRow]

        text = array
        return self.cols , self.rows
        
    def update(self, array):
        self.text = self.getCharArray(array)
        
    def refresh(self):
        for row in range(self.rows):
            for col in range(self.cols):
                screen.addch(row,col,self.text[col][row])
        
    def insertChar(self, x, y, char):
        self.text[x][y] = char
        return self.getBoolArray(self.text)

init()
start()
stop()


