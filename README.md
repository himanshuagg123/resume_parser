# 🧠 Resume Parser (Django Project)

A simple **Resume Parsing System** built with **Django** that allows users to upload resumes (in PDF or DOCX format), automatically extracts candidate information such as **name**, **email**, **phone number**, and **skills**, and displays the parsed details neatly on a web page.

---

## 🚀 Features

- Upload resumes in **.pdf** or **.docx** format  
- Extract key details automatically:
  - 👤 Name  
  - 📧 Email address  
  - 📞 Phone number  
  - 💡 Skills (e.g., Python, Django, AWS, etc.)
- Uses **spaCy NLP** for name extraction  
- Uses **Regex** for phone and email detection  
- Clean UI for uploading and viewing parsed resumes  
- Deployed live on **Render (Free Plan)**

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django (Python) |
| Parsing | spaCy, pdfminer, docx2txt, regex |
| Server | Gunicorn (for Render deployment) |
| Deployment | Render Cloud |
| Frontend | HTML (Django Templates) |

---

## ⚙️ How It Works

1. **User uploads a resume** through the upload form.  
2. The system extracts text content using:
   - `pdfminer` → for PDF files  
   - `docx2txt` → for Word files  
3. Extracted text is analyzed with:
   - `spaCy` → to detect candidate’s name (PERSON entity)  
   - `re` (regex) → to find email and phone number  
   - Keyword matching → to identify known skills  
4. Parsed information is saved to the database and displayed on a detail page.

---

## 📁 Project Structure

resume_parser/
│
├── parser_app/
│ ├── models.py # Resume model
│ ├── forms.py # Django form for upload
│ ├── views.py # Upload and detail views
│ ├── utils.py # Resume parsing logic (NLP + Regex)
│ ├── templates/
│ │ ├── parser_app/
│ │ │ ├── upload.html
│ │ │ └── detail.html
│
├── resume_parser/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── manage.py
└── requirements.txt


---

## 🧩 Installation Guide (Local Setup)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/resume_parser.git
   cd resume_parser
   
2.Create Virtual Environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

4.Run Migrations
python manage.py migrate

5.Start Development Server
python manage.py runserver

6 Visit the app at:
👉 http://127.0.0.1:8000/  #visit when you are using local host

🌐 Deployment (Render)

The app can be deployed easily using Render’s free web service.

🛠️ Future Enhancements

Add persistent database (PostgreSQL)

Support for image-based resumes (OCR)

Add skill categorization (Tech, Soft skills, etc.)

Add user authentication (Login/Register)

Export parsed results to CSV or JSON

👨‍💻 Author

Himanshu Aggarwal

live url of the project: https://resume-parser-yo0o.onrender.com/

