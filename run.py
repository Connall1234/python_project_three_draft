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

# Our function to get the player name    
def get_player_name():
    trigger = "off"
    while trigger == "off":
        try:
            name_not_capitalized = input("What is your name, please use three letters only. ")
            if len(name_not_capitalized) > 3 or len(name_not_capitalized) < 3:
                raise ValueError("Wrong amount of characters, try again! ")
            elif name_not_capitalized.isalpha():
                name = name_not_capitalized.capitalize()
                return name
                trigger = "on"
        except ValueError as e:
            print("Error:", e)

#This is the function to get the ships on the board 
def print_boats(boat):
    random_numbers = random.sample(range(0, 24), 2)
    boat.extend(random_numbers)

#This is our functuon to get the players hit 

def get_hit(hit_ship_player, miss_ship_player, boat_player):
    while True:
        try:
            ro = input("\nPlease select a row? ")
            row = int(ro) 
            if row in range(0,5):
                break
            elif row not in range(0,5):
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nPssst, it's meant to be a number!")
    while True:
        try:
            co = input("\nPlease select a column? ")
            column = int(co) 
            if column in range(0,5):
                break
            elif column not in range(0,5):
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nHey now, it's meant to be a number!")
    return (row * 5) + column

#This is our function to have the players turn 
def player_turn(hit_ship_player, miss_ship_player, boat_player):
    player_hit = "n"
    player_hit = get_hit(hit_ship_player, miss_ship_player, boat_player)
    while True:
        #This will check if the guess is in these lists, if it is we need to guess again
        if player_hit in hit_ship_player or player_hit in miss_ship_player:
            print("Looks like you had that guess!")
            player_hit = get_hit(hit_ship_player, miss_ship_player, boat_player)
        else:
            return player_hit
            break


#This will get the computer's guess 
def computer_guess(computer_poss_guesses):
    computer_hit = random.choice(computer_poss_guesses)
    computer_poss_guesses.remove(computer_hit)
    return computer_hit

#This wll check if the guess hit a boat, if it does it's added to hit, if not it's a miss 
def check(miss, hit, boat, result):
    if result in boat:
        boat.remove(result)
        hit.append(result)
    else:
        miss.append(result)      

#This is our function to check for the winner        
def check_winner(boat_player, boat_computer):
    if len(boat_computer) == 0 and len(boat_player) == 0:
        print("\nAll ships are down,  it's a tie! ")
        return True 
    elif len(boat_computer) == 0:
        print("\nYour ships are down, computer wins! ")
        return True 
    elif len(boat_player) == 0:
        print("\nComputer's ships are down, you win! ")  
        return True 
    else:
        return