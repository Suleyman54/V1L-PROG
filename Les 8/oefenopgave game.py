import random
def game(rows,cols):

    table = (rows*cols-1) * [''] + ['B']
    random.shuffle(table)
    while True:
        pos = input('Enter next position (format: x y):')
        position = pos.split()
        if table[int(position[0])-1*cols + int(position[1])-1] == 'B':
            print('You found the bomb!')
            break
        else:
            print('No bomb at positions', pos)

game(3,3)
