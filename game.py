class Game():
    def __init__(self):
        self.State = True
        self.Win = " "
        self.Board = [ [ " ", " ", " " ],
                       [ " ", " ", " " ], 
                       [ " ", " ", " " ] ]
        self.Turn = "x"
        self.TotalTurns = 9

    def print_board(self):
        print("\n\n")
        print(f" {self.Board[0][0]} |" \
              f" {self.Board[0][1]} | {self.Board[0][2]} ")
        print(f"---+---+---")
        print(f" {self.Board[1][0]} |" \
              f" {self.Board[1][1]} | {self.Board[1][2]} ")
        print(f"---+---+---")
        print(f" {self.Board[2][0]} |"\
              f" {self.Board[2][1]} | {self.Board[2][2]} ")

    def print_turn(self):
         print(f"It's {self.Turn} turn.")
         print("Enter a Row number followed by a Column number "\
               "[Example: 1 1 is top left]")

    def make_move(self, x, y):
        self.Board[x][y] = self.Turn
        self.TotalTurns = self.TotalTurns -1
        self.check_win()
        if self.Turn == "x":
            self.Turn = "o"
        else:
            self.Turn = "x"
    
    def validate_values(self, xy):
        values = xy.split(" ")
        if len(values) == 2:
            x = int(values[0]) - 1 
            y = int(values[1]) - 1
            if (x in range(0,3) 
                and y in range(0,3)
                and self.Board[x][y] == " "):
                self.make_move(x, y)
                return 
        print("Invalid Move.")


    def check_win(self):
        # Column and row Win Conditions
        for i in range(0, 2):
            if (self.Board[i][0] == self.Board[i][1] 
                and self.Board[i][0] == self.Board[i][2]):
                self.Win = self.Board[i][0]
            if (self.Board[0][i] == self.Board[1][i] 
                and self.Board[0][i] == self.Board[2][i]):
                self.Win = self.Board[0][i]     
        # Diagnal Win conditions
        if (self.Board[0][0] == self.Board[1][1]
                and self.Board[0][0] == self.Board[2][2]):
                self.Win = self.Board[0][0]
        if (self.Board[0][2] == self.Board[1][1]
                and self.Board[0][2] == self.Board[2][0]):
                self.Win = self.Board[0][2]
        if self.TotalTurns <= 0 or self.Win != " ":
             self.State = False
        
    def game_over(self):
        if self.Win != " ":
            print(f"Congratulations {self.Turn} - You've won!")
        else:
             print("Game over- Match ended in a Draw!")