import pygame
pygame.init()

class Button:
    def __init__(self):
        self.pressed = 0
        self.on_press = 0
        self.on_release = 0
    def update(self, new_state):
        self.on_press = new_state != self.pressed if new_state else 0
        self.on_release = 0 if new_state else new_state != self.pressed
        self.pressed = new_state

class KeyMap:
    R1 = 0
    L1 = 1
    start = 2
    select = 3
    R2 = 4
    L2 = 5
    F1 = 6
    F2 = 7
    A = 8
    B = 9
    X = 10
    Y = 11
    up = 12
    right = 13
    down = 14
    left = 15


class Joystick:
    def __init__(self):
        self.lx = 0
        self.ly = 0
        self.rx = 0
        self.ry = 0
        self.button = [Button() for _ in range(16)]
        # Check for connected joysticks
        assert pygame.joystick.get_count() > 0, "No joystick found. Please connect a joystick to control the robot."
        assert pygame.joystick.get_count() == 1, "Only one joystick is supported. Please disconnect other joysticks."
        self.pygame_joystick = pygame.joystick.Joystick(0)
        self.pygame_joystick.init()

    def update(self):
        pygame.event.pump()
        # XBOX joystick mapping
        self.button[KeyMap.R1].update(self.pygame_joystick.get_button(5))
        self.button[KeyMap.L1].update(self.pygame_joystick.get_button(4))
        self.button[KeyMap.start].update(self.pygame_joystick.get_button(7))
        self.button[KeyMap.select].update(self.pygame_joystick.get_button(6))
        self.button[KeyMap.R2].update(self.pygame_joystick.get_button(7))
        self.button[KeyMap.L2].update(self.pygame_joystick.get_axis(2) > 0)
        self.button[KeyMap.F1].update(0)
        self.button[KeyMap.F2].update(0)
        self.button[KeyMap.A].update(self.pygame_joystick.get_button(0))
        self.button[KeyMap.B].update(self.pygame_joystick.get_button(1))
        self.button[KeyMap.X].update(self.pygame_joystick.get_button(2))
        self.button[KeyMap.Y].update(self.pygame_joystick.get_button(3))
        self.button[KeyMap.up].update(self.pygame_joystick.get_hat(0)[1] == 1)
        self.button[KeyMap.right].update(self.pygame_joystick.get_hat(0)[0] == 1)
        self.button[KeyMap.down].update(self.pygame_joystick.get_hat(0)[1] == -1)
        self.button[KeyMap.left].update(self.pygame_joystick.get_hat(0)[0] == -1)
        self.lx = self.pygame_joystick.get_axis(0)
        self.ly = self.pygame_joystick.get_axis(1)
        self.rx = self.pygame_joystick.get_axis(3)
        self.ry = self.pygame_joystick.get_axis(4)