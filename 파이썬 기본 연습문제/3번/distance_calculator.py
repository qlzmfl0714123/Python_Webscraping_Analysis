import math

point1 = (0, 0)
point2 = (3, 4)

print("점1:", point1)
print("점2:", point2)

distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
print("두 점 사이의 거리:", distance)