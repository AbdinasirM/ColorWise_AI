# from rembg import remove

# import cv2

# # Read image
# img = cv2.imread('C:/Users/Abdi/ColorWise_AI/Backend/imageProcessing/person.jpg')

# # Convert the image to RGB as rembg works with RGB images
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Remove background
# img_no_bg = remove(img_rgb)

# # Convert back to BGR
# img_no_bg_bgr = cv2.cvtColor(img_no_bg, cv2.COLOR_RGB2BGR)

# # Resize image
# img_no_bg_bgr = cv2.resize(img_no_bg_bgr, (640, 480))

# # Show images
# cv2.imshow('office', img)
# cv2.imshow('office no bg', img_no_bg_bgr)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


from rembg import remove
from PIL import Image

# Load the image
input_image_path = 'C:/Users/Abdi/ColorWise_AI/Backend/imageProcessing/person.jpg'
output_image_path = 'C:/Users/Abdi/ColorWise_AI/Backend/imageProcessing/output_image.png'

# Open the image file
input_image = Image.open(input_image_path)

# Remove the background
output_image = remove(input_image)

# Save the result
output_image.save(output_image_path)

print(f'Background removed and saved to {output_image_path}')