from sklearn.ensemble import RandomForestClassifier

def train_urgency_level_classifier(X, y):
    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf