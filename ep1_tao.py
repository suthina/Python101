Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.right(90)
>>> tao.right(90)
>>> tao.left(180)
>>> tao.forword(100)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tao.forword(100)
AttributeError: 'Turtle' object has no attribute 'forword'. Did you mean: 'forward'?
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.clear()
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 
...     
>>> tao.penup()
>>> tao.goto(200,200)
>>> tao.goto(200,-200)
>>> tao.pendown()
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 
...     
>>> tao.clear()
>>> tao.penup()
>>> tao.goto(0,0)
>>> tao.circle(30)
>>> tao.pendown()
>>> tao.circle(60)
>>> tao.penup()
>>> tao.goto(100,100)
>>> tao.clear
<bound method RawTurtle.clear of <turtle.Turtle object at 0x0000026250E407D0>>
tao.clear()
tao.goto(0,0)
tao.goto(100,100)
tao.pendown()
tao.left(45)
tao.forward(50)
tao.right(45)
tao.right(45)
tao.forword(45)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tao.forword(45)
AttributeError: 'Turtle' object has no attribute 'forword'. Did you mean: 'forward'?
tao.forward(45)
tao.rigth(90)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tao.rigth(90)
AttributeError: 'Turtle' object has no attribute 'rigth'. Did you mean: 'right'?
tao.right(90)
tao.forward(60)
tao.forward(20)
tao.right(90)
tao.forward(80)
tao.undo(80)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    tao.undo(80)
TypeError: RawTurtle.undo() takes 1 positional argument but 2 were given
tao.undo()
tao.undo()
tao.forward(20)
tao.right(90)
tao.forward(100)
tao.right(90)
tao.forward(20)
tao.undo()
tao.forward(45)
tao.right(90)
tao.forward(50)
tao.left(45)
tao.forward(10)
tao.penup()
tao.goto(0,0)
tao.clear()
tao.circle(80)
tao.pendown()
tao.fillcolor(violet)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tao.fillcolor(violet)
NameError: name 'violet' is not defined
tao.fillcolor('violet')
tao.circle(80)
