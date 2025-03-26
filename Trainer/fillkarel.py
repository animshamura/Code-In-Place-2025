from karel.stanfordkarel import *

def put():
    move()
    put_beeper()

def turns():
    turn_left()
    turn_left()

def moves():
    move()
    move()
    move()
    move()

def fill():
    put_beeper()
    put()
    put()
    put()
    put()

def backnup():
    turns()
    moves()
    turns()
    turn_left()
    move()
    turns()
    turn_left()
  
def fnb():
    fill()
    backnup()
  
def main():
   
    fnb()
    fnb()
    fnb()
    fnb()
    fill()

if __name__ == '__main__':
    main()
