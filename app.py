from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from helper import *
from ai import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@1ocalhost/patients'

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def connect_table():
    if request.method == "POST":
        print(request.form.get("nric"))
        print(request.form.get("medication"))
        print('Hello World')

        current_drugs = query_prescribed_drugs()
        new_drugs = request.form.get("medication")
        ddi = query_implications()
        medical_condition = query_mc()
        biconditionals = {frozenset([new_drugs, frozenset(list(query_bc()))])}

        # find all symbols that are not currently taking or are not prescribed
        not_included = find_not_included(current_drugs, new_drugs, ddi, medical_condition, biconditionals)

        print(f'current drugs: {current_drugs}')
        print(f'new drugs: {new_drugs}')
        print(f'medical_condition: {medical_condition}')
        print(f'biconditionals: {biconditionals}')
        print(f'not included: {not_included}')

        if is_safe(current_drugs, new_drugs, not_included, ddi, medical_condition, biconditionals):
            print('Test 3 Passed')
        else:
            print('Test 3 Failed')

        return render_template("final.html")


    else:
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
        return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
