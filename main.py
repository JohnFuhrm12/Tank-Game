from ursina import *

def bullet():
    Bullet = Entity(model='cube',
                    color=color.blue,
                    texture='grass',
                    position=TankChassis.position,
                    rotation=(0, 0, 0),
                    scale=1,
                    collider='mesh',
                    )

def update():
    # Tank Chassis Movement-Forward/Backward
    if held_keys['w']:
        global Speed
        TankChassis.position += TankChassis.forward * time.dt * 10
    if held_keys['s']:
        TankChassis.position -= TankChassis.forward * time.dt * 10
    # Tank Chassis Movement-Rotate
    if held_keys['a']:
        TankChassis.rotation_y -= 50 * time.dt
    if held_keys['d']:
        TankChassis.rotation_y += 50 * time.dt

    # Turret Movement
    if held_keys['q'] and camera.rotation_y > -20:
        Turret.rotation_y -= 80 * time.dt
        camera.rotation_y -= 30 * time.dt
        camera.x += 5 * time.dt
    if held_keys['e'] and camera.rotation_y < 20:
        Turret.rotation_y += 80 * time.dt
        camera.rotation_y += 30 * time.dt
        camera.x -= 5 * time.dt

    # Test Enemy Movement
    TurretEn.rotation_y -= 50 * time.dt
    TankChassisEn.position += TankChassisEn.forward * time.dt
    TankChassisEn.rotation_y += 50 * time.dt

    # Test Bullet
    if held_keys['left mouse']:
        bullet()

    # Camera Zoom in and Out (Make Mouse Wheel if possible)
    if held_keys['i'] and camera.rotation_x > 3:
        camera.rotation_x -= 50 * time.dt
        camera.z -= 50 * time.dt
    if held_keys['k'] and camera.rotation_x < 25:
        camera.rotation_x += 50 * time.dt
        camera.z += 50 * time.dt

    # Collision Testing
    if TankChassis.intersects(TankChassisEn):
        TankChassis.position -= TankChassis.forward * time.dt * 10
    if TankChassis.intersects(BuildingBlock):
        TankChassis.position -= TankChassis.forward * time.dt * 10
    if TankChassis.intersects(BuildingBlock2):
        TankChassis.position -= TankChassis.forward * time.dt * 10

# Window Settings
main = Ursina()
window.title = 'World of Tenks'
window.borderless = False
window.exit_button.visible = False

# Ground
Ground = Entity(model='plane',
                color=color.green,
                texture='grass',
                position=(0, 0, 0),
                rotation=(0, 0, 0),
                scale=1000,
                collider='mesh'
                )

# Spawn TankChassis
TankChassis = Entity(model='Assets/TankChassis.obj',
                     color=color.blue,
                     texture='grass',
                     position=(0, 0, 0),
                     rotation=(0, 0, 0),
                     scale=1,
                     collider='box',
                     )

# Spawn Turret on top and attached to TankChassis
Turret = Entity(parent=TankChassis,
                model='Assets/Turret.obj',
                color=color.blue,
                texture='brick',
                position=(0, 0, 0),
                scale=1,
                collider='mesh',
                )

# Spawn Enemy Test TankChassis
TankChassisEn = Entity(model='Assets/TankChassis.obj',
                       color=color.gray,
                       texture='Assets/Metal.jpg',
                       position=(20, 0, 0),
                       rotation=(0, 0, 0),
                       scale=1,
                       collider='mesh',
                       )

# Spawn Turret on top and attached to TankChassis
TurretEn = Entity(parent=TankChassisEn,
                  model='Assets/Turret.obj',
                  color=color.blue,
                  texture='brick',
                  position=(0, 0, 0),
                  scale=1,
                  collider='mesh',
                  )

# Buildings
BuildingBlock = Entity(model='Assets/HouseBlock.obj',
                       color=color.gray,
                       texture='Assets/Metal.jpg',
                       position=(30, 0, 200),
                       rotation=(0, 0, 0),
                       scale=0.8,
                       collider='mesh',
                       )

BuildingBlock2 = Entity(model='Assets/HouseBlock.obj',
                       texture='grass',
                       position=(-10, 0, 200),
                       rotation=(0, 180, 0),
                       scale=0.8,
                       collider='mesh',
                       )



# Make sky and editor camera
Sky()
camera.parent = TankChassis

# Camera Starting Position
camera.z = -28
camera.y = 10
camera.rotation_x = 10
# Run Program
main.run()
