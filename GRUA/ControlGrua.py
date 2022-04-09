

from AMSpi import AMSpi
from threading import Thread


class ControlGrua(object):
    def __init__(self):
        self.amspi = AMSpi()


        # Set PINs for controlling shift register (GPIO numbering)
        self.amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        self.amspi.set_L293D_pins(5, 6, 13, 19)

        self.carroON = False

    def moverCarroGrua(self, direccion):
        if direccion != None:
            print(direccion)
            if (self.carroON):
                self.amspi.stop_dc_motor(self.amspi.DC_Motor_4)

            self.carroON = True
            thread = Thread(target=self.tareaMoverCarro, args=(direccion,))
            thread.start()
            thread.join()

        else:
            self.pararCarroGrua()

    def pararCarroGrua(self):
        print('parar el carro')
        self.amspi.stop_dc_motor(self.amspi.DC_Motor_4)
        self.carroON = False

    def tareaMoverCarro(self, direccion):
        while (self.carroON):
            self.amspi.run_dc_motor(self.amspi.DC_Motor_4, clockwise=direccion,
                                    speed=99)