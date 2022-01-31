from flask import Flask,request,render_template,redirect,flash,jsonify

from random import randint,choice,sample



app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#Flask Debug Toolbar & Redirects
#The Debug Toolbar makes redirects explicit
#This is very useful for debugging!
#If you don’t want this, you can turn it off:





MOVIES={"Spider Man", "Avengers" , "Sing2"}

@app.route('/')
def home_page():
    html="""
    <html>
      <body>
        <h1>Home Page</h1>
        <p>This is the home page</p>
        <a href='/hello'>Go to the hello page</a>
      </body>
    </html>
    """
    return html
  
@app.route("/old-home-page")
def redirect_to_home():
      """Redirects to new homepage"""
      return redirect("/")
  
  
@app.route("/movies")
def show_all_movies():
    """Show all movies in fake database"""
    return render_template("movies.html", movies=MOVIES)


@app.route('/movies/json')
def get_movies_json():
    return jsonify(list(MOVIES)) #in here MOVIES was a set,and we cannot use jsonify in sets,
#so we convert it to a list then use jsonify & don't forget to add jsonify to the top to import.



@app.route("/movies/new", methods=["POST"])
def add_movie():
    title=request.form["title"]
    
    #the list we defined will pretend as a fake database
    #return render_template('movies.html', movies=MOVIES): 
    #sayfayi yeniledigimde enson yazdigim movie ismini tekrar tekrar ekledi.
    #o yuzden bu kodun yerine redirect kullanip, sayfayi yeniledigim zaman ana sayfaya donmesini
    #soyleyebilirim.boylese hem post request i yapip hem save oluoyor?
    
    if title in MOVIES:
        flash("Movie already exists, so I'm not adding that again!", "error")
    else:
        MOVIES.add(title)
        flash("The new movie is added","success")
    
    return redirect('/movies')  