def on_button_pressed_a():
    global run
    if run == False:
        basic.pause(1000)
    else:
        basic.pause(50)
    run = not (run)
input.on_button_pressed(Button.A, on_button_pressed_a)

SpeedR = 0
SpeedL = 0
speed = 0
D = 0
I = 0
P = 0
run = False
run = False
error = 0
Maxspeed = 90
lasterror = 0
BasespeedL = 60
BasespeedR = 60
Kp = 0.035
Ki = 0.0012
Kd = 0.3

def on_forever():
    global error, P, I, D, lasterror, speed, SpeedL, SpeedR
    if run:
        error = CutebotPro.get_offset()
        P = error
        I = I + error
        D = error - lasterror
        lasterror = error
        speed = Kp * P + (Ki * I + Kd * D)
        SpeedL = BasespeedL + speed
        SpeedR = BasespeedR - speed
        if SpeedL > Maxspeed:
            SpeedL = Maxspeed
        if SpeedR > Maxspeed:
            SpeedR = Maxspeed
        if SpeedL < 0:
            SpeedL = 0
        if SpeedR < 0:
            SpeedR = 0
        CutebotPro.pwm_cruise_control(SpeedL, SpeedR)
    else:
        CutebotPro.stop_immediately(CutebotProMotors.ALL)
basic.forever(on_forever)
