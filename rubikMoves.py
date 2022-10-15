 
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

        # Representing the cube
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

    """ Shift right layer clockwise"""
    def r(self):
        face0Lower = self.face0[2]
        self.face0[2] = self.takeColumn(self.face1, 2)[::-1]
        self.changeColumn(self.face1, 2, self.face5[0])
        self.face5[0] = self.takeColumn(self.face3, 0)[::-1]
        self.changeColumn(self.face3, 0, face0Lower)

    """ Shift left layer clockwise"""
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

    """Prime methods"""
    def prime(self, move):
        for i in range(3):
            move()

    ############# MOVE TWICE ###############

    """Completes the given move twice"""
    def twice (self, move):
        for i in range(2):
            move()

    

    ############ AUXILIARY METHODS #############

    """"Returns an array with a column of a face"""
    def takeColumn(self, face, colIndex):
        col = []
        for layer in face:
            col.append(layer[colIndex])
        return col

    """"Changes the column of a face with a given input"""
    def changeColumn(self, face, colIndex, newColumn):
        for i in range(len(newColumn)):
            face[i][colIndex] = newColumn[i]

    



    ###########  FILE OUTPUT  ##########
    
    """ove """
    def faceToText(self, face):
        text = ""
        for layer in face:
            for color in layer:
                text += color
        
        return text

    """"Transforms face 4 to text in a format that works with our simulator"""
    def face4ToText(self):
        text = self.faceToText(self.face4)
        text = text[::-1]
        return text

    """Creates a file with the current status of the cube"""
    def fileOutput(self):
        f = open("cubeStatus.txt", "w")

        for face in self.faces:
            if (face == self.face4):
                continue
            else:
                f.write(self.faceToText(face))
                f.write("\n")
            
        f.write(self.face4ToText())
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


