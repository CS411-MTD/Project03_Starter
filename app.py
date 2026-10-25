"""
UIC CS 411 - Project 03: Naive Bayes Text Classifier from Scratch
"""

import os
import csv
import math
import re


def train_model(train_file="data/train.csv"):
    """
    Train the Naive Bayes classifier on the training dataset.
    TODO: Implement your preprocessing, vocabulary extraction,
          class priors, and word likelihoods with Laplace smoothing.
    """
    pass


def predict(text):
    """
    Predict sentiment class for an input sentence.
    Returns: 'positive' or 'negative'
    Tie-breaking: If scores are tied, select the class with the higher prior P(c),
                  or default to 'positive' if priors are equal.
    TODO: Implement your log-score calculation and class prediction.
    """
    return "positive"


def evaluate_model(test_file="data/test.csv"):
    """
    Evaluate classifier performance on a test dataset.
    Returns:
        dict: A dictionary containing at least:
            {
                "accuracy": float,
                "confusion_matrix": {"TP": int, "TN": int, "FP": int, "FN": int}
            }
    TODO: Implement your evaluation logic (accuracy, confusion matrix).
    """
    pass


if __name__ == "__main__":
    train_model()
