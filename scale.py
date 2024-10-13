import argparse
import os
from PIL import Image

def scale_images(input_folder, output_folder, scale_percentage):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    img.load()
                    
                    width, height = img.size
                    new_width = int(width * (scale_percentage/100.0))
                    new_height = int(height * (scale_percentage/100.0))
                    
                scaled_img = img.resize((new_width, new_height), Image.LANCZOS)
                
                output_extension = '.png' if img.mode == 'RGBA' else '.jpg'
                output_filename = os.path.splitext(filename)[0] + output_extension
                output_path = os.path.join(output_folder, output_filename)
                scaled_img.save(output_path)
    
                print(f"Scaled {filename} and saved to {output_path}")
            except (IOError, AttributeError, ValueError) as e:
                print(f"Could not process {filename}: {e}")
                
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scale images in a folder by a given percentage.")
    parser.add_argument("input_folder", type=str, help="Directory containing images to scale.")
    parser.add_argument("output_folder", type=str, help="Directory to save the scaled images.")
    parser.add_argument("scale_percentage", type=float, help="Percentage to scale images by (e.g., 50 for 50%).")
    
    args = parser.parse_args()
    
    scale_images(args.input_folder, args.output_folder, args.scale_percentage)
        