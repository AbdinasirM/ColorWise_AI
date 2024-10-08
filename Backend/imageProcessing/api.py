# from fastapi import FastAPI, UploadFile, File
# from typing import Dict
# import numpy as np
# import cv2
# from io import BytesIO

# app = FastAPI()

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, any]:
#     # Read the image file
#     image_bytes = await file.read()
    
#     # Convert bytes to numpy array
#     np_array = np.frombuffer(image_bytes, np.uint8)
    
#     # Decode the numpy array into an image
#     image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
#     if image is None:
#         return {"error": "Invalid image format or cannot decode image"}
    
#     # Convert the image to the HSV color space
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # Define a range of HSV values for skin tones
#     lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#     upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#     # Threshold the image to select only skin pixels
#     skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#     # Apply the mask to the original image to show only the skin pixels
#     skin = cv2.bitwise_and(image, image, mask=skin_mask)

#     # Convert the skin-only image to HSV color space for analysis
#     skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#     # Calculate the average skin color
#     skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#     average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#     # Average skin color in HSV
#     average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#     # Convert HSV to BGR
#     average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#     # Define a color palette for recommendations (BGR format)
#     color_palette = {
#         'White': [255, 255, 255],
#         'Black': [0, 0, 0],
#         'Red': [0, 0, 255],
#         'Green': [0, 255, 0],
#         'Blue': [255, 0, 0],
#         'Yellow': [0, 255, 255],
#         'Orange': [0, 165, 255],
#         'Purple': [128, 0, 128],
#         'Pink': [203, 192, 255],
#         'Beige': [245, 245, 220],
#         'Brown': [42, 42, 165],
#         'Gray': [128, 128, 128],
#         'Light Gray': [211, 211, 211],
#         'Dark Gray': [169, 169, 169],
#         'Light Blue': [173, 216, 230],
#         'Dark Blue': [0, 0, 139],
#         'Turquoise': [64, 224, 208],
#         'Teal': [0, 128, 128],
#         'Coral': [255, 127, 80],
#         'Salmon': [250, 128, 114],
#         'Lavender': [230, 230, 250],
#         'Olive': [128, 128, 0],
#         'Maroon': [128, 0, 0],
#         'Indigo': [75, 0, 130],
#         'Mint': [189, 252, 201]
#     }

#     # Function to convert BGR to HSV
#     def bgr_to_hsv(bgr):
#         bgr_image = np.uint8([[bgr]])
#         hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#         return hsv_image[0][0]

#     # Function to calculate the Euclidean distance between two colors
#     def color_distance(color1, color2):
#         return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#     # Calculate the complementary color (180 degrees opposite in hue)
#     def complementary_color(hsv):
#         hue = hsv[0]
#         hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#         return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#     # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#     def analogous_colors(hsv, num_colors=10):
#         hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#         return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#     # Convert average skin color to HSV
#     skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#     # Get complementary and analogous colors
#     complementary_hsv = complementary_color(skin_hsv)
#     complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#     analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#     analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#     # Collect all colors for comparison
#     recommendations = {
#         'Average Skin Color': average_skin_color_bgr.tolist(),
#         'Complementary': complementary_bgr.tolist()
#     }
#     for i, color_bgr in enumerate(analogous_colors_bgr):
#         recommendations[f'Analogous {i+1}'] = color_bgr.tolist()

#     return recommendations

# from fastapi import FastAPI, UploadFile, File
# from typing import Dict
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove
# from PIL import Image


# app = FastAPI()

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, any]:
#     # Read the image file
#     image_bytes = await file.read()
#     output = remove(image_bytes)
    
#     # Convert bytes to numpy array
#     np_array = np.frombuffer(output, np.uint8)
    
#     # Decode the numpy array into an image
#     image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
#     if image is None:
#         return {"error": "Invalid image format or cannot decode image"}
    
