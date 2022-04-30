

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
        global plumaON
        #GPIO.setmode(GPIO.BCM)

        #INDUCTIVO GANCHO
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #TACOMETRO
        GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        #FINALES DE CARRERA PLUMA
        GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # FINALES DE CARRERA CARRO
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)


        #LED VERDE
        GPIO.setup(23, GPIO.OUT)

        # LED ROJO
        GPIO.setup(24, GPIO.OUT)

        # RELE
        GPIO.setup(10, GPIO.OUT)


        # Set PINs for controlling shift register (GPIO numbering)
        self.amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        self.amspi.set_L293D_pins(5, 6, 13, 19)
        ganchoON = False
        carroON = False
        plumaON = False
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
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)
                sleep(.2)
            carroON = True
            thread = Thread(target=self.tareaMoverCarro, args=(direccion,))
            thread.start()
            print('aqui')
        else:
            self.pararCarroGrua()

    def pararCarroGrua(self):
        global carroON
        print('parar el carro')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)
        sleep(.2)
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)
        carroON = False

    def tareaMoverCarro(self, direccion):
        global carroON
        #button_state = GPIO.input(18)

        # while (carroON and button_state):
        #     button_state = GPIO.input(18)
        #
        fcC1 = GPIO.input(27)
        fcC2 = GPIO.input(22)
        if fcC1 == 0 and not direccion:
            print("NO TE PUEDES MOVER, FCC1 ESTA ACTIVADO")
        elif fcC2 == 0 and direccion:
            print("NO TE PUEDES MOVER, FCC2 ESTA ACTIVADO")
        else:
            self.amspi.run_dc_motor(self.amspi.DC_Motor_3, clockwise=direccion,
                                    speed=40)
            sleep(1)
            while (carroON):
                fcC1 = GPIO.input(27)
                fcC2 = GPIO.input(22)
                print("MUEVE CARRO")
                if fcC1 == 0 or fcC2 == 0:
                    self.pararCarroGrua()
                    break


    ####################################################
    ############GANCHO#################################

    def moverGanchoGrua(self, direccion):
        global ganchoON
        if direccion != None:
            print(direccion)
            if (ganchoON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)

            ganchoON = True
            thread = Thread(target=self.tareaMoverGancho, args=(direccion,))
            thread.start()
            print('aqui')
        else:
            self.pararGanchoGrua()

    def pararGanchoGrua(self):
        global ganchoON
        print('parar el gancho')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)
        sleep(.2)
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_1)
        ganchoON = False
        GPIO.output(23, 0)

    def tareaMoverGancho(self, direccion):
        global ganchoON
        inductivo_state = GPIO.input(4)
        self.amspi.run_dc_motor(self.amspi.DC_Motor_1, clockwise=direccion,
                               speed=99)
        c = 0
        GPIO.output(23,1)
        while (ganchoON and not inductivo_state):
            inductivo_state = GPIO.input(4)
            sensor = GPIO.input(14)
            # if (sensor):
            #     c = c + 1
            #     print("CONTADOR", c)
            if inductivo_state == 1:
                self.pararGanchoGrua()
                break



    ####################################################
    ############PLUMA#################################

    def moverPlumaGrua(self, direccion):
        global plumaON
        if direccion != None:
            print(direccion)
            if (plumaON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_2)

            plumaON = True
            thread = Thread(target=self.tareaMoverPluma,
                            args=(direccion,))
            thread.start()
            print('aquiPluma')
        else:
            self.pararPlumaGrua()

    def pararPlumaGrua(self):
        global plumaON
        print('parar la pluma')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_2)
        sleep(.2)
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_2)
        plumaON = False

    def tareaMoverPluma(self, direccion):
        global plumaON

        fcP1 = GPIO.input(15)
        fcP2 = GPIO.input(17)
        if fcP1 == 0 and not direccion:
            print("NO TE PUEDES MOVER, FCP1 ESTA ACTIVADO")
        elif fcP2 == 0 and direccion:
            print("NO TE PUEDES MOVER, FCP2 ESTA ACTIVADO")
        else:
            self.amspi.run_dc_motor(self.amspi.DC_Motor_2, clockwise=direccion,
                                    speed=80)
            sleep(2)
            while (plumaON):
                fcP1 = GPIO.input(15)
                fcP2 = GPIO.input(17)

                if fcP1 == 0 or fcP2 == 0:
                    self.pararPlumaGrua()
                    break