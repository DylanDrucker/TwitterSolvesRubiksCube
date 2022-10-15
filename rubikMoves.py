 
 
class Rubik(object):

    def __init__(self):

        w = 'w' # white
        y = 'y' # yellow
        b = 'b' # blue
        g = 'g' # green
        r = 'r' # red
        o = 'o' # orange

        # Faces:
        #   0
        # 1 2 3 4
        #   5


        self.face0 =   [[w,w,w], 
                        [w,w,w], 
                        [w,w,w]]
        self.face1 =   [[o,o,o], 
                        [o,o,o], 
                        [o,o,o]]
        self.face2 =   [[b,b,b], 
                        [b,b,b], 
                        [b,b,b]]
        self.face3 =   [[r,r,r], 
                        [r,r,r], 
                        [r,r,r]]
        self.face4 =   [[g,g,g], 
                        [g,g,g], 
                        [g,g,g]]
        self.face5 =   [[y,y,y], 
                        [y,y,y], 
                        [y,y,y]]

        self.faces = [self.face0, self.face1, self.face2, self.face3, self.face4, self.face5]

    ############ MOVES #############

    """ Shift upper layer clockwise"""
    def u(self):
        face1self.face1Upper = self.face1[0]
        self.face1[0] = self.face2[0]
        self.face2[0] = self.face3[0]
        self.face4[0] = self.face5[0]
        self.face5[0] = face1self.face1Upper

    """ Shift lower layer clockwise"""
    def d(self):
        face4self.face4Lower = self.face4[2]
        self.face4[2] = self.face3[2]
        self.face3[2] = self.face2[2]
        self.face2[2] = self.face1[2]
        self.face1[2] = face4self.face4Lower
        
    """ Shift right layer clockwise"""
    def r(self):
        face0Right = self.getRightSide(self.face0)
        self.changeRightSide(self.face0, self.face2)
        self.changeRightSide(self.face2, self.face5)
        self.changeRightSide(self.face5, self.face2)
        self.face2[0] = self.face4[0]
        self.face4[0] = self.face4[0]
        self.face4[0] = face0Right

    def changeSides(self, faceFrom, faceTo):
        faceFrom[0][2] = faceTo[0][2]
        faceFrom[1][2] = faceTo[1][2]
        faceFrom[2][2] = faceTo[2][2]

    def getRightSide(self, face):
        return [face[0][2], face[1][2], face[2][2]]

    def setRightSide(self, face, newSide):
        face[0][2] = newSide[0]
        face[1][2] = newSide[1]
        face[2][2] = newSide[2]

    """ Shift upper layer anticlockwise"""
    def uPrime(self):
        face1self.face1Upper = self.face1[0]
        self.face1[0] = self.face2[0]
        self.face2[0] = self.face4[0]
        self.face4[0] = self.face4[0]
        self.face4[0] = face1self.face1Upper



    ###########  FILE OUTPUT  ##########
    def faceToText(self, face):
        text = ""
        for layer in face:
            for color in layer:
                text += color
        
        return text

    def fileOutput(self):
        f = open("myfile.txt", "w")

        for face in self.faces:
            f.write(self.faceToText(face))
            f.write("\n")


    ########## PRINT INSTANCE ###########
    def __str__(self):
        cube = ""
        
        cube += " "*13 + "-"*15 + "\n"
        
        for row in self.face0:
            cube += " "*13 # black space
            cube += "|| {} | {} | {} ".format(row[0], row[1], row[2])
            cube += "||\n"
        
        cube += "-"*54 + "\n"

        for i in range(3):
            for face in [self.face1, self.face2, self.face4, self.face4]:
                cube += "|| {} | {} | {} ".format(face[i][0], face[i][1], face[i][2])
            
            cube += "||\n"
        
        cube += "-"*54 + "\n"

        for row in self.face5:
            cube += " "*13 # black space
            cube += "|| {} | {} | {} ".format(row[0], row[1], row[2])
            cube += "||\n"
        
        cube += " "*13 + "-"*15 + "\n"

        return cube





def main():
    cube = Rubik()
    print(cube.faceToText(cube.face0))
    cube.fileOutput()
    print(cube)
    
if __name__ == "__main__":
    main()     

