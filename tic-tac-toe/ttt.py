"""Tic Tac Toe
This programe construct a Tic Tac Toe game with graphical user interface
In each turn, the user can put either X in an empty space
Once the user complete, then the computer will put an O randomly on the remaining space
In order to win, either the user or computer must put 3 O/X in a row/column/diagonal


1. construct a (3x3) matrix to store the X/O
2. init the matrix with (3x3) None values
3. When the user put a X at position (i,j), then change position to m_ij from None -> 1
4. exclude the chosen position, then let the program redomly pick new (i,j) and change the value from None -> 0
5. define win_rule: check whether user/computer wins at each turn: boolean function: False -> True

"""

import numpy as np
import random


# initialise the playground
def box(size: int = 3):
    return np.array([[None for _ in range(size)] for _ in range(size)])


def init_plot(data):
    # data = box informatin
    print("This is the layout of the tic-tac-toe")
    print("------------")
    for k in range(3):
        for i in range(3):
            if data[k][i] == None:
                print(str(i + k * 3 + 1) + "|", end="")
        print("\n------------")


# def plot playground
def plot(data):
    # data = box informatin
    print("------------")
    for k in range(3):
        for i in range(3):
            if data[k][i] == None:
                print("   " + "|", end="")
            elif data[k][i] == 1:
                print("X" + "|", end="")
            elif data[k][i] == 0:
                print("O" + "|", end="")
        # print("\n")
        print("\n-------------")


# define win rule:
def check_not_win(data):
    n = len(data)
    # Check row and columns
    for i in range(n):
        if np.all(data[i, :] == np.ones(n)) or np.all(data[:, i] == np.ones(n)):
            print("player wins")
            return False
        elif np.all(data[i, :] == np.zeros(n)) or np.all(data[:, i] == np.zeros(n)):
            print("computer wins")
            return False
    # check diagonal
    if np.all(np.diagonal(data) == np.ones(n)):
        print("player wins")
        return False
    elif np.all(np.diagonal(np.fliplr(data)) == np.zeros(n)):
        print("computer wins")
        return False
    return True


if __name__ == "__main__":
    # init the box
    data = box()
    # init plot
    init_plot(data)

    pos_dict = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
    }
    num_none = 9
    not_win = True
    while (not_win) and (num_none > 0):
        result = input("Enter the position number (1-9)")
        if (int(result) < 1) or (int(result) > 9):
            raise ValueError(" input position should be within 1 - 9")
        elif result not in pos_dict:
            print("The position is occupied, please choose the other")
            # skip current loop
            continue
        # extract the result from dict
        pos = pos_dict[result]
        x, y = int(pos[0]), int(pos[1])
        # delete the value from dict
        pos_dict.pop(result)

        # Player Turn
        if data[x, y] == None:
            data[x, y] = 1
            print("player turn")
            plot(data)
            num_none -= 1
        else:
            print("The space is occupied, please choose the other")

        # Computer turn
        if len(pos_dict) > 0:
            random_key = random.choice(list(pos_dict.keys()))
            pos_comp = pos_dict[random_key]
            x_comp, y_comp = int(pos_comp[0]), int(pos_comp[1])
            pos_dict.pop(random_key)
            if data[x_comp, y_comp] == None:
                data[x_comp, y_comp] = 0
                print("computer turn")
                plot(data)
                num_none -= 1
            else:
                print("The space is occupied, please choose the other")
        # Check Win when player & computer finish their turn
        not_win = check_not_win(data)
        print(f"reamining none {num_none}")
    print("Game Over")
