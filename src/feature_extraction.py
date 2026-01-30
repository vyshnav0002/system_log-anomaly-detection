from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(logs):
    vectorizer = TfidfVectorizer(
        max_features=200,
        ngram_range=(1, 2)
    )
    X = vectorizer.fit_transform(logs)
    return X, vectorizer
