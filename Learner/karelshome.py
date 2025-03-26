from karel.stanfordkarel import *

def move_down():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

def move_left():
    turn_left()
    turn_left()
    move()

def move_up():
    turn_left()
    turn_left()
    turn_left()
    move()

def move_straight():
    turn_left()
    move()
    move()
    turn_left()
    turn_left()

def main():
    move()
    move()
    move_down()
    move()
    pick_beeper()
    move_left()
    move_up()
    move_straight()

if __name__ == '__main__':
    main()
