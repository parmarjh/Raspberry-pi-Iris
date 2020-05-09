import  cv2

def preprocess(image):
    """Preprocesses the image to enhance the process of finding the iris. Crops high values of the image and blurs it.

    :param image: Image of an eye
    :return: Preprocessed image
    """
    img = image.copy()
    img[img > 225] = 30
    return cv2.medianBlur(img, 21)

image = cv2.imread('Denoised.bmp')

img = preprocess(image)

cv2.imwrite('Desired_name.jpg', img)
