from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
    name_str = request.args.get('name')
    age_str = request.args['age']
    #return "congrats on your API "+name_str+" and your age "+age_str
    return render_template('welcome.html')
    

@app.route("/what")
def run_something():
        return "We have hit something"

@app.route("/buy",methods=['POST'])
def handle_get_and_post():
    post_value = request.form["post_parameter1"]
    return "we have successfully handled post request with parameter"+post_value 

if(__name__ == "__main__"):
    app.run()