#     # Convert the image to the HSV color space
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # Define a range of HSV values for skin tones
#     lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#     upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#     # Threshold the image to select only skin pixels
#     skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#     # Apply the mask to the original image to show only the skin pixels
#     skin = cv2.bitwise_and(image, image, mask=skin_mask)

#     # Convert the skin-only image to HSV color space for analysis
#     skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#     # Calculate the average skin color
#     skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#     average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#     # Average skin color in HSV
#     average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#     # Convert HSV to BGR
#     average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#     # Define a color palette for recommendations (BGR format)
#     color_palette = {
#         'White': [255, 255, 255],
#         'Black': [0, 0, 0],
#         'Red': [0, 0, 255],
#         'Green': [0, 255, 0],
#         'Blue': [255, 0, 0],
#         'Yellow': [0, 255, 255],
#         'Orange': [0, 165, 255],
#         'Purple': [128, 0, 128],
#         'Pink': [203, 192, 255],
#         'Beige': [245, 245, 220],
#         'Brown': [42, 42, 165],
#         'Gray': [128, 128, 128],
#         'Light Gray': [211, 211, 211],
#         'Dark Gray': [169, 169, 169],
#         'Light Blue': [173, 216, 230],
#         'Dark Blue': [0, 0, 139],
#         'Turquoise': [64, 224, 208],
#         'Teal': [0, 128, 128],
#         'Coral': [255, 127, 80],
#         'Salmon': [250, 128, 114],
#         'Lavender': [230, 230, 250],
#         'Olive': [128, 128, 0],
#         'Maroon': [128, 0, 0],
#         'Indigo': [75, 0, 130],
#         'Mint': [189, 252, 201]
#     }

#     # Function to convert BGR to HSV
#     def bgr_to_hsv(bgr):
#         bgr_image = np.uint8([[bgr]])
#         hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#         return hsv_image[0][0]

#     # Function to calculate the Euclidean distance between two colors
#     def color_distance(color1, color2):
#         return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#     # Calculate the complementary color (180 degrees opposite in hue)
#     def complementary_color(hsv):
#         hue = hsv[0]
#         hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#         return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#     # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#     def analogous_colors(hsv, num_colors=10):
#         hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#         return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#     # Convert average skin color to HSV
#     skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#     # Get complementary and analogous colors
#     complementary_hsv = complementary_color(skin_hsv)
#     complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#     analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#     analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#     # Collect all colors for comparison
#     recommendations = {
#         'Average Skin Color': average_skin_color_bgr.tolist(),
#         'Complementary': complementary_bgr.tolist()
#     }
#     for i, color_bgr in enumerate(analogous_colors_bgr):
#         recommendations[f'Analogous {i+1}'] = color_bgr.tolist()

#     return recommendations

# from fastapi import FastAPI, UploadFile, File, HTTPException
# from typing import Dict
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove  # Assuming remove is async
# from PIL import Image

# app = FastAPI()

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, any]:
#     try:
#         # Read the image file
#         image_bytes = await file.read()
        
#         # Asynchronously remove the background
#         output = remove(image_bytes)  # Ensure this function is awaited if it's async
#         await output.save('out.png')
#         # Convert bytes to numpy array
#         np_array = np.frombuffer(output, np.uint8)
        
#         # Decode the numpy array into an image
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
#         if image is None:
#             raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
#         # Convert the image to the HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define a range of HSV values for skin tones
#         lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#         upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#         # Threshold the image to select only skin pixels
#         skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#         # Apply the mask to the original image to show only the skin pixels
#         skin = cv2.bitwise_and(image, image, mask=skin_mask)

