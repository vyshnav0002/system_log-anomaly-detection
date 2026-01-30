from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(
        n_estimators=150,
        contamination=0.2,
        random_state=42
    )
    model.fit(X)
    return model

def predict(model, X):
    scores = model.decision_function(X)
    predictions = model.predict(X)
    return predictions, scores
