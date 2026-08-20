# AI Recruiter — Skill Extraction System

## 📌 Project Overview

AI Recruiter is a Python-based skill extraction system that analyzes a user's description of their experience or skills and identifies relevant **skills, technologies, and programming languages**.

The system uses predefined lists and keyword matching to extract relevant information from the user's input and presents the result in a structured JSON format.

## 🎯 Problem Statement

Recruiters often need to identify relevant technical skills and programming languages from candidate information.

Manually extracting this information can be time-consuming. This project demonstrates a simple automated approach for identifying important skills and technologies from user-provided text.

## ⚙️ Installation Instructions

### Prerequisites

* Python 3.x
* Git (optional, if cloning the repository)

### Steps

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run:

```bash
python app.py
```

4. Enter a description of your experience or skills when prompted.

## 📊 Dataset Used

This project does **not use an external dataset**.

Instead, it uses predefined lists containing:

* Technical skills
* Technologies and frameworks
* Programming languages

The user's input is compared against these predefined lists to identify matching terms.

## 🔬 Methodology

The system follows a keyword-based extraction approach:

**User Input → Lowercase Conversion → Word/Sentence Matching → Information Extraction → JSON Output**

### Process

1. The user enters a description of their skills or experience.
2. The input is converted to lowercase for consistent matching.
3. The text is split into individual words.
4. The system checks the input against predefined lists of skills, technologies, and programming languages.
5. Matching terms are stored in separate lists.
6. The extracted information is displayed as formatted JSON.

The system also handles multi-word skills such as:

* Machine Learning
* Deep Learning
* Data Science
* Web Development
* Natural Language Processing

## 🛠️ Technologies Used

* **Python**
* **JSON**
* Keyword-based text processing

## 📈 Results

The system successfully extracts relevant information from user input.

For example, when the user enters:

> I love solving coding questions using Python and Java. I am interested in machine learning.

The system identifies:

* **Skill:** Machine Learning
* **Programming Language:** Python

The output is displayed in a structured JSON format.

> **Current limitation:** In this example, Java is not detected because the current word-matching approach does not remove punctuation such as the `.` after `Java`.

## 🚧 Challenges Faced

* Handling both single-word and multi-word skills.
* Matching user input with predefined terms.
* Handling punctuation in natural language input.
* Ensuring consistent matching by converting text to lowercase.
* Creating structured JSON output from extracted information.

## 🚀 Future Improvements

Future versions of the project could include:

* Natural Language Processing (NLP) techniques for improved extraction.
* Better handling of punctuation and different word forms.
* Fuzzy matching for misspelled skills.
* Resume/PDF upload and automatic skill extraction.
* A graphical or web-based user interface.
* Larger skill and technology databases.
* Machine learning-based entity extraction.
* Integration with a recruiter dashboard or database.
