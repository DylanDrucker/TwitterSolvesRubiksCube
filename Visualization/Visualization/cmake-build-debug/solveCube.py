import rubikMoves

def main():
    cube = rubikMoves.Rubik()

    # Takes input from user
    while(True):
        move = input("What move do you want to take: ")
        if move == "quit":
            break

        move = move.upper()

        if move == "U":
            cube.u()
        elif move == "D":
            cube.d()
        elif move == "R":
            cube.r()
        elif move == "L":
            cube.l()
        elif move == "F":
            cube.f()
        elif move == "B":
            cube.b()

        elif move == "U'":
            cube.prime(cube.u)
        elif move == "D'":
            cube.prime(cube.d)
        elif move == "R'":
            cube.prime(cube.r)
        elif move == "L'":
            cube.prime(cube.l)
        elif move == "F'":
            cube.prime(cube.f)
        elif move == "B'":
            cube.prime(cube.b)

        elif move == "U2":
            cube.twice(cube.u)
        elif move == "D2":
            cube.twice(cube.d)
        elif move == "R2":
            cube.twice(cube.r)
        elif move == "L2":
            cube.twice(cube.l)
        elif move == "F2":
            cube.twice(cube.f)
        elif move == "B2":
            cube.twice(cube.b)
            
        
        
        print(cube)
        cube.fileOutput()
            
        


main()