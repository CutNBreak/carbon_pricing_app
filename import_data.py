import os
import sys
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define models here to avoid circular imports
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

def import_excel(filepath):
    print(f"Reading Excel file: {filepath}")
    
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Read Excel file
        df = pd.read_excel(filepath)
        
        # Process each row
        for _, row in df.iterrows():
            try:
                category_name = str(row['Category']).strip()
                product_name = str(row['Product']).strip()
                
                # Try to convert price, use 0.0 as default if conversion fails
                try:
                    price_str = str(row['Price']).strip()
                    if price_str == 'xx.xx' or not price_str:
                        price = 0.0
                    else:
                        price = float(price_str)
                except (ValueError, TypeError):
                    price = 0.0
                    print(f"Warning: Invalid price for {product_name}, setting to 0.0")
                
                # Skip if category or product name is empty
                if not category_name or not product_name:
                    continue
                    
                # Get or create category
                category = Category.query.filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    db.session.add(category)
                    db.session.commit()
                    print(f"Created new category: {category_name}")
                
                # Create product if it doesn't exist
                product = Product.query.filter_by(name=product_name, category_id=category.id).first()
                if not product:
                    product = Product(name=product_name, price=price, category=category)
                    db.session.add(product)
                    print(f"Added product: {product_name} (${price:.2f}) to category: {category_name}")
            
            except Exception as e:
                print(f"Error processing row: {row}")
                print(f"Error details: {str(e)}")
                continue
        
        # Commit all changes
        db.session.commit()
        print("Data import completed successfully")

if __name__ == '__main__':
    import_excel('product_catalog_20241106_165749.xlsx')
