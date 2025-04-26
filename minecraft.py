from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
app = Ursina()
player = FirstPersonController()
Sky()
textures = ['rock.png', 'grass.png']
runways = ['runwayleft.png', 'runwayright.png']
runwaycoord = random.randint(5,12)
terminalside = 0 if runwaycoord > 10 else 1
thewall = random.choice(['wall.png', 'wall2.png'])
thedoor = random.choice(['door.png', 'door2.png'])
thetile = random.choice(['tile.png', 'tile2.png'])
theroof = random.choice(['roof.png', 'roof2.png'])

def inTerminal(num):
    if (runwaycoord < num) and (terminalside == 1):
        return True
    if (runwaycoord > num) and (terminalside == 0):
        return True
    return False

def wheredoor(i, j):
    if terminalside == 1:
        if j == runwaycoord + 2 and (i ==16 or i == 17): 
            return True
    elif j == runwaycoord - 1 and i == 16 and i == 17:  
        return True
    else: return False

def inRoof(i, j):
    if terminalside:
        return True if j > runwaycoord + 1 else False
    else:
        return True if j < runwaycoord else False

def onEdge(i, j):
    if j == runwaycoord or j == runwaycoord + 1:
        return False
    if terminalside == 1:
        if j == runwaycoord + 2 and i != 16 and i != 17: 
            return True
        if j > runwaycoord + 2:
            if j == 19 or i == 0 or i == 19:
                return True
    else:  
        if j == runwaycoord - 1 and i != 16 and i != 17:  
            return True
        if j < runwaycoord - 1:
            if j == 0 or i == 0 or i == 19:
                return True
    return False


boxes = []

for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j,-1,i),
                          texture= 'rock.png', parent=scene, origin_y=0.5)
        boxes.append(box)
for i in range(20):
    for j in range(20):
        if (j != runwaycoord) and (j != runwaycoord+1):
            if (not inTerminal(j)):
              box = Button(color=color.white, model='cube', position=(j,0,i),
                          texture=random.choice(textures), parent=scene, origin_y=0.5)
            else:
              box = Button(color=color.white, model='cube', position=(j,0,i),
                          texture= thetile, parent=scene, origin_y=0.5)
            boxes.append(box)

for i in range(20):
    for j in range(20):
        if (j != runwaycoord) and (j != runwaycoord+1) and (random.randint(0,20) == 0) and (not inTerminal(j)):
            box = Button(color=color.white, model='cube', position=(j,1,i),
                         texture='rock.png', parent=scene, origin_y=0.5)
            boxes.append(box)
for height in range(1,5):
    for i in range(20):
      for j in range(20):
          if wheredoor(i, j):
              box = Button(color=color.white, model='cube', position=(j,height,i),
             texture=thedoor, parent=scene, origin_y=0.5)
              box.is_door = True
              boxes.append(box)
for height in range(5):
  for i in range(20):
      for j in range(20):
          if onEdge(i, j):
              box = Button(color=color.white, model='cube', position=(j,height,i),
                          texture='name.png', parent=scene, origin_y=0.5) if height == 4 else (Button(color=color.white, model='cube', position=(j,height,i),
                          texture=thewall, parent=scene, origin_y=0.5) if height != 3 else Button(color=color.white, model='cube', position=(j,height,i),
                          texture='window.png', parent=scene, origin_y=0.5))
              boxes.append(box)

if not terminalside: 
    posx = random.randint(2, runwaycoord-2)
    posy = random.randint(2, 18)
    boxes.append(Button(color=color.white, model='cube', position=(posx,3,posy),
                          texture='flightattendent.png', parent=scene, origin_y=0.5))
else:
    posx = random.randint(runwaycoord + 3, 18)
    posy = random.randint(2, 18)
    boxes.append(Button(color=color.white, model='cube', position=(posx,3,posy),
                          texture='flightattendent.png', parent=scene, origin_y=0.5))
boxes.append(Button(color=color.white, model='cube', position=(posx,2,posy),
                        texture='shirt.png', parent=scene, origin_y=0.5))
