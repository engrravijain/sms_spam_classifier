from flask import Flask,render_template,url_for,request, jsonify
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import *
from sklearn.svm import *


app = Flask(__name__)
global Classifier
global Vectorizer

# load data
data = pd.read_csv('data/sms-spam-collection-dataset/spam.csv', encoding='latin-1')
train_data = data[:4400] # 4400 items
test_data = data[4400:] # 1172 items

# train model
Classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True))
Vectorizer = TfidfVectorizer()
vectorize_text = Vectorizer.fit_transform(train_data.v2)
Classifier.fit(vectorize_text, train_data.v1)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	error = ''
	predict_proba = ''
	predict = ''
	if request.method == 'POST':
		message = request.form['message']
		try:
			if len(message) > 0:
				vectorize_message = Vectorizer.transform([message])
				predict = Classifier.predict(vectorize_message)[0]
				predict_proba = Classifier.predict_proba(vectorize_message).tolist()
			else:
				predict = 2
		except BaseException as inst:
			error = str(type(inst).__name__) + ' ' + str(inst)
	if (predict == 'ham'):
		predict = 1
	elif (predict == 'spam'):
		predict = 0
	return render_template('index.html', prediction = predict)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)