#         # Convert the skin-only image to HSV color space for analysis
#         skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#         # Calculate the average skin color
#         skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#         if skin_pixels.size == 0:
#             raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
#         average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#         # Average skin color in HSV
#         average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#         # Convert HSV to BGR
#         average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         # Define a color palette for recommendations (BGR format)
#         color_palette = {
#             'White': [255, 255, 255],
#             'Black': [0, 0, 0],
#             'Red': [0, 0, 255],
#             'Green': [0, 255, 0],
#             'Blue': [255, 0, 0],
#             'Yellow': [0, 255, 255],
#             'Orange': [0, 165, 255],
#             'Purple': [128, 0, 128],
#             'Pink': [203, 192, 255],
#             'Beige': [245, 245, 220],
#             'Brown': [42, 42, 165],
#             'Gray': [128, 128, 128],
#             'Light Gray': [211, 211, 211],
#             'Dark Gray': [169, 169, 169],
#             'Light Blue': [173, 216, 230],
#             'Dark Blue': [0, 0, 139],
#             'Turquoise': [64, 224, 208],
#             'Teal': [0, 128, 128],
#             'Coral': [255, 127, 80],
#             'Salmon': [250, 128, 114],
#             'Lavender': [230, 230, 250],
#             'Olive': [128, 128, 0],
#             'Maroon': [128, 0, 0],
#             'Indigo': [75, 0, 130],
#             'Mint': [189, 252, 201]
#         }

#         # Function to convert BGR to HSV
#         def bgr_to_hsv(bgr):
#             bgr_image = np.uint8([[bgr]])
#             hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#             return hsv_image[0][0]

#         # Function to calculate the Euclidean distance between two colors
#         def color_distance(color1, color2):
#             return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#         # Calculate the complementary color (180 degrees opposite in hue)
#         def complementary_color(hsv):
#             hue = hsv[0]
#             hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#             return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#         # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#         def analogous_colors(hsv, num_colors=10):
#             hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#             return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#         # Convert average skin color to HSV
#         skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#         # Get complementary and analogous colors
#         complementary_hsv = complementary_color(skin_hsv)
#         complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#         analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#         # Collect all colors for comparison
#         recommendations = {
#             'Average Skin Color': average_skin_color_bgr.tolist(),
#             'Complementary': complementary_bgr.tolist()
#         }
#         for i, color_bgr in enumerate(analogous_colors_bgr):
#             recommendations[f'Analogous {i+1}'] = color_bgr.tolist()

#         return recommendations

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post('/test-upload')
# async def test_upload(file: UploadFile = File(...)):
#     return {"filename": file.filename}

# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Dict
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove
# from PIL import Image
# import os



# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Directory where the uploaded images will be saved
# UPLOAD_DIRECTORY = "uploaded_images"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, any]:
#     try:
#         # Save the uploaded file temporarily in the root directory
#         input_file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
#         with open(input_file_path, "wb") as f:
#             f.write(await file.read())
        
#         # Read the saved image file
#         with open(input_file_path, "rb") as f:
#             image_bytes = f.read()
        
#         # Remove the background
#         output_bytes = remove(image_bytes)
        
#         # Save the processed image in the root directory
#         output_image = Image.open(BytesIO(output_bytes))
#         output_image_path = os.path.join(".", "processed_" + file.filename)
#         output_image.save(output_image_path, format='PNG')  # Save as PNG to handle RGBA
        
#         # Convert bytes to numpy array
#         np_array = np.frombuffer(output_bytes, np.uint8)
        
#         # Decode the numpy array into an image
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
#         if image is None:
#             raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
#         # Convert the image to the HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define a range of HSV values for skin tones
#         lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#         upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#         # Threshold the image to select only skin pixels
#         skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#         # Apply the mask to the original image to show only the skin pixels
#         skin = cv2.bitwise_and(image, image, mask=skin_mask)

