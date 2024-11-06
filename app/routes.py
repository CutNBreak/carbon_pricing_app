from flask import Blueprint, render_template, request
from app.models import Category, Product

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

@bp.route('/category/<int:category_id>')
def category_view(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.filter_by(category_id=category.id).all()
    return render_template('category.html', category=category, products=products)

@bp.route('/search')
def search():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    return render_template('search_results.html', query=query, products=products)
