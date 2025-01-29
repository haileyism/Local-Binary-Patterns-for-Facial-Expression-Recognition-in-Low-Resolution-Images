import cv2
import numpy as np

def lbp_calculate(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Initialize the LBP image
    lbp = np.zeros_like(gray)
    
    # Compute the LBP for each pixel
    for i in range(1, gray.shape[0]-1):
        for j in range(1, gray.shape[1]-1):
            center = gray[i, j]
            binary = ''
            for row in range(i-1, i+2):
                for col in range(j-1, j+2):
                    if row == i and col == j:
                        continue
                    binary += '1' if gray[row, col] > center else '0'
            lbp[i, j] = int(binary, 2)
    return lbp

# Load your image
image = cv2.imread('WechatIMG9526.jpg')

# Calculate LBP
lbp_image = lbp_calculate(image)

# Save or display the LBP image
cv2.imwrite('lbp_image.jpg', lbp_image)
cv2.imshow('LBP Image', lbp_image)
cv2.waitKey(0)
# cv2.destroyAllWindows()
