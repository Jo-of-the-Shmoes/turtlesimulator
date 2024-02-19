input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . # . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . # . .
        . # . . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . # . .
        . . # . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . # . .
        . . . # .
        . # # # .
        . # # # #
        . . . # #
        `)
    Feeling = randint(1, 2)
    if (Feeling == 1) {
        basic.showIcon(IconNames.Happy)
    }
    if (Feeling == 2) {
        basic.showIcon(IconNames.Heart)
    }
    basic.pause(2000)
    basic.showIcon(IconNames.Tortoise)
    Feeling += 1
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # # #
        . . # # #
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . # # # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # # #
        . . # # #
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # . # .
        . . . . .
        `)
    energy += 1
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . # . . .
        . . . . .
        . . . . .
        . . . . #
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        . . . . .
        . . . # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . # . . .
        . . # # .
        . . # # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # # .
        . . # # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . # #
        . . . # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . #
        `)
    Feeling = randint(1, 2)
    if (Feeling == 1) {
        basic.showIcon(IconNames.Happy)
    }
    if (Feeling == 2) {
        basic.showIcon(IconNames.Heart)
    }
    basic.pause(2000)
    basic.showIcon(IconNames.Tortoise)
    Food += 1
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Coin flip!")
    Coin = randint(1, 2)
    if (Coin == 1) {
        basic.showIcon(IconNames.StickFigure)
        basic.pause(1000)
        basic.showString("You Won!")
    }
    if (Coin == 2) {
        basic.showIcon(IconNames.Tortoise)
        basic.pause(1000)
        basic.showString("I Won!")
    }
    basic.showIcon(IconNames.Tortoise)
    fun += 1
})
let fun = 0
let Coin = 0
let Food = 0
let energy = 0
let Feeling = 0
basic.showIcon(IconNames.Tortoise)
basic.pause(1000)
basic.showLeds(`
    # . # . #
    # . # . .
    # # # . #
    # . # . #
    # . # . #
    `)
basic.pause(1000)
basic.showIcon(IconNames.Tortoise)
let Bigturtle = images.createBigImage(`
    . . . # # # . . # .
    . . # # # # # . . #
    . # # # # # # # . .
    . . # # # # # # . .
    . . # . . # . . . .
    `)
basic.forever(function () {
    if (energy == 2) {
        energy += -1
    }
    if (Feeling == 2) {
        Feeling += -1
    }
    if (Food == 2) {
        Food += -1
    }
    if (fun == 2) {
        fun += -1
    }
})
basic.forever(function () {
    if (energy == 1 && fun == 1 && Feeling == 1 && Food == 1) {
        basic.showString("Goodnight!")
        basic.showIcon(IconNames.Heart)
        basic.pause(1000)
        basic.showString("ZZZ")
        Bigturtle.scrollImage(1, 200)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(10000000000)
    }
})
