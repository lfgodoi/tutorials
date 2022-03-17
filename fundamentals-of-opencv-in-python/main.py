# Importing packages
import cv2

# Opening an RGB image
image = cv2.imread("images/messi.jpg")
cv2.imshow("Original image", image)
cv2.waitKey()
    
# Checking RGB image dimensions
print("Original image shape:", image.shape)

# Convert image from RGB to grayscale
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", image_grayscale)
cv2.waitKey()

# Checking grayscale image dimensions
print("Grayscale image shape:", image_grayscale.shape)

# Removing blue and green channels: [0 = blue, 1 = green, 2 = red]
image_red = image.copy()
image_red[:, :, :2] = 0 
cv2.imshow("Red image", image_red)
cv2.waitKey()

# Checking red image dimensions
print("Red image shape:", image_red.shape)

# Rotating image
height, width, _ = image.shape
center = (width//2, height//2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0) 
image_rotated = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow("Rotated image", image_rotated)
cv2.waitKey()

# Resizing the image
new_size = (width//3, height//3)
image_resized = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized image", image_resized)
cv2.waitKey()

# Checking new shape
print("Resized image shape:", image_resized.shape)

# Drawing a line in image
image_line = cv2.line(image.copy(), (0, 0), (height//2, width//2), (0, 255, 255), 10)
cv2.imshow("Image with line", image_line)
cv2.waitKey()

# Drawing a rectangle in image
image_rectangle = cv2.rectangle(image.copy(), (500, 150), (900, 550), (0, 255, 255), 5)
cv2.imshow("Image with rectangle", image_rectangle)
cv2.waitKey()

# Drawing a circle in image
image_circle = cv2.circle(image.copy(), (300, 300), 200, (0, 255, 255), 5)
cv2.imshow("Image with circle", image_circle)









