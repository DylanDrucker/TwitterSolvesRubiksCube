 
 
class Rubik(object):

    def __init__(self):

        w = 'w' # white
        y = 'y' # yellow
        b = 'b' # blue
        g = 'g' # green
        r = 'r' # red
        o = 'o' # orange

        # Faces:
        #   1
        # 2 3 4 5
        #   6

        self.face1 =   [[w,w,w], 
                        [w,w,w], 
                        [w,w,w]]
        self.face2 =   [[y,y,y], 
                        [y,y,y], 
                        [y,y,y]]
        self.face3 =   [[b,b,b], 
                        [b,b,b], 
                        [b,b,b]]
        self.face4 =   [[g,g,g], 
                        [g,g,g], 
                        [g,g,g]]
        self.face5 =   [[r,r,r], 
                        [r,r,r], 
                        [r,r,r]]
        self.face6 =   [[o,o,o], 
                        [o,o,o], 
                        [o,o,o]]

    ############ MOVES #############

    """ Shift upper layer clockwise"""
    def u(self):
        face2Upper = self.face2[0]
        self.face2[0] = self.face3[0]
        self.face3[0] = self.face4[0]
        self.face4[0] = self.face5[0]
        self.face5[0] = face2Upper

    """ Shift lower layer clockwise"""
    def d(self):
        face5Lower = self.face5[2]
        self.face5[2] = self.face4[2]
        self.face4[2] = self.face3[2]
        self.face3[2] = self.face2[2]
        self.face2[2] = face5Lower
        
    """ Shift right layer clockwise"""
    def r(self):
        face1Right = self.face1[0][2]
        self.face2[0] = self.face3[0]
        self.face3[0] = self.face4[0]
        self.face4[0] = self.face5[0]
        self.face5[0] = face2Upper

    def 


    def __str__(self):
        for row in self.face1:
            print("                ", end="") # black space
            print("| {} | {} | {} ".format(row[0], row[1], row[2]), end="")
            print("|")

        for i in range(3):
            for face in [self.face2, self.face3, self.face4, self.face5]:
                print("| {} | {} | {} ".format(face[i][0], face[i][1], face[i][2]), end = "")
            print("|")


        for row in self.face6:
            print("                ", end="") # black space
            print("| {} | {} | {} ".format(row[0], row[1], row[2]), end="")
            print("|")

def main():
    print("Hello")
    cube = Rubik()
    print(cube)
    
if __name__ == "__main__":
    main()     

