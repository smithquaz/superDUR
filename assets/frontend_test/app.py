from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text

app = Flask(__name__)

#change to name of database, add path if necessary
db_name_NRIC = 'nric.db'
#database connection string for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name_NRIC
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app = Flask(__name__)
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

class nric_info(db.Model):
    nric = db.Column(db.Integer, primary_key=True, nullable=False)
    medical_conditions = db.Column(db.String(200), default=None) #false means user wont be able to create new task and leave it empty
    drug_allergies = db.Column(db.String(200), default=None)
    current_medication = db.Column(db.String(200), default=None)

    #function that returns a string every time a new element is created
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def get_patient_details():
    #if request sent to this route is POST, do stuff
    if request.method == 'POST':
        patient_details = request.form['content']
        nric_content = nric_info(content=patient_details)

        try:
            person_nric = nric_info.query.get(nric_content)
            print(f'{person_nric} | Existing conditions: {nric_info.medicalconditions} | Allergies: {nric_info.allergies} | Current medication: {nric_info.currentmedication}')
            return redirect('/') #back to index page
        except:
            return 'There was an issue checking your NRIC details'
    # else:
        # #looks at db contents by date created, displays all of them
        # tasks = nric_info.query.order_by(Todo.date_created).all()
        # return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)