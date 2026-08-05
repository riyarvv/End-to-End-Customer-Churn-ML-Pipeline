from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

import pandas as pd


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a classification model and return key metrics.
    """

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:,1]

    return {
        "Accuracy": accuracy_score(y_test, predictions),
        "Precision": precision_score(
            y_test,
            predictions,
            pos_label="Yes"
        ),
        "Recall": recall_score(
            y_test,
            predictions,
            pos_label="Yes"
        ),
        "F1 Score": f1_score(
            y_test,
            predictions,
            pos_label="Yes"
        ),
        "ROC AUC": roc_auc_score(
            (y_test=="Yes").astype(int),
            probabilities
        )
    }