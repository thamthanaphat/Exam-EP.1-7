Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World
import turtle
T= turtle.Pen()
T.shap("turtle")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    T.shap("turtle")
AttributeError: 'Turtle' object has no attribute 'shap'. Did you mean: 'shape'?
T.shape("turtle")
for i in rang(200):
    t.circle(120-i,20)
    t.left(20)
    t.circle(120-i,20)
    t.left(5)

    
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for i in rang(200):
NameError: name 'rang' is not defined. Did you mean: 'range'?

for i in range(200):
    t.circle(120-i,20)
    t.left(20)
    t.circle(120-i,20)
    t.left(5)

    
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    t.circle(120-i,20)
NameError: name 't' is not defined. Did you mean: 'T'?
for i in rang(200):
    T.circle(120-i,20)
    T.left(20)
    T.circle(120-i,20)
    T.left(5)

    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    for i in rang(200):
NameError: name 'rang' is not defined. Did you mean: 'range'?
for i in range(200):
...     T.circle(120-i,20)
...     T.left(20)
...     T.circle(120-i,20)
...     T.left(5)
... 
...     

... T.clear()
>>> T.clear()
>>> 
>>> T.reset()
>>> for i in range(400):
...     T.circle(190-i,90)
...     T.left(90)
...     T.circle(190-i,90)
...     T.left(10)
... 
...     

