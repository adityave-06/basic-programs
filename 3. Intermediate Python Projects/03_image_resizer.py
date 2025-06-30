import cv2 

source = "scenery.jpg"
destination = "newImage.jpg"
src = cv2.imread("scenery.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)

scale_percent = 50
 
new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

output = cv2.resize(src,(new_width, new_height))

cv2.imwrite('newImage.jpg', output)
cv2.waitKey(0)