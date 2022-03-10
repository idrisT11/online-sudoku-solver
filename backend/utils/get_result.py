import cv2
import torch as tc
import torchvision.transforms as transforms
import imutils
import numpy as np
from skimage.segmentation import clear_border

import utils.model as model
from utils.model_utils import four_point_transform, order_point

import matplotlib.pyplot as plt



toTensor = transforms.ToTensor()

NetworkModel = model.NumberNetwork()
NetworkModel.load_state_dict(tc.load('./utils/model.nt'))

def getPrediction(cell):
    input_tensor = tc.tensor(cell, dtype=tc.float)
    input_tensor = input_tensor.unsqueeze(0).unsqueeze(0)

    prediction = NetworkModel(input_tensor)
    value = prediction.argmax(dim=1)
    return value

def get_result(imgPath, border):

    imgOri = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

    puzzleCnt = np.array(border)
    order_point(puzzleCnt)

    warpedOri = four_point_transform(imgOri, puzzleCnt.reshape(4, 2))

    warped = cv2.GaussianBlur(warpedOri, (7, 7), 3)   
    warped = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    warped = cv2.bitwise_not(warped)


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

        #cell = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
        cell = cv2.GaussianBlur(cell, (5, 5), 2)

        thresh = cv2.threshold(cell, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
        thresh = clear_border(thresh)

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

        ##########
        digit_value = getPrediction(cell_to_analyse)

        cell_val[i//9][i%9] = digit_value

    f = lambda x : x == 0

    return cell_val.tolist(), f(cell_val).tolist()