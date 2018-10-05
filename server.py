"""
Examr server code
by: fash22
"""

from flask import Flask, render_template, url_for, request
from wtforms import StringField
from flask_wtf import Form
import dummy
import os

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'knjdfshadfha'

db = SQLAlchemy(app)

class Examinee(db.Model):
    __tablename__ = 'examinees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    school = db.Column(db.String(100))

class RegisterForm(Form):
    first_name = StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')
    school = StringField('School')



@app.route('/test/admin/base')
def test_admin_base():
    return render_template('admin-base.html')

@app.route('/test/admin/listbase')
def test_admin_list_base():
    examinees = dummy.examinees
    return render_template('admin-list-base.html', examinees=examinees)

@app.route('/test/admin/appbase')
def test_admin_app_base():
    return render_template('admin-app-base.html', examinee=dummy.examinee)

@app.route('/examinees')
def examinees():
    examinees = Examinee.query.all()
    return render_template('examinees.html', examinees=examinees)

@app.route('/examinees/documents')
def documents():
    return render_template('documents.html', examinee=dummy.examinee)

@app.route('/examinees/interviews')
def interviews():
    return render_template('interviews.html', examinee=dummy.examinee)

@app.route('/examinees/postings')
def postings():
    return render_template('postings.html', examinee=dummy.examinee)

@app.route('/examinees/payments')
def payments():
    return render_template('payments.html', examinee=dummy.examinee)

@app.route('/examinees/results')
def results():
    return render_template('results.html', examinee=dummy.examinee)

@app.route('/examinees/analytics')
def analytics():
    return 'analytics'


@app.route('/exam/general-instructions/')
def get_instruction():
    return render_template('exam-general-instruction.html')

@app.route('/exam/sample/')
def exam_sample():
    return render_template('sample-exam.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    template = 'no template'
    form = RegisterForm()
    if request.method == 'GET':
        template = render_template('register.html', form=form)
    if request.method == 'POST':
        form = RegisterForm()
        f = form.first_name.data
        m = form.middle_name.data
        l = form.last_name.data
        sc = form.school.data

        examinee = Examinee(first_name=f,middle_name=m,last_name=l,school=sc)
        db.session.add(examinee)
        db.session.commit()
        template = 'Hello %s' % f
        print(form.data)



    return template


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
