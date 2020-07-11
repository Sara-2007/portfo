from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('project.html')

@app.route('/thanks')
def thank():
    return render_template('thankyou.html')

def writecsv(data):
    with open('database.csv', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvwrite = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwrite.writerow([email,subject,message])

@app.route('/submitted', methods=['POST', 'GET'])
def submitted():
    if request.method == 'POST':
        data = request.form.to_dict()
        writecsv(data)
        return redirect('/thanks')
    else:
        return 'This looks like it is by Baskaran Pillai Technology\'s'
