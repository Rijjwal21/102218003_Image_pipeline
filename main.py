import subprocess
import os

def run_command(command):
    """Utility function to run a command using subprocess."""
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    
if __name__ == "__main__":
    
    keyword = input("Enter the keyword for image search: ")
    max_num = input("Enter the maximum number of images to download: ")
    scale_percentage = input("Enter the scaling percentage (e.g., 50 for 50%): ")
    recipient_email = input("Enter the recipient email address: ")
    
    # Create necessary directories
    create_directory("data/of1")
    create_directory("data/of2")
    create_directory("data/of3")
    
     # Step 1: Download images
    download_command = f"python main_codes/download_images.py {keyword} {max_num} data/of1"
    run_command(download_command)

    # Step 2: Convert images to grayscale
    grayscale_command = f"python main_codes/convertToGrayScale.py data/of1 data/of2"
    run_command(grayscale_command)

    # Step 3: Scale images
    scale_command = f"python main_codes/scale.py data/of2 data/of3 {scale_percentage}"
    run_command(scale_command)

    # Step 4: Zip the scaled images
    zip_command = f"python main_codes/zip.py data/of3 data/of3.zip"
    run_command(zip_command)

    # Step 5: Send the zip file via email
    email_command = f"python main_codes/sendEmail.py data/of3.zip {recipient_email}"
    run_command(email_command)

    print("Process completed successfully!")
