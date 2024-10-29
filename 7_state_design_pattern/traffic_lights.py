from abc import abstractmethod, ABC

import pygame
import time
from enum import Enum


class Color(Enum):
    RED='Red'
    YELLOW='Yellow'
    GREEN='Green'

#define the interface for traffic light state
class TrafficLightState(ABC):
    # for transitioning to next state
    @abstractmethod
    def next(self,light:'TrafficLight'):
        pass

    # to get current color
    @abstractmethod
    def get_color(self):
        pass



class GreenSate(TrafficLightState):
    def next(self,light:'TrafficLight'):
        light.current_state=YellowState()

    def get_color(self):
        return Color.GREEN

class YellowState(TrafficLightState):
    def next(self,light:'TrafficLight'):
        light.current_state=RedState()

    def get_color(self):
        return Color.YELLOW

class RedState(TrafficLightState):
    def next(self,light:'TrafficLight'):
        light.current_state=GreenSate()

    def get_color(self):
        return Color.RED

class TrafficLight:
    current_state = GreenSate()

    def next(self):
        self.current_state.next(self)

    def get_color(self):
        return self.current_state.get_color()


class TrafficLightSimulation:
    def __init__(self):
        self.light=TrafficLight()
        self.cycle=0
        self.screen=None
        self.width=400
        self.height=800


    def stop(self):
        pygame.quit()

    def draw(self):
        self.screen.fill((211,211,211))

        red_color=(255,0,0)
        yellow_color=(255,255,0)
        green_color=(0,255,0)

        outline_color=(70,70,70)

        rectx=self.width//4
        recty=self.height//8
        rect_width=self.width//2
        rect_height=self.height//1.5

        pygame.draw.rect(self.screen,outline_color,(rectx,recty,rect_width,rect_height),10)

        radius=50
        centerx=self.width//2
        centery=self.height//2

        #draw outline and color of red light

        pygame.draw.circle(self.screen,outline_color,(centerx,centery-(rect_height//4)),radius+5,5)
        if self.light.get_color()==Color.RED:
            pygame.draw.circle(self.screen,red_color,(centerx,centery-(rect_height//4)),radius)
        else:
            pygame.draw.circle(self.screen,(211,211,211),(centerx,centery-(rect_height//4)),radius)

        # draw the outline and color of yellow light
        pygame.draw.circle(self.screen,outline_color,(centerx,centery),radius+5,5)
        if self.light.get_color()==Color.YELLOW:
            pygame.draw.circle(self.screen,yellow_color,(centerx,centery),radius)
        else:
            pygame.draw.circle(self.screen,(211,211,211),(centerx,centery),radius)

        # draw the outline and color of green light
        pygame.draw.circle(self.screen,outline_color,(centerx,centery+(rect_height//4)),radius+5,5)
        if self.light.get_color()==Color.GREEN:
            pygame.draw.circle(self.screen,green_color,(centerx,centery+(rect_height//4)),radius)
        else:
            pygame.draw.circle(self.screen,(211,211,211),(centerx,centery+(rect_height//4)),radius)







    def start(self):
        pygame.init()
        self.screen=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Traffic Light Simulation")

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

            self.cycle+=1
            self.light.next()

            self.draw()
            pygame.display.update()
            time.sleep(4)

if __name__ == '__main__':
    simulation = TrafficLightSimulation()
    try:
        simulation.start()
    except KeyboardInterrupt:
        simulation.stop()