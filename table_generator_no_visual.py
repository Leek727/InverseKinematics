import math
import time
import json

# arm length
arm_lengths = [100, 100, 100]

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

if __name__ == "__main__":
    # loop through every angle by step
    for a in range(0, 180, 1):
        for b in range(0, 360, 1):
            for c in range(0, 360, 1):
                # ------------------ forward kinematics part ------------------
                vector_array = [(arm_lengths[0], a), (arm_lengths[1], b), (arm_lengths[2], c)] # polar vectors

                # dont draw full arm
                cum_vector = [0,0]
                for vector in vector_array:
                    v1 = convert_cartesian(vector)
                    cum_vector = sum_vector(cum_vector, v1)


                # ------------------ hash map making part ------------------
                end_point = []
                key = str(round(cum_vector[0])) + "," + str(round(cum_vector[1]))
                try:
                    end_point = data[key]
                
                except:
                    data[key] = []

                end_point.append([a,b,c])

        print(f"{round((a / 180) * 100)}%")


print("Writing stuff...")
with open("vector_table.json", "w") as write_file:
    json.dump(data, write_file)

print("Done!")