input.onButtonPressed(Button.A, function () {
    if (run == false) {
        basic.pause(1000)
    } else {
        basic.pause(50)
    }
    run = !(run)
})
let SpeedR = 0
let SpeedL = 0
let speed = 0
let lasterror = 0
let D = 0
let I = 0
let P = 0
let error = 0
let run = false
run = false
let Maxspeed = 90
let BasespeedL = 60
let BasespeedR = 60
let Kp = 0.035
let Ki = 0.0012
let Kd = 0.3
basic.forever(function () {
    if (run) {
        error = CutebotPro.getOffset()
        P = error
        I = I + error
        D = error - lasterror
        lasterror = error
        speed = Kp * P + (Ki * I + Kd * D)
        SpeedL = BasespeedL + speed
        SpeedR = BasespeedR - speed
        if (SpeedL > Maxspeed) {
            SpeedL = Maxspeed
        }
        if (SpeedR > Maxspeed) {
            SpeedR = Maxspeed
        }
        if (SpeedL < 0) {
            SpeedL = 0
        }
        if (SpeedR < 0) {
            SpeedR = 0
        }
        CutebotPro.pwmCruiseControl(SpeedL, SpeedR)
    } else {
        CutebotPro.stopImmediately(CutebotProMotors.ALL)
    }
})
