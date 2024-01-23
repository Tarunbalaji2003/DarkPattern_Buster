import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
df =pd.read_csv('./dataset.tsv', sep='\t')
import re
def cleantext(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    grammatical_words = [
    'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'so',
    'am', 'is', 'are', 'was', 'were', 'be', 'being', 'been',
    'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
    'my', 'your', 'his', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs',
    'this', 'that', 'these', 'those',
    'with', 'at', 'by', 'from', 'into', 'during', 'including', 'to', 'in', 'on', 'above', 'below', 'over', 'under', 'through', 'between', 'among',
    'some', 'any', 'no', 'every', 'other', 'all', 'both', 'either', 'neither', 'each', 'few', 'many', 'several', 'much', 'more', 'most',
    'about', 'after', 'before', 'behind', 'beside', 'between', 'in front of', 'next to', 'under', 'over', 'on top of',
    'how', 'what', 'where', 'when', 'who', 'whom', 'which', 'whose', 'why', 'that', 'whether', 'while', 'because',
    'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must',
    'am', 'is', 'are', 'was', 'were', 'be', 'being', 'been',
    'do', 'does', 'did', 'doing',
    'have', 'has', 'had', 'having',
    'can', 'could', 'will', 'would', 'shall', 'should', 'may', 'might', 'must',
    'am', 'is', 'are', 'was', 'were', 'be', 'being', 'been',
    'there', 'here', 'where', 'when', 'why', 'how'
]

    cleanText = ' '.join(word for word in cleanText.split() if word.lower() not in grammatical_words)
    return cleanText
df['text'] = df['text'].apply(lambda x: cleantext(x))
df['text'][4]
'newsletter signup privacy policy'
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

tfidf.fit(df['text'])
requredTaxt  = tfidf.transform(df['text'])
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(requredTaxt, df['Pattern Category'], test_size=0.2, random_state=42)
X_train.shape
X_test.shape
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score

clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(X_train,y_train)
ypred = clf.predict(X_test)
print(accuracy_score(y_test,ypred))
#import pickle
#pickle.dump(tfidf,open('tfidf.pkl','wb'))
#pickle.dump(clf, open('clf.pkl', 'wb'))
def test(txt):
    import pickle
    clf = pickle.load(open('./clf.pkl', 'rb'))
    cleaned_text = cleantext(txt)
    input_features = tfidf.transform([cleaned_text])
    prediction_id = clf.predict(input_features)[0]
    dark_pattern_mapping = {
        0: "Not Dark Pattern",
        1: "Scarcity",
        2: "Social Proof",
        3: "Urgency",
        4: "Misdirection",
        5: "Obstruction",
        6: "Sneaking",
        7: "Forced Action",
    }
    dark_pattern_name = dark_pattern_mapping.get(prediction_id)
    return prediction_id