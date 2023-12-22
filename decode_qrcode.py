import cv2
detector = cv2.QRCodeDetector()

# The filename of the picture to be decoded
img_name = "output/fig_0010.png"

img = cv2.imread(img_name)
cropped_img = img[0:290, 0:290]
data, bbox, _ = detector.detectAndDecode(img)
print(f"qrcode = {data}")
