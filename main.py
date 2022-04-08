import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


def encenderLed():
    requests.get("192.168.1.116:8071/raspberryON")

def cambiarPantalla( pantalla):
    sm.current = pantalla
    onn=False
    if onn:
        requests.get('http://192.168.1.116:8071/raspberryOFF')
        onn = False
    else:
        requests.get('http://192.168.1.116:8071/raspberryON')
        onn = True
class PrimeraApp(App):
    def build(self):
        return sm


screen1 = Screen(name='screen1')
screen2 = Screen(name='screen2')
sm = ScreenManager()



etiqueta = Label()
etiqueta.text = 'Ejemplo etiqueta'
etiqueta.color = (1,0,0,1)
etiqueta.bold = True
etiqueta.pos = (0,0)

Window.size = (800,800)
screen1.add_widget(etiqueta)
sm.add_widget(screen1)
sm.add_widget(screen2)
sm.current = 'screen1'

btn1 = Button()
btn1.bind(on_press=lambda x: cambiarPantalla('screen2') )
btn1.size = (200,50)
btn1.size_hint = (None, None)
btn1.text = 'IR A SCREEN2'
screen1.add_widget(btn1)

btn2 = Button()
btn2.bind(on_press=lambda x: cambiarPantalla('screen1') )
btn2.size = (200,50)
btn2.size_hint = (None, None)
btn2.text = 'IR A SCREEN1'
screen2.add_widget(btn2)
onn =True
PrimeraApp().run()