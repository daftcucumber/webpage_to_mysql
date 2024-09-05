
# step 1 - import library 
from flask import Flask,render_template,request

#step 2 - import database library
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']=''

mysql=MySQL(app)

table_name = ""

@app.route('/')

from flask import render_template  
  
def index(table_name, conditions=None):  
    cur = mysql.connection.cursor()  
    query = f"SELECT * FROM {table_name}"  
    if conditions:  
        query += f" WHERE {conditions}"  
      
    try:  
        cur.execute(query)  
        datas = cur.fetchall()  
    except Exception as e:  
        # perror  
        print(f"Error executing query: {e}")  
        datas = []   
      
    # ensure data is defined  
    if not isinstance(datas, list):  
        datas = []  
      
    return render_template('index.html', employees=data)



if __name__=="__main__":
    app.run(debug=True)

