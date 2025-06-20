from sklearn.linear_model import LogisticRegression

def train_issue_type_classifier(X, y):
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, y)
    return clf