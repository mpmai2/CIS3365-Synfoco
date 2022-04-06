import pyodbc
from pyodbc import Error
"""server = 'cis3365.cmw1mzqnf8ed.us-east-2.rds.amazonaws.com'
database = 'Synfoco'
username = 'synfoco'
password = 'synfocospring22'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()"""
# cnxn = create_cnxn('cis3365.cmw1mzqnf8ed.us-east-2.rds.amazonaws.com,1433', 'Synfoco', 'synfoco', 'synfocospring22')


def create_cnxn(server_name, db_name, user_name, user_password):
    cnxn = None
    try:
        server = server_name
        database = db_name
        username = user_name
        password = user_password
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';Trusted_Connection=no;'
        )
        print("Connection established successfully.")
    except Error as e:
        print(f"The error '{e}' has occured")
    return cnxn

def execute_query(cnxn, query):
    cursor = cnxn.cursor()
    try:
        cursor.execute(query)
        cnxn.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#returns query value list into JSON serializable format
def execute_read_query(cnxn, query):
    cursor = cnxn.cursor()
    result = None
    query_values = []
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            query_values.append([x for x in row])
        #EXAMPLE: query_values = [[1, 'Will'], [2, 'John']]
        return query_values
    except Error as e:
        print(f"The error '{e}' occurred")

# returns query with a list of dictionaries retrieved from database into serializable format
def execute_read_dic(cnxn, query):
    cursor = cnxn.cursor()
    results = []
    try:
        cursor = cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        #EXAMPLE: results = [{'id': 1, 'name': 'Will', }, {'id': 2, 'name': 'John'}]
        return results
    except Error as e:
        print(f"The error '{e}' occurred")