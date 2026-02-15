import re
import json
import pdfplumber
import docx
from Resume_analyzer.candidate import Candidate


def parse_resume_text(text):
    name = ""
    email = ""
    degree = ""
    skills = []
    experience = 0

    lines = text.split("\n")

    for line in lines:
        l = line.lower()

        if not name and line.strip():
            name = line.strip()

        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", line)
        if email_match:
            email = email_match.group()

        if "btech" in l or "b.e" in l:
            degree = "B.Tech"
        elif "mtech" in l:
            degree = "M.Tech"
        elif "bsc" in l:
            degree = "B.Sc"
        elif "msc" in l:
            degree = "M.Sc"

        if "skills" in l:
            skills = [s.strip() for s in line.split(",")]

        if "year" in l:
            nums = re.findall(r"\d+", line)
            if nums:
                experience = int(nums[0])

    return Candidate(name, email, degree, skills, experience)


def parse_resume_file(path):
    if path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return parse_resume_text(f.read())

    elif path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return parse_resume_text(text)

    elif path.endswith(".docx"):
        doc = docx.Document(path)
        text = "\n".join([p.text for p in doc.paragraphs])
        return parse_resume_text(text)

    elif path.endswith(".json"):
        with open(path, "r") as f:
            data = json.load(f)
        return Candidate(
            data.get("name", ""),
            data.get("email", ""),
            data.get("degree", ""),
            data.get("skills", []),
            data.get("experience", 0),
        )

    else:
        raise Exception("Unsupported file format")