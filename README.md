# Data Quality Automation Scripts 🚀

A collection of Python scripts to automate data quality checks and save your team valuable time. These scripts help identify missing values, ensure data consistency, and detect duplicates with minimal setup.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

- **Smart Missing Value Detector**: Automatically identify and categorize missing data with impact assessment
- **Data Consistency Guardian**: Catch impossible values, statistical outliers, and validation issues
- **Duplicate Detective**: Find exact and partial duplicates with pattern recognition

## 📋 Requirements

- Python 3.7+
- pandas
- numpy
- datetime

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ikrzm/data-quality-scripts.git

# Navigate to the project directory
cd data-quality-scripts

# Install required packages
pip install -r requirements.txt
```

### Basic Usage

```python
import pandas as pd
from data_quality import check_missing_values, check_data_consistency, check_duplicates

# Load your data
df = pd.read_csv('your_data.csv')

# Check for missing values
missing_report = check_missing_values(df)
print(missing_report)

# Check data consistency
consistency_issues = check_data_consistency(
    df,
    date_columns=['date_column'],
    numeric_columns=['amount_column']
)
print(consistency_issues)

# Check for duplicates
duplicate_report = check_duplicates(
    df,
    subset_columns=['id', 'transaction_date']
)
print(duplicate_report)
```

## 📊 Example Output

### Missing Value Report
```
           total_missing  percent_missing impact
email               150            15.0%   High
phone                50             5.0%   Low
address              80             8.0%   Medium
```

### Consistency Report
```
WARNING: 5 future dates found in transaction_date
WARNING: 12 outliers found in amount_column
```

### Duplicate Report
```
{
    'exact_duplicates': 25,
    'partial_duplicates': 42
}
```

## 🛠️ Configuration

### Custom Validation Rules
```python
validation_rules = {
    'date_columns': ['transaction_date', 'signup_date'],
    'numeric_ranges': {
        'age': (0, 120),
        'transaction_amount': (0, 1000000)
    }
}
```

## 📈 Performance

- Processes 1M rows in ~30 seconds
- Memory efficient with chunk processing for large datasets
- Configurable performance settings

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Inspired by real-world data quality challenges
- Thanks to all contributors who have helped improve these scripts
- Special thanks to the data science community for feedback and suggestions

## 📧 Contact


Project Link: [https://github.com/yourusername/data-quality-scripts](https://github.com/ikrzm/data-quality-scripts)

## 📚 Additional Resources

- [Medium Article]([your-medium-article-link](https://medium.com/@datainsights17/3-python-scripts-that-will-transform-your-data-quality-checks-a-complete-guide-bca143b7d011))
- [LinkedIn Post](your-linkedin-post-link)
