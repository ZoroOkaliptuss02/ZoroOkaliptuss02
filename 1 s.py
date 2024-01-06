import turtle
window = turtle.Screen()
window.title("Minecraft benzeri Oyun")
window.bgcolor("skyblue")


player = turtle.Turtle()
player.shape("square")
player.color("yellow")
player.penup()
player.speed(0)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)


window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")


while True:
    window.update()
    import tkinter as tk

 
def hide_tkinter_window():
    root = turtle.Screen()._root
    root.iconify()

#ESC tuşuna basıldığında çalışacak fonksiyon
def on_key_press():
    turtle.bye()  # Turtle penceresini kapat

# Ana program
screen = turtle.Screen()
screen.onkey(on_key_press, "Escape")  # ESC tuşuna basıldığında on_key_press fonksiyonunu çağır
screen.listen()  # Tuş girişlerini dinle

# Tkinter penceresini gizle
hide_tkinter_window()

# Ana döngüyü başlat
turtle.mainloop()

import turtle

def on_esc_press():
    window.bye()

window = turtle.Screen()
window.title("Minecraft benzeri Oyun")
window.bgcolor("skyblue")

player = turtle.Turtle()
player.shape("square")
player.color("yellow")
player.penup()
player.speed(0)

def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def move_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

window.listen()
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(on_esc_press, "Escape")  # ESC tuşuna basıldığında on_esc_press fonksiyonunu çağır

while True:
    window.update()
