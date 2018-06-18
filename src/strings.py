from test1 import ysize

s= list("Hello World!")
s2 =''
for i in range(len(s)):
    s2 += (s.pop(-1))
#     s2 += ''.join(s.pop(-1))
print(s2)

for i in range(1,len(s)+1):
    try:
        s2 += s[-1*i]
        print(' fff  ', s[-1*i], end='')
    except ValueError:
        pass
print('s2 ', s2)

# screenX, screenY = 100, 70
# pointX, pointY = 88, 15
# found = False
# index = 1
# for y in range(0, screenY+1):
#     if found == True:
#         break
#
#     for x in range(0, screenX+1):
#         index +=1
#         if x== pointX and y == pointY:
#             found = True
#             print('point position is ', x,y)
#         else:
#             continue
# print(index)


# screenX, screenY = 100, 70
# pointX, pointY = 88, 15
# found = False
# index = 1

#
# for y in range(0, screenY+1):
#     if found == True:
#         break
#
#     for x in range(0, screenX+1):
#         index +=1
#         if x== pointX and y == pointY:
#             found = True
#             print('point position is ', x,y)
#         else:
#             continue
# print(index)
#
#
#

screenX, screenY = 100, 70
pointX, pointY = 8, 15
found = False
index = 1
for y in range(0, screenY+1,11):
    index +=1
    if found == True:
        break
    for x in range(0, screenX+1):
        if x== pointX and y == pointY:
            found = True
            print('1 point position is ', x,y)
        elif x+1== pointX and y+1 == pointY:
            found = True
            print('2 point position is ', x,y)
        elif x+2== pointX and y+2 == pointY:
            found = True
            print('3 point position is ', x,y)
        elif x + 3 == pointX and y + 3 == pointY:
            found = True
            print('4 point position is ', x, y)
        else:
            continue
print(index)
b = ['', 'a', 'aa', 'aaa', 'a1aaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']
a = [x for x in range(10) if x != 9]
print(a)

print(set(b)-set(a))
screenX, screenY = 10, 16
pointX, pointY = 8, 15
brokenX = []
brokenY = ''
for y in range(0, screenY+1):
    index +=1
    [brokenX.append((y, x)) for y in range(0, screenY+1) if (y == pointY) and y not in brokenX
     for x in range(0, screenX+1) if (x == pointX) and (x) not in brokenX]

    # [brokenX.append(y, x) for y in range(0, screenY+1) if (y == pointY) and y not in brokenX]
    # [brokenX.append(x) for x in range(0, screenX+1) if (x == pointX) and x not in brokenX]
print(set(brokenX))
print(index)


data = [1,2,3,4,5,6,7,8,9,10,11]
target = 9
print(len(data))
def search(data):
    low = 0
    high = len(data)-1
    # print('start'.center(20,'='))
    while low <= high:
        md = (low + high) // 2
        print((low + high) )
        # print(('meridian '+str(md)).center(50,'='))
        if target == data[md]:
            print(' found', data[md])
            return True
        elif target < data[md]:
            high = md-1
        else:
            low = md + 1
    return False

print('search ', search(data))


import requests
# req = requests.get('https://cdn.pixabay.com/photo/2015/03/26/09/40/forest-690058_1280.jpg', stream=True)
# a = req.raise_for_status()
# print(a)
# with open('Forest.jpg', 'wb') as fd:
#     for chunk in req.iter_content(chunk_size=50000):
#         print('Received a Chunk')
#         fd.write(chunk)

# req = requests.post('https://mail.ru/', data = {'q':'Nanotechnology'})
# req = requests.post('https://mail.ru/')
ssn = requests.Session()
ssn.cookies.update({'visit-month': 'May'})

reqOne = ssn.get('http://httpbin.org/cookies')
print(reqOne.text)

# req.raise_for_status()
# with open('Nanotechnology.html', 'wb') as fd:
#     for chunk in req.iter_content(chunk_size=50000):
#         fd.write(chunk)


import random
import time, sys


def main():
    qa_team = ['Bogdan', 'Deepika', 'Kevin', 'Kimtan', 'Megha', 'Sharlin', 'Svitlana', 'Xiaoqing']
    for i in range(random.randint(30, 50)):
        volunteer = random.choice(qa_team)
        print( volunteer)
        sys.stdout.flush()
        time.sleep(.3)
        print( "\b" * (len(volunteer) + 1))

    print("%s!" % volunteer)



st = 'TOYOTA'
srevrs = ''
def rev(st):
    for i in range(1,len(st)+1):
        print(st[-1*i], end='')

rev(st)
print('\n')

y_size, x_size =70+1,99+1
point_x, point_y = 51, 20
index_x, index_y = 0,0
for y in range(y_size):
    index_y +=1
    for x in range(int(x_size/2)):
        # print(' X ', x)
        left = [x for x in range(0,(int(x_size/2)))]
        right = [x for x in range((int(x_size/2)),(x_size))]
        index_x +=1
        # from left to center
        if left[x] == point_x and y == point_y:
            found = True
            print('point was found on the left at x = {} y = {}'.format(left[x],y))
        if right[x] == point_x and y == point_y:
            found = True
            print('point was found on right at x = {} y = {}'.format(right[x],y))


print('index_x', index_x, 'index_y', index_y, ' total ', index_x+index_y)
# index_x 7000 index_y 70  total  7070



# ------------------------------

y_size, x_size =70+1,99+1
point_x, point_y = 51, 20

print('========================================================================================')

def searchnew(y):
    global x, left, right
    index_x, index_y = 0,0
    index_y += 1
    for x in range(int(x_size / 2)):
        # print(' X ', x)
        left = [x for x in range(0, (int(x_size / 2)))]
        right = [x for x in range((int(x_size / 2)), (x_size))]
        index_x += 1
        # from left to center
        if left[x] == point_x and y == point_y:
            # print('point was found on the left at x = {} y = {}'.format(left[x], y))
            return 'point was found on the left at x = {} y = {}'.format(left[x], y)
        if right[x] == point_x and y == point_y:
            # print('point was found on right at x = {} y = {}'.format(right[x], y))
            return 'point was found on right at x = {} y = {}'.format(right[x], y)
    # print('index_x', index_x, 'index_y', index_y, ' total ', index_x + index_y)
    # return ('index_x', index_x, 'index_y', index_y, ' total ', index_x + index_y)
    return ('index_x', index_x, 'index_y', index_y, ' total ', index_x + index_y)


a = searchnew(100)
print('===================================================')
for y in range(y_size):
    print(searchnew(y))

print('===================================================')
class SearchX():

    def __init__(self, x, size):
        self.x = x
        self.size  = size
        self.segment = 4
        self.segment1 = [x for x in range(0, (int(x_size / self.segment)))]
        self.segment2 = [x for x in range((int(x_size / self.segment)),self.size - ((int(x_size / self.segment)))*2)]
        self.segment3 = [x for x in range(self.size - ((int(x_size / self.segment)))*2,self.size - ((int(x_size / self.segment))))]
        self.segment4 = [x for x in range(self.size - ((int(x_size / self.segment))),x_size+1)]
        print('1  len =', len(self.segment1),self.segment1)
        print('2  len =', len(self.segment2),self.segment2)
        print('3  len =', len(self.segment3),self.segment3)
        print('4  len =', len(self.segment4),self.segment4)

        # for i in range(self.segment):
        #     i = Finder()

    # def runX(self):
    #
    #     for i in range(self.x+1/self.segment):



# class Finder():
#     def __init__(self, quantity):
#         self.qty = quantity



z = SearchX(1,100)

import numpy as np

aaa = [1,1,1,1,2,0,1]
ddd = [1,1,1,1,1,1,1]

def comp(a, b):
    for i in range(len(a)):
        print(a[i], '  ---  ',b[i])
        if a[i] != b[i]:
            print('found', a[i])

comp(aaa,ddd)

screenX, screenY = 100, 70
pointX, pointY = 88, 15
found = False
index = 1


for y in range(0, screenY+1):
    if found == True:
        break

    for x in range(0, screenX+1):
        index +=1
        if x == pointX and y == pointY:
            found = True
            print('1 point position is ', x,y)
        else:
            continue
print(' index ', index)
print('==================================================================')
f = 'More'

for i in range(1,len(f)+1):
    print(f[-1*i], end='')