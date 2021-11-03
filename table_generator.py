import pygame
import math
import time
import json

pygame.init()

screen_w, screen_h = 600, 600

# Set up the drawing window
screen = pygame.display.set_mode([screen_w, screen_h])

# draw cartesian vector
def draw_cvector(screen, tail, head, color=(255,255,255)):
    pygame.draw.line(screen, color, ((tail[0] + screen_w/2), (screen_h-tail[1])), ((head[0] + screen_w/2), (screen_h-head[1])))

# sums two vectors
def sum_vector(A, B):
    # A = (x, y)
    return (A[0] + B[0], A[1] + B[1])

# converts polar to the other one
def convert_cartesian(A):
    # A = (mag, angle)
    angle = (A[1] * math.pi) / 180
    mag = A[0]
    return (mag * math.cos(angle), mag * math.sin(angle))

data = {} # big table that stores positions to angles

# Run until the user asks to quit
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # loop through every angle by step
    for a in range(0, 180, 10):
        for b in range(0, 360, 10):
            for c in range(0, 360, 10):
                # ------------------ forward kinematics part ------------------
                screen.fill((0, 0, 0)) # clear screen
                vector_array = [(50, a), (50, b), (50, c)] # polar vectors

                # draw full arm
                cum_vector = [0,0] # cumulative vector
                for vector in vector_array:
                    v1 = convert_cartesian(vector)
                    draw_cvector(screen, cum_vector, sum_vector(cum_vector, v1))
                    cum_vector = sum_vector(cum_vector, v1)

                # draw end point
                draw_cvector(screen, (0,0), cum_vector, (255,255,0))


                # ------------------ hash map making part ------------------
                end_point = []
                key = str(round(cum_vector[0])) + "," + str(round(cum_vector[1]))
                try:
                    end_point = data[key]
                
                except:
                    data[key] = []

                end_point.append([a,b,c])
                data[key] = end_point




                # ------------------ Update display ------------------
                pygame.display.update()

                #time.sleep(.01)

        print(f"{round((a / 180) * 100)}%")

    running = False

pygame.quit()

with open("vector_table.json", "w") as write_file:
    json.dump(data, write_file)

"""
Generator
make hash map
loop through all angles and find stuff:
    key = end point, [x,y]
    value = list of angles, [[a,b,c], [a,b,c]]

write to json
----------------------------------------------

Inverse Kinematics Part
Load json to python dict
get mouse position and try to find in table
choose the first value for now and render arm
"""