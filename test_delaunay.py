# -*- coding: utf-8 -*-
"""test_delaunay.ipynb

"""

import random
import numpy as np

# 使用OpenCV進行圖像處理
import cv2

# 1.定義起始終點
startPoint = (100, 100)
endPoint = (500, 500)

# 2.生成隨機點
points = []
points.append(startPoint)
points.append(endPoint)

for i in range(20):
    x = random.randint(100, 500)
    y = random.randint(100, 500)
    points.append((x, y))

# 3.德勞內三角剖分
# 3.1.將隨機點進行排序
points.sort(key=lambda x: x[0])
# 3.2.進行德勞內三角剖分
tri = cv2.Subdiv2D((0, 0, 600, 600))
for p in points:
    # print(type(p))
    tri.insert(p)
# 3.3.將隨機點轉換為numpy array
points = np.array(points)
# # 3.4.獲取三角剖分的結果
triangleList = tri.getTriangleList()
# 3.5.將三角剖分的結果轉換為list
triangles = []
for t in triangleList:
    triangles.append(((t[0], t[1]), (t[2], t[3]), (t[4], t[5])))
# 3.6.將三角剖分的結果轉換為numpy array
triangles = np.array(triangles)

# 到目前先繪圖
import cv2

img = np.zeros((600, 600, 3), np.uint8)
for t in triangles:
    pt1 = (int(t[0][0]), int(t[0][1]))
    pt2 = (int(t[1][0]), int(t[1][1]))
    pt3 = (int(t[2][0]), int(t[2][1]))

    cv2.line(img, pt1, pt2, (255, 255, 255), 1)
    cv2.line(img, pt2, pt3, (255, 255, 255), 1)
    cv2.line(img, pt3, pt1, (255, 255, 255), 1)
for p in points:
    cv2.circle(img, p, 2, (255, 255, 255), 2)
cv2.circle(img, startPoint, 2, (0, 255, 0), 2)
cv2.circle(img, endPoint, 2, (0, 0, 255), 2)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()