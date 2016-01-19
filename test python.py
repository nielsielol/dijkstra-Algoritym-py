class Point:

    def __init__(self, name, isEnd):
        self.name = name
        self.isEnd = isEnd
        self.path = ""
        self.linkers = []
        self.vortex = -2

    def setLinkers(self, linkers):
        self.linkers = linkers

    def getLinkers(self):
        return self.linkers

class Linker:

    def __init__(self, pointerTo, distance):
        self.pointerTo = pointerTo
        self.distance = distance

class Program:
    

    #this function needs to be executed!
    def Main():
        pointers = []
        visited = []
        pointers.append(Point("A", False)) 
        pointers.append(Point("B", False))
        pointers.append(Point("C", False))
        pointers.append(Point("D", False))
        pointers.append(Point("E", False))
        pointers.append(Point("F", True))
        pointers.append(Point("G", False))

        #A
        linker = []
        linker.append(Linker(pointers[1], 4))
        linker.append(Linker(pointers[2], 3))
        linker.append(Linker(pointers[4], 7))
        pointers[0].setLinkers(linker)

        #B
        linker = []
        linker.append(Linker(pointers[0], 4))
        linker.append(Linker(pointers[2], 6))
        linker.append(Linker(pointers[3], 5))
        pointers[1].setLinkers(linker)

        #C
        linker = []
        linker.append(Linker(pointers[0], 3))
        linker.append(Linker(pointers[1], 6))
        linker.append(Linker(pointers[3], 11))
        linker.append(Linker(pointers[4], 8))
        pointers[2].setLinkers(linker)

        #D
        linker = []
        linker.append(Linker(pointers[1], 5))
        linker.append(Linker(pointers[2], 11))
        linker.append(Linker(pointers[4], 7))
        linker.append(Linker(pointers[6], 10))
        linker.append(Linker(pointers[5], 2))
        pointers[3].setLinkers(linker)

        #E
        linker = []
        linker.append(Linker(pointers[0], 7))
        linker.append(Linker(pointers[2], 8))
        linker.append(Linker(pointers[3], 2))
        linker.append(Linker(pointers[6], 5))
        pointers[4].setLinkers(linker)

        #F
        linker = []
        linker.append(Linker(pointers[3], 2))
        linker.append(Linker(pointers[6], 3))
        pointers[5].setLinkers(linker)

        #G
        linker = []
        linker.append(Linker(pointers[4], 5))
        linker.append(Linker(pointers[3], 10))
        linker.append(Linker(pointers[5], 3))
        pointers[6].setLinkers(linker)

        for pointer in pointers:
            pointer.vortex = -1

        pointers[0].vortex = 0;
        visited.append(pointers[0])

        theChosenOne = None
        foundAnswer = False

        while (foundAnswer == False):
            print("started")
            if(theChosenOne == None and len(visited) == 1):
                theChosenOne = visited[0]
                print("we added the first!: ", theChosenOne.name)
                theChosenOne.path = theChosenOne.path + theChosenOne.name

            print("the chosenOne: ",theChosenOne.name)
            for linker in theChosenOne.getLinkers():
                print(theChosenOne.name, " --> ", linker.pointerTo.name, " linker vortex: ", linker.pointerTo.vortex, \
                      " distance: ", (theChosenOne.vortex + linker.distance))
                if (linker.pointerTo.vortex == -1 or linker.pointerTo.vortex > (theChosenOne.vortex + linker.distance)):
                    for point in pointers:
                        if(point == linker.pointerTo):
                            print("we are setting a new pointerVortex: ", point.name, "the old Vortex = ", point.vortex)
                            point.vortex = theChosenOne.vortex + linker.distance
                            print("the new vortex = ", point.vortex, " ( ", theChosenOne.vortex, " ) ")

                            point.path = theChosenOne.path
                            point.path = point.path + point.name
                            print("point.pathh: ", point.path)
                            if(point.isEnd):
                                print("We found the end!")
                                foundAnswer = True

            if(foundAnswer == False):
                theChosenOne = None
                
                for pointer in pointers:
                    print(pointer.name)
                    if(visited.count(pointer) == 0):
                        if(theChosenOne == None):
                            print("the chosen one is null so the first occurrence is: ", pointer.name, " ", pointer.vortex)
                            theChosenOne = pointer
                            
                        elif (pointer.vortex < theChosenOne.vortex and pointer.vortex != -1):
                            print("we found a lower vortes: ", pointer.name, " ", pointer.vortex)
                            theChosenOne = pointer
                    
                
                print("the new chosen one: ", theChosenOne.name)
                print()
                visited.append(theChosenOne)

        for point in pointer:
            if(pointer.isEnd):
                print(pointer.path)

        

Program.Main()








        
