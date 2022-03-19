import numpy as np
import cv2


def order_point(pts):
    rect = np.zeros((4, 2), dtype = "float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    
    return rect

def four_point_transform(image, pts):

    (tl, tr, br, bl) = rect = order_point(pts)

    width_top = np.sqrt((tl[0] - tr[0])**2 + (tl[1] - tr[1])**2)
    width_bottom = np.sqrt((bl[0] - br[0])**2 + (bl[1] - br[1])**2)

    #Le width de l'image final va etre le max entre le width du coté du haut
    #et du coté du bas, (le int() sert à transformer la matrice numpy en integer)
    width_image_final = max(int(width_bottom), int(width_top))

    height_left = np.sqrt((tl[0] - bl[0])**2 + (tl[1] - bl[1])**2)
    height_right = np.sqrt((tr[0] - br[0])**2 + (tr[1] - br[1])**2)

    #De memepour le height
    height_image_final = max(int(height_left), int(height_right))


    #On crée ensuite la matrice qui va encoder notre y transformation 

    tr = np.array([
        [0, 0],
        [width_image_final -1, 0],
        [width_image_final -1, height_image_final-1],
        [0, height_image_final-1]
    ], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, tr)

    new_img = cv2.warpPerspective(image, M, (width_image_final, height_image_final))

    return new_img
