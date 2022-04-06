import flask
from flask import jsonify, make_response, request
from mssql import create_cnxn, execute_query, execute_read_query, execute_read_dic

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

# setting up home page to test connection
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Connection</h1>"

# returns table data
@app.route('/api/customers', methods=['GET'])
def getcustomers():
    #connect to database 
    cnxn = create_cnxn('cis3365.cmw1mzqnf8ed.us-east-2.rds.amazonaws.com,1433', 'Synfoco', 'synfoco', 'synfocospring22')
    query = 'SELECT * FROM Customers'
    #execute sql return statement and get customer records
    customers = execute_read_query(cnxn, query)
    return jsonify(customers)

@app.route('/api/testpost', methods=['POST'])
def testpost():
    req_data = request.get_json()
    newid = req_data['id']
    newfn = req_data['firstname']
    return 'ID: {}, Name: {}'.format(newid, newfn)

# test connection
@app.route('/api/cnxn', methods=['GET'])
def testcnxn():
    #connect to database 
    cnxn = create_cnxn("cis3365.cmw1mzqnf8ed.us-east-2.rds.amazonaws.com,1433", "Synfoco", "synfoco", "synfocospring22")
    query = """
    SELECT * FROM Customers
    WHERE ID = 1
    """
    #execute sql return statement and get customer records
    customers = execute_read_query(cnxn, query)
    return jsonify(customers)



app.run()