import time

def gameboard_drawing(pos_list):
    print(" ___ ___ ___ ")
    for i in range(3):
        print("|", pos_list[i*3],"|", pos_list[i*3+1],"|", pos_list[i*3+2], "|")
        print(" ___ ___ ___ ")

def position_detect(arr: list): 
    for i in range(3):
        if arr[i * 3]==arr[i * 3 + 1] ==arr[i * 3 + 2]:
            return False
        if arr[i]==arr[i+3] ==arr[i+6]:
            return False
    if arr[0]==arr[4] ==arr[8] or arr[2]==arr[4] ==arr[6]:
        return False
    return True

print("Game starts!")
counter = 1
pos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while position_detect(pos_list) and counter <= 9:
    gameboard_drawing(pos_list)
    print("Please make your next move(choose your position)!")
    position = int(input())
    if counter % 2 != 0: pos_list[position - 1] = "Ø"
    else: pos_list[position - 1] = "×"
    counter += 1
else:
    if counter % 2 == 0:
        print("'O' wins!")
    elif counter % 2 != 0:
        print("'X' wins!")
    else:
        gameboard_drawing(pos_list)
        print("Draw!")
time.sleep(10)
