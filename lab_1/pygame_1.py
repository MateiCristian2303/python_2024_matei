import pygame
from pygame.draw import *
import math

pygame.init()

fps = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

face_color = (255, 255, 0)
outline_color = (0, 0, 0)
eye_color = (255, 0, 0)


def draw_eyebrows(x, y, angle):
    rectangle_center = (x, y)
    rectangle_angle_radians = math.radians(angle)
    rectangle_width = 140
    rectangle_height = 20
    half_width = rectangle_width / 2
    half_height = rectangle_height / 2
    cos_theta = math.cos(rectangle_angle_radians)
    sin_theta = math.sin(rectangle_angle_radians)
    vertices = [
        (rectangle_center[0] + half_width * cos_theta - half_height * sin_theta,
         rectangle_center[1] + half_width * sin_theta + half_height * cos_theta),
        (rectangle_center[0] - half_width * cos_theta - half_height * sin_theta,
         rectangle_center[1] - half_width * sin_theta + half_height * cos_theta),
        (rectangle_center[0] - half_width * cos_theta + half_height * sin_theta,
         rectangle_center[1] - half_width * sin_theta - half_height * cos_theta),
        (rectangle_center[0] + half_width * cos_theta + half_height * sin_theta,
         rectangle_center[1] + half_width * sin_theta - half_height * cos_theta)
    ]
    polygon(screen, outline_color, vertices)


def draw_eye(x, y, eye_color, size):
    """
    draws an eye with the color 'eye_color' and of size 'size'
    :param x: x coords of place
    :param y: y coords of place
    :param eye_color: color of the iris
    :param size: size of the eye
    :return: eye
    """
    black_color = (0, 0, 0)
    circle(screen, eye_color, (x, y), size)
    circle(screen, black_color, (x, y), size, 3)
    circle(screen, black_color, (x, y), size / 2)


circle(screen, face_color, (300, 300), 200)
circle(screen, outline_color, (300, 300), 200, 5)
draw_eye(220, 250, eye_color, 40)
draw_eye(380, 250, eye_color, 30)
rect(screen, outline_color, ((210, 420), (180, 30)))
draw_eyebrows(205, 195, 20)
draw_eyebrows(395, 215, 180)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()