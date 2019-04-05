Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 57958
>>> X % 10

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    X % 10
NameError: name 'X' is not defined
>>> x % 10
8
>>> x = X // 10

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = X // 10
NameError: name 'X' is not defined
>>> x = x // 10
>>> x
5795
>>> 
