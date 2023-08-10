import sys

def fuck():
    print("nuh uh")
    exit()
    
if (len(sys.argv)) == 1:
     fuck()
     
if sys.argv[1].isnumeric() == False:
     fuck()

if sys.argv[1] == '²':
     fuck()

starNumber = int(sys.argv[1])

if starNumber > 300:
     print("Star too big, brain cant count that high")
     exit()
if starNumber == 0:
    exit()
    
def starMaker():
    
    #variables for loopin
    counter = 0
    inverseCounter = 0
    gapFlatStar = starNumber * 2 - 3
    if starNumber == 1:
        gapFlatStar = 1
    #variables for whitespace

    firstStarSpace = starNumber * 3 - 1
    firstPartSpaceNumber = starNumber * 2 
    settingEmptySpace = ' ' * firstPartSpaceNumber
    flatStar = "*" * starNumber * 2 + '*'

    for star in range(10):
        if star == 0:
            if starNumber != 1:
                print(firstStarSpace * ' ', end='',file=f)
                print("*",file=f)
            if starNumber == 1:
                print(firstStarSpace * ' ' + ' ', end='',file=f)
                print("*",file=f)
            for star in range(starNumber - 1):
                counter += 1
                for star in range(starNumber - counter - 1):
                    print(" ", end='',file=f)
                print(settingEmptySpace, end='',file=f)
                print("*",end='',file=f)
                for star in range(inverseCounter + inverseCounter + 1):
                    print(" ", end='',file=f)
                print("*",file=f)
                inverseCounter += 1
        if star == 1:
                for star in range(3):
                     if star == 0:
                         print(flatStar, end='',file=f)
                     if star == 1:
                         print(" " * gapFlatStar, end='',file=f)
                     if star == 2:
                        print(flatStar,file=f)
        if star == 3:
            counter = 1
            inverseCounter = 3
            if starNumber == 1:
                 inverseCounter = 2
            for star in range(starNumber):
                for star in range(counter):
                        print(" ", end='',file=f)
                print("*", end='',file=f)
                counter += 1
                for star in range ((starNumber * 6 + 1) - inverseCounter * 2):
                        print(" ", end='',file=f)
                print("*",file=f)
                inverseCounter += 1

        if star == 5:
            inverseCounter = starNumber * 4 - 1
            for star in range(starNumber - 1):
                for star in range(counter - 2):
                    print(" ", end='',file=f)
                print("*",end='',file=f)
                counter -= 1
                for star in range(inverseCounter):
                     print(" ", end='',file=f)
                print("*",file=f)
                inverseCounter += 2
        if star == 7:
            for star in range(3):
                     if star == 0:
                         print(flatStar, end='',file=f)
                     if star == 1:
                         print(" " * gapFlatStar, end='',file=f)
                     if star == 2:
                        print(flatStar,file=f)
        if star == 9:
                counter = starNumber * 2
                inverseCounter = gapFlatStar
                for star in range(starNumber - 1):
                    for star in range(counter):
                         print(" ", end='',file=f)
                    print("*", end='',file=f)
                    counter += 1
                    for star in range(inverseCounter):
                         print(" ", end='',file=f)
                    print("*",file=f)
                    inverseCounter -= 2
                if starNumber != 1:
                     print(firstStarSpace * ' ', end='',file=f)
                     print("*",file=f)
                if starNumber == 1:
                    print(firstStarSpace * ' ' + ' ', end='',file=f)
                    print("*",file=f)

with open("Star.txt", 'w') as f:
         starMaker()
