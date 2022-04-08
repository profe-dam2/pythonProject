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

url = 'http://192.168.3.10:8071'

class Boton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledGRIS.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        self.on = True

    def on_touch_down(self, touch):
        if self.on:
            self.on = False
            self.background_normal = 'imagenes/ledOFF.png'
            angle = {'data': '179'}
            x = requests.post(url + '/raspberryServo3AUTO', data=json.dumps(angle),
                              headers={"Content-Type": "application/json"})
            print(x.text)
        else:
            self.on = True
            self.background_normal = 'imagenes/ledON.png'

class BotonRojo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledGRIS.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .25, 'center_y': .5}
        self.on = False

    def on_press(self):
        if self.on:
            self.on = False
            self.background_normal = 'imagenes/ledGRIS.png'
            data = {'data': 'off'}


        else:
            self.on = True
            self.background_normal = 'imagenes/ledOFF.png'
            data = {'data': 'on'}
        x = requests.post(url + '/raspberryROJO',
                              data=json.dumps(data),
                              headers={"Content-Type": "application/json"})
        print(x)
        sleep(.5)

class BotonAmarillo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledGRIS.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        self.on = False

    def on_release(self):
        print("PRESIONAR")
        if self.on:
            self.on = False
            self.background_normal = 'imagenes/ledGRIS.png'
            data = {'data': 'off'}
            print("PULSO Y ESTA OFF")

        else:
            self.on = True
            self.background_normal = 'imagenes/ledAMARILLO.png'
            data = {'data': 'on'}
            print("PULSO Y ESTA ON")

        x = requests.post(url + '/raspberryAMARILLO',
                              data=json.dumps(data),
                              headers={"Content-Type": "application/json"})
        print(x)
        sleep(1)

