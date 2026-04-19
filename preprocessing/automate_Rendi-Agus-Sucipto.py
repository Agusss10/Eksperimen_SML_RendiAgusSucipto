import pandas as pd

def preprocess_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)

    # Handle missing values
    df['person_emp_length'] = df['person_emp_length'].fillna(df['person_emp_length'].median())
    df['loan_int_rate'] = df['loan_int_rate'].fillna(df['loan_int_rate'].median())

    # Encoding kategorikal
    df = pd.get_dummies(df, drop_first=True)

    # Save hasil preprocessing
    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    preprocess_data(
        input_path="../credit_risk_raw/credit_risk_dataset.csv",
        output_path="credit_risk_preprocessing/data_processed.csv"
    )