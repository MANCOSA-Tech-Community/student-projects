# Spam Classifier

**Author:** Shivian Naidoo ([@shiviancodes](https://github.com/shiviancodes))
**Category:** AI/ML
**Year:** 2026

## What it does

A classic text-classification project: it labels SMS messages as **spam** or
**ham** (legitimate). It's a clean, well-scoped example of an end-to-end NLP
pipeline - load data, vectorise text, train a model, evaluate it, and run live
predictions from the command line. It doubles as the seed example for this
showcase, so other contributors can see exactly what a finished entry looks like.

## Tech stack

- **Python 3**
- **scikit-learn** - `TfidfVectorizer` + `MultinomialNB`
- **pandas** - data loading and inspection
- Dataset: the public **SMS Spam Collection** (linked below, not committed)

## How to run

```bash
git clone https://github.com/shiviancodes/spam-classifier.git
cd spam-classifier
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Train the model and print evaluation metrics:
python train.py

# Classify a message interactively:
python predict.py "Congratulations! You've won a free prize, claim now"
# -> spam (0.98)
```

## Results

On a held-out 20% test split, the model reaches roughly **98% accuracy** with high
precision on the spam class - strong for such a small, fast pipeline. Confusion
matrix and a full classification report are printed by `train.py`.

## Data and large files

The dataset is **not committed** to this repository (it stays under the per-file
size limit, but linking keeps the repo lean and is the convention here):

- **SMS Spam Collection** - https://archive.ics.uci.edu/dataset/228/sms+spam+collection

Download it and place `spam.csv` in the project root before running `train.py`.

## Notes

- Intentionally simple and dependency-light so it's easy to read and reproduce.
- Possible improvements: swap in a linear SVM, add n-gram tuning, or expose the
  model behind a small Flask endpoint for the `demo` link.
- This is a community sample project; it is not affiliated with or endorsed by
  MANCOSA.
