import graphics as g
from math import *

win = g.GraphWin(title="My Window",width=500,height=500)
win.setBackground("red") #send the setBackground message which makes win's background red
p = g.Point(250, 250) #created a point object with attributes x=250 y=250
p.move(100,0) # move(dx,dy), self.x + dx becomes the new self.x for p
p.draw(win)
c = g.Circle(p, 20)
c.setFill("green")
c.draw(win)

alias_c = c
alias_c.setFill("yellow")

clone_c = c.clone()
clone_c.move(-100,0)
clone_c.setFill("green")
clone_c.draw(win)

r = g.Rectangle(g.Point(0,0), g.Point(240, 240))
r.setFill("purple")
r.draw(win)

s = str("hi")
s = int(10)

class Teacher:
  def __init__(self, name):
    self.name = name

class Student:
  def __init__(self, name, gpa, adr, teacher):
    print("init was called with these value:", name, gpa)
    # this is what data a student object holds
    self.name = name
    self.gpa = gpa
    self.adr = adr
    self.favorite_teacher = teacher

  def print_student_information(self):
    print(self.name, "lives at", self.adr)
  
  def print_teacher(self):
    print(self.favorite_teacher.name, "teaches", self.name)

s1 = Student("Matthew", 2.0, 'somehwere', Teacher("Matt's teacher"))
s2 = Student("Casey", 4.5, "somehwere else", Teacher("Casey's teacher"))
my_str = "cat"
print(s2.gpa)
s2.print_teacher()
my_class = [s1,s2]
for student in my_class:
  student.print_student_information()
  student.print_teacher()

