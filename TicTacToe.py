from msvcrt import getch

pos = [0, 0]

def fright():
    global pos
    pos[0] += 1

def fleft():
    global pos 
    pos[0] -= 1

def fup():
    global pos
    pos[1] += 1

def fdown():
    global pos
    pos[1] -= 1

while True:
    print('Distance from zero: ', pos)
    key = ord(getch())
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        print('selected')
    elif key == 32: #Space
        print('jump')
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            print('down')
            fdown
        elif key == 72: #Up arrow
            print('up')
            fup()
        elif key == 75: #Left arrow
            print('left')
            fleft()
        elif key == 77: #Right arrow
            print('right')
            fright()