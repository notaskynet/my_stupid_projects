def gameboard_drawing(position_list):
    pass

def position_detect(position_tracking_list):
    pass

position_tracking_list = []
position = 1
symbol = "X"


print("Game starts!") # Game start! Now you can choose X or O and make your
while True:
    gameboard_drawing(position_tracking_list)
    if position_detect(position_tracking_list):
        print("Game over!")
        break
    print("Please make your next move and then indicate your symbol!")
    position = list(map(input(), position, symbol))
    position_tracking_list.append(position)
print("If you wanna play again you need open this program again!")
