# Financial Fraud Detection System

## Project Overview
Financial fraud is a major concern for banks and digital payment services. This project aims to develop a Machine Learning (ML) model that detects suspicious transactions using anomaly detection techniques. The system helps financial institutions identify fraudulent transactions in real-time, reducing financial risks and enhancing security.

## Problem Statement
Fraudulent transactions can cause massive financial losses and impact trust in financial systems. Traditional rule-based methods are often ineffective due to the evolving nature of fraud tactics. This project leverages Machine Learning to automatically detect anomalies in financial transactions and flag them for further review.

## Key Features
- **Anomaly Detection**: Identifies suspicious transactions using ML algorithms.
- **Real-time Processing**: Analyzes transactions dynamically as they occur.
- **Visualization Dashboard**: Provides insights using interactive visualizations with Plotly.
- **User Authentication**: Ensures secure access to the fraud detection system.
- **API Integration**: Exposes RESTful APIs for data retrieval and model interaction.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Machine Learning**: Scikit-learn, TensorFlow
- **Database**: MongoDB (NoSQL)
- **Frontend**: Bootstrap, HTML, CSS
- **Visualization**: Plotly

## Dependencies
Ensure you have the following dependencies installed:
```sh
asgiref==3.8.1
Django==3.1.12
djangorestframework==3.13.1
djongo==1.3.7
numpy==2.2.4
packaging==24.2
pandas==2.2.2
plotly==5.22.0
pymongo==3.11.4
python-dateutil==2.9.0.post0
pytz==2025.1
six==1.17.0
sqlparse==0.2.4
tenacity==9.0.0
tzdata==2025.1


## Setup Instructions
1. **Clone the repository:**
   ```sh
    https://github.com/rishurai123/Fraudshield.git
   
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up MongoDB and configure database settings in Django** (update `settings.py` accordingly).

5. **Run migrations and start the server:**
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

6. **Access the dashboard at:**
   ```
   http://127.0.0.1:8000
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/transactions/` | Fetch all transactions |
| GET | `/api/transactions/{id}/` | Fetch transaction details |
| POST | `/api/transactions/analyze/` | Analyze a new transaction for fraud detection |

## Contribution Guidelines
If you would like to contribute:
- Fork the repository.
- Create a feature branch.
- Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License.

## Future Plans
- Implement deep learning techniques for improved fraud detection.
- Integrate with third-party financial APIs.
- Deploy the system using cloud services like AWS or Azure.

---
**Author:** Your Name  
**GitHub:** [YourUsername](https://github.com/yourusername)

