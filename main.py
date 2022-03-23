from ursina import *

def Bullet():
    bullet = Entity(model='cube',
           color=color.blue,
           texture='grass',
           position=Turret.position,
           rotation=(0, 0, 0),
           scale=1,
           collider='mesh',
           )

def update():
    # Tank Chassis Movement-Forward/Backward
    if held_keys['w']:
        TankChassis.position += TankChassis.forward * time.dt
    if held_keys['s']:
        TankChassis.position -= TankChassis.forward * time.dt
    # Tank Chassis Movement-Rotate
    if held_keys['a']:
        TankChassis.rotation_y -= 50 * time.dt
    if held_keys['d']:
        TankChassis.rotation_y += 50 * time.dt

    # Test Bullet
    if held_keys['left mouse']:
        Bullet()

    # Turret Movement
    if held_keys['q']:
        Turret.rotation_y -= 50 * time.dt
    if held_keys['e']:
        Turret.rotation_y += 50 * time.dt

    # Test Enemy Movement
    TurretEn.rotation_y -= 50 * time.dt
    TankChassisEn.position += TankChassisEn.forward * time.dt
    TankChassisEn.rotation_y += 50 * time.dt

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
                scale=100,
                collider='mesh'
                )

# Spawn TankChassis
TankChassis = Entity(model='Assets/TankChassis.obj',
                     color=color.blue,
                     texture='grass',
                     position=(0, 0, 0),
                     rotation=(0, 0, 0),
                     scale=1,
                     collider='mesh',
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
                     color=color.blue,
                     texture='grass',
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


# Make sky and editor camera
Sky()
camera.parent = TankChassis
camera.x = 2
camera.y = 10
camera.rotation_x = 16

# Run Program
main.run()


