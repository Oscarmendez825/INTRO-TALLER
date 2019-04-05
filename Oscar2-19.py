Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [1, 2, 5, 8, 0, 50]
>>> x [0]
1
>>> x[5]
50
>>> x[-1]
50
>>> x[-6]
1
>>> x[3:]
[8, 0, 50]
>>> x[2:4]
[5, 8]
>>> x.insert(3, 45)
>>> x
[1, 2, 5, 45, 8, 0, 50]
>>> x.remove(45)
>>> x
[1, 2, 5, 8, 0, 50]
>>> x.reverse()
>>> x
[50, 0, 8, 5, 2, 1]
>>> x.sort()
>>> x
[0, 1, 2, 5, 8, 50]
>>> x.pop()
50
>>> x
[0, 1, 2, 5, 8]
>>> x.append(50)
>>> x
[0, 1, 2, 5, 8, 50]
>>> 
