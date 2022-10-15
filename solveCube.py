import rubikMoves

def main():
    cube = rubikMoves.Rubik()

    while(true):
        move = input("What move to you want to take: ")

        move = move.toUpper()

        match move:
            case "U":
                cube.u()
                print(cube)
            case "D":
                cube.d()









main()