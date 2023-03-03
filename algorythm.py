matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

lining = ""
for line in matrix:
    for item in line:
        if item == 0:
            lining += "□ "
        else:
            lining += "■ "
    print(lining)
    lining = ""

i = 0
j = 0

for y in range(len(matrix)-1):
    for x in range(len(matrix[0])-1):
        if matrix[y][x] + matrix[y][x+1] + matrix[y+1][x] + matrix[y+1][x+1] == 1:
            i += 1
        if matrix[y][x] + matrix[y][x+1] + matrix[y+1][x] + matrix[y+1][x+1] == 3:
            j += 1

print(f"\nN = (i - j) / 4 = ({i} - {j}) / 4 = {int((i-j)/4)}")
