from microbit import *

# Created by: Adam Derango
# 
# Date: september 28
# 
# This sets the hungryness level to 0 on start
hungryness = 0
# Created by: Adam Derango
# 
# Date: september 28
# 
# This adds 1 to the hungryness each time you press A 
# and resets the counter to zero each time you press B

def on_forever():
    global hungryness
    if input.button_is_pressed(Button.A):
        hungryness = hungryness + 1
        basic.show_number(hungryness)
    elif input.button_is_pressed(Button.B):
        hungryness = 0
        basic.show_number(hungryness)
basic.forever(on_forever)
