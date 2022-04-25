from flask import render_template, request, Blueprint

from flaskblog.models import Post, User

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)

@main.route("/about")
def about():
	return render_template('about.html', title='About')

@main.route("/searchText")
def searchText():
	page = request.args.get('page', 1, type=int)
	
	search_input = request.args.get('search-input')
	search_input = f'%{search_input}%'

	posts = Post.query.filter(Post.title.contains(search_input)).order_by(Post.date_posted.desc()).paginate(page=page, per_page=50)

	return render_template('home.html', posts=posts)		

@main.route("/searchDate")
def searchDate():
	page = request.args.get('page', 1, type=int)

	date_input = request.args.get('date-input')
	date_input = f'%{date_input}%'

	posts = Post.query.filter(Post.date_posted.contains(date_input)).order_by(Post.date_posted.desc()).paginate(page=page, per_page=50)

	return render_template('home.html', posts=posts)	

@main.route("/searchAuthor")
def searchAuthor():
	page = request.args.get('page', 1, type=int)
	
	search_author = request.args.get('search-author')
	search_author = f'%{search_author}%'

	user = User.query.filter(User.username.contains(search_author)).first_or_404()
	posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=50)

	return render_template('home.html', posts=posts)
