import cv2
img = cv2.imread("photo.jpg")

# resize the image
img_rgb = cv2.resize(img, (300, 300))
cv2.imshow("Original image", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# extracting the height and width of an image
h, w = img_rgb.shape[:2]
print("Height = {}, Width = {}".format(h, w))

# convert image to gray scale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#saving image

cv2.imwrite("newimg.jpg", img_gray)

# rotating image

img_rotate_90_clockwise = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated image", img_rotate_90_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()


# flipping image

# flip vertical

flip = cv2.flip(img_rgb, 0)
cv2.imshow("Vertical image flip", flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

# flip horizontal

flip = cv2.flip(img_rgb, 1)
cv2.imshow("Horizontal image flip", flip)
cv2.waitKey(0)
cv2.destroyAllWindows()


# change the color of image
b = img_rgb.copy()
# set green and red channel to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

r = img_rgb.copy()
# set green and blue channel to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

g = img_rgb.copy()
# set blue and red channel to 0
g[:, :, 0] = 0
g[:, :, 2] = 0


# RGB - BLUE

cv2.imshow("blue image ", b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RGB - GREEN
cv2.imshow("GREEN image ", g)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rgb - red

cv2.imshow("red image ", r)
cv2.waitKey(0)
cv2.destroyAllWindows()



