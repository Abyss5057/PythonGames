# Input
height = 2
width = 3

data = [
    [3,6,1],
    [5,8,7]
]

frame = "#"

print(frame * (len(data[0]) + 2))

for i in range(height):
    line = frame

    for j in range(width):
        line += str(data[i][j])
    
    line += frame
    print(line)

print(frame * (len(data[0]) + 2))

