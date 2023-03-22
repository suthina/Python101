Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyperclip
>>> pyperclip.copy('สวัสดีจ้าาา')
>>> t = pyperclip.plaste()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t = pyperclip.plaste()
AttributeError: module 'pyperclip' has no attribute 'plaste'. Did you mean: 'paste'?
>>> t = pyperclip.paste()
>>> print(t)
Are you overpaying your bank? ; 100 THB, 2.91971 USD ; 250 THB, 7.29927 USD ; 500 THB, 14.59855 USD ; 1000 THB, 29.19710 USD.
