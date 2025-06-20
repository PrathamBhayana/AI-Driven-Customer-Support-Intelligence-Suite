# AI Driven Customer Support Intelligence Suite

This project is a machine learning-based system for classifying customer support tickets. It predicts the issue type and urgency level of each ticket and extracts key entities such as product names, dates, and complaint keywords from the ticket text.

---

## Features

- **Issue Type Classification:** Automatically predicts the type of issue reported in a ticket.
- **Urgency Level Classification:** Predicts the urgency level of the ticket.
- **Entity Extraction:** Extracts product names, dates, and complaint-related keywords from ticket descriptions.
- **Exploratory Data Analysis (EDA):** Visualizes ticket distributions, trends, and common keywords.

---

## Project Structure

```
AI-Driven-Customer-Support-Intelligence-Suite/
│
├── data/
│   └── tickets_complex_1000.xls   # Dataset
│
├── models/                                          # Saved ML models and vectorizer
│
├── notebooks/
│   └── exploratory_analysis.ipynb                   # EDA notebook
│
├── src/
│   ├── data_preparation.py
│   ├── entity_extraction.py
│   ├── feature_engineering.py
│   ├── issue_type_classifier.py
│   ├── pipeline.py
│   └── urgency_level_classifier.py
│
├── requirements.txt
└── README.md
```

---

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/PrathamBhayana/AI-Driven-Customer-Support-Intelligence-Suite
   cd AI-Driven-Customer-Support-Intelligence-Suite
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run**
   ```sh
   python -m src.pipeline   
   ```

---

## Usage

1. **Data Preparation**: Use the `data_preparation.py` module to clean and preprocess the ticket data.
2. **Feature Engineering**: Utilize the `feature_engineering.py` module to extract features from the preprocessed data.
3. **Model Training**: Train the classifiers using `issue_type_classifier.py` and `urgency_level_classifier.py`.
4. **Entity Extraction**: Extract key entities from ticket text using the `entity_extraction.py` module.
5. **Pipeline Integration**: Use the `pipeline.py` module to integrate all components and make predictions on new ticket data.

## Example

To classify a new ticket and extract entities, you can use the integrated pipeline as follows:

```python
from src.pipeline import classify_ticket

result = classify_ticket("Your ticket text here.")
print(result)
```
