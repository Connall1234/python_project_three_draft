import random 

class Board:
    """
    This is a class that will create the board, size of the board, and keep track of hits/misses, as well as the player name/computer
    """

    def __init__(self, board_size, whos_playing, type):
        self.board_size = board_size
        self.whos_playing = whos_playing
        self.type = type

    #We will use the below function to set up the two boards 

    def print_board(self, miss_ship, hit_ship, boat_player):
        place = 0
        print("__________________")
        print(f"\n{self.whos_playing}'s board\n")
        print("__________________")
        print("     0  1  2  3  4")
        for point in range(5):
            row = ""
            for y in range(5):
                ch = " _ "
                if self.type == "Type A" and place in miss_ship_player:
                    ch = " x "
                elif self.type == "Type B" and place in miss_ship_computer:
                    ch = " x "
                elif self.type == "Type A" and place in hit_ship_player:
                    ch = " o "
                elif self.type == "Type B" and place in hit_ship_computer:
                    ch = " o "
                elif self.type == "Type A" and place in boat_player:
                    ch = " @ "
                elif self.type == "Type B" and place in boat_computer:
                    ch = " @ "
                row = row + ch
                place = place + 1
            print(point, " ", row)