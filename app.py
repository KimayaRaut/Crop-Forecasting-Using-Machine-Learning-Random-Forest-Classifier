from flask import Flask, render_template, request
import numpy as np
import pickle

from numpy.core.fromnumeric import var

model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    data1=0
    data2=0
    data3=0
    data4=0
    data5=0
    data6=0
    data7=0
    data8=0
    new_pred = ""
    if request.method=='POST':
        data1 = request.form['data1']
        data2 = request.form['data2']
        data3 = request.form['data3']
        data4 = request.form['data4']
        data5 = request.form['data5']
        data6 = request.form['data6']
        data7 = request.form['data7']

    arr = np.array([[data1, data2, data3, data4,data5,data6,data7]])
    pred = model.predict(arr)

    if pred == 20:
        new_pred = 'Rice'
    elif pred == 11:
        new_pred = 'Maize'
    elif pred == 3:
        new_pred = 'Chickpea'
    elif pred == 9:
        new_pred = 'Kidneybeans'
    elif pred == 18:
        new_pred ='pigeonpeas'
    elif pred == 13:
        new_pred ='mothbeans'
    elif pred == 14:
        new_pred ='mungbean'
    elif pred == 2:
        new_pred ='blackgram'
    elif pred == 10:
        new_pred ='lentil'
    elif pred == 1:
        new_pred ='pomegranate'
    elif pred == 12:
        new_pred ='banana'
    elif pred == 7:
        new_pred ='mango'
    elif pred == 21:
        new_pred ='grapes'
    elif pred == 15:
        new_pred ='watermelon'
    elif pred == 0:
        new_pred ='apple'
    elif pred == 16:
        new_pred ='orange'
    elif pred == 17:
        new_pred ='papaya'
    elif pred == 4:
        new_pred ='coconut'
    elif pred == 6:
        new_pred ='cotton'
    elif pred == 8:
        new_pred ='jute'
    elif pred == 5:
        new_pred ='coffee'
    

    return render_template('index.html',var=new_pred)

if __name__ == "__main__":
    app.run(debug=True, port=8000)