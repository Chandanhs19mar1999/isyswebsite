from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,request,redirect,url_for
from forms import formone



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///isysarticle.sqlite3'
app.config['SECRET_KEY'] = "******************"
db=SQLAlchemy(app)
class article(db.Model):
    id = db.Column('article_id', db.Integer, primary_key = True)
    usn = db.Column(db.String(11))
    name  = db.Column(db.String(30))
    email = db.Column(db.String(200))
    articledata= db.Column(db.String(1000))

def __init__(self, name,usn, email, articledata):
   self.name = name
   self.usn = usn
   self.email = email
   self.articledata = articledata

@app.route("/")
def home():
    return render_template("page1.html")


@app.route("/sendarticle")
def articleform():
    firstform=formone()
    return render_template("articleform.html",firstform=firstform)

@app.route("/addarticle",methods=['POST','GET'])
def addarticle():
    firstform = formone(request.form)
    if request.method == 'POST' and firstform.validate():
        art = article(name=firstform.name.data,usn=firstform.usn.data,email=firstform.email.data,articledata=firstform.articledata.data)
        db.session.add(art)
        db.session.commit()
        return render_template("success.html")
    else:
        return "<h1>something went wrong </h1>"



@app.route("/aboutisys")
def about():
    return render_template("about.html")


@app.route("/adminlogin")
def adminlogin():
    return render_template("adlogin.html")

@app.route("/logindetails",methods=['POST','GET'])
def logindetails():
    if request.method == 'POST':
        username=request.form['uname']
        password=request.form['pw']
        if username == "***********" and password == "***************" :
            return render_template("viewdata.html",data=article.query.all())
        else:
            return "<h1>Something went wrong</h1>"
    else:
        return "<h1>Something went wrong </h1>"


@app.route("/deletedata")
def dele():
    article.query.delete()
    db.session.commit()
    return render_template('adlogin.html')


if __name__ == '__main__':
    db.create_all()
    app.run(port=5000,debug=True)
        
