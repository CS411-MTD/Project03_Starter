# UIC CS 411: Artificial Intelligence
## Project 3: Naive Bayes Text Classifier from Scratch — Starter Code

This repository contains the starter files, directory structure, and guidelines for **Project 3: Naive Bayes Text Classifier (Sentiment Analysis)**.

For complete project instructions, algorithm specifications, AI policy, dataset requirements, and the video presentation rubric, refer to **[Project_Guidelines.md](Project_Guidelines.md)**.

---

## Directory Structure

You must use the exact file names and directory structure shown below:

```text
.
├── app.py                 # Main entry point with train_model(), predict(), evaluate_model()
├── data/                  # Dataset directory
│   ├── train.csv          # Training sentences (text,label)
│   └── test.csv           # Testing sentences (text,label)
├── video_link.txt         # Video presentation URL and student declaration
├── AI_declaration.png     # PETRA AI Student Declaration
├── requirements.txt       # Python dependencies (pure Python standard library)
├── Project_Guidelines.md  # Detailed project requirements and marking scheme
├── .gitignore             # Git ignore file
└── README.md              # This starter guide
```

---

## Getting Started

### 1. Set Up Python Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 2. Run Your Classifier
```bash
python app.py
```
This executes `app.py` to train on `data/train.csv` and evaluate on `data/test.csv`.

---

## Project Guidelines

Please read **[Project_Guidelines.md](Project_Guidelines.md)** carefully before starting. It covers:
- **AI Policy & Declaration:** Allowed vs. prohibited AI use; mandatory PETRA AI Student Declaration (`AI_declaration.png`).
- **Dataset Preparation:** 100 positive and 100 negative sentences (80/80 train, 20/20 test); AI generation of data is strictly prohibited.
- **Algorithm Specifications:** Bag-of-words counting, class priors, Laplace smoothing, log-space scoring, and tie-breaking rules.
- **Video Presentation Rubric (30 marks):** 5–7 minute video recording walkthrough (no written report).
- **🌟 +30% Non-English Language Bonus:** Guidelines and interview booking link for non-English language submissions.

---

## Submission Instructions

Submit all files listed in the directory structure (including `app.py`, `data/train.csv`, `data/test.csv`, `video_link.txt`, `AI_declaration.png`, and `requirements.txt`) to **Gradescope** under **Project 3**.

For complete requirements and the evaluation rubric, refer to [Project_Guidelines.md](Project_Guidelines.md).
