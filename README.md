# UIC CS 411: Artificial Intelligence
## Project 3: Naive Bayes Text Classifier from Scratch — Starter Code

This repository contains the starter files, dataset templates, and guidelines for **Project 3: Naive Bayes Text Classifier (Sentiment Analysis)**.

---

## Directory Structure

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

## Your Implementation Tasks

1. **Dataset Preparation (`data/train.csv` and `data/test.csv`)**:
   - Provide labeled sentences with columns `text,label`.
   - Labels must be `positive` and `negative`.
   - Ensure both classes are present in training and testing datasets.

2. **Naive Bayes from Scratch (`app.py`)**:
   - **Pure Python standard library only** (no `scikit-learn`, `nltk`, `pandas`, `numpy`, `torch`).
   - Implement tokenization, bag-of-words counting, class priors $P(c)$, and Laplace-smoothed word likelihoods $P(w \mid c)$.
   - Predict sentiment using log scores:
     $$\operatorname{score}(c) = \log P(c) + \sum_{w \in \text{tokens} \cap V} \log P(w \mid c)$$
   - Ignore words that do not appear in the training vocabulary without crashing.

3. **Prediction Engine**:
   - Ensure `predict(text)` returns `"positive"` or `"negative"`.
   - The classifier must successfully predict on the provided test set and on unseen sentences.

4. **Video Recording (No Written Report)**:
   - **No written report is required.** Your work is evaluated through your code and a **5–7 minute video presentation** with your face visible.
   - Walk through code, bag-of-words counts, probability math, live sentence prediction, and perform the live data mutation test.
   - Upload to YouTube / Google Drive / Dropbox and paste the link in `video_link.txt`.

5. **🌟 +30% Non-English Language Bonus**:
   - Earn **+30% bonus marks** if you build your dataset and run classification in a natural language other than English.

---

## Submission Instructions

Submit all files listed in the directory structure (including `app.py`, `video_link.txt`, `AI_declaration.png`, and the `data/` directory) to **Gradescope** under **Project 3**.

For complete requirements, mathematical formulas, and the detailed video presentation rubric, refer to [Project_Guidelines.md](Project_Guidelines.md).
