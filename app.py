from flask import Flask,render_template,url_for,redirect,request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
import bcrypt
from flask_mysqldb import MySQL
app=Flask(__name__)

#Mysql configuration
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="_your__password"
app.config['MYSQL_DB']="DB18"
app.secret_key="secret123"
mysql=MySQL(app)


class Registration(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=PasswordField("Email",validators=[DataRequired(),Email()])
    password=StringField("Password",validators=[DataRequired()])
    Submit=SubmitField("Register")

    def validate_email(self,field):
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (field.data,))
        user=cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError("Email already taken")


class LoginForm(FlaskForm):
    
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired()])
    submit=SubmitField("login")
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['GET','POST'])
def register():
    form=Registration()#pass the form
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data
        hashed_password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        #store the data into database
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users (name,email,password)values (%s,%s,%s)",(name,email,hashed_password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))



    return render_template("register.html",form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed")
            return redirect(url_for('login'))

    return render_template("login.html", form=form)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id=session['user_id']
        cursor=mysql.connection.cursor()
        cursor.execute("Select * from users where id=%s",(user_id,))
        user_data=cursor.fetchone()
        cursor.close()

        if user_data:
            return render_template("dashboard.html",user=user_data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    flash("You have been logged out successsfully.")
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)
