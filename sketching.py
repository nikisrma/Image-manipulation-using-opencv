# How to make sketch of an made using opencv
import cv2
img = cv2.imread('photo.jpg')
img_rgb = cv2.resize(img, (300, 300))
cv2.imshow("Original image", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# convert the color image into gray image by using cv2.COLOR_BGR2GRAY
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# now we invert the grey image into reverse
img_gray_inv = 255-img_gray
cv2.imshow("Invert gray scale", img_gray_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# blur the image
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(301, 301), sigmaX=0, sigmaY=0)
cv2.imshow("Blur Inverted Gray scale", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

# the dodgev2 function will mask gray image with img_blur
def dodgev2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

img_blend = dodgev2(img_gray, img_blur)
cv2.imshow("sketch", img_blend)
cv2.waitKey(0)
cv2.destroyAllWindows()

