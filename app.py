from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
from flask_mysqldb import MySQL

app=Flask(__name__,static_url_path='', static_folder='static',template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='logintest'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@app.route('/index.html')
def home():
	return render_template('index.html')

@app.route('/highschool.html')
def highschool():
	return render_template('highschool.html')


@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("select * from users where EMAIL=%s and UPASS=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["UNAME"]
            flash('Login Successfully','success')
            return redirect('/index.html')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")


#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return render_template('index.html')



@app.route("/project.html")
def project():
    return render_template("project.html") 
@app.route("/news.html")
def news():
    return render_template("news.html") 
@app.route("/member.html")
def member():
    return render_template("member.html") 
@app.route("/media.html")
def media():
    return render_template("media.html") 


@app.route("/module.html")
def module():
    return render_template("module.html") 




@app.route("/2022-aug01.html")
def f2022aug01():
    return render_template("2022-aug01.html") 
@app.route("/2022-aug02.html")
def f2022aug02():
    return render_template("2022-aug02.html") 
@app.route("/2022-aug03.html")
def f2022aug03():
    return render_template("2022-aug03.html") 
@app.route("/2022-aug04.html")
def f2022aug04():
    return render_template("2022-aug04.html") 
@app.route("/2022-mar03.html")
def f2022mar03():
    return render_template("2022-mar03.html") 
@app.route("/1110302.html")
def f1110302():
    return render_template("1110302.html") 
@app.route("/1110314.html")
def f1110314():
    return render_template("1110314.html") 
@app.route("/1110329.html")
def f1110329():
    return render_template("1110329.html") 
@app.route("/1110416.html")
def f1110416():
    return render_template("1110416.html") 
@app.route("/1110428.html")
def f1110428():
    return render_template("1110428.html") 
@app.route("/1110428b.html")
def f1110428b():
    return render_template("1110428b.html") 
@app.route("/1110503.html")
def f1110503():
    return render_template("1110503.html") 
@app.route("/1110511.html")
def f1110511():
    return render_template("1110511.html") 
@app.route("/1110521.html")
def f1110521():
    return render_template("1110521.html") 
@app.route("/1110524.html")
def f1110524():
    return render_template("1110524.html") 
@app.route("/1110601.html")
def f1110601():
    return render_template("1110601.html") 
@app.route("/1110607.html")
def f1110607():
    return render_template("1110607.html") 
@app.route("/1110624.html")
def f1110624():
    return render_template("1110624.html") 
@app.route("/1110718.html")
def f1110718():
    return render_template("1110718.html") 


@app.route("/module-a101.html")
@is_logged_in
def modulea101():
    return render_template("module-a101.html") 
@app.route("/module-a102.html")
@is_logged_in
def modulea102():
    return render_template("module-a102.html") 
@app.route("/module-a103.html")
@is_logged_in
def modulea103():
    return render_template("module-a103.html") 
@app.route("/module-a104.html")
@is_logged_in
def modulea104():
    return render_template("module-a104.html") 
@app.route("/module-a105.html")
@is_logged_in
def modulea105():
    return render_template("module-a105.html") 
@app.route("/module-a106.html")
@is_logged_in
def modulea106():
    return render_template("module-a106.html") 
@app.route("/module-a107.html")
@is_logged_in
def modulea107():
    return render_template("module-a107.html") 
@app.route("/module-a108.html")
@is_logged_in
def modulea108():
    return render_template("module-a108.html") 
@app.route("/module-a109.html")
@is_logged_in
def modulea109():
    return render_template("module-a109.html") 
@app.route("/module-a110.html")
@is_logged_in
def modulea110():
    return render_template("module-a110.html") 
@app.route("/module-b101.html")
@is_logged_in
def moduleb101():
    return render_template("module-b101.html") 
@app.route("/module-b102.html")
@is_logged_in
def moduleb102():
    return render_template("module-b102.html") 
@app.route("/module-b103.html")
@is_logged_in
def moduleb103():
    return render_template("module-b103.html") 
@app.route("/module-b104.html")
@is_logged_in
def moduleb104():
    return render_template("module-b104.html") 
@app.route("/module-c101.html")
@is_logged_in
def modulec101():
    return render_template("module-c101.html") 
@app.route("/module-c102.html")
@is_logged_in
def modulec102():
    return render_template("module-c102.html") 
@app.route("/module-c103.html")
@is_logged_in
def modulec103():
    return render_template("module-c103.html") 
@app.route("/module-c104.html")
@is_logged_in
def modulec104():
    return render_template("module-c104.html") 
@app.route("/module-c105.html")
@is_logged_in
def modulec105():
    return render_template("module-c105.html") 
@app.route("/module-c106.html")
@is_logged_in
def modulec106():
    return render_template("module-c106.html") 
@app.route("/module-c107.html")
@is_logged_in
def modulec107():
    return render_template("module-c107.html") 
@app.route("/module-c108.html")
@is_logged_in
def modulec108():
    return render_template("module-c108.html") 
@app.route("/module-c109.html")
@is_logged_in
def modulec109():
    return render_template("module-c109.html") 

@app.route("/module-z101.html")
@is_logged_in
def modulez101():
    return render_template("module-z101.html") 









if __name__=='__main__':
    app.secret_key='ssecreettt'
    app.run(debug=True)