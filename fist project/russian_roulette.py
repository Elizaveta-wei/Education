# coding: utf-8

import turtle
# import tkSimpleDialog     # 2.x Python
import random
import math
import mrrobot

PHI = 360 / 7
R = 50

phi = 360 / 7
r = 50


def gotoxy(x, y):
    turtle.penup()  # поднимаем перо
    turtle.goto(x, y)  # перемещаем перо в указанную точку
    turtle.pendown()  # опускаем перо
    # turtle.circle()  # рисуем окружность


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


turtle.speed(0)


def draw_pistol(base_x, base_y):
    # основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)  # рисуем окружность
    # мушка
    gotoxy(base_x, base_y + 160)
    draw_circle(5, "red")
    # turtle.fillcolor('red')     # указать цвет
    # turtle.begin_fill()     # заполнить цвет
    # turtle.circle(5)       # нарисую окружность и укажу радиус
    # turtle.end_fill()       # закончить заполнение цветом
    # барабан
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "white")


draw_pistol(100, 100)


def rotate_pistol(base_x, base_y, start):
    global phi_rad, i
    for i in range(start, random.randrange(7, 100)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, "brown")
        draw_circle(22, "white")

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, "brown")
    return i % 7


# gotoxy(0, -50)
# turtle.circle(120)

answer = ''
start = 0
while answer != "N":
    answer = turtle.textinput("Играть?", "Y/N")
    # tkSimpleDialog.askstring("Нарисовать окружность","Y/N")    # for 2.x Python
    if answer == 'Y' or answer == 'y':
        start = rotate_pistol(100, 100, start)
        start = 0
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы приграли!", font=("Arial", 18, "normal"))

            z = random.randrange(0,3)
            if z ==0:
                robot.duble_files("test")
            elif z ==1:
                robot.random_delete("test")
            else:
                gotoxy(-100, -50)
                turtle.write("Вам повезло!", font=("Arial", 20, "normal"))
    else:
        pass

        # robot.duble_files('.')

        # turtle.penup() удаление линий перед
        # turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        # turtle.pendown() удаление линий после
        # turtle.fillcolor(random.random(), random.random(), random.random()) три числа те 3 цвета
        # turtle.begin_fill() перед рисованием замкнутой фигуры
        # turtle.circle(random.randrange(1, 100))
        # turtle.end_fill() после токо как фигура нарисована
