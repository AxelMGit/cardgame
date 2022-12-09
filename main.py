from ursina import *

app = Ursina()
camera.orthographic = True
camera.fov = 10

## Entité : Fond ##
circuit = Entity(
    model='quad',
    texture='ressources/background',
    scale=(15, 10),
    z=1
)


## Entité + Collision : Voiture  ##
card1 = Entity(
    model='quad',
    texture='ressources/img/1p',
    #texture='ressources/PB',
    scale=(1,1.5),
    #scale=(0.25,0.25),
    position = Vec3(0.5,4,0)
    #rotation_z=(-90) 
    #size=(285, 199)
)
#car.collider = 'sphere'
#car.collider = SphereCollider(car, center=Vec3(0,0,0), radius=.5)

def test():
    print('OK')

b = Button(
    texture='ressources/img/1p',
    icon='ressources/img/1p', 
    scale=.2, 
    text_origin=(-.5,0),
    on_click=test()
)







def update():
  return
# Boule principale


def input(key):
  if key == 'space':
    jump.play

app.run()