# Smart Document Shadow Removal

**Mini Project – Python, OpenCV and Streamlit**

## Student Details
- Student 1: Supritha M — 1JB25CS437
- Student 2: Shalini M — 1JB25CS432
- College: SJB Institute of Technology (SJBIT)
- Department: Computer Science
- Guide: Dr. Krishana A N

## 1. Project Overview
Smart Document Shadow Removal is a simple image-processing application that reduces uneven shadows in photographs of documents. It uses OpenCV to estimate background illumination, normalize brightness and improve text contrast. Streamlit provides a browser-based interface for uploading and downloading images.

## 2. Features
- Upload a document image (PNG, JPG, JPEG or BMP).
- View the original and processed images side by side.
- Reduce uneven illumination and shadows.
- Improve contrast for better readability.
- Download the processed document as a PNG image.

## 3. Technologies Used
- Python
- OpenCV
- NumPy
- Pillow
- Streamlit

## 4. Project Structure
```text
Smart_Document_Shadow_Removal/
├── app.py
├── requirements.txt
└── README.md
```

## 5. Setup Instructions (Windows)

1. Install Python 3.10 or newer from https://www.python.org/downloads/.
2. Extract this ZIP file.
3. Open Command Prompt in the extracted `Smart_Document_Shadow_Removal` folder.
4. (Optional but recommended) Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

7. Streamlit will show a local address, usually `http://localhost:8501`. Open it in your browser.

## 6. How to Use
1. Click **Choose a document image**.
2. Select a document photo from your computer.
3. Compare the original image with the processed result.
4. Click **Download cleaned document** to save the output.

## 7. How It Works
1. The uploaded image is converted to a suitable color representation.
2. A median filter estimates slowly changing background illumination.
3. Illumination normalization reduces bright and dark regions caused by shadows.
4. CLAHE (Contrast Limited Adaptive Histogram Equalization) improves local contrast.
5. The enhanced image is displayed and made available for download.

## 8. Limitations
- Very dark, strong or complex shadows may not be fully removed.
- Blurred or low-resolution photographs may remain difficult to read.
- Results depend on lighting, page color and image quality.

## 9. Future Enhancements
- Add automatic document cropping and perspective correction.
- Support batch processing of multiple pages.
- Add OCR to extract text from cleaned documents.
- Develop a mobile-friendly interface.

## 10. Troubleshooting
- If `python` is not recognized, reinstall Python and enable **Add Python to PATH**.
- If `pip` is not recognized, try `python -m pip install -r requirements.txt`.
- If the Streamlit command is not recognized, run `python -m streamlit run app.py`.
