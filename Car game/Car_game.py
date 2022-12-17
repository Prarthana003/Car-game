import pygame
from pygame.locals import *
from tkinter import *
from PIL import Image, ImageTk
import random

'''
root=Tk()

canvas=Canvas(width=1200,height=800)
canvas.pack()


bg=Image.open("fp.png")
bg=ImageTk.PhotoImage(image=bg)

canvas.create_image(0,0,image=bg,anchor='nw')

def click():
    root.destroy()
    
play=Button(root,text='Play',padx=10,pady=5,command=click)
play.pack()

root.mainloop()
'''



# Pugame part
# Drawing variables

size=width,height=(1200,700)
road_w=width//1.6
road_mark=width//80

right_lane=354
left_lane=728


pygame.init()
running=True
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Car game")

#Background color
screen.fill((60,220,0))

# draw graphics



# Load images

#car1
car=pygame.image.load("Car 1.png")
car_loc=car.get_rect()
car_loc[0]=right_lane
car_loc[1]=height*0.8

#car2


car2=pygame.image.load("Car 3.png")
car2_loc=car.get_rect()
car2_loc[0]=right_lane
car2_loc[1]=-200


#game variables

speed=1
count=0
score=0

# Logic

while running:

    count=count+1

    if count==3000:
        speed=speed+0.5
        count=0
        score=score+500

    car2_loc[1]=car2_loc[1]+speed
    pygame.display.update()


    if car2_loc[1]>900:

        
        s=random.randint(0,1)
        if s==0:
            car2_loc[0]=right_lane
            car2_loc[1]=-200

        else:
             car2_loc[0]=left_lane
             car2_loc[1]=-200

    if (car2_loc[1]+96//2>car_loc[1]-96  and car2_loc[0]==car_loc[0]):
            print("GAME OVER! YOU LOSE")
            break
        
        
    for event in pygame.event.get() :

        
        if event.type==QUIT:
            running=False

        if event.type==KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                car_loc[0]=right_lane

            if event.key in [K_d,K_RIGHT]:
                car_loc[0]=left_lane

    
    #road
    pygame.draw.rect(
        screen,
        (50,50,50),
        ((width/2-road_w/2),0,road_w,height)
        )

    #road markings

    pygame.draw.rect(
        screen,
        (255,240,60),
        ((width//2-road_mark/2),0,road_mark,height)
        )

    pygame.draw.rect(
        screen,
        (255,255,255),
        ((width//5-road_mark/2+road_mark),0,road_mark,height)
        )

    pygame.draw.rect(
        screen,
        (255,255,255),
        ((4*width//5-road_mark/2-road_mark),0,road_mark,height)
        )


            

    screen.blit(car,car_loc)
    #pygame.display.update()

    screen.blit(car2,car2_loc)
    pygame.display.update()
    

print(score)
pygame.quit()

    

