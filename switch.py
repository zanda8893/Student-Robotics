import boolean
import robot

R.ruggeduinos[0].pin_mode(2, INPUT_PULLUP)

while True:
    if R.ruggeduinos[0].digital_read(2) == False:
        clamped = True

    else:
        clamped = False