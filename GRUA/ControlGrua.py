

from AMSpi import AMSpi
from threading import Thread
from time import sleep
import RPi.GPIO as GPIO

global ganchoON
global carroON


class ControlGrua(object):
    def __init__(self):
        self.amspi = AMSpi()
        global carroON
        global ganchoON
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        # Set PINs for controlling shift register (GPIO numbering)
        self.amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        self.amspi.set_L293D_pins(5, 6, 13, 19)
        ganchoON = False
        carroON = False
        print('INICIAL CONTROL GRUA')
        #self.prueba()


    def prueba(self):
        sensor = GPIO.input(23)
        c = 0
        while(True):
            sensor = GPIO.input(23)
            if (sensor):
                c = c + 1
                print("CONTADOR",c)
                sleep(1)


    def moverCarroGrua(self, direccion):
        global carroON
        if direccion != None:
            print(direccion)
            if (carroON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)

            carroON = True
            thread = Thread(target=self.tareaMoverCarro, args=(direccion,))
            thread.start()
            print('aqui')
        else:
            self.pararCarroGrua()

    def pararCarroGrua(self):
        global carroON
        print('parar el carro')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)
        sleep(.2)
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)
        carroON = False

    def tareaMoverCarro(self, direccion):
        global carroOn
        button_state = GPIO.input(18)
        while (carroON and button_state):

            button_state = GPIO.input(18)
            self.amspi.run_dc_motor(self.amspi.DC_Motor_1, clockwise=direccion)


    ####################################################
    ############GANCHO#################################

    def moverGanchoGrua(self, direccion):
        global ganchoON
        if direccion != None:
            print(direccion)
            if (ganchoON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)

            ganchoON = True
            thread = Thread(target=self.tareaMoverGancho, args=(direccion,))
            thread.start()
            print('aqui')
        else:
            self.pararGanchoGrua()

    def pararGanchoGrua(self):
        global ganchoON
        print('parar el gancho')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)
        sleep(.2)
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)
        ganchoON = False

    def tareaMoverGancho(self, direccion):
        global ganchoON
        button_state = GPIO.input(18)
        while (ganchoON and button_state):

            button_state = GPIO.input(18)
            self.amspi.run_dc_motor(self.amspi.DC_Motor_3, clockwise=direccion)