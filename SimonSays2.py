from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
import random
import time
from kivy.clock import Clock
from functools import partial


boje=['r','g','b','y']

        
class SimonSays(App):
    def timer(self,tipka,boja,a):
        tipka.background_color=boja
        
    def flash(self,lo):
        for i in range(len(lo)):
            p=lo[i]
            if p=='r':
                Clock.schedule_once(partial(self.timer,self.bu1,(0.961, 0.178, 0.137,1)),i)
                Clock.schedule_once(partial(self.timer,self.bu1,(0.961, 0.078, 0.137,0.75)),1+i)
                continue
            elif p=='g':
                Clock.schedule_once(partial(self.timer,self.bu2,(0.224, 0.567, 0.255,1)),i)
                Clock.schedule_once(partial(self.timer,self.bu2,(0.224, 0.467, 0.255,0.75)),1+i)
                continue
            elif p=='b':
                Clock.schedule_once(partial(self.timer,self.bu3,(0.376, 0.747, 0.855,1)),i)
                Clock.schedule_once(partial(self.timer,self.bu3,(0.376, 0.647, 0.855,0.75)),1+i)
                continue
            elif p=='y':
                Clock.schedule_once(partial(self.timer,self.bu4,(0.988, 0.935, 0.341,1)),i)

                Clock.schedule_once(partial(self.timer,self.bu4,(0.988, 0.835, 0.341,0.75)),1+i)
                continue
            
    def hoc(self,bonk):

        if bonk==self.l1[0]:
            del(self.l1[0])
            if self.l1==[]:
                self.l.append(boje[random.randint(0,3)])
                self.l1=list(self.l)

                self.flash(self.l)
        else:
            print('Score:{}'.format(int(len(self.l))-1))
            
    
    def btnfunc(self,obj):
        print("start")
        self.l=[boje[random.randint(0,3)]]
        self.l1=list(self.l)

        self.flash(self.l)
        
            
        
        
    def btnfunc1(self,obj):
        self.hoc('r')
    def btnfunc2(self,obj):
        self.hoc('g')
    def btnfunc3(self,obj):
        self.hoc('b')
    def btnfunc4(self,obj):
        self.hoc('y')


    def build(self):

        r1=RelativeLayout(size=(300,300))

        self.bust=Button(text="Start",size_hint=(.2, .2),pos_hint={'center_x': .5, 'center_y': .2},on_release=self.btnfunc)
     

        self.bu1=Button(background_color=(0.961, 0.078, 0.137,0.75),size_hint=(.2, .2),pos_hint={'center_x': .4, 'center_y': .6},on_release=self.btnfunc1)

        self.bu2=Button(background_color=(0.224, 0.467, 0.255,0.75),size_hint=(.2, .2),pos_hint={'center_x': .6, 'center_y': .6},on_release=self.btnfunc2)

        self.bu3=Button(background_color=(0.376, 0.647, 0.855,0.75),size_hint=(.2, .2),pos_hint={'center_x': .4, 'center_y': .4},on_release=self.btnfunc3)

        self.bu4=Button(background_color=(0.988, 0.835, 0.341,0.75),size_hint=(.2, .2),pos_hint={'center_x': .6, 'center_y': .4},on_release=self.btnfunc4)

        r1.add_widget(self.bust)
        r1.add_widget(self.bu1)
        r1.add_widget(self.bu2)
        r1.add_widget(self.bu3)
        r1.add_widget(self.bu4)
        return r1

    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    SimonSays().run()
