import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def load_and_clean_data(filepath):
    df = pd.read_excel(filepath, engine='xlrd')
    df = df.dropna(subset=['ticket_text', 'issue_type', 'urgency_level', 'product'])
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        tokens = text.split()
        tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
        return ' '.join(tokens)

    df['clean_text'] = df['ticket_text'].apply(clean_text)
    return df