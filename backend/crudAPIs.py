import flask
from flask import jsonify, make_response, request, flash, render_template, redirect, url_for
from mssql import create_cnxn, execute_query, execute_read_query, execute_read_dic

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser
app.secret_key = "Synfoco16"

# setting up home page to test connection
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Connection</h1>"

#(DONE) returns Customers table
@app.route('/api/customers', methods=['GET'])
def getcustomers():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Customers'
    #execute sql return statement and get customer records
    customers = execute_read_query(cnxn, query)
    return jsonify(customers)

#(DONE) returns Companies tables
@app.route('/api/companies', methods=['GET'])
def getcompanies():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Companies'
    #execute sql return statement and get companies records
    companies = execute_read_query(cnxn, query)
    return jsonify(companies)

#(DONE) returns Drivers tables
@app.route('/api/drivers', methods=['GET'])
def getdrivers():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Drivers'
    #execute sql return statement and get drivers records
    drivers = execute_read_query(cnxn, query)
    return jsonify(drivers)

#DONE returns Employees tables
@app.route('/api/employees', methods=['GET'])
def getemployees():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Employees'
    #execute sql return statement and get employees records
    employees = execute_read_query(cnxn, query)
    return jsonify(employees)

#DONE returns Orders tables
@app.route('/api/orders', methods=['GET'])
def getorders():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    query = 'SELECT * FROM Orders'
    #execute sql return statement and get orders records
    orders = execute_read_query(cnxn, query)
    return jsonify(orders)

#DONE ADD record in Companies table
@app.route('/api/companies', methods=['POST'])
def addcompany():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    if request.method == 'POST':
        companyname = request.form['companyname']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        email = request.form['email']
        phone = request.form['phone']
        query = """INSERT INTO Companies (Comp_Name, Comp_Street, Comp_City, Comp_State, Comp_Zip_Code, Comp_Email, Comp_Phone)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (companyname, street, city, state, zipcode, email, phone)
        
        execute_query(cnxn, query)
        flash('Company Added Successfully!')

        return 'Done'

#DONE ADD record in Customers table
@app.route('/api/customers', methods=['POST'])
def addcustomer():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        phone = request.form['phone']
        email = request.form['email']
        rating = request.form['rating']
        query = """
        INSERT INTO Customers 
        (Customer_FN, Customer_LN, Customer_Street, Customer_City, Customer_State, Customer_Zip_Code, Customer_Contact_Number, Customer_Email, Customer_Rating)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s)
        """ % (firstname, lastname, street, city, state, zipcode, phone, email, rating)
        
        execute_query(cnxn, query)
        flash('Customer Added Successfully!')
        return 'Success'

#DONE ADD record in Drivers table
@app.route('/api/drivers', methods=['POST'])
def adddriver():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        companyID = request.form['companyID']
        insuranceID = request.form['insuranceID']
        policynum = request.form['policy_number']
        policyexp = request.form['policy_expiration']
        employeeID = request.form['employeeID']

        query = """
        INSERT INTO Drivers 
        (Driver_FN, Driver_LN, Contact_number, Email, Company_ID, Insurance_ID, Policy_Number, Policy_Expiration, Employee_ID)
        VALUES ('%s', '%s', '%s', '%s', %s, %s, '%s', '%s', %s, %s)
        """ % (firstname, lastname, phone, email, companyID, insuranceID, policynum, policyexp, employeeID)
    
        execute_query(cnxn, query)
        flash('Driver Added Successfully!')
        return 'Success'

#DONE ADD record in Employees table
@app.route('/api/employees', methods=['POST'])
def addemployee():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        position = request.form['position']
        phone = request.form['phone']
        email = request.form['email']

        query = """
        INSERT INTO Employees 
        (Emp_FN, Emp_LN, Emp_Position, Emp_Contact_Number, Emp_Email)
        VALUES ('%s', '%s', '%s', '%s')
        """ % (firstname, lastname, position, phone, email)
    
        execute_query(cnxn, query)
        flash('Employee Added Successfully!')
        return 'Success'

#TODO ADD record in Orders table
@app.route('/api/Orders', methods=['POST'])
def addemployee():
    #connect to database 
    cnxn = create_cnxn('172.26.54.133', 'Synfoco_Logistic_Management_System', 'synfoco', 'Synfoco16')
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        position = request.form['position']
        phone = request.form['phone']
        email = request.form['email']

        query = """
        INSERT INTO Employees 
        (Emp_FN, Emp_LN, Emp_Position, Emp_Contact_Number, Emp_Email)
        VALUES ('%s', '%s', '%s', '%s')
        """ % (firstname, lastname, position, phone, email)
    
        execute_query(cnxn, query)
        flash('Employee Added Successfully!')
        return 'Success'


app.run()