#         # Convert the skin-only image to HSV color space for analysis
#         skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#         # Calculate the average skin color
#         skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#         if skin_pixels.size == 0:
#             raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
#         average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#         # Average skin color in HSV
#         average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#         # Convert HSV to BGR
#         average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         # Define a color palette for recommendations (BGR format)
#         color_palette = {
#             'White': [255, 255, 255],
#             'Black': [0, 0, 0],
#             'Red': [0, 0, 255],
#             'Green': [0, 255, 0],
#             'Blue': [255, 0, 0],
#             'Yellow': [0, 255, 255],
#             'Orange': [0, 165, 255],
#             'Purple': [128, 0, 128],
#             'Pink': [203, 192, 255],
#             'Beige': [245, 245, 220],
#             'Brown': [42, 42, 165],
#             'Gray': [128, 128, 128],
#             'Light Gray': [211, 211, 211],
#             'Dark Gray': [169, 169, 169],
#             'Light Blue': [173, 216, 230],
#             'Dark Blue': [0, 0, 139],
#             'Turquoise': [64, 224, 208],
#             'Teal': [0, 128, 128],
#             'Coral': [255, 127, 80],
#             'Salmon': [250, 128, 114],
#             'Lavender': [230, 230, 250],
#             'Olive': [128, 128, 0],
#             'Maroon': [128, 0, 0],
#             'Indigo': [75, 0, 130],
#             'Mint': [189, 252, 201]
#         }

#         # Function to convert BGR to HSV
#         def bgr_to_hsv(bgr):
#             bgr_image = np.uint8([[bgr]])
#             hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#             return hsv_image[0][0]

#         # Function to calculate the Euclidean distance between two colors
#         def color_distance(color1, color2):
#             return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#         # Calculate the complementary color (180 degrees opposite in hue)
#         def complementary_color(hsv):
#             hue = hsv[0]
#             hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#             return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#         # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#         def analogous_colors(hsv, num_colors=10):
#             hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#             return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#         # Convert average skin color to HSV
#         skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#         # Get complementary and analogous colors
#         complementary_hsv = complementary_color(skin_hsv)
#         complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#         analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#         # Collect all colors for comparison
#         recommendations = {
#             'Average Skin Color': average_skin_color_bgr.tolist(),
#             'Complementary': complementary_bgr.tolist()
#         }
#         for i, color_bgr in enumerate(analogous_colors_bgr):
#             recommendations[f'Analogous {i+1}'] = color_bgr.tolist()

#         return {
#             "recommendations": recommendations,
#             "output_image_path": output_image_path
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post('/test-upload')
# async def test_upload(file: UploadFile = File(...)):
#     return {"filename": file.filename}


# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Dict
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove
# from PIL import Image
# import os

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Directory where the uploaded images will be saved
# UPLOAD_DIRECTORY = "uploaded_images"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# # Define a Pydantic model for the response
# class ColorRecommendation(BaseModel):
#     recommendations: Dict[str, List[int]]
#     output_image_path: str

# @app.post('/imageprocessing', response_model=ColorRecommendation)
# async def image_processing(file: UploadFile = File(...)) -> ColorRecommendation:
#     try:
#         # Save the uploaded file temporarily in the root directory
#         input_file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
#         with open(input_file_path, "wb") as f:
#             f.write(await file.read())
        
#         # Read the saved image file
#         with open(input_file_path, "rb") as f:
#             image_bytes = f.read()
        
#         # Remove the background
#         output_bytes = remove(image_bytes)
        
#         # Save the processed image in the root directory
#         output_image = Image.open(BytesIO(output_bytes))
#         output_image_path = os.path.join(".", "processed_" + file.filename)
#         output_image.save(output_image_path, format='PNG')  # Save as PNG to handle RGBA
        
#         # Convert bytes to numpy array
#         np_array = np.frombuffer(output_bytes, np.uint8)
        
#         # Decode the numpy array into an image
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
#         if image is None:
#             raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
#         # Convert the image to the HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define a range of HSV values for skin tones
#         lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#         upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#         # Threshold the image to select only skin pixels
#         skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#         # Apply the mask to the original image to show only the skin pixels
#         skin = cv2.bitwise_and(image, image, mask=skin_mask)

#         # Convert the skin-only image to HSV color space for analysis
#         skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#         # Calculate the average skin color
#         skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#         if skin_pixels.size == 0:
#             raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
#         average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#         # Average skin color in HSV
#         average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#         # Convert HSV to BGR
#         average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         # Define a color palette for recommendations (BGR format)
#         color_palette = {
#             'White': [255, 255, 255],
#             'Black': [0, 0, 0],
#             'Red': [0, 0, 255],
#             'Green': [0, 255, 0],
#             'Blue': [255, 0, 0],
#             'Yellow': [0, 255, 255],
#             'Orange': [0, 165, 255],
#             'Purple': [128, 0, 128],
#             'Pink': [203, 192, 255],
#             'Beige': [245, 245, 220],
#             'Brown': [42, 42, 165],
#             'Gray': [128, 128, 128],
#             'Light Gray': [211, 211, 211],
#             'Dark Gray': [169, 169, 169],
#             'Light Blue': [173, 216, 230],
#             'Dark Blue': [0, 0, 139],
#             'Turquoise': [64, 224, 208],
#             'Teal': [0, 128, 128],
#             'Coral': [255, 127, 80],
#             'Salmon': [250, 128, 114],
#             'Lavender': [230, 230, 250],
#             'Olive': [128, 128, 0],
#             'Maroon': [128, 0, 0],
#             'Indigo': [75, 0, 130],
#             'Mint': [189, 252, 201]
#         }

#         # Function to convert BGR to HSV
#         def bgr_to_hsv(bgr):
#             bgr_image = np.uint8([[bgr]])
#             hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#             return hsv_image[0][0]

#         # Function to calculate the Euclidean distance between two colors
#         def color_distance(color1, color2):
#             return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#         # Calculate the complementary color (180 degrees opposite in hue)
#         def complementary_color(hsv):
#             hue = hsv[0]
#             hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#             return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#         # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#         def analogous_colors(hsv, num_colors=10):
#             hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#             return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#         # Convert average skin color to HSV
#         skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#         # Get complementary and analogous colors
#         complementary_hsv = complementary_color(skin_hsv)
#         complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#         analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#         # Collect all colors for comparison
#         recommendations = {
#             'Average Skin Color': average_skin_color_bgr.tolist(),
#             'Complementary': complementary_bgr.tolist()
#         }
#         for i, color_bgr in enumerate(analogous_colors_bgr):
#             recommendations[f'Analogous {i+1}'] = color_bgr.tolist()

#         return ColorRecommendation(
#             recommendations=recommendations,
#             output_image_path=output_image_path
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post('/test-upload')
# async def test_upload(file: UploadFile = File(...)):
#     return {"filename": file.filename}



# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Dict
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove
# from PIL import Image
# import os



# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Directory where the uploaded images will be saved
# UPLOAD_DIRECTORY = "uploaded_images"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, any]:
#     try:
#         # Save the uploaded file temporarily in the root directory
#         input_file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
#         with open(input_file_path, "wb") as f:
#             f.write(await file.read())
        
#         # Read the saved image file
#         with open(input_file_path, "rb") as f:
#             image_bytes = f.read()
        
#         # Remove the background
#         output_bytes = remove(image_bytes)
        
#         # Save the processed image in the root directory
#         output_image = Image.open(BytesIO(output_bytes))
#         output_image_path = os.path.join(".", "processed_" + file.filename)
#         output_image.save(output_image_path, format='PNG')  # Save as PNG to handle RGBA
        
#         # Convert bytes to numpy array
#         np_array = np.frombuffer(output_bytes, np.uint8)
        
#         # Decode the numpy array into an image
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
#         if image is None:
#             raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
#         # Convert the image to the HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define a range of HSV values for skin tones
#         lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#         upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#         # Threshold the image to select only skin pixels
#         skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#         # Apply the mask to the original image to show only the skin pixels
#         skin = cv2.bitwise_and(image, image, mask=skin_mask)

#         # Convert the skin-only image to HSV color space for analysis
#         skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#         # Calculate the average skin color
#         skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#         if skin_pixels.size == 0:
#             raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
#         average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#         # Average skin color in HSV
#         average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#         # Convert HSV to BGR
#         average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         # Define a color palette for recommendations (BGR format)
#         color_palette = {
#             'White': [255, 255, 255],
#             'Black': [0, 0, 0],
#             'Red': [0, 0, 255],
#             'Green': [0, 255, 0],
#             'Blue': [255, 0, 0],
#             'Yellow': [0, 255, 255],
#             'Orange': [0, 165, 255],
#             'Purple': [128, 0, 128],
#             'Pink': [203, 192, 255],
#             'Beige': [245, 245, 220],
#             'Brown': [42, 42, 165],
#             'Gray': [128, 128, 128],
#             'Light Gray': [211, 211, 211],
#             'Dark Gray': [169, 169, 169],
#             'Light Blue': [173, 216, 230],
#             'Dark Blue': [0, 0, 139],
#             'Turquoise': [64, 224, 208],
#             'Teal': [0, 128, 128],
#             'Coral': [255, 127, 80],
#             'Salmon': [250, 128, 114],
#             'Lavender': [230, 230, 250],
#             'Olive': [128, 128, 0],
#             'Maroon': [128, 0, 0],
#             'Indigo': [75, 0, 130],
#             'Mint': [189, 252, 201]
#         }

#         # Function to convert BGR to HSV
#         def bgr_to_hsv(bgr):
#             bgr_image = np.uint8([[bgr]])
#             hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#             return hsv_image[0][0]

#         # Function to calculate the Euclidean distance between two colors
#         def color_distance(color1, color2):
#             return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#         # Calculate the complementary color (180 degrees opposite in hue)
#         def complementary_color(hsv):
#             hue = hsv[0]
#             hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#             return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#         # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#         def analogous_colors(hsv, num_colors=10):
#             hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#             return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#         # Convert average skin color to HSV
#         skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#         # Get complementary and analogous colors
#         complementary_hsv = complementary_color(skin_hsv)
#         complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#         analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#         # Collect all colors for comparison
#         recommendations = {
#             'Average Skin Color': average_skin_color_bgr.tolist(),
#             'Complementary': complementary_bgr.tolist()
#         }
#         for i, color_bgr in enumerate(analogous_colors_bgr):
#             recommendations[f'Analogous {i+1}'] = color_bgr.tolist()
#         print("recommendations", recommendations)
#         return {
#             "recommendations": recommendations,
#             "output_image_path": output_image_path
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post('/test-upload')
# async def test_upload(file: UploadFile = File(...)):
#     return {"filename": file.filename}


# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Dict, Union, List
# import numpy as np
# import cv2
# from io import BytesIO
# from rembg import remove
# from PIL import Image
# import os

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Directory where the uploaded images will be saved
# UPLOAD_DIRECTORY = "uploaded_images"
# os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# @app.post('/imageprocessing')
# async def image_processing(file: UploadFile = File(...)) -> Dict[str, Union[str, Dict[str, Union[List[int], List[float]]]]]:
#     try:
#         # Save the uploaded file temporarily in the root directory
#         input_file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
#         with open(input_file_path, "wb") as f:
#             f.write(await file.read())
        
#         # Read the saved image file
#         with open(input_file_path, "rb") as f:
#             image_bytes = f.read()
        
#         # Remove the background
#         output_bytes = remove(image_bytes)
        
#         # Save the processed image in the root directory
#         output_image = Image.open(BytesIO(output_bytes))
#         output_image_path = os.path.join(".", "processed_" + file.filename)
#         output_image.save(output_image_path, format='PNG')  # Save as PNG to handle RGBA
        
#         # Convert bytes to numpy array
#         np_array = np.frombuffer(output_bytes, np.uint8)
        
#         # Decode the numpy array into an image
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
#         if image is None:
#             raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
#         # Convert the image to the HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define a range of HSV values for skin tones
#         lower_skin = np.array([0, 25, 75], dtype=np.uint8)
#         upper_skin = np.array([25, 255, 255], dtype=np.uint8)

#         # Threshold the image to select only skin pixels
#         skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

#         # Apply the mask to the original image to show only the skin pixels
#         skin = cv2.bitwise_and(image, image, mask=skin_mask)

#         # Convert the skin-only image to HSV color space for analysis
#         skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

#         # Calculate the average skin color
#         skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
#         if skin_pixels.size == 0:
#             raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
#         average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

#         # Average skin color in HSV
#         average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

#         # Convert HSV to BGR
#         average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         # Define a color palette for recommendations (BGR format)
#         color_palette = {
#             'White': [255, 255, 255],
#             'Black': [0, 0, 0],
#             'Red': [0, 0, 255],
#             'Green': [0, 255, 0],
#             'Blue': [255, 0, 0],
#             'Yellow': [0, 255, 255],
#             'Orange': [0, 165, 255],
#             'Purple': [128, 0, 128],
#             'Pink': [203, 192, 255],
#             'Beige': [245, 245, 220],
#             'Brown': [42, 42, 165],
#             'Gray': [128, 128, 128],
#             'Light Gray': [211, 211, 211],
#             'Dark Gray': [169, 169, 169],
#             'Light Blue': [173, 216, 230],
#             'Dark Blue': [0, 0, 139],
#             'Turquoise': [64, 224, 208],
#             'Teal': [0, 128, 128],
#             'Coral': [255, 127, 80],
#             'Salmon': [250, 128, 114],
#             'Lavender': [230, 230, 250],
#             'Olive': [128, 128, 0],
#             'Maroon': [128, 0, 0],
#             'Indigo': [75, 0, 130],
#             'Mint': [189, 252, 201]
#         }

#         # Function to convert BGR to HSV
#         def bgr_to_hsv(bgr):
#             bgr_image = np.uint8([[bgr]])
#             hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
#             return hsv_image[0][0]

#         # Function to calculate the Euclidean distance between two colors
#         def color_distance(color1, color2):
#             return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

#         # Calculate the complementary color (180 degrees opposite in hue)
#         def complementary_color(hsv):
#             hue = hsv[0]
#             hue = (hue + 90) % 180  # 90 degrees offset for complementary color
#             return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

#         # Calculate 10 analogous colors (evenly spaced around the hue wheel)
#         def analogous_colors(hsv, num_colors=10):
#             hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
#             return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

#         # Convert average skin color to HSV
#         skin_hsv = bgr_to_hsv(average_skin_color_bgr)

#         # Get complementary and analogous colors
#         complementary_hsv = complementary_color(skin_hsv)
#         complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

#         analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
#         analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

#         # Collect all colors for comparison
#         recommendations = {
#             'Average Skin Color': average_skin_color_bgr.tolist(),
#             'Complementary': complementary_bgr.tolist()
#         }
#         for i, color_bgr in enumerate(analogous_colors_bgr):
#             recommendations[f'Analogous {i+1}'] = color_bgr.tolist()
        
#         return {
#             "recommendations": recommendations,
#             "output_image_path": output_image_path
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post('/test-upload')
# async def test_upload(file: UploadFile = File(...)):
#     return {"filename": file.filename}

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Union, List
import numpy as np
import cv2
from io import BytesIO
from rembg import remove
from PIL import Image

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post('/imageprocessing')
async def image_processing(file: UploadFile = File(...)) -> Dict[str, Union[str, Dict[str, Union[List[int], List[float]]]]]:
    try:
        # Read the uploaded image file
        image_bytes = await file.read()
        
        # Remove the background
        output_bytes = remove(image_bytes)
        
        # Convert bytes to numpy array
        np_array = np.frombuffer(output_bytes, np.uint8)
        
        # Decode the numpy array into an image
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image format or cannot decode image")
        
        # Convert the image to the HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define a range of HSV values for skin tones
        lower_skin = np.array([0, 25, 75], dtype=np.uint8)
        upper_skin = np.array([25, 255, 255], dtype=np.uint8)

        # Threshold the image to select only skin pixels
        skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Apply the mask to the original image to show only the skin pixels
        skin = cv2.bitwise_and(image, image, mask=skin_mask)

        # Convert the skin-only image to HSV color space for analysis
        skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

        # Calculate the average skin color
        skin_pixels = skin_hsv[skin_mask > 0]  # Extract skin pixels
        if skin_pixels.size == 0:
            raise HTTPException(status_code=400, detail="No skin pixels detected in the image")
        
        average_skin_color = np.mean(skin_pixels, axis=0)  # Compute mean color

        # Average skin color in HSV
        average_skin_color_hsv = np.array(average_skin_color, dtype=np.float32)

        # Convert HSV to BGR
        average_skin_color_bgr = cv2.cvtColor(np.uint8([[average_skin_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

        # Define a color palette for recommendations (BGR format)
        color_palette = {
            'White': [255, 255, 255],
            'Black': [0, 0, 0],
            'Red': [0, 0, 255],
            'Green': [0, 255, 0],
            'Blue': [255, 0, 0],
            'Yellow': [0, 255, 255],
            'Orange': [0, 165, 255],
            'Purple': [128, 0, 128],
            'Pink': [203, 192, 255],
            'Beige': [245, 245, 220],
            'Brown': [42, 42, 165],
            'Gray': [128, 128, 128],
            'Light Gray': [211, 211, 211],
            'Dark Gray': [169, 169, 169],
            'Light Blue': [173, 216, 230],
            'Dark Blue': [0, 0, 139],
            'Turquoise': [64, 224, 208],
            'Teal': [0, 128, 128],
            'Coral': [255, 127, 80],
            'Salmon': [250, 128, 114],
            'Lavender': [230, 230, 250],
            'Olive': [128, 128, 0],
            'Maroon': [128, 0, 0],
            'Indigo': [75, 0, 130],
            'Mint': [189, 252, 201]
        }

        # Function to convert BGR to HSV
        def bgr_to_hsv(bgr):
            bgr_image = np.uint8([[bgr]])
            hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
            return hsv_image[0][0]

        # Function to calculate the Euclidean distance between two colors
        def color_distance(color1, color2):
            return np.sqrt(np.sum((np.array(color1) - np.array(color2)) ** 2))

        # Calculate the complementary color (180 degrees opposite in hue)
        def complementary_color(hsv):
            hue = hsv[0]
            hue = (hue + 90) % 180  # 90 degrees offset for complementary color
            return np.array([hue, hsv[1], hsv[2]], dtype=np.float32)

        # Calculate 10 analogous colors (evenly spaced around the hue wheel)
        def analogous_colors(hsv, num_colors=10):
            hues = [(hsv[0] + (i * 360 / num_colors)) % 180 for i in range(num_colors)]
            return [np.array([hue, hsv[1], hsv[2]], dtype=np.float32) for hue in hues]

        # Convert average skin color to HSV
        skin_hsv = bgr_to_hsv(average_skin_color_bgr)

        # Get complementary and analogous colors
        complementary_hsv = complementary_color(skin_hsv)
        complementary_bgr = cv2.cvtColor(np.uint8([[complementary_hsv]]), cv2.COLOR_HSV2BGR)[0][0]

        analogous_colors_hsv = analogous_colors(skin_hsv, num_colors=10)
        analogous_colors_bgr = [cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0] for color in analogous_colors_hsv]

        # Collect all colors for comparison
        recommendations = {
            'Average Skin Color': average_skin_color_bgr.tolist(),
            'Complementary': complementary_bgr.tolist()
        }
        for i, color_bgr in enumerate(analogous_colors_bgr):
            recommendations[f'Analogous {i+1}'] = color_bgr.tolist()
        
        return {
            "recommendations": recommendations
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/test-upload')
async def test_upload(file: UploadFile = File(...)):
    return {"filename": file.filename}
