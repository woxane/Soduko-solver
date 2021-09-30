#!/usr/bin/python3

import numpy


soduko_puzzle = numpy.array([list(map(int , input().split(" "))) for i in range(9)]) #get puzzle one by one row and convert it to int .

def possible(y,x,n) : 
    #this fucntion test is the n number can fit in the y,x of puzzle .
    for horizontal_numbers in range(9) : 
        if soduko_puzzle[y][horizontal_numbers] == n :
            return False #check for is any n number in horizontal row . 

    for vertical_numbers in range(9) :
        if soduko_puzzle[vertical_numbers][x] == n :
            return False #check if any n number in vertical row .

    x_square = (x//3)*3
    y_square = (y//3)*3

    for row in range(3) :
        for column in range(3) : 
            if soduko_puzzle[y_square+row][x_square+column] == n : 
                return False #check if any number in the sqaure of the y,x .

    return True 

result = []
def solver() :
    global soduko_puzzle
    global result 

    for y in range(9) :
        for x in range(9) : 
            if soduko_puzzle[y][x] == 0 :
                for n in range(1,10) :
                    if possible(y,x,n) :
                        soduko_puzzle[y][x] = n
                        solver()
                        soduko_puzzle[y][x] = 0

                return
    result = soduko_puzzle.tolist() #idk why if i dont convert it to list and pass it to variable it doesnt work , if any one know please fork and make correct :> .


solver()
print(numpy.array(result))
