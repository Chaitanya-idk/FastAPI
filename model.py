import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib


df = pd.read_csv('../dataset/data.csv', encoding='latin1')
df = df.dropna(subset=['text', 'sentiment'])
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

encoder = LabelEncoder()
y = encoder.fit_transform(df['sentiment'])

model = LogisticRegression()
model.fit(X, y)


joblib.dump(model, 'model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(encoder, 'encoder.joblib')
