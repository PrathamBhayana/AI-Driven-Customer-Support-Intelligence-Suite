from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(df):
    vectorizer = TfidfVectorizer(max_features=1000)
    X_tfidf = vectorizer.fit_transform(df['clean_text'])
    df['ticket_length'] = df['clean_text'].apply(len)
    return X_tfidf, df[['ticket_length']], vectorizer