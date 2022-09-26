import keyboard
from PIL import ImageGrab, ImageOps
import pyautogui
import time

px = ImageGrab.grab().load()


print(pyautogui.size())


# while 1:
    # print(pyautogui.position())
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

color = px[x, y]

class Board:
    c1 = [0, 0]
    c2 = [0, 0]
    c3 = [0, 0]
    c4 = [0, 0]
    tile = ['0  ', '0  ', '0  ', '0  ',
            '0  ', '0  ', '0  ', '0  ',
            '0  ', '0  ', '0  ', '0  ',
            '0  ', '0  ', '0  ', '0  ']
    tileWidth = 106.25
    
    width = 500 # it might not be 100 if it is zoomed in

board = Board

class Values:
    empty = (205, 193, 180)
    two = (238, 228, 218)
    four = (237, 224, 200)
    eight = (242, 177, 121)
    sixteen = (245, 149, 99)
    thirtyTwo = (246, 124, 95)
    sixtyFour = (246, 94, 59)
    oneTwentyEight = (237, 207, 114)
    twoFiftySix = (237, 204, 97)
    fiveOneTwo = (237, 200, 80)
    oneZeroTwoFour = 193
    twoZeroFourEight = 189

def FindEdge():
    print('Finding Board...')
    px = ImageGrab.grab().load()
    pyautogui.FAILSAFE=False
    foundEdge=False
    for y in range(0, pyautogui.size().height, 14):
        for x in range(0, pyautogui.size().width, 14):
            color = px[x, y]
            if color == outlineClr:
                print(x, y)
                # it has located a pixel with the same color as the board
                # it doesn't know for sure if it has located the board
                if px[x, y] == outlineClr:
                    for i in range(300):
                        foundEdge=True
                        x+=1
                        if px[x, y] != outlineClr:
                            foundEdge=False
                            break
                    x-=i    # it now knows it has located the board
                    if foundEdge==True:
                        break
            if keyboard.is_pressed('g') and keyboard.is_pressed('h'):
                pyautogui.FAILSAFE=True
                # this is to escape out because this uses pyautogui and could lock the mouse
                break
        if keyboard.is_pressed('g') and keyboard.is_pressed('h'):
                break
        if foundEdge == True:
            break

    pyautogui.FAILSAFE=True
    if foundEdge:
        x+=5
        while color == outlineClr:
            y-=1
            color = px[x, y]
            # it is finding the y of the board
        y+=1
        color = px[x, y]
        board.c1[1] = y
        # it now knows where the top of the board is
        while color == outlineClr:
            x-=1
            color = px[x, y]
        x-=5
        board.c1[0] = x

        # the curve of the board is 6 pixels, it has already exceeded by one pixel
        # now it knows the courdanites of the board, but not the dimensions, which are inconsistent from device to device.
        # sometimes the window is zoomed in which can make things more complicated
        y+=6
        color = px[x, y]

        while color == outlineClr:
            y+=1
            color = px[x, y]
        y+=5
        color = px[x, y]
        board.c3[1] = y
        board.width = board.c3[1] - board.c1[1]
        board.tileWidth = (board.width - 75) / 4
        # the width and height are the same
        board.c2[0] = board.c1[0] + board.width
        board.c3[0] = board.c1[0]
        board.c4[0] = board.c1[0] + board.width

        board.c2[1] = board.c1[1]
        board.c3[1] = board.c1[1] + board.width
        board.c4[1] = board.c1[1] + board.width
        '''
        c1-----c2
        |       |
        |       |
        c3-----c4
        '''
    else:
        print("Error: could not find the board, try https://www.2048.org/")



def TileQuard(tile):
    if tile >= 12:
        return board.c1[0] + (20 * (tile - 11)) + (board.tileWidth) * (tile - 12), board.c1[1] + (board.tileWidth * 3) + 80
    if tile >= 8:
        return board.c1[0] + (20 * (tile - 7)) + (board.tileWidth) * (tile - 8), board.c1[1] + (board.tileWidth * 2) + 60
    if tile >= 4:
        return board.c1[0] + (20 * (tile - 3)) + (board.tileWidth) * (tile - 4), board.c1[1] + board.tileWidth + 40
    if tile >= 0:
        return board.c1[0] + (20 * (tile + 1)) + (board.tileWidth) * tile, board.c1[1] + 20
    return 'Error', tile, 'is not a tile number'

def ScanTile(quard):
    color = px[quard[0], quard[1]]
    # print(color, Values.empty, quard[0], quard[1])
    if color == Values.empty:
        return '0  '
    if color == Values.two:
        return '2  '
    if color == Values.four:
        return '4  '
    if color == Values.eight:
        return '8  '
    if color == Values.sixteen:
        return '16 '
    if color == Values.thirtyTwo:
        return '32 '
    if color == Values.sixtyFour:
        return '64 '
    if color == Values.oneTwentyEight:
        return '128'
    if color == Values.twoFiftySix:
        return '256'
    if color == Values.fiveOneTwo:
        return '512'
    if color == outlineClr:
        return quard[0], quard[1], 'is the edge, needs a different quardanite'
    return 'Error: no tile found'

def ScanTiles():
    for i in range(16):
        board.tile[i] = ScanTile(TileQuard(i))
        print('tile', i, board.tile[i])

FindEdge()

px = ImageGrab.grab().load()
ScanTiles()
def DisplayTiles():
    print(board.tile[0], board.tile[1], board.tile[2], board.tile[3])
    print(board.tile[4], board.tile[5], board.tile[6], board.tile[7])
    print(board.tile[8], board.tile[9], board.tile[10], board.tile[11])
    print(board.tile[12], board.tile[13], board.tile[14], board.tile[15])

DisplayTiles()
print(board.width)

# 187, 173, 160 - the outline

# def testFun1(x):
#     print(x, x[0], x[1])

# def testFun2():
#     return [5, 1]

# testFun1(testFun2())