# Carbon Diamond Abrasives Price List Application

A web-based price list application for Carbon Diamond Abrasives, built with Flask and SQLAlchemy.

## Features

- Product catalog organized by categories:
  - Chemicals
  - Diamond
  - Equipment
  - Other
  - Parts & Accessories
  - Safety Equipment
- Search functionality across all products
- Responsive design for all screen sizes
- Clean and professional interface with Carbon Diamond Abrasives branding

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd pricelist_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Data Input Instructions

1. Prepare your Excel file with the following columns:
   - Category: The product category (e.g., Chemicals, Diamond, Equipment)
   - Product: The product name
   - Price: The product price (numeric value)

2. Save your Excel file in the project root directory

3. Update the import_data.py script with your Excel file name:
```python
if __name__ == '__main__':
    import_excel('your_file_name.xlsx')
```

4. Run the import script:
```bash
python import_data.py
```

The script will:
- Create categories if they don't exist
- Add products under appropriate categories
- Skip incomplete entries
- Handle price formatting automatically
- Provide feedback on import progress

## Running the Application

1. Start the Flask development server:
```bash
python run.py
```

2. Access the application in your web browser at:
```
http://127.0.0.1:5000
```

## Roadmap

### Phase 1: AI-Powered Data Categorization (Q1 2024)
- Implement machine learning model to automatically categorize products
- Features will include:
  - Natural language processing for product descriptions
  - Pattern recognition for product naming conventions
  - Automatic category suggestion based on similar products
  - Confidence scoring for categorization accuracy
  - Manual override option for uncertain categorizations

### Phase 2: AI Chatbot Integration (Q2 2024)
- Add an intelligent chatbot with the following capabilities:
  - Answer pricing queries in natural language
  - Provide product recommendations
  - Compare similar products
  - Explain product specifications
  - Handle bulk pricing inquiries
  - Generate quotes based on conversation

### Phase 3: Smart Order Form Generation (Q3 2024)
- Develop AI-powered order form system:
  - Automatic form population based on chat history
  - Smart product bundling suggestions
  - Quantity optimization recommendations
  - Pricing tier calculations
  - Delivery time estimation
  - Integration with inventory management
  - PDF quote generation
  - Email quote functionality

### Phase 4: Advanced Analytics and Optimization (Q4 2024)
- Implement AI-driven insights:
  - Purchase pattern analysis
  - Demand prediction
  - Price optimization suggestions
  - Customer behavior analysis
  - Inventory optimization recommendations
  - Seasonal trend detection
  - Custom reporting capabilities

## Contact Information

### Perth Office
- Phone: 08 6243 1778
- Address: Unit 1/21 Delage Street, Joondalup, WA
- Email: sales@carbondiamondabrasives.com.au
- Website: carbondiamondabrasives.com.au

### Melbourne Office
- Phone: 08 6243 1778
- Address: 2/11 Friars Road, Moorabbin, VIC
- Email: salesvic@carbonda.com.au
- Website: carbondiamondabrasives.com.au

## Development

The application is built using:
- Flask (Web framework)
- SQLAlchemy (Database ORM)
- Bootstrap (Frontend framework)
- Custom CSS for styling

## License

This project is proprietary software owned by Carbon Diamond Abrasives.
