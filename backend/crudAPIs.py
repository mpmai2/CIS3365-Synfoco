import flask
from flask import jsonify, make_response, request
from mssql import create_cnxn, execute_query, execute_read_query

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

# setting up home page to test connection
@app.route('/', methods=['GET'])
def home():
    return "<h1>Test Connection</h1>"

# returns table data
@app.route('/api/getcustomers', methods=['GET'])
def getcustomers():
    #connect to database 
    cnxn = create_cnxn('cis3365.cmw1mzqnf8ed.us-east-2.rds.amazonaws.com,1433', 'Synfoco', 'synfoco', 'synfocospring22')
    query = 'SELECT * FROM Customers'
    #execute sql return statement and get customer records
    customers = execute_read_query(cnxn, query)
    return jsonify(customers)

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
    # append records into list
    ##records = []
    ##for row in customers:
        ##records.append(row)
    return jsonify(customers)



app.run()