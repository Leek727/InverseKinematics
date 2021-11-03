import pygame
import math
import time
import json
#from closest_point import find_closest

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

# function to chose closest next arm position
def best_angle(old_angles, new_angles):
    # return if only one possible angle
    if len(new_angles) == 1:
        return new_angles[0]

    best_angles = []
    angle_distance = 1000000
    for angle_arr in new_angles:
        temp_distance = 0
        for i in range(len(angle_arr)):
            temp_distance += abs(angle_arr[i] - old_angles[i])

        if temp_distance < angle_distance:
            angle_distance = temp_distance
            best_angles = angle_arr
    
        print(angle_distance)

    return best_angles
        

print("Loading data table...")
data = {} # load angle table
with open("vector_table.json", "r") as f:
    data = json.loads(f.read())

print("Done!")

# store converted mouse pos
pos = []
# store array of vectors representing arm segments
vector_array = []
angles = []
# Run until the user asks to quit
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos
            pos = [round(pos[0] - screen_w/2), screen_h-pos[1]]

    try:
        str_pos = str(pos[0]) + "," + str(pos[1])
        angles = best_angle(angles, data[str_pos])

        
    
    except:
        print("Waiting for mouse pos...")
        print(pos)
    
    if len(angles) == 3:
        vector_array = [(50, angles[0]), (50, angles[1]), (50, angles[2])]
    

    screen.fill((0, 0, 0))

    # draw full arm
    cum_vector = [0,0] # cumulative vector
    for vector in vector_array:
        v1 = convert_cartesian(vector)
        draw_cvector(screen, cum_vector, sum_vector(cum_vector, v1))
        cum_vector = sum_vector(cum_vector, v1)

    # draw end point
    draw_cvector(screen, (0,0), cum_vector, (255,255,0))

    pygame.display.update()
pygame.quit()


"""
Inverse Kinematics Part
Load json to python dict
get mouse position and try to find in table
choose the first value for now and render arm
"""