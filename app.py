from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import datetime
app = Flask(__name__)

myclient = MongoClient("mongodb:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(myclient.list_database_names())
#print(mydb.list_collection_names())

#todos.insertOne({'content':'blah', 'degree':'0'})

@app.route('/', methods=('GET', 'POST'))
def index():
    if(request.method=='POST'):
        content = request.form['content']
        degree = request.form['degree']
        #todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    utc_dt = datetime.datetime.utcnow()
    #all_todos = todos.find()
    return render_template('index.html', utc_dt=utc_dt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
