import pandas as pd
from app import create_app, db
from app.models import Category, Product

def import_excel(filepath):
    print(f"Reading Excel file: {filepath}")
    app = create_app()
    
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Read Excel file
        df = pd.read_excel(filepath)
        
        # Process each row
        for _, row in df.iterrows():
            category_name = str(row['Category']).strip()
            product_name = str(row['Product']).strip()
            price = float(row['Price'])
            
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
        
        # Commit all changes
        db.session.commit()
        print("Data import completed successfully")

if __name__ == '__main__':
    import_excel('product_catalog_20241106_165749.xlsx')
