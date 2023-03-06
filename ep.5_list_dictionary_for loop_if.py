Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = ['somchai','somsak','somsri']
friend.append('sompong')
print(friend)
['somchai', 'somsak', 'somsri', 'sompong']
friend.remove('somsak')
print(friend)
['somchai', 'somsri', 'sompong']
del friend[0]
print(friend)
['somsri', 'sompong']
print(friend[0])
somsri
number =[5,1,6,7,9]
number.sort()
print(number)
[1, 5, 6, 7, 9]
del number[0]
print(number)
[5, 6, 7, 9]
del number[-1]
print (number)
[5, 6, 7]
number[0]+number[1]+number[2]
18
print(sum(number))
18
tel = {'eak':'0856541111','faa':'0896391555','loong':'0812345678'}
print(tel[eak])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(tel[eak])
NameError: name 'eak' is not defined
print(tel['eak'])
0856541111
print(tel['faa'])
0896391555
tel['eak'] = '0899999999'
print(tel)
{'eak': '0899999999', 'faa': '0896391555', 'loong': '0812345678'}
tel.item()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tel.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
tel.items()
dict_items([('eak', '0899999999'), ('faa', '0896391555'), ('loong', '0812345678')])
for f in friend:
    print(f)

    
somsri
sompong
for i in range(5):
    print(i)

    
0
1
2
3
4
list(rang(5))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(rang(5))
NameError: name 'rang' is not defined. Did you mean: 'range'?
list(range(5))
[0, 1, 2, 3, 4]
for i in [0,1,2,3,4]:
    print(i)

    
0
1
2
3
4
for t in tel.items():
    print(t)

    
('eak', '0899999999')
('faa', '0896391555')
('loong', '0812345678')
for t in tel.items():
    print(t[1])

    
0899999999
0896391555
0812345678
for t in tel.values():
    print(t)

    
0899999999
0896391555
0812345678
for t in tel.key():
    print(t)

    
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for t in tel.key():
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
for t in tel.keys():
    print(t)

    
eak
faa
loong
import time
while True:
    print('สวัสดีวันอังคาร')
    time.sleep(1)

    
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
Traceback (most recent call last):
  File "<pyshell#54>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt

KeyboardInterrupt
KeyboardInterrupt
while False:
    print('hello')

    
while False:
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')

    
friend = 'Tuu'
while friend == 'Tuu':
    print("Let's go")

    
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Traceback (most recent call last):
  File "<pyshell#67>", line 2, in <module>
    print("Let's go")
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
def YourMoney(money):
    if money > 300:
        print('กินบุฟเฟ่กัน')
    else money > 200:
        
SyntaxError: expected ':'
    elif money > 200:
        
SyntaxError: unexpected indent
def YourMoney(money):
    if money >300:
        print('กินบุฟเฟ่กัน')
    elif money >200:
        print('กินซูชิ')
    else :
        print('ข้าวแกง')

        
YourMoney(400)
กินบุฟเฟ่กัน
YourMoney(300)
กินซูชิ
def YourMoney(money):
    if money >= 300:
        print('กินบุฟเฟ่กัน')
    elif money >= 200:
        print('กินซูชิ')
    else :
        print('ข้าวแกง')

        
YourMoney(300)
กินบุฟเฟ่กัน
True
True
False
False
if True:
    print('hi')

    
hi
if False:
    print('hi')

    
money = 100
while money <= 100:
    print('ยอดเงินในบัญชี')
    time.sleep(1)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> money = 100
>>> while money <= 100:
...     print('ยอดเงินในบัญชี')
...     time.sleep(1)
... 
...     
ยอดเงินในบัญชี
ยอดเงินในบัญชี
ยอดเงินในบัญชี
ยอดเงินในบัญชี
ยอดเงินในบัญชี
ยอดเงินในบัญชี
Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> KeyboardInterrupt
>>> def checkage(friend):
...     for f in friend.item():
...         if f[1] >= 20 :
...             print(f[0], f[1])
... 
...             
>>> friend = {'somchai':17,'simsak' :15,'sompong':21}
>>> checkage(friend)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    checkage(friend)
  File "<pyshell#104>", line 2, in checkage
    for f in friend.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> def checkage(friend):
...     for f in friend.items():
...         if f[1] >= 20 :
...              print(f[0], f[1])
... 
...              
>>> friend = {'somchai':17,'simsak' :15,'sompong':21}
>>> checkage(friend)
sompong 21
>>> friend = {'somchai':17,'simsak' :15,'sompong':21,'somkiat':25}
>>> checkage(friend)
sompong 21
somkiat 25
