import graphics as gr

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Dog:
  def __init__(self, name:str, owner:Person):
    self.name = name
    self.owner = owner
  #the messages defined on a dog
  def bark(self):
    print("Roof Roof Roof", "said", self.name)
  def sit(self):
    print(self.name, "lazily sat down")
  def beg_for_food(self):
    print(self.name, "begged", self.owner.name, "for some food")


p1 = Person(name="Kern", age=400)
p2 = Person(name="Austin", age=1)
d = Dog("Fido",p2)
d.bark()
d.beg_for_food()
# rover = Dog(name="Rover", owner=p1)
# rover.beg_for_food()
# from graphics import *
def main():
    win = gr.GraphWin("Celsius Converter", 640, 400)
    x = gr.Point(x=320, y=320)
    x.draw(win)
    point_where_they_clicked = win.getMouse() #pauses until you click the window
    print(point_where_they_clicked.getX())
    x.undraw()
    point_where_they_clicked.draw(win)
    
#     # Draw the interface
#     Text(Point(1,3), "   Celsius Temperature:").draw(win)
#     Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
#     inputText = Entry(Point(2.25,3), 5)
#     inputText.setText("0.0")
#     inputText.draw(win)
#     outputText = Text(Point(2.25,1),"")
#     outputText.draw(win)
#     button = Text(Point(1.5,2.0),"Convert It")
#     button.draw(win)
#     Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

#     # wait for a mouse click
#     win.getMouse()

#     # convert input
#     celsius = float(inputText.getText())
#     fahrenheit = 9.0/5.0 * celsius + 32

#     # display output and change button
#     outputText.setText(round(fahrenheit,2))
#     button.setText("Quit")

#     # wait for click and then quit
#     win.getMouse()
#     win.close()
    
main()
