from game import Game   

def main():
    g = Game()
    print("welcome to two player Tic Tac Toe!")
    print("To select a square, enter a Row and" \
           "Column number ( 1 through 3 )")
    print("X goes first!")
    while g.State:
        g.print_board()
        g.print_turn()
        g.validate_values(input("Row Column:"))
    
    g.game_over()

if __name__ == "__main__":
    main()