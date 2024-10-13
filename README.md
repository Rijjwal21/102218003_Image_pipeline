## Image Processing Pipeline

This project automates the process of downloading images, converting them to grayscale, resizing them, compressing them into a ZIP file, and sending the final results via email.

### Project Overview

The pipeline includes the following steps:

1. **Download Images**: Downloads images from Google based on a specified keyword.
2. **Convert to Grayscale**: Converts downloaded images to grayscale.
3. **Resize Images**: Scales images by a specified percentage.
4. **Compress Files**: Compresses the processed images into a ZIP file.
5. **Send Email**: Sends the ZIP file as an email attachment to a specified recipient.

### Prerequisites

- Python 3.7+
- Required Python packages:
  - `icrawler`
  - `Pillow`
  - `argparse`
  - `yagmail`
  
Install the required packages using:
```bash
pip install -r requirements.txt
```

### How to Run

1. **Run the Pipeline**:

   You can run the entire pipeline using the main script. It will prompt for necessary inputs and guide you through the steps:

   ```bash
   python main.py
   ```

   Alternatively, run each step individually:

2. **Step-by-Step Execution**:

   - **Download Images**:
     ```bash
     python src/download_images.py <max_num> <keyword> <output_folder1>
     ```

   - **Convert to Grayscale**:
     ```bash
     python src/convertToGrayScale.py <output_folder1> <output_folder2>
     ```

   - **Scale Images**:
     ```bash
     python src/scale.py <output_folder2> <output_folder3>
     ```

   - **Zip Files**:
     ```bash
     python src/zip.py <output_folder3> <zip_name>
     ```

   - **Send Email**:
     ```bash
     python src/sendEmail.py <zip_file_path> <recipient_email>
     ```

### Example Command

```bash
python main.py
```

This command will prompt you for the following inputs:

- Number of images to download
- Keyword for image search
- Scaling percentage
- Recipient email address

