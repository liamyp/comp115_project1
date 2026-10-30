import turtle
t = turtle.Turtle()
s = turtle.Screen()
def movement(x, y):
    t.goto(x, y)
    steps.append(f"t.goto({t.pos()})")
def while_drag(x, y):
    t.ondrag(None)
    t.pendown()
    t.goto(x, y)
    steps.append("t.pendown()")
    steps.append(f"t.goto({t.pos()})")
    steps.append("t.penup()")
    t.penup()
    t.ondrag(while_drag)
def colour():
    global c 
    c = turtle.textinput("colour", "please input colour")
    t.color(c)
    steps.append(f"t.color({c})")
    s.listen()
def size():
    g = turtle.textinput("size", "please input size")
    t.pensize(g)
    steps.append(f"t.pensize({g})")
    s.listen()
steps = ["import turtle", "t = turtle.Turtle()", "turtle.tracer(4, 0)", "t.penup()"]
c = "black"
t.shape("circle")
t.shapesize(2)
t.speed(0)
t.penup()
s.onscreenclick(movement, 3)
t.ondrag(while_drag)
s.onkeypress(colour, "c")
s.onkeypress(size, "g")
s.listen()
turtle.mainloop()
steps.append("turtle.mainloop()")
with open("destination.py", "w") as file:
    file.writelines(f"{item}\n" for item in steps)