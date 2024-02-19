def on_button_pressed_a():
    global Feeling
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . # . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . # . .
        . # . . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . # . .
        . . . # .
        . # # # .
        . # # # #
        . . . # #
        """)
    Feeling = randint(1, 2)
    if Feeling == 1:
        basic.show_icon(IconNames.HAPPY)
    if Feeling == 2:
        basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.show_icon(IconNames.TORTOISE)
    Feeling += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global energy
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . # # #
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . # # #
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        # # # # #
        . # . # .
        . . . . .
        """)
    energy += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Feeling, Food
    basic.show_leds("""
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . # . . .
        . . . . .
        . . . # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . # . . .
        . . # # .
        . . # # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # .
        . . # # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . # #
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        """)
    Feeling = randint(1, 2)
    if Feeling == 1:
        basic.show_icon(IconNames.HAPPY)
    if Feeling == 2:
        basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.show_icon(IconNames.TORTOISE)
    Food += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global Coin, fun
    basic.show_string("Coin flip!")
    Coin = randint(1, 2)
    if Coin == 1:
        basic.show_icon(IconNames.STICK_FIGURE)
        basic.pause(1000)
        basic.show_string("You Won!")
    if Coin == 2:
        basic.show_icon(IconNames.TORTOISE)
        basic.pause(1000)
        basic.show_string("I Won!")
    basic.show_icon(IconNames.TORTOISE)
    fun += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

fun = 0
Coin = 0
Food = 0
energy = 0
Feeling = 0
basic.show_icon(IconNames.TORTOISE)
basic.pause(1000)
basic.show_leds("""
    # . # . #
    # . # . .
    # # # . #
    # . # . #
    # . # . #
    """)
basic.pause(1000)
basic.show_icon(IconNames.TORTOISE)
Bigturtle = images.create_big_image("""
    . . . # # # . . # .
    . . # # # # # . . #
    . # # # # # # # . .
    . . # # # # # # . .
    . . # . . # . . . .
    """)

def on_forever():
    if energy == 1 and fun == 1 and Feeling == 1 and Food == 1:
        basic.show_string("Goodnight!")
        basic.show_icon(IconNames.HEART)
        basic.pause(1000)
        basic.show_string("ZZZ")
        Bigturtle.scroll_image(1, 200)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.pause(10000000000)
basic.forever(on_forever)

def on_forever2():
    global energy, Feeling, Food, fun
    if energy == 2:
        energy += -1
    if Feeling == 2:
        Feeling += -1
    if Food == 2:
        Food += -1
    if fun == 2:
        fun += -1
basic.forever(on_forever2)
