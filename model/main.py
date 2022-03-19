import cv2
from utils import four_point_transform
from utils import order_point
import model

import torch as tc
import torchvision.transforms as transforms
import imutils

import numpy as np
import matplotlib.pyplot as plt

from skimage.segmentation import clear_border



toTensor = transforms.ToTensor()

NetworkModel = model.NumberNetwork()
NetworkModel.load_state_dict(tc.load('./modelFinal.nt')) 
image_path = './images/sudoku.jpg'



def getPrediction(cell):
    input_tensor = tc.tensor(cell, dtype=tc.float)
    input_tensor = input_tensor.unsqueeze(0).unsqueeze(0)
    print(input_tensor.shape)
    prediction = NetworkModel(input_tensor)
    value = prediction.argmax(dim=1)
    value += 1

    return value


imgOri = cv2.imread(image_path)

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

img = cv2.GaussianBlur(img, (7, 7), 3)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img = cv2.bitwise_not(img)

plt.imshow(img)
plt.show()


cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)#Pour calculer l'aire waqil
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

####################
#####"????????"
####################
puzzleCnt = None

for c in cnts:
    
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    
    # if our approximated contour has four points, then we can
	# assume we have found the outline of the puzzle
    if len(approx) == 4:
        puzzleCnt = approx
        break


####################
#####END "????????"
####################
puzzleCnt = puzzleCnt.reshape(4, 2)
#print(puzzleCnt)#numpy array
order_point(puzzleCnt)

imgOri = cv2.imread(image_path)


img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

warped = four_point_transform(img, puzzleCnt.reshape(4, 2))
warpedOri = four_point_transform(imgOri, puzzleCnt.reshape(4, 2))


cv2.drawContours(imgOri, [approx], -1, (0, 255, 0), 2)

plt.imshow(warped)
plt.show()


#################################################################

width_grid = warped.shape[0]
height_grid = warped.shape[1]

width_cell = int(width_grid / 9)
height_cell = int(height_grid / 9)

cells_img_array = []

cell_val = np.zeros((9, 9))

for i in range(9):
    for j in range(9):
        x = i*width_cell
        y = j*height_cell

        cells_img_array.append(warpedOri[x:x+width_cell, y:y+height_cell])

for i, cell in enumerate(cells_img_array):

    cell = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
    cell = cv2.GaussianBlur(cell, (5, 5), 2)

    thresh = cv2.adaptiveThreshold(cell, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    _, thresh1 = cv2.threshold(cell, 0, 255,  cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    thresh = clear_border(thresh)
    #print(thresh)
    #plt.imshow(thresh)
    #plt.show()
    #plt.imshow(thresh1)
    #plt.show()

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    #Si ya aucun contour, c'est que ya pas de nombre
    if len(cnts) == 0:
        continue
    
    c = max(cnts, key=cv2.contourArea)
    mask = np.zeros(thresh.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1) # Le fait d'avoir mis -1 à la fin sert à remplir le contour

    (h, w) = thresh.shape
    percentFilled = cv2.countNonZero(mask)/float(w*h)

    #Si le truc detecté represente moin de 5% de la case, c'est que c'est une fluctuation (un bruit)
    if percentFilled < 0.05:
        continue


    #Sinon on applique le masque sur la case pour enlever toute fluctuations possibles
    cell_with_digit = cv2.bitwise_and(thresh, mask)
    cell_to_analyse = cv2.resize(cell_with_digit, (28, 28))
    #cell_to_analyse = cv2.threshold(cell_to_analyse, 127, 255, cv2.THRESH_BINARY)[1]


    ##########
    digit_value = getPrediction(cell_to_analyse)
    print(digit_value)
    cell_val[i//9][i%9] = digit_value
    plt.imshow(cell_to_analyse)
plt.show()   

print(cell_val)     
