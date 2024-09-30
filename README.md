# OCR Web Application

This repository contains Python scripts for an OCR web application that processes images to extract text and includes search functionality.

## Features

- Image uploading for text extraction
- Search functionality to find keywords in the extracted text
- User-friendly web interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package installer)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AishwaryaChandel27/OCR.git
   cd OCR
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv ocr_env
   ```

3. **Activate the virtual environment:**

   On Windows:

   ```bash
   ocr_env\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source ocr_env/bin/activate
   ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   python app.py
   ```

6. **Access the application:**

   Open your web browser and navigate to http://127.0.0.1:5000 to access the application.

## Usage

1. Upload an image containing text.
2. Click the 'Extract Text' button to process the image.
3. Use the search functionality to find keywords in the extracted text.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
