# Multilangauge-invoice-extraction
🧾 Multilanguage Invoice Extraction
This project is designed to automatically extract key information from invoices in multiple languages using OCR (Optical Character Recognition) and natural language processing techniques. It supports diverse invoice formats and languages, making it adaptable for real-world business scenarios.

🚀 Features
🔍 Extracts key fields like:

Invoice Number

Date

Vendor Name

GST Number

Total Amount

Tax Breakdown

🌐 Multilanguage support (English, Hindi, regional languages, etc.)

🧠 Uses Tesseract OCR and Pytesseract for text extraction

🗃 Handles various invoice formats (PDF, PNG, JPEG)

🧼 Pre-processing: Noise removal, grayscale, binarization for better OCR

⚙️ Modular codebase for easy customization and scaling

🛠️ Tech Stack
Python

Tesseract OCR

OpenCV

Pytesseract

Streamlit (optional for UI)

📂 Folder Structure
bash
Copy
Edit
.
├── app.py                # Main execution file
├── requirements.txt      # Dependencies
├── .gitignore
└── README.md
🧪 How to Run
Clone the repo

bash
Copy
Edit
git clone https://github.com/Yash6241/Multilangauge-invoice-extraction.git
cd Multilangauge-invoice-extraction
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
📌 To Do
 Add support for handwritten invoices

 Add a web interface using Streamlit or Flask

 Export extracted data to Excel or JSON

 Add language detection feature

