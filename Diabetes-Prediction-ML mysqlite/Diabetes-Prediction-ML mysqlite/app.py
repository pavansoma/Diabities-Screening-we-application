from flask import Flask,request, url_for, redirect, render_template
from flask import Flask, request, jsonify, render_template
#from flask_mysqldb import MySQL
import pickle
import numpy as np
import joblib
import sqlite3

app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'Root_123'
#app.config['MYSQL_DB'] = 'drd'

#mysql = MySQL(app)
#model=pickle.load(open('model.pkl','rb'))
model = joblib.load("models/randomforest_model.sav")

@app.route("/")
def home():
    # return the homepage
    return render_template("login.html")

@app.route("/signup")
def signup():
    name = request.args.get('username1','')
    mail = request.args.get('mail1','')
    password = request.args.get('password1','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `details` (`name`, `mail`, `password`) VALUES (?, ?, ?)",(name,mail,password))
    con.commit()
    con.close()

    return render_template("login.html")

@app.route("/signin")
def signin():
    mail1 = request.args.get('username','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `mail`, `password` from details where `mail` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("login.html")

    elif mail1 == data[0] and password1 == data[1]:
        return render_template("diabetes.html")

    
    else:
        return render_template("login.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")


@app.route('/predict',methods=['POST','GET'])
def predict():  
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final=[np.array(int_features)]
    print(final)
    prediction=model.predict(final)
    output=round(prediction[0],2)
    print(output)
    if output==1:
        return render_template('diabetes.html',pred='You have diabetes',result="diabetes")
    else:
        return render_template('diabetes.html',pred='You dont have diabetes',result="not diabetes")

if __name__ == '__main__':
    app.run(debug=True)