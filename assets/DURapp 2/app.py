from flask import Flask, render_template, request
from form import PatientForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@1ocalhost/patients'

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def connect_table():
    import pymysql

    host='localhost'
    user = 'root'
    password = 'password'
    db = 'patient'

    try:
        con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
        
    except:
        return "There was an error."

    cur = con.cursor()
    cur.execute("SELECT * FROM patient_history")
    data = cur.fetchall()
    # render_template('index.html', data=data)
    

    return render_template('index.html', data=data)


def get_info():
    if request.method == "POST":
        print(request.form.get("nric"))
        print(request.form.get("medication"))


    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)