boxes.append(Button(color=color.white, model='cube', position=(posx,1,posy),
                          texture='pants.png', parent=scene, origin_y=0.5))
for i in [-1,0,1]:
    for j in [-1,0,1]:   
      if [i, j] != [0,0]: 
        boxes.append(Button(color=color.white, model='cube', position=(posx+i,1,posy+j),
                          texture='table.png', parent=scene, origin_y=0.5))
for i in range(20):
    for j in range(20):
        if (j == runwaycoord) or (j == runwaycoord+1):
            box = Button(color=color.white, model='cube', position=(j,0,i),
                         texture=runways[not j%2], parent=scene, origin_y=0.5)
            boxes.append(box)

for i in range(20):
    for j in range(20):
        if inRoof(i, j):
            box = Button(color=color.white, model='cube', position=(j,5,i),
                         texture=theroof, parent=scene, origin_y=0.5) if (i % 4) and (j % 4) else Button(color=color.white, model='cube', position=(j,5,i),
                         texture='light.png', parent=scene, origin_y=0.5)
            boxes.append(box)

planecoord = random.randint(8,12)
for i in range(planecoord,planecoord + 6):
    for j in range(runwaycoord, runwaycoord + 2):
        if i % 2:
          box = Button(color=color.white, model='cube', position=(j,1,i),
                          texture='wheel.png', parent=scene, origin_y=0.5)
        box = Button(color=color.white, model='cube', position=(j,2,i),
                         texture='airplanewindow.png', parent=scene, origin_y=0.5) if i != planecoord else (Button(color=color.white, model='cube', position=(j,2,i),
                         texture='airplaneleft.png', parent=scene, origin_y=0.5) if j == runwaycoord else Button(color=color.white, model='cube', position=(j,2,i),
                         texture='airplaneright.png', parent=scene, origin_y=0.5))
        boxes.append(box)
        box = Button(color=color.white, model='cube', position=(j,2,i),
       texture='white.png', parent=scene, origin_y=0, scale=(1, 0.05, 1))
box = Button(color=color.white, model='cube', position=(runwaycoord- (1 if terminalside else -2),2,planecoord+3),
       texture='white.png', parent=scene, origin_y = 0.5)
box = Button(color=color.white, model='cube', position=(runwaycoord- (2 if terminalside else -2),2,planecoord+3),
       texture='white.png', parent=scene, origin_y = 0.5)

icoord = random.randint(5, 15)
jcoord = runwaycoord+3 if terminalside else runwaycoord-2
randstore = random.choice(['warrencuisine.png', 'gemshoppy.png','grandbazaar.png', 'ridgehackmerch.png', 'simcardsshop.png'])
boxes.append(Button(color=color.white, model='cube', position=(jcoord,3,icoord),
                        texture='flightattendent.png', parent=scene, origin_y=0.5))
boxes.append(Button(color=color.white, model='cube', position=(jcoord,2,icoord),
                        texture='shirt.png', parent=scene, origin_y=0.5))
boxes.append(Button(color=color.white, model='cube', position=(jcoord,1,icoord),
                          texture='pants.png', parent=scene, origin_y=0.5))

for i in [-1,0,1]:
    for j in [-1,0,1]:   
      if [i, j] != [0,0]: 
        boxes.append(Button(color=color.white, model='cube', position=(jcoord+i,1,icoord+j),
                          texture=randstore, parent=scene, origin_y=0.5))
def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                if hasattr(box, 'is_door') and box.is_door:
                    if not hasattr(box, 'door_open'):
                        box.door_open = False

                    if not box.door_open:
                        box.position += Vec3(0, 0, 1)  # move right to open
                        box.door_open = True
                    else:
                        box.position -= Vec3(0, 0, 1)  # move back to close
                        box.door_open = False
                else:
                    new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                                 texture='grass.png', parent=scene, origin_y=0.5)
                    boxes.append(new)

            if key == 'right mouse down':
                if hasattr(box, 'is_door') and box.is_door:
                    pass  # don't destroy door
                else:
                    boxes.remove(box)
                    destroy(box)



app.run()