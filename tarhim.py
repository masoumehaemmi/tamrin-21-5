
import cv2

dainasor = cv2.imread("T_rex.jpg", 0)


for i in range(270):
    if i <= 50:
        for j in range(50-i, 270-i):
            if (j >= 0):
                dainasor[i, j] = 0
    else:
        for j in range(0, 270-i):
            if (j >= 0):
                dainasor[i, j] = 0
    
cv2.imwrite("dinosaur_dead.jpg", dainasor)

cv2.waitKey()