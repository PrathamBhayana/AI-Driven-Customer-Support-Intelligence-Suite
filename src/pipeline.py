import os
import pickle
import re

from .data_preparation import load_and_clean_data
from .feature_engineering import extract_features
from .issue_type_classifier import train_issue_type_classifier
from .urgency_level_classifier import train_urgency_level_classifier
from .entity_extraction import extract_entities

# src/pipeline.py
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'tickets_complex_1000.xls')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
ISSUE_CLF_PATH = os.path.join(MODELS_DIR, 'issue_clf.pkl')
URGENCY_CLF_PATH = os.path.join(MODELS_DIR, 'urgency_clf.pkl')
VECTORIZER_PATH = os.path.join(MODELS_DIR, 'vectorizer.pkl')

def train_and_save():
    os.makedirs(MODELS_DIR, exist_ok=True)
    df = load_and_clean_data(DATA_PATH)
    X_tfidf, extra_features, vectorizer = extract_features(df)
    issue_clf = train_issue_type_classifier(X_tfidf, df['issue_type'])
    urgency_clf = train_urgency_level_classifier(X_tfidf, df['urgency_level'])
    with open(ISSUE_CLF_PATH, 'wb') as f:
        pickle.dump(issue_clf, f)
    with open(URGENCY_CLF_PATH, 'wb') as f:
        pickle.dump(urgency_clf, f)
    with open(VECTORIZER_PATH, 'wb') as f:
        pickle.dump(vectorizer, f)

def classify_ticket(ticket_text):
    with open(ISSUE_CLF_PATH, 'rb') as f:
        issue_clf = pickle.load(f)
    with open(URGENCY_CLF_PATH, 'rb') as f:
        urgency_clf = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    clean_text = re.sub(r'[^a-z0-9\s]', '', ticket_text.lower())
    X = vectorizer.transform([clean_text])
    issue_type = issue_clf.predict(X)[0]
    urgency_level = urgency_clf.predict(X)[0]
    entities = extract_entities(ticket_text)
    return {
        'issue_type': issue_type,
        'urgency_level': urgency_level,
        'entities': entities
    }

if __name__ == "__main__":
    train_and_save()
    # Success message
    print("Models Successfully trained and saved.")