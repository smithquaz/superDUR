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

        # nric and medication
        nric = request.form.get('nric')
        new_drugs = request.form.get('medication')

        # fill all the various AI parameters
        current_drugs = query_prescribed_drugs(nric)
        medical_condition = query_mc(nric)

        # handle where user input multiple new drugs
        prescription_list = new_drugs.split(',')

        # currently can only handle 2 new drugs
        if len(prescription_list) == 2:
            ddi = query_implications(prescription_list[0])
            bc = query_bc(prescription_list[0])
        else:
            ddi = query_implications(new_drugs)
            bc = query_bc(new_drugs)

        # store the biconditional set into a list
        values = []
        for val in bc:
            values.append(str(val))
        
        # fill the biconditional up to 3 nested sets (0, 1, 2)
        if len(values) == 0:
            biconditionals = {}
        elif len(values) == 1:
            values.append(prescription_list[0])
            biconditionals = {frozenset(values)}
        else:
            biconditionals = {frozenset([prescription_list, frozenset(values)])}

        # find all symbols that are not currently taking or are not prescribed
        not_included = find_not_included(current_drugs, prescription_list, ddi, medical_condition, biconditionals)
        
        # runs the AI to determine if the drug is safe to prescribe
        safe = is_safe(current_drugs, prescription_list, not_included, ddi, medical_condition, biconditionals)

        #makes string for ddis
        str_ddis = ''
        if len(ddi)!= 0:
            str_ddis = 'cannot be prescribed with: '
            for blah in ddi:
                str_ddis += blah +", "
            str_ddis = str_ddis[:-2]
        else:
            str_ddis = ' does not clash with any medication'

        #makes string for current drugs
        str_current_drugs = ''
        if len(current_drugs) != 0:
            str_current_drugs = ' is currently taking: '
            for item in current_drugs:
                str_current_drugs += item + ', '
            str_current_drugs = str_current_drugs[:-2]
        else: 
            str_current_drugs += ' does not take other medication'


        #makes string for patient comorbidities
        str_medical_condition = ''
        if len(medical_condition) != 0:
            for thing in medical_condition:
                str_medical_condition += thing +', '
            str_medical_condition = str_medical_condition[:-2]
        else: 
            str_medical_condition = 'no comorbidities'

        return render_template("final.html", safe=safe, medication=new_drugs, str_ddis=str_ddis, str_current_drugs=str_current_drugs, str_medical_condition=str_medical_condition)


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
