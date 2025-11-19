from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('logistic.pkl','rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl','rb'))


def predict_mail(input_text):
    input_features = feature_extraction.transform([input_text])
    prediction = model.predict(input_features)
    return prediction[0]


@app.route('/', methods=['GET','POST'])
def analyze_mail():
    if request.method == 'POST':
        mail = request.form.get('mail')
        predicted_mail = predict_mail(mail)
        
        result = "Ham" if predicted_mail == 1 else "Spam"
        return render_template('index.html', classify=result)

    return render_template('index.html', classify=None)


if __name__ == '__main__':
    app.run(debug=True)