class BotonVerde(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = 'imagenes/ledGRIS.png'
        self.background_down = 'imagenes/ledGRIS.png'
        self.border = (0, 0, 0, 0)
        self.size_hint = (.1, .2)
        self.pos_hint = {'center_x': .75, 'center_y': .5}
        self.on = False

    def on_press(self):
        if self.on:
            self.on = False
            self.background_normal = 'imagenes/ledGRIS.png'
            data = {'data': 'off'}

        else:
            self.on = True
            self.background_normal = 'imagenes/ledON.png'
            data = {'data': 'on'}

        x = requests.post(url + '/raspberryVERDE', data=json.dumps(data),
                          headers={"Content-Type": "application/json"})
        print(x)
        sleep(.5)

class Screen1(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)
        self.size_hint = (1, 1)
        self.pos_hint = {'x':0, 'y':0}
        self.ang1 = 0
        self.ang2 = 0
        self.ang3 = 0
        angle = {'data': '0'}
        requests.post(url + '/raspberryServo1', data=json.dumps(angle),
                      headers={"Content-Type": "application/json"})

        requests.post(url + '/raspberryServo2', data=json.dumps(angle),
                      headers={"Content-Type": "application/json"})

        requests.post(url + '/raspberryServo3', data=json.dumps(angle),
                      headers={"Content-Type": "application/json"})

        s = Slider(orientation='vertical')
        s.min = 0
        s.max = 180
        s.step = 20
        #s.bind(on_touch_down=lambda x,y: self.cambiarAngulo(int(s.value)))

        fondo = Image(source='imagenes/FONDO1.jpg',keep_ratio=False, allow_stretch=True)
        fondo.size_hint = self.size_hint
        fondo.pos_hint = self.pos_hint

        etiqueta = Label()
        etiqueta.pos_hint = {'x':0, 'y':.4}
        etiqueta.size_hint = self.size_hint
        etiqueta.bold = True
        etiqueta.color = (1,1,0,1)
        etiqueta.text = 'PANTALLA 1'
        etiqueta.font_size = 60

        ledON = Image(source='imagenes/ledON.png',keep_ratio=False, allow_stretch=True)
        ledON.size_hint = (.1,.2)
        ledON.pos_hint = {'center_x':.5, 'center_y':.5}

        btnLed = Boton()

        btnUPServo1 = Button(size_hint=(.1, .1), text='+10',
                             pos_hint={'x': 0, 'y': .1})
        btnUPServo1.bind(on_press=lambda x: self.cambiarAngulo2(10, 'Servo1'))

        btnDOWNServo1 = Button(size_hint=(.1, .1), text='-10',
                               pos_hint={'x': .1, 'y': .1})
        btnDOWNServo1.bind(
            on_press=lambda x: self.cambiarAngulo2(int(-10), 'Servo1'))

        btnUPServo2 = Button(size_hint=(.1,.1),text='+10', pos_hint={'x':0,'y':.3})
        btnUPServo2.bind(on_press=lambda x: self.cambiarAngulo2(10,'Servo2'))

        btnDOWNServo2 = Button(size_hint=(.1, .1), text='-10',pos_hint={'x':.1,'y':.3})
        btnDOWNServo2.bind(on_press=lambda x: self.cambiarAngulo2(int(-10),'Servo2'))



        btnUPServo3 = Button(size_hint=(.1, .1), text='+10',
                             pos_hint={'x': 0, 'y': .6})
        btnUPServo3.bind(on_press=lambda x: self.cambiarAngulo2(10, 'Servo3'))

        btnDOWNServo3 = Button(size_hint=(.1, .1), text='-10',
                               pos_hint={'x': .1, 'y': .6})
        btnDOWNServo3.bind(
            on_press=lambda x: self.cambiarAngulo2(int(-10),'Servo3'))



        txt = TextInput()
        txt.size_hint =(.5,.2)



        self.add_widget(fondo)
        self.add_widget(etiqueta)
        #self.add_widget(btnLed)
        #self.add_widget(s)

        self.add_widget(btnUPServo1)
        self.add_widget(btnDOWNServo1)

        self.add_widget(btnUPServo2)
        self.add_widget(btnDOWNServo2)

        self.add_widget(btnUPServo3)
        self.add_widget(btnDOWNServo3)
        #self.add_widget(txt)


    def cambiarAngulo(self,angulo):
        angle = {'data': angulo}
        x = requests.post(url + '/raspberryServo2', data=json.dumps(angle),
                          headers={"Content-Type": "application/json"})
        print(x.text)

    def cambiarAngulo3(self,angulo):
        angle = {'data': angulo}
        x = requests.post(url + '/raspberryServo2', data=json.dumps(angle),
                          headers={"Content-Type": "application/json"})
        print(x.text)

    def cambiarAngulo2(self,angulo,servo):
        angle = {'data': False}
        if servo == 'Servo1':
            if self.ang1 + angulo > 0 and self.ang1 + angulo < 200:
                self.ang1 = self.ang1 + angulo
                angle = {'data': self.ang1}
        elif servo == 'Servo2':
            if self.ang2 + angulo > 0 and self.ang2 + angulo < 200:
                self.ang2 = self.ang2 + angulo
                angle = {'data': self.ang2}
        else:
            if self.ang3 + angulo > 0 and self.ang3 + angulo < 200:
                self.ang3 = self.ang3 + angulo
                angle = {'data': self.ang3}


        x = requests.post(url + '/raspberry'+servo, data=json.dumps(angle),
                          headers={"Content-Type": "application/json"})
        print(x.text)

class Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.size_hint = (1, 1)
        self.pos_hint = {'x': 0, 'y': 0}

        data = {'data': 'off'}
        x = requests.post(url + '/raspberryVERDE', data=json.dumps(data),
                          headers={"Content-Type": "application/json"})

        x = requests.post(url + '/raspberryROJO', data=json.dumps(data),
                          headers={"Content-Type": "application/json"})

        x = requests.post(url + '/raspberryAMARILLO', data=json.dumps(data),
                          headers={"Content-Type": "application/json"})

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



class Proyecto2App(App):
    def build(self):


        return layout

def cambiarPantalla(nombreScreen):
    sm.current = nombreScreen

sm = ScreenManager()
sm.size_hint = (.5, .9)
sm.pos_hint = {'x':0, 'y':0}

screen1 = Screen1(name='screen1')
screen2 = Screen2(name='screen2')

screen1.pos_hint = {'x':0, 'y':0}
screen2.pos_hint = {'x':0, 'y':0}

sm.add_widget(screen1)
sm.add_widget(screen2)

sm.current = 'screen1'


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
    ANG = 0