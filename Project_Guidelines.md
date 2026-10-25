## AI Policy: Use & Declaration

- **Limited AI Use:** AI coding assistants (e.g., GitHub Copilot) may be used for syntax suggestions, debugging, coding support, and learning assistance.
- **Prohibited — Project Materials:** Do not paste project prompts, guidelines, problem statements, or substantial portions of project materials into AI systems for code generation, completion, or debugging.
- **Prohibited — Written Work:** All submitted explanations, video commentary, and mathematical reasoning must be **your own voice and reasoning**.
- **Responsibility:** Submitted work must reflect your own understanding, implementation, and problem-solving effort.

### AI Use Declaration

1. Complete the [PETRA AI Student Declaration](https://www.petraai.org/student) based on your actual AI use for this project.
2. Generate and save the declaration image as **`AI_declaration.png`**.
3. Include **`AI_declaration.png`** in your project repository root.

> **Required:** Your declaration must accurately reflect how you used AI tools for this project.

### Code Resources & Rules
- **Implement Naive Bayes from Scratch:** Do NOT use machine-learning or NLP libraries (e.g., `scikit-learn`, `nltk`, `pandas`, `numpy`, `scipy`, `torch`, `transformers`).
- **Python Standard Library Only:** Standard modules (such as `csv`, `math`, `collections`, `re`, `random`) are permitted.
- **Learn from the Dataset:** The classifier must compute counts, priors, and likelihoods dynamically from the training file. Do not hard-code sentiment words or fixed probabilities.
- **Keep Train and Test Separate:** Never train or calculate word likelihoods using test sentences.
- **No Written Report Required:** There is no written report. Your conceptual understanding, mathematical derivations, and analysis are evaluated directly from your **video presentation**.

---

## Project Overview: Naive Bayes Text Classifier from Scratch

In this assignment, you will model and implement a binary sentiment classifier (**Positive** vs. **Negative**) using **Multinomial Naive Bayes**, built entirely from scratch. You will write your own text preprocessing, bag-of-words counting, probability engine with Laplace smoothing, and log-score classification.

### Learning Objectives

1. **Dataset Construction:** Build and organize a labeled text dataset split cleanly into training and testing sets.
2. **Text Preprocessing & Bag-of-Words:** Implement tokenization, vocabulary extraction, and word frequency counting using standard Python data structures.
3. **Probabilistic Modeling:** Calculate class priors and word likelihoods with Laplace smoothing ($\alpha = 1$).
4. **Log-Space Classification:** Implement sentence prediction using log probabilities to prevent numerical underflow.
5. **Model Evaluation & Generalization:** Evaluate classifier performance on a held-out test set and test dynamic prediction on unseen sentences.

---

## 🌟 +30% Bonus: Non-English Language

Earn **+30% bonus marks** (up to 130/100) if you create your dataset and implement your classifier for a natural language other than English (e.g., Spanish, Burmese, Hindi, Chinese, German, Arabic, Tagalog, Vietnamese, French, etc.)!
- To claim the bonus, indicate your chosen language in `video_link.txt` and demonstrate tokenization, vocabulary counts, and predictions in that language in your video presentation.
- Students must also book an interview through the provided [calendar booking link](https://calendar.app.google/J5EejvwkKgtPE8oKA) and answer 5 questions demonstrating their understanding of the implementation. Bonus marks will be awarded based on interview performance.

---

## Your Job

1. Prepare your labeled datasets in `data/train.csv` and `data/test.csv`.
2. Implement your Naive Bayes model in `app.py`.
3. Provide the main interface functions in `app.py`:
   - `train_model(train_file="data/train.csv")`
   - `predict(text)`: returns `"positive"` or `"negative"`
   - `evaluate_model(test_file="data/test.csv")`
4. Record a 5–7 minute video presentation with your face visible and paste the link in `video_link.txt`.
5. Test your implementation by running `python app.py`.

---

### Project Directory

You must use the exact file names and folder structure shown below:

```text
├── app.py                 # Core Naive Bayes implementation
├── data/
│   ├── train.csv          # Training sentences (text,label)
│   └── test.csv           # Testing sentences (text,label)
├── video_link.txt         # Video presentation link & language declaration
├── AI_declaration.png     # PETRA AI Student Declaration
├── requirements.txt       # Python dependencies (pure Python standard library)
├── Project_Guidelines.md  # This document
├── .gitignore             # Git ignore file
└── README.md              # Quick-start guide
```

---

### 📋 Task 1: Dataset Preparation (`data/*.csv`)

Create labeled sentences in CSV format with columns `text,label`:
- **Labels:** Must be exactly `positive` and `negative`.
- **Training Set (`data/train.csv`):** Contains training sentences balanced between both classes.
- **Testing Set (`data/test.csv`):** Contains held-out test sentences balanced between both classes.
- Ensure sentences feature realistic vocabulary, varied lengths, and distinct phrasing.

---

### 📋 Task 2: Naive Bayes Probabilities & Smoothing

Implement the probability calculations inside `app.py` using **training sentences only**:

1. **Tokenization & Bag of Words:**
   - Lowercase the text and tokenize into words.
   - Build a vocabulary $V$ containing all unique training words.
   - Count word occurrences for each class: $\operatorname{count}(w, c)$.
   - Track total word occurrences in each class: $N_c = \sum_{w \in V} \operatorname{count}(w, c)$.

2. **Class Priors:**
   $$P(c) = \frac{\text{number of training sentences in class } c}{\text{total training sentences}}$$

3. **Word Likelihood with Laplace Smoothing ($\alpha = 1$):**
   $$P(w \mid c) = \frac{\operatorname{count}(w, c) + 1}{N_c + |V|}$$
   where $|V|$ is the number of unique words in the training vocabulary.

---

### 📋 Task 3: Prediction Engine & Evaluation (`app.py`)

1. **Log-Space Prediction:**
   For any input sentence, tokenize it and calculate the log score for each class:
   $$\operatorname{score}(c) = \log P(c) + \sum_{w \in \text{tokens} \cap V} \log P(w \mid c)$$
   - Ignore words absent from the training vocabulary $V$ (do not crash on unseen words).
   - Predict the class with the higher score:
     $$\hat{c} = \arg\max_{c \in \{\text{positive}, \text{negative}\}} \operatorname{score}(c)$$

2. **Standard Functions in `app.py`:**
   - `train_model(train_file="data/train.csv")`: trains the classifier.
   - `predict(text)`: returns `"positive"` or `"negative"`.
   - `evaluate_model(test_file="data/test.csv")`: returns accuracy and confusion matrix (TP, TN, FP, FN).
   - Running `python app.py` should train the model, display evaluation metrics, and provide an interactive loop to test sentences.

3. **Testing Scope:**
   - Your `predict()` function must successfully classify:
     - Sentences from the held-out test set (`data/test.csv`).
     - A few other unseen sentences entered interactively or tested by the autograder.

---

### 📋 Task 4: Record a Video Presentation (30 Marks)

> [!IMPORTANT]
> **No written report is required.** Your project understanding, mathematical derivation, and implementation are evaluated entirely through your video presentation.

Record a **5–7 minute video presentation** (.mp4 format, uploaded to YouTube / Google Drive / Dropbox with public/accessible permissions). Paste the link into `video_link.txt`.

#### Video Requirements:
- **Face visible:** Your face must remain visible on camera throughout the video.
- **Duration:** 5 to 7 minutes (maximum 7 minutes).
- **Public link:** Ensure the link is accessible without permission requests.

#### Detailed Video Rubric:

| Component | Marks | What You Must Demonstrate in the Video |
| :--- | :---: | :--- |
| **1. Project Directory & Dataset** | **4** | Show your project files. Open `train.csv` and `test.csv`. Show sentence samples, class balance, and dataset size. If claiming the +30% bonus, state the non-English language chosen. |
| **2. Bag-of-Words & Counts** | **5** | Walk through your tokenization logic. Show vocabulary size ($|V|$) and total words per class ($N_{pos}, N_{neg}$). Pick 2 specific words and show their exact counts in both positive and negative training classes. |
| **3. Priors & Likelihood Mathematics** | **6** | Display the formulas for $P(c)$ and $P(w \mid c)$. Walk through **actual numeric calculations**: show the numerator ($\text{count} + 1$) and denominator ($N_c + |V|$) with Laplace smoothing. Prove numbers come from training data. |
| **4. Step-by-Step Prediction Calculation** | **5** | Enter an input sentence and trace the math live: show extracted tokens, word likelihoods for each class, total log scores, and winning prediction. Show that an unknown word is ignored without crashing. |
| **5. Live Data Mutation Test (Crucial)** | **6** | **Live on camera:** Open `data/train.csv`, modify or add a sentence (e.g. repeat a keyword in the opposite class), rerun `python app.py`, and demonstrate that word counts, probabilities, and scores update dynamically. |
| **6. Test Set & Unseen Sentences Evaluation** | **4** | Run evaluation on `test.csv` and show accuracy and the confusion matrix. Test live on camera at least **3 brand new, unseen sentences**. Discuss at least one limitation, edge case, or misclassification. |
| **Total Video Marks** | **30** | |

---

## Marking Scheme (100 marks Total + 30 Bonus Marks)

### 1. Autograder Evaluation (70 marks)
- **Task 1: Having Data (Train & Test) (30 marks):**
  - Dataset files exist and are non-empty: **10 marks**
  - Dataset CSV format and columns (`text,label`): **10 marks**
  - Both `positive` and `negative` classes present in datasets: **10 marks**
- **Task 2: Algorithm Prediction & Rules (40 marks):**
  - Pure Python standard library rule (no external ML libraries): **10 marks**
  - Prediction accuracy on given test set (`data/test.csv`): **15 marks**
  - Prediction handling of unseen sentences and unknown words: **15 marks**

### 2. Video Presentation (30 marks)
- Project directory & dataset walkthrough: **4 marks**
- Bag-of-words and word counts: **5 marks**
- Prior and Laplace-smoothed likelihood calculations: **6 marks**
- Step-by-step prediction calculation: **5 marks**
- Live data mutation test: **6 marks**
- Test set & unseen sentences evaluation: **4 marks**

### 3. 🌟 Non-English Language Bonus (+30 marks / +30%)
- Students who prepare their dataset and implement their classifier in a natural language other than English are eligible for up to 30 bonus marks.
- To claim the bonus, students must book an interview through the provided calendar link and answer 5 questions demonstrating their understanding of the implementation. Bonus marks will be awarded based on their interview performance.
- **Interview Booking Link:** [Book Interview Appointment](https://calendar.app.google/J5EejvwkKgtPE8oKA) (https://calendar.app.google/J5EejvwkKgtPE8oKA)

---

## Submission Instructions

### 1. Pre-Submission Check
Before submitting to Gradescope, verify that:
- `python app.py` executes cleanly without errors.
- `train.csv` and `test.csv` exist with valid labeled sentences.
- `video_link.txt` contains your accessible video presentation URL.
- `AI_declaration.png` is placed in the project root.

### 2. Submission to Gradescope
- Submit all required files (`app.py`, `data/train.csv`, `data/test.csv`, `video_link.txt`, `AI_declaration.png`, `requirements.txt`) to **Gradescope** under **Project 3**.
- Do not rename or alter the required directory structure.
- Confirm your video link in `video_link.txt` is accessible without permissions.
- Only the official Gradescope evaluation will be used for final automated grading.
