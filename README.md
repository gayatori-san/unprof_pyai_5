# 🔍 Regex Text Information Extractor

A lightweight Python CLI application that uses the **`re` (Regular Expressions)** module to extract structured information from unstructured text. This project identifies **email addresses**, **phone numbers**, and **dates**, while also demonstrating basic text cleaning using **`re.sub()`**.

---

## ✨ Features

📧 **Email Extraction**

* Detects and extracts standard email addresses from text.

📱 **Phone Number Extraction**

* Supports multiple phone number formats, including:

  * International numbers (`+91`)
  * Hyphen-separated numbers
  * Space-separated numbers
  * US-style formats with or without parentheses

📅 **Date Extraction & Standardization**

* Recognizes dates in multiple formats:

  * `DD/MM/YYYY`
  * `DD-MM-YYYY`
  * `YYYY/MM/DD`
  * `YYYY-MM-DD`
* Converts extracted dates into a consistent **`YYYY-MM-DD`** format.

🧹 **Text Cleaning (Optional)**

* Demonstrates how to clean and preprocess text using `re.sub()`.
* Removes unnecessary spaces or unwanted characters before extraction.

---

## 🛠️ Technologies Used

* **Python 3**
* **re (Regular Expressions Module)**

---

## 📖 Regex Patterns

### 📧 Email Pattern

```python
r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
```

### 📱 Phone Number Pattern

```python
r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
```

### 📅 Date Pattern

```python
r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})\b'
```

---

## 📂 Project Structure

```text
Regex-Text-Extractor/
│
├── text_extractor.py     # Main Python script
├── README.md             # Project documentation
└── sample_text.txt       # (Optional) Sample input file
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Regex-Text-Extractor
```

### 3️⃣ Run the Script

```bash
python3 text_extractor.py
```

---

## 📌 Example Input

```text
Contact us at support@example.com or admin123@gmail.com.

Call:
+91 9876543210
(555) 123-4567

Meeting Dates:
25/06/2026
2026-06-25
```

---

## ✅ Example Output

```text
Emails:
support@example.com
admin123@gmail.com

Phone Numbers:
+91 9876543210
(555) 123-4567

Dates:
2026-06-25
2026-06-25
```

---

## 🎯 Learning Objectives

This project demonstrates how to:

* Use Python's **`re`** module effectively.
* Build efficient regular expressions.
* Extract structured data from raw text.
* Normalize extracted information.
* Perform basic text preprocessing using regex substitution.

---
