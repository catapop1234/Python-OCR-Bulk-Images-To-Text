import pytesseract
from PIL import Image
import os

# Path to the folder containing the images
folder_path = 'VideoToText/Poze'

# Output text file
output_file = 'VideoToText/extracted_text_from_poze.txt'

# List to hold extracted text from all images
extracted_texts = []

# Process each image in the folder
for image_file in os.listdir(folder_path):
    # Get the full path of the image file
    image_path = os.path.join(folder_path, image_file)
    
    # Check if the file is an image (you can add more extensions if needed)
    if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif','.PNG','.JPG','.JPEG')):
        # Open the image file
        image = Image.open(image_path)
        
        # Use OCR to extract text from the image
        text = pytesseract.image_to_string(image)
        
        # Append the image file name and extracted text to the list
        extracted_texts.append(f'Filename: {image_file}\n{text}\n\n')

# Save the extracted texts to a single text file
with open(output_file, 'w') as file:
    file.writelines(extracted_texts)

print(f'Text extraction complete. Check {output_file} for results.')
