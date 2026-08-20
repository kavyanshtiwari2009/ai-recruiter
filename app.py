import json

print("=" * 40)
print("          AI RECRUITER")
print("     Skill Extraction System")
print("=" * 40)

# ---------------- PREDEFINED LISTS ----------------

skills = [
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "computer vision",
    "natural language processing",
    "data science",
    "data analysis",
    "web development",
    "frontend development",
    "backend development",
    "full stack development",
    "cybersecurity",
    "cloud computing",
    "database management",
    "software development"
]

technologies = [
    "tensorflow",
    "pytorch",
    "opencv",
    "pandas",
    "numpy",
    "scikit-learn",
    "flask",
    "django",
    "fastapi",
    "react",
    "node.js",
    "mysql",
    "mongodb",
    "postgresql",
    "git",
    "github",
    "docker",
    "kubernetes"
]

languages = [
    "python",
    "java",
    "c++",
    "c#",
    "c",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "sql"
]

# ---------------- USER INPUT ----------------

experience = input("\nDescribe your experience or skills:\n> ")

# Convert everything to lowercase
text = experience.lower()

# Split the sentence into individual words
words = text.split()

# ---------------- EXTRACTION ----------------

extracted_skills = []
extracted_technologies = []
extracted_languages = []

# Check skills
for skill in skills:

    # For single-word skills
    if " " not in skill:
        if skill in words:
            extracted_skills.append(skill.title())

    # For multi-word skills
    else:
        if skill in text:
            extracted_skills.append(skill.title())


# Check technologies
for technology in technologies:

    if " " not in technology:
        if technology in words:
            extracted_technologies.append(technology)

    else:
        if technology in text:
            extracted_technologies.append(technology)


# Check languages
for language in languages:

    if " " not in language:
        if language in words:
            extracted_languages.append(language)

    else:
        if language in text:
            extracted_languages.append(language)


# ---------------- JSON RESULT ----------------

result = {
    "skills": extracted_skills,
    "technologies": extracted_technologies,
    "languages": extracted_languages
}

# ---------------- DISPLAY RESULT ----------------

print("\n" + "=" * 40)
print("         EXTRACTED INFORMATION")
print("=" * 40)

print(json.dumps(result, indent=4))