import random
from abc import ABC, abstractmethod

import pygame


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self,surface):
        pass

class Circle(Shape):
    def __init__(self,x,y):
        super().__init__(x=x,y=y)
        self.color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        self.radius=random.randint(0,100)

    def draw(self,surface):

        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)


class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__(x=x,y=y)
        self.color=random.randint(0,255),random.randint(0,255),random.randint(0,255)
        self.length=random.randint(0,100)
        self.width=random.randint(0,100)

    def draw(self,surface):

        pygame.draw.rect(surface,self.color,(self.x,self.y, self.width, self.length))

class ShapeFactory:
    @staticmethod
    def getShape(shapeType,x,y):
        if shapeType == 'circle':
            return Circle(x,y)
        elif shapeType == 'rectangle':
            return Rectangle(x,y)
        else:
            raise Exception('Invalid shape type')


def invoke_game():
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('Random Shapes')
    clock=pygame.time.Clock()

    shapes=[]
    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                shapeType=random.choice(['circle','rectangle'])
                shape=ShapeFactory.getShape(shapeType,x,y)
                shapes.append(shape)

        screen.fill((0,0,0))# black screen
        # if one shape is there, first black screen then that shape(s)

        for shape in shapes:
            shape.draw(surface=screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    invoke_game()
