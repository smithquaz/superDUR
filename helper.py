#python simple_execute_function.py
#import the library
import mysql.connector

def query_mc(nric):

  # creating connection
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database ="patient"
  )

  # import the cursor from the connection (conn)
  mycursor1 = conn.cursor()
  mycursor2 = conn.cursor()

  mycursor1.execute(f"SELECT pre_existing_mc FROM patient_history WHERE patient_id = {nric}")
  v = mycursor1.fetchone()
  # print(v)

  mycursor2.execute(f"SELECT inverse_drug FROM medical_condition WHERE mc = '{v[0]}' ")
  n = mycursor2.fetchone()
  
  mycursor1.close()
  mycursor2.close()
  conn.close()

  return n[0]

#print(query_mc())
#print(type(query_mc()))

def query_implications(new_drug):

  # creating connection
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database ="patient"
  )

  # import the cursor from the connection (conn)
  mycursor2 = conn.cursor()

  mycursor2.execute(f"SELECT implications FROM drug_interaction WHERE drug = '{new_drug}'")
  v = mycursor2.fetchone()

  # we close the cursor and conn both
  mycursor2.close()
  conn.close()

  return v[0]
#print(query_implications())
#print(type(query_implications()))

def query_prescribed_drugs(nric):

# creating connection
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database ="patient"
  )

  # import the cursor from the connection (conn)
  mycursor1 = conn.cursor()

  mycursor1.execute(f"SELECT prescribed_drugs FROM patient_history WHERE patient_id = {nric}")
  v = mycursor1.fetchone()
  # print(v)

  #close the cursor and conn
  mycursor1.close()
  conn.close()

  return v[0]
#print(query_prescribed_drugs())
#print(type(query_prescribed_drugs()))

def query_bc(new_drug):

# creating connection
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database ="patient"
  )

  # import the cursor from the connection (conn)
  mycursor3 = conn.cursor()
  mycursor3.execute(f"SELECT biconditional FROM drug_interaction WHERE drug = '{new_drug}'")

  v = mycursor3.fetchone()
  

  # we close the cursor and conn both
  mycursor3.close()
  conn.close()

  return v[0]
