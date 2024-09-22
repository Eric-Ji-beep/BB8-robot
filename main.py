# importing necessary libraries
from machine import Pin
import time
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
display.clear()
from machine import Pin, ADC
import micropythonSampleCode_AudioAmplifier
from xglcd_font import XglcdFont
import random



font = XglcdFont('Unispace12x24.c', 12, 24) # set desired font

soundSensor = ADC(28) # Pin where sensor device (Microphone) is connected
led = Pin('LED', Pin.OUT)
baseline = 25000 # You may need to change this, but your mic should be reading around here as a baseline. 
variability = 0.10 # By being more selective about what we conside a spike, we can filter out noise. 10% is a good base level for a quiet room. 
led = Pin('LED', Pin.OUT)
PirSensor = Pin(0, Pin.IN, Pin.PULL_DOWN)


def functions():
    while True:
        motion_det()
        sound_det()


def menu_message():
    display.clear()
    display.draw_text(180, 290, "Say something and I'll", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(150, 290, "generate a random math", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(120, 280, "problem, or wave at me", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(90, 270, "and I'll share a fun", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(60, 240, "fact with you!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    sleep(5)
    display.clear()
    static_face()


def static_face():
    display.fill_hrect(150, 80, 32, 32, color565(255, 251, 0))
    display.fill_hrect(150, 210, 32, 32, color565(255, 251, 0))
    display.fill_hrect(50, 72, 24, 180, color565(255, 251, 0))


def anim_face():
    i = 0
    while i < 3:
        display.fill_hrect(150, 80, 32, 32, color565(255, 251, 0))
        display.fill_hrect(150, 210, 32, 32, color565(255, 251, 0))
        display.fill_hrect(50, 72, 24, 180, color565(255, 251, 0))
        sleep(2.5)
        display.fill_hrect(150, 80, 32, 32, color565(0, 0, 0))
        display.fill_hrect(150, 210, 32, 32, color565(0, 0, 0))
        display.fill_hrect(150, 80, 10, 32, color565(255, 251, 0))
        display.fill_hrect(150, 210, 10, 32, color565(255, 251, 0))
        sleep(0.5)
        i += 1


def lightsaber():
    display.fill_rectangle(60, 40, 20, 60, color565(216, 213, 213))
    display.fill_rectangle(60, 50, 20, 5, color565(0, 0, 0))
    i = 0
    b = 100
    sleep(2)
    while i < 3:
        display.fill_rectangle(60, b, 20, 60, color565(85, 113, 236))
        sleep(2)
        i += 1
        b += 60
        
        
def star_creator(num_stars):
    i = 0
    while i < num_stars:
        x = random.randint(1, 238)
        y = random.randint(1, 318)
        #x = random.randint(110, 150)
        #y = random.randint(50, 280)

            
        if (((x < 110) or (x > 150))):
            display.fill_circle(x, y, 1, color565(255, 255, 255))
        elif (((x > 110) and (x < 150))): 
                if ((y < 35) or (y > 270)):
                    display.fill_circle(x, y, 1, color565(255, 255, 255))
        i += 1
        
        
# Note: Screen is (240x320 pixels)
def greeting():
    display.clear()
    font = XglcdFont('Unispace12x24.c', 12, 24)
    display.draw_text(119, 260, 'Hello, Jedi Master!', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    star_creator(200)
    micropythonSampleCode_AudioAmplifier.play_sound()
    time.sleep(5)
        
        
def math_problem_generator():
    problem_num = random.randint(0,3)
    if problem_num == 0:
        # addition
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        prob = str(x) + ' + ' + str(y)
        ans = x + y
    elif problem_num == 1:
        # subtraction
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if x > y:
            prob = str(x) + ' - ' + str(y)
            ans = x - y
        else:
            prob = str(y) + ' - ' + str(x)
            ans = y - x
    elif problem_num == 2:
        # multiplication
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        prob = str(x) + ' x ' + str(y)
        ans = x * y
    else:
        # division
        div_prob_num = random.randint(1, 10)
        if div_prob_num == 1:
            prob = '4 / 2'
            ans = 2
        elif div_prob_num == 2:
            prob = '8 / 4'
            ans = 2
        elif div_prob_num == 3:
            prob = '9 / 3'
            ans = 3
        elif div_prob_num == 4:
            prob = '24 / 3'
            ans = 8
        elif div_prob_num == 5:
            prob = '49 / 7'
            ans = 7
        elif div_prob_num == 6:
            prob = '15 / 5'
            ans = 3
        elif div_prob_num == 7:
            prob = '16 / 4'
            ans = 4
        elif div_prob_num == 8:
            prob = '64 / 16'
            ans = 4
        elif div_prob_num == 9:
            prob = '121 / 11'
            ans = 11
        else:
            prob = '54 / 9'
            ans = 6
    display.clear()
    micropythonSampleCode_AudioAmplifier.play_sound() # sound
    display.draw_text(160, 255, 'Your problem is: ', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(130, 180, prob, font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(100, 270, 'You have 10 seconds', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(70, 210, 'to solve.', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    #sleep(10)
    # timer for 10 seconds:
    for i in range(10):
        print(str(10-i))
        display.draw_text(40, 159, '  '+ str(10-i), font, color565(255, 251, 0), landscape=True, rotate_180=True)
        micropythonSampleCode_AudioAmplifier.beep_sound() # sound
        sleep(1)
    # Add sound for timer ending
    display.clear()
    display.draw_text(140, 215, "Time's up!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(110, 260, 'I hope you got ' + str(ans) + '.', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    sleep(10) # ten seconds to see answer


def sound_det():
    #print(soundSensor.read_u16())
    # If we detect a spike in the waveform greater than a 10% deviation from our baseline, someone is probably talking.
    if soundSensor.read_u16() > (baseline + baseline*variability) or soundSensor.read_u16() < (baseline - baseline*variability):
        display.clear()
        print('Sound detected') # prints to console only
        # add sound effect
        msg = 'Math problem'
        display.draw_text(137, 210, msg, font, color565(255, 251, 0), landscape=True, rotate_180=True)
        msg2 = 'generating...'
        display.draw_text(111, 225, msg2, font, color565(255, 251, 0), landscape=True, rotate_180=True)
        lightsaber()
        math_problem_generator()
        sleep(5)
        display.clear()
        anim_face()
        display.clear()
        menu_message()


def fun_fact_generator():
    display.clear()
    display.draw_text(120, 260, "Fact generating...", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    lightsaber()
    display.clear()
    fact_num = random.randint(1,10)
    micropythonSampleCode_AudioAmplifier.play_sound() # sound
    if fact_num == 1:
       display.draw_text(180, 312, "The world's largest pizza ", font, color565(255, 251, 0), landscape=True, rotate_180=True)
       display.draw_text(150, 300, "ever made was over 122", font, color565(255, 251, 0), landscape=True, rotate_180=True)
       display.draw_text(120, 265, "feet in diameter!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
       display.draw_text(90, 290, "It was created in Rome,", font, color565(255, 251, 0), landscape=True, rotate_180=True)
       display.draw_text(60, 290, "Italy, in December 2012.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 2:
        display.draw_text(180, 290, "Did you know that some", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 312, "cats are actually allergic", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 290, "to humans? Just like ", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 300, "some people are allergic", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 290, "to cats, it can happen", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(30, 305, "the other way around too!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 3:
        display.draw_text(180, 290, "Cows have best friends!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 319, "They often form close bonds", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 295, "with other cows in their", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 265, "herd and prefer to", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 270, "spend time with them.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 4:
        display.draw_text(180, 310, "There are more stars in the", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 295, "universe than grains of", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 310, "sand on all the beaches on", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 255, "Earth combined!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 230, "Just imagine", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(30, 305, "how many stars there are!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 5:
        display.draw_text(180, 300, "The electric eel produces", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 312, "electricity strong enough", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 300, "to power 10 light bulbs!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 300, "They use this ability to ", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 310, "stun their prey and defend", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(30, 310, "themselves from predators.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 6:
        display.draw_text(180, 290, "A group of flamingos is", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 300, 'called a "flamboyance."', font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 280, "Just imagine seeing a", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 300, "flamboyance of flamingos", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 280, "all standing together!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 7:
        display.draw_text(180, 290, "The Eiffel Tower can be", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 270, '15cm taller during', font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 230, "the summer!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 300, "This is because the metal", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 300, "expands when it gets hot.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 8:
        display.draw_text(180, 300, "The smell of freshly cut", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 280, 'grass is actually a', font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 240, "distress call!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 270, "When grass is cut, it", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 316, "releases a chemical signal", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(30, 305, "that warns nearby plants.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    elif fact_num == 9:
        display.draw_text(180, 280, "The shortest recorded", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 280, 'war in history lasted', font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 250, "only 23 minutes!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 290, "It was between Britain", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 290, "and Zanzibar in 1896.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    else:
        display.draw_text(180, 270, "Honey never spoils!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(150, 305, 'Archaeologists have found', font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(120, 300, "pots of honey in ancient", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(90, 290, "Egyptian tombs that are", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(60, 300, "3,000 years old and still", font, color565(255, 251, 0), landscape=True, rotate_180=True)
        display.draw_text(30, 270, "perfectly edible.", font, color565(255, 251, 0), landscape=True, rotate_180=True)
    sleep(15)
    display.clear()
    display.draw_text(150, 260, 'I hope you enjoyed', font, color565(255, 251, 0), landscape=True, rotate_180=True)
    display.draw_text(120, 210, "the fact!", font, color565(255, 251, 0), landscape=True, rotate_180=True)
       
       
def motion_det():
    if PirSensor.value() == 1: # status of PIR output
        display.clear()
        print('motion detected') # print the response
        fun_fact_generator()
        time.sleep(4)
        display.clear()
        anim_face()
        display.clear()
        menu_message()
    else:
        print("no motion")
        time.sleep(0.5)
   
   
def main_menu():
    display.clear()
    menu_message()
    
 
# Running the Code:
greeting()
main_menu()
functions()
