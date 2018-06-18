string = 'string must be reversed'

reversed_string = ''
# print(string)
# print(list(string))
print('version 1 '.center(70,'-'))
for i in reversed(string):
    # print(''.join(i))
    reversed_string += ''.join(i)
print(reversed_string)


print('version 2 '.center(70,'-'))
for i in range(len(string)):
    print(string[-1*i], end='')

print()

print('version 3 '.center(70,'-'))
reversed_string = ''
for i in reversed(string):
    # print(i, end='')
    reversed_string += ''.join(i)

print(reversed_string)





d = ''
for i in reversed(string):
    d += ''.join(i)
print(d)


from random import randint
sizeX, sizeY = 800, 600
pointX = randint(0,1080)
pointY =  randint(0,720)
print('x = {}, y = {}'.format(pointX, pointY))
indexX = 0
found = False
for y in range(0,sizeY):# Y
    indexX +=1
    if found == True:
        break
    for x in range(0,sizeX): # X
        indexX +=1
        if  x == pointX and y == pointY:
            print('coordinats of found at point X = {}, Y = {}\nafter {} attemps'.format(x, y, indexX))
            found = True
            # break
            # else:
            #     continue
            # print(found)
            # if (y == sizeY and x == sizeX) and found == False:
            #     print('no broken pixels')



ysize = 20
xsize = 20
pointy = randint(0,20)
pointx = randint(0,20)
found = False
for y in range(0, ysize+1):
    if found == True:
        break
    for x in range(0, xsize+1):
        if x == pointx and y == pointy:
            found = True
            print("point was found at position {} {}".format(x,y))
        else:
            continue



# import requests
#
# r = requests.get('https://api.github.com/events')
# # print(r.headers)
# print('Date ', r.headers['Date'])
# print('status_code ', r.status_code)
# print('history ', r.history)
# # print(r.json())
# print('url ', r.url)


