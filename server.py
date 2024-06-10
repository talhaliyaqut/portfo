
from flask import Flask,render_template,url_for,request,redirect
import csv
import os

app=Flask(__name__)

# @app.route('/')
# @app.route('/index.html')
# def home_page():
#     return render_template('index.html')

# @app.route('/works.html')
# def work_page():
#     return render_template('works.html')

# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database:
        fieldnames = ['email', 'subject','message']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        if os.stat('database.csv').st_size==0:
            writer.writeheader()
        writer.writerow(data)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method== 'POST':
        data=request.form.to_dict()
        # print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:    
        return "Something is worng"