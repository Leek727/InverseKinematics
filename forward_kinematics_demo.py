""" Da plan
Find first vector and for next vectors add angle to first one and it should work
"""
import pygame
import math
import time

pygame.init()

screen_w, screen_h = 600, 600

# Set up the drawing window
screen = pygame.display.set_mode([screen_w, screen_h])

# draw cartesian vector
def draw_cvector(screen, tail, head, color=(255,255,255)):
    pygame.draw.line(screen, color, ((tail[0] + screen_w/2), (screen_h-tail[1])), ((head[0] + screen_w/2), (screen_h-head[1])))

def sum_vector(A, B):
    return (A[0] + B[0], A[1] + B[1])

def convert_cartesian(A):
    # A = (mag, angle)
    angle = (A[1] * math.pi) / 180
    mag = A[0]
    return (mag * math.cos(angle), mag * math.sin(angle))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for a in range(0, 180, 20):
        for b in range(0, 180, 20):
            for c in range(0, 180, 20):
                screen.fill((0, 0, 0))
                vector_array = [(50, a), (50, b), (50, 65)] # polar vectors

                # draw full arm
                cum_vector = [0,0] # cumulative vector
                for vector in vector_array:
                    v1 = convert_cartesian(vector)
                    draw_cvector(screen, cum_vector, sum_vector(cum_vector, v1))
                    cum_vector = sum_vector(cum_vector, v1)

                # draw end point
                draw_cvector(screen, (0,0), cum_vector, (255,255,0))

                # Flip the display
                pygame.display.flip()

                time.sleep(.01)

# Done! Time to quit.
pygame.quit()