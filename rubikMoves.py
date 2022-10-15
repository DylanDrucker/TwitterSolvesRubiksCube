 
 
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


        self.face0 =   [[y,y,y], 
                        [y,y,y], 
                        [y,y,y]]
        self.face1 =   [[b,b,b], 
                        [b,b,b], 
                        [b,b,b]]
        self.face2 =   [[r,r,r], 
                        [r,r,r], 
                        [r,r,r]]
        self.face3 =   [[g,g,g], 
                        [g,g,g], 
                        [g,g,g]]
        self.face4 =   [[o,o,o], 
                        [o,o,o], 
                        [o,o,o]]
        self.face5 =   [[w,w,w], 
                        [w,w,w], 
                        [w,w,w]]

        self.faces = [self.face0, self.face1, self.face2, self.face3, self.face4, self.face5]

    ############ MOVES #############

    """ Shift upper layer clockwise"""
    def u(self):
        face1Upper = self.face1[0]
        self.face1[0] = self.face2[0]
        self.face2[0] = self.face3[0]
        self.face3[0] = self.face4[0]
        self.face4[0] = face1Upper

    """ Shift lower layer clockwise"""
    def d(self):
        face4Lower = self.face4[2]
        self.face4[2] = self.face3[2]
        self.face3[2] = self.face2[2]
        self.face2[2] = self.face1[2]
        self.face1[2] = face4Lower

    def r2(self):
        face0Lower = self.face0[2]
        self.face0[2] = self.takeColumn(self.face1, 2)[::-1]
        self.changeColumn(self.face1, 2, self.face5[0])
        self.face5[0] = self.takeColumn(self.face3, 0)[::-1]
        self.changeColumn(self.face3, 0, face0Lower)

    """ Shift Left Layer Clockwise"""
    def l(self):
        face0Upper = self.face0[0]
        self.face0[0] = self.takeColumn(self.face3, 2)
        self.changeColumn(self.face3, 2, self.face5[2])
        self.face5[2] = self.takeColumn(self.face1, 0)
        self.changeColumn(self.face1, 0, face0Upper)

    """Shift back side clockwise"""
    def b(self):
        face0Right = self.takeColumn(self.face0, 2)
        self.changeColumn(self.face0, 2, self.takeColumn(self.face2, 2))
        self.changeColumn(self.face2, 2, self.takeColumn(self.face5, 2))
        self.changeColumn(self.face5, 2, self.takeColumn(self.face4, 0)[::-1])
        self.changeColumn(self.face4, 0, face0Right[::-1])

    """"Shift front side clockwise"""
    def f(self):
        face0Left = self.takeColumn(self.face0, 0)
        self.changeColumn(self.face0, 0, self.takeColumn(self.face4, 2)[::-1])
        self.changeColumn(self.face4, 2, self.takeColumn(self.face5, 0)[::-1])
        self.changeColumn(self.face5, 0, self.takeColumn(self.face2, 0))
        self.changeColumn(self.face2, 0, face0Left)
        
    ############# COUNTERCLOCKWISE MOVES ###############

    """ prime methods"""
    def prime(self, move):
        for i in range(3):
            move()

    def twice (self, move):
        for i in range(2):
            move()

    

    ############ AUXILIAR METHODS #############

    def takeColumn(self, face, colIndex):
        col = []
        for layer in face:
            col.append(layer[colIndex])
        return col

    def changeColumn(self, face, colIndex, newColumn):
        for i in range(len(newColumn)):
            face[i][colIndex] = newColumn[i]

    



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
            for face in [self.face1, self.face2, self.face3, self.face4]:
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
    print(cube)
    cube.prime(cube.u)
    print(cube)
    
if __name__ == "__main__":
    main()     

