from karel.stanfordkarel import *

def back():
    turn_left()
    turn_left()
    while front_is_clear(): 
         move()

def fnp():
    while front_is_clear(): 
         move()
         put_beeper()

def straight():
    turn_left()
    turn_left()
    turn_left()

def left():
    straight()
    if front_is_clear():
         move()
         put_beeper()
         straight()
         fnp()
         back()
         left()
    else: 
         turn_left()
         back()

def main():
   put_beeper()
   fnp()
   back()
   left()
        
if __name__ == '__main__':
    main()
