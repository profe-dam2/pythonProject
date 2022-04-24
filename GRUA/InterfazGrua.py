import json
from time import sleep

import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from urllib.parse import urlencode
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *

url = 'http://192.168.1.116:8071'

class BotonRojo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledOFF.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .25, 'center_y': .5}
        self.on = False

    def on_press(self):

        data = {'direccion': False}

        x = requests.post(url + '/carroGrua',
                              data=json.dumps(data),
                              headers={"Content-Type": "application/json"})
        print(x)


class BotonAmarillo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledAMARILLO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        self.on = False

    def on_press(self):
        data = {'direccion': True}

        x = requests.post(url + '/carroGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)


class BotonVerde(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledON.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .75, 'center_y': .5}
        self.on = False

    def on_press(self):
        data = {'direccion': None}

        x = requests.post(url + '/carroGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)


class BotonGanchoAbajo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledOFF.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .25, 'center_y': .75}
        self.on = False

    def on_press(self):

        data = {'direccion': False}

        x = requests.post(url + '/ganchoGrua',
                              data=json.dumps(data),
                              headers={"Content-Type": "application/json"})
        print(x)


class BotonGanchoArriba(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledAMARILLO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .5, 'center_y': .75}
        self.on = False

    def on_press(self):
        data = {'direccion': True}

        x = requests.post(url + '/ganchoGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)


class BotonGanchoParar(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledON.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .75, 'center_y': .75}
        self.on = False

    def on_press(self):
        data = {'direccion': None}

        x = requests.post(url + '/ganchoGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)



class BotonPlumaAbajo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledOFF.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .25, 'center_y': .25}
        self.on = False

    def on_press(self):

        data = {'direccion': False}

        x = requests.post(url + '/plumaGrua',
                              data=json.dumps(data),
                              headers={"Content-Type": "application/json"})
        print(x)


class BotonPlumaArriba(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledAMARILLO.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .5, 'center_y': .25}
        self.on = False

    def on_press(self):
        data = {'direccion': True}

        x = requests.post(url + '/plumaGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)


class BotonPlumaParar(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledON.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .75, 'center_y': .25}
        self.on = False

    def on_press(self):
        data = {'direccion': None}

        x = requests.post(url + '/plumaGrua',
                          data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)




class Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.size_hint = (1, 1)
        self.pos_hint = {'x': 0, 'y': 0}

        image1 = Image(source='imagenes/FONDO2.jpg', keep_ratio=False,
                       allow_stretch=True)
        image1.size_hint = self.size_hint
        image1.pos_hint = self.pos_hint

        etiqueta = Label()
        etiqueta.pos_hint = {'x': 0, 'y': .4}
        etiqueta.size_hint = self.size_hint
        etiqueta.bold = True
        etiqueta.color = (1, 1, 0, 1)
        etiqueta.text = 'PANTALLA 2'
        etiqueta.font_size = 60
        self.add_widget(image1)
        self.add_widget(etiqueta)

        btn = Button()
        btn.text = 'ACEPTAR'

        btnROJO = BotonRojo()
        btnAMARILLO = BotonAmarillo()
        btnVERDE = BotonVerde()

        self.add_widget(btnROJO)
        self.add_widget(btnAMARILLO)
        self.add_widget(btnVERDE)

        self.add_widget(BotonGanchoAbajo())
        self.add_widget(BotonGanchoArriba())
        self.add_widget(BotonGanchoParar())

        self.add_widget(BotonPlumaAbajo())
        self.add_widget(BotonPlumaArriba())
        self.add_widget(BotonPlumaParar())

class Proyecto2App(App):
    def build(self):


        return layout

def cambiarPantalla(nombreScreen):
    sm.current = nombreScreen

sm = ScreenManager()
sm.size_hint = (.5, .9)
sm.pos_hint = {'x':0, 'y':0}


screen2 = Screen2(name='screen2')


screen2.pos_hint = {'x':0, 'y':0}


sm.add_widget(screen2)

sm.current = 'screen2'


layout = FloatLayout()
layout.size_hint = (1,1)
layout.pos_hint = {'x':0, 'y':0}
btn1 = Button()
btn1.text = 'IR A PANTALLA 1'
btn1.size_hint = (.5,.1)
btn1.pos_hint = {'x': 0, 'y': .9}
btn1.bind(on_press=lambda x: cambiarPantalla('screen1') )

btn2 = Button()
btn2.text = 'IR A PANTALLA 2'
btn2.size_hint = (.5,.1)
btn2.pos_hint = {'x': .5, 'y': .9}
btn2.bind(on_press=lambda x: cambiarPantalla('screen2'))

sm.size_hint = (1,.9)
sm.pos_hint = {'x': 0, 'y': 0}

layout.add_widget(btn1)
layout.add_widget(btn2)
layout.add_widget(sm)


w, h = Window.size = (800,480)

if __name__ == '__main__':
    Proyecto2App().run()
