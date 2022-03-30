from victory_handler import check_game
from grid import create_array, print_grid
from input_handler import get_input

rows=3
columns=3
empty_sign="_"
grid=create_array(rows,columns,empty_sign)
empty_places= rows*columns
move_counter=0

player_symbol={
    1: "o",
    2: "x"
}

game_over=False

for round_num in range(1,6):
    print ("Round number is", round_num)
    for player in range (1,3):
        while True:
            print("Players", player, "turn")
            print_grid(grid,rows,columns)
            print("Enter the ROW coordinate")
            x=get_input()
            print("Enter the COLUMN coordinate")
            y=get_input()
            if x>=rows or x<0 or y>=columns or y<0:
                print("Sorry, coordinates out of range please reenter")
                continue
            if grid[x][y] !=empty_sign:
                print("Sorry, place is not free")
                continue
            break
        grid[x][y] = player_symbol[player]
        if check_game(grid, rows,columns,player_symbol[player]):
            winner=player
            game_over=True
            break
        move_counter +=1
        if move_counter==empty_places:
            print ("Draw")
            game_over=True
            break
    if game_over:
        print_grid(grid,rows,columns)
        print("Player ", winner, "has won!")
        break