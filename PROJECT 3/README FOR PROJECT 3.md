# 🧭 Tech Stack Recommender — AI Recommendation Logic
**Project 3 | Artificial Intelligence Track**
**Batch: 2026 | Powered by DecodeLabs**

---

## 📌 Project Overview

This project builds a content-based recommendation engine that maps a user's skills and interests to the most relevant tech career paths. It moves beyond "passive classification" (Project 2) into "active prediction" — proactively suggesting job roles before the user explicitly asks for them, the same logic that powers recommendation engines like Netflix and Amazon.

This is the **personalization phase** of the AI Engineering track at DecodeLabs: Pattern Alignment through pure similarity logic.

---

## 🎯 Goal

Create a recommendation system that takes a user's skills as input, mathematically matches them against a dataset of job roles, and returns the Top 3 most relevant career paths.

---

## ⚙️ How It Works (IPO Framework)

| Stage | What Happens |
|---|---|
| **Input** | User enters at least 3 skills/interests (e.g. "Python, Cloud Computing, Automation") |
| **Process** | Skills and job descriptions are converted into TF-IDF vectors in a shared vocabulary space, then compared using Cosine Similarity |
| **Output** | The Top 3 highest-scoring job roles are sorted, filtered, and displayed with a match percentage |

---

## 🧠 Key Concepts Used

- **Content-Based Filtering** — Recommendations driven by item attributes (job skills), not other users' behavior, so no cold-start problem with new roles
- **TF-IDF Vectorization** — Converts text-based skills into numerical vectors. Term Frequency rewards skills that appear often in a role's profile; Inverse Document Frequency penalizes generic skills that appear across many roles
- **Shared Vocabulary Space** — The user's input and the job dataset are combined *before* vectorizing, ensuring both map to the exact same dimensions
- **Cosine Similarity** — Measures the angle between the user's vector and each job's vector, focusing on orientation/overlap rather than raw size — this is why a short user profile can still strongly match a longer job description
- **4-Step Ranking Pipeline** — Ingestion (load data + user input) → Scoring (cosine similarity) → Sorting (descending order) → Filtering (Top-N cutoff)
- **Minimum Input Validation** — Script enforces at least 3 skills to ensure sufficient data density for accurate matching

---

## 🗂️ Project Structure

```
Project3-TechStackRecommender/
│
├── tech_stack_recommender.py   # Main script
├── raw_skills.csv               # Dataset: job roles mapped to required skills
└── README.md                     # Project documentation
```

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Install the required libraries:

```bash
pip install pandas scikit-learn
```

3. Run the script:

```bash
python tech_stack_recommender.py
```

4. When prompted, enter at least 3 skills separated by commas (e.g. `Python, SQL, AWS`).
5. The script will print your Top 3 recommended career paths with match percentages.

---

## 📊 Sample Run #1

```
Your skills (comma-separated): Python, Cloud Computing, Automation

🎯 TOP 3 RECOMMENDED CAREER PATHS FOR YOU

#1  Cloud Architect
     Match Score : 54.4%
     Key Skills  : AWS,Cloud Computing,Networking,Security,Automation,Docker

#2  Network Engineer
     Match Score : 54.0%
     Key Skills  : Networking,Security,Linux,Automation,Cloud Computing,Routing

#3  Data Engineer
     Match Score : 39.5%
     Key Skills  : Python,SQL,ETL,Data Structures,Cloud Computing,Big Data
```

## 📊 Sample Run #2

```
Your skills (comma-separated): Java, SQL, APIs

🎯 TOP 3 RECOMMENDED CAREER PATHS FOR YOU

#1  Backend Developer
     Match Score : 52.9%
     Key Skills  : Java,Python,SQL,APIs,Spring Boot,Databases

#2  QA Automation Engineer
     Match Score : 38.3%
     Key Skills  : Python,Java,Test Automation,Selenium,CI/CD,APIs

#3  Full Stack Developer
     Match Score : 35.0%
     Key Skills  : JavaScript,Python,React,APIs,SQL,HTML
```

Both runs confirm the engine correctly surfaces the most logical career match first (Cloud Architect for cloud/automation skills, Backend Developer for Java/SQL/APIs).

---

## 📋 Specification Checklist

- [x] Take user input (choices or interests) — minimum 3 skills enforced
- [x] Match preferences using logic or similarity — TF-IDF + Cosine Similarity
- [x] Display recommended items — Top 3 ranked job roles with match scores
- [x] Dataset of job roles used as recommendation "items" (`raw_skills.csv`)
- [x] Content-based filtering approach (avoids cold-start problem)

---

## 🔑 Key Skills Demonstrated

- Logic building and pattern matching
- Text vectorization with TF-IDF
- Similarity scoring with Cosine Similarity
- Building a ranking and filtering pipeline
- Recommendation system fundamentals (content-based filtering)
- Working with Pandas for dataset handling

---

## 👨‍💻 Author

**Marvin Tettey | DecodeLabs AI Intern — Batch 2026**

---

*"We are now building systems to cure Choice Overload."*
*— DecodeLabs*
