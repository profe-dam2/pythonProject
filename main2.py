import RPi.GPIO as gpio
from flask import Flask, request
import raspModule
from time import sleep


app = Flask(__name__)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
#gpio.setup(3, gpio.OUT)
#pwm=gpio.PWM(3, 50)
#pwm.start(0)
gpio.output(11, True)
gpio.output(13, True)
gpio.output(15, True)

@app.route('/raspberryServo3', methods=['POST'])
def RaspberryServo3Angle():
    print('SERVO1')
    print(request.json['data'])
    gpio.setup(7, gpio.OUT)
    pwm=gpio.PWM(3, 50)
    pwm.start(0)
    angle = int(request.json['data'])
    print(type(angle))
    duty = angle /18 + 2
    gpio.output(7, True)
    #pwm.ChangeDutyCycle(duty)
    pwm.ChangeDutyCycle(angle_to_percent(angle))
    sleep(.2)
    gpio.output(7, False)
    #pwm.ChangeDutyCycle(0)
    pwm.stop()
    #gpio.cleanup()
    return {'response': 'se mueve'}



@app.route('/raspberryServo2', methods=['POST'])
def RaspberryServo2Angle():
    print('SERVO2')
    print(request.json['data'])
    gpio.setup(5, gpio.OUT)
    pwm=gpio.PWM(3, 50)
    pwm.start(0)
    angle = int(request.json['data'])
    print(type(angle))
    duty = angle /18 + 2
    gpio.output(5, True)
    #pwm.ChangeDutyCycle(duty)
    pwm.ChangeDutyCycle(angle_to_percent(angle))
    sleep(.2)
    gpio.output(5, False)
    #pwm.ChangeDutyCycle(0)
    pwm.stop()
    #gpio.cleanup()
    return {'response': 'se mueve'}


@app.route('/raspberryVERDE', methods=['GET'])
def RaspberryVERDE():
    print('RASPBERRYVERDE')
    if request.json['data'] == 'on':
        gpio.output(11, True)
    else:
        gpio.output(11, False)

    return {'response': 'led verde'}


@app.route('/raspberryAMARILLO', methods=['GET'])
def RaspberryAMARILLO():
    print('RASPBERRYAMARILLO')
    if request.json['data'] == 'on':
        gpio.output(13, True)
    else:
        gpio.output(13, False)

    return {'response': 'led amarillo'}

@app.route('/raspberryROJO', methods=['GET'])
def RaspberryROJO():
    print('RASPBERRYROJO')
    if request.json['data'] == 'on':
        gpio.output(15, True)
    else:
        gpio.output(15, False)

    return {'response': 'led rojo'}


@app.route('/raspberryServo3AUTO', methods=['POST'])
def RaspberryServo3AUTO():
    print('SERVO3AUTO')
    print(request.json['data'])
    gpio.setup(3, gpio.OUT)
    pwm=gpio.PWM(3, 50)
    pwm.start(0)
    gpio.output(3, True)
    pwm.ChangeDutyCycle(angle_to_percent(0))
    sleep(1)
    gpio.output(3, False)
    pwm.stop()
    gpio.setup(3, gpio.OUT)
    pwm = gpio.PWM(3, 50)
    pwm.start(0)
    gpio.output(3, True)
    pwm.ChangeDutyCycle(angle_to_percent(200))
    sleep(1)
    gpio.output(3, False)
    pwm.stop()
    return {'response': 'se mueve'}

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


    print(request.json['data'])
    gpio.setup(3, gpio.OUT)
    pwm=gpio.PWM(3, 50)
    pwm.start(0)
    gpio.output(3, True)
    pwm.ChangeDutyCycle(angle_to_percent(0))
    sleep(.2)
    pwm.ChangeDutyCycle(angle_to_percent(200))
    sleep(.2)
    gpio.output(3, False)
    pwm.stop()
    return {'response': 'se mueve'}