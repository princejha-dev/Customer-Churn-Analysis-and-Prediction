# Customer Churn Analysis and Prediction

A machine learning project to predict customer churn for telecommunications companies. Uses logistic regression to identify at-risk customers and enable targeted retention strategies.

## Problem Statement

Customer churn directly impacts revenue and business growth. This project helps identify which customers are likely to leave, enabling:
- Proactive retention strategies for high-value customers
- Improved customer lifetime value through targeted interventions
- Data-driven insights into factors influencing customer loyalty

## Solution

- **Exploratory Data Analysis**: Analyze 7,043 customer records across 21 attributes
- **Data Preprocessing**: Clean data, encode categorical variables, scale features
- **Predictive Model**: Logistic regression model trained on historical churn patterns
- **Interactive Interface**: Streamlit web app for real-time churn predictions
- **Key Features**: Demographics, services, billing, and tenure information

## Project Structure

``
Customer-Churn-Analysis-and-Prediction/
│
├── README.md
├── requirements.txt
├── app.py # Streamlit prediction interface
├── model.pkl # Trained model
│
├── data/
│ └── raw/
│ └── Telco Customer Churn Dataset.csv
│
├── notebooks/
│ └── Churn_Prediction.ipynb # Full analysis & model training
│
├── models/ # Model artifacts
├── tests/ # Unit tests
└── docs/ # Documentation
``

## Installation

``bash
# Clone repository
git clone https://github.com/princejha-dev/Customer-Churn-Analysis-and-Prediction.git
cd Customer-Churn-Analysis-and-Prediction

# Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
``

## Usage

**Jupyter Notebook** (Full analysis & model development):
``bash
jupyter notebook notebooks/Churn_Prediction.ipynb
``

**Web Application** (Interactive predictions):
``bash
streamlit run app.py
``
Open browser to `http://localhost:8501`

## Model Details

- **Algorithm**: Logistic Regression
- **Target**: Customer Churn (Yes/No)
- **Features**: 20 customer attributes (demographics, services, billing)
- **Train/Test Split**: 80/20
- **Key Predictors**: Contract type, tenure, internet service type, monthly charges

## Technologies

- Python 3.x
- Pandas, NumPy
- Scikit-learn (ML algorithms)
- Matplotlib, Seaborn (visualization)
- Streamlit (web interface)
- Jupyter Notebook

## Dependencies

``
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
``

See `requirements.txt` for complete list.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

---

**Status**: Active | **Last Updated**: January 2026
