import re
import pdfminer.high_level
import docx2txt
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = ["Python", "Django", "FastAPI", "Flask", "AWS", "Docker", "SQL", "Machine Learning", "Java"]

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return pdfminer.high_level.extract_text(file_path)
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    else:
        return ""

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\+?\d[\d -]{8,12}\d', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    found = [skill for skill in SKILLS if skill.lower() in text.lower()]
    return list(set(found))

def parse_resume(file_path):
    text = extract_text(file_path)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": ", ".join(extract_skills(text))
    }
