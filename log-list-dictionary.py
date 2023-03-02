Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 3, in <module>
    with open('data.txt','w',endcoding='utf-8') as file:
TypeError: 'endcoding' is an invalid keyword argument for open()

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 3, in <module>
    with open('data.txt','w',endcoding='utf-8') as file:
TypeError: 'endcoding' is an invalid keyword argument for open()

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 12, in <module>
    adddata('น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาท')
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 10, in adddata
    filr.write(text)
NameError: name 'filr' is not defined. Did you mean: 'file'?

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
Traceback (most recent call last):
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 13, in <module>
    adddata('ดินสอ 10 บาท')
  File "C:/Users/ACER/Desktop/suthina/Python 101/writefile.py", line 10, in adddata
    file.writeสรืำ(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeสรืํา'

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
['น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทปากกา 10 บาท\n', 'ยางลบ 10 บาท\n', 'ยางลบ 10 บาท\n', 'สมุดวาดรูป 6 บาท\n', 'กบเหลา 3 บาท\n']

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
['น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทปากกา 10 บาท\n', 'ยางลบ 10 บาท\n', 'ยางลบ 10 บาท\n', 'สมุดวาดรูป 6 บาท\n', 'กบเหลา 3 บาท\n', 'ยางลบ 10 บาท\n', 'สมุดวาดรูป 6 บาท\n', 'กบเหลา 3 บาท\n']

======== RESTART: C:/Users/ACER/Desktop/suthina/Python 101/writefile.py ========
น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทปากกา 10 บาท
ยางลบ 10 บาท
ยางลบ 10 บาท
สมุดวาดรูป 6 บาท
กบเหลา 3 บาท
ยางลบ 10 บาท
สมุดวาดรูป 6 บาท
กบเหลา 3 บาท

box = []
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')
print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
print(box[])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
box.append('ปากกา')
print(box[1])
ดินสอ
print(box[0])
ปากกา
print(box[2])
ยางลบ
print(box[1])
ดินสอ
print(box[-2])
ยางลบ
print(box[-3])
ดินสอ
print(box[-4])
ปากกา
print(box[-5])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(box[-5])
IndexError: list index out of range
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['hourse','staedtler'],'eraser':'ยางลบ2ไทย'}
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['hourse','staedtler'],'eraser':'ยางลบ2สี'}
print(brand['pen'][1])
Pentel
print(brand['pen'][0])
Lamy
print(brand['pencil'][1])
staedtler
print(brand['pencil'][0])
hourse
print(brand['eraser'][0])
ย
print(brand['eraser']
      )
ยางลบ2สี
print(brand['eraser']
      print(brand['eraser']
            
SyntaxError: '(' was never closed
print(brand['eraser'])
            
ยางลบ2สี
print(brand['eraser'])
            
ยางลบ2สี
print(brand['eraser'][0])
            
ย
print(brand['pencil'][0])
            
hourse
brand = {'pen':['Lamy','Pentel','Fiber-castel'],'pencil':['hourse','staedtler'],'eraser':'ยางลบ2สี'}
            
print(brand['eraser'])
            
ยางลบ2สี
print(box)
            
['ปากกา', 'ดินสอ', 'ยางลบ', 'ปากกา']
print(brand.keys())
            
dict_keys(['pen', 'pencil', 'eraser'])
print(brand.values())
            
dict_values([['Lamy', 'Pentel', 'Fiber-castel'], ['hourse', 'staedtler'], 'ยางลบ2สี'])
for b in box :
        print(b)

            
ปากกา
ดินสอ
ยางลบ
ปากกา
>>> for br in brand.keys():
...             print(br)
... 
...             
pen
pencil
eraser
>>> for br in brand.values():
...             print(br)
... 
...             
['Lamy', 'Pentel', 'Fiber-castel']
['hourse', 'staedtler']
ยางลบ2สี
>>> for br in brand:
...             print(br)
... 
...             
pen
pencil
eraser
>>> for br in brand.items:
...             print(br)
... 
...             
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for br in brand.items:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for br in brand.items():
...             print(br)
... 
...             
('pen', ['Lamy', 'Pentel', 'Fiber-castel'])
('pencil', ['hourse', 'staedtler'])
('eraser', 'ยางลบ2สี')
>>> len(brand)
...             
3
