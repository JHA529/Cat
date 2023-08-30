from flask import *
# from form import BasicForm
import pymysql



app = Flask(__name__)
app.config['SECRET_KEY']='woop'

def connection():
    server = 'localhost'
    db = 'rubberducks'
    uid = 'sky'
    pwd = 'Qwerty1001?'
    conn = pymysql.connect(host=server, user=uid, password=pwd, database=db)
    conn.autocommit(True)
    return conn

@app.route('/')
def homepage():
    return render_template("Home_PZ.html")

@app.route('/Order')
def Order():
    return render_template("Order.html")

@app.route('/Menu')
def Menu():
    return render_template("Menu.html")

@app.route('/Events')
def Events():
    return render_template("Events.html")

@app.route('/AboutUs_pz')
def AboutUs_pz():
    return render_template("AboutUs_pz.html")

@app.route('/Order', methods=['GET', 'POST'])
def order():
    if request.method == "POST":
        your_name = request.form["Your Name"]  # Update field name to match HTML
        number_of_guests = request.form["Number_of_Guests"]  # Update field name to match HTML
        email = request.form["Email"]

        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (firstname, lastname, email) VALUES (%s, %s, %s)",
                       (your_name, number_of_guests, email))
        conn.close()
        return "Customer successfully added"
    return render_template("Order.html")

@app.route('/AddOrder', methods=['POST'])
def add_order():
    if request.method == "POST":
        dish = request.form["dish"]
        event_name = request.form["eventname"]  # Update field name to match HTML
        event_date = request.form["eventdate"]  # Update field name to match HTML

        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (dish, eventname, eventdate) VALUES (%s, %s, %s)",
                       (dish, event_name, event_date))
        conn.close()
        return "Order successfully added"
    return render_template("Order.html")

if __name__ == "__main__":
    app.run()