import os
import sys
from PIL import Image

def convert_to_grayscale(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(img_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            img = Image.open(img_path)
            
            gray_img = img.convert('L')
            
            gray_img.save(os.path.join(output_folder, filename))
            
    print(f"All images have been converted to grayscale and saved to {output_folder}")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convertToGrayScale.py inputFolder outputFolder")
        sys.exit(1)
        
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    convert_to_grayscale(input_folder, output_folder)        
    