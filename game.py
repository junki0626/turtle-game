from turtle import Turtle, Screen

t = Turtle()  
screen = Screen() 
t.shape("turtle")
t.color("cyan")
screen.title("game")

screen.onscreenclick(t.goto)  
screen.mainloop() 
