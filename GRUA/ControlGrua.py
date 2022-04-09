

from AMSpi import AMSpi
from threading import Thread
from time import sleep
global carroON

class ControlGrua(object):
    def __init__(self):
        self.amspi = AMSpi()
        global carroON

        # Set PINs for controlling shift register (GPIO numbering)
        self.amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        self.amspi.set_L293D_pins(5, 6, 13, 19)

        carroON = False


    def moverCarroGrua(self, direccion):
        global carroON
        if direccion != None:
            print(direccion)
            if (carroON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_3)

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
        global carroOn
        while (carroON):
            self.amspi.run_dc_motor(self.amspi.DC_Motor_3, clockwise=direccion, speed = 50)