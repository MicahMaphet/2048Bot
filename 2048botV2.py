import keyboard
from PIL import ImageGrab, ImageOps
import pyautogui
import time

px = ImageGrab.grab().load()

# while 1:
#     px = ImageGrab.grab().load()
#     print(px[pyautogui.position().x, pyautogui.position().y])
#     if keyboard.is_pressed('g') and keyboard.is_pressed('h'):
#         break


pyautogui.FAILSAFE=False
outlineClr=(187, 173, 160)
foundEdge=False
x = 0
y = 0

class Board:
    c1 = [0, 0]
    c2 = [0, 0]
    c3 = [0, 0]
    c4 = [0, 0]

class Values:
    empty = (205, 193, 180)
    two = (238, 228, 218)
    four = (237, 224, 200)
    eight = (242, 177, 121)
    sixteen = (245, 149, 99)
    thirtyTwo = (246, 124, 95)
    sixtyFour = (246, 124, 95)
    oneTwentyEight = (237, 207, 114)
    twoFiftySix = (237, 204, 97)
    fiveOneTwo = (237, 200, 80)
    oneZeroTwoFour = 193
    twoZeroFourEight = 189


def FindEdge():
    px = ImageGrab.grab().load()
    pyautogui.FAILSAFE=False
    foundEdge=False
    for y in range(0, pyautogui.size().height, 14):
        for x in range(0, pyautogui.size().width, 14):
            color = px[x, y]
            if color == outlineClr:
                print(x, y)
                if px[x + 480, y] == outlineClr:
                    foundEdge=True
                break
            if keyboard.is_pressed('g') and keyboard.is_pressed('h'):
                break
        if keyboard.is_pressed('g') and keyboard.is_pressed('h'):
                break
        if foundEdge == True:
            break

    pyautogui.FAILSAFE=True

    board = Board
    if foundEdge:
        x+=5
        while color == outlineClr:
            y-=1
            color = px[x, y]
        y+=1
        color = px[x, y]
        board.c1[1] = y

        while color == outlineClr:
            x-=1
            color = px[x, y]
        y+=5
        color = px[x, y]
        while color == outlineClr:
            x-=1
            color = px[x, y]

        x+=1
        color = px[x, y]
        board.c1[0] = x
        board.c2[0] = board.c1[0] + 500
        board.c3[0] = board.c1[0]
        board.c4[0] = board.c1[0] + 500

        board.c2[1] = board.c1[1]
        board.c3[1] = board.c1[1] + 500
        board.c4[1] = board.c1[1] + 500
        '''
    c1-----c2
    |       |
    |       |
    c3-----c4
        '''
        print(board.c1[0], board.c1[1])
        pyautogui.moveTo(board.c1[0], board.c1[1])
        pyautogui.moveTo(board.c2[0], board.c2[1], 0.5)
        pyautogui.moveTo(board.c3[0], board.c3[1], 0.5)
        pyautogui.moveTo(board.c4[0], board.c4[1], 0.5)
        print(board)
    else:
        print("Error: could not find the board, try https://www.2048.org/")

FindEdge()
# 187, 173, 160 - the outline