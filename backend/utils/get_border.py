import cv2
import torchvision.transforms as transforms
import imutils
from skimage.segmentation import clear_border


toTensor = transforms.ToTensor()

def get_border(imgPath):

    imgOri = cv2.imread(imgPath)


    img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (7, 7), 3)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img = cv2.bitwise_not(img)


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
        
        if len(approx) == 4:
            puzzleCnt = approx
            break


    ####################
    #####END "????????"
    ####################
    puzzleCnt = puzzleCnt.reshape(4, 2)

    return puzzleCnt.tolist()

