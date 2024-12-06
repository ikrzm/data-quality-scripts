import pandas as pd
from datetime import datetime
from typing import List, Optional, Dict, Any

def check_data_consistency(
    df: pd.DataFrame,
    date_columns: Optional[List[str]] = None,
    numeric_columns: Optional[List[str]] = None,
    custom_rules: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Validates data consistency including dates, numerical values, and custom rules.
    
    Args:
        df: Input DataFrame
        date_columns: List of column names containing dates
        numeric_columns: List of column names containing numeric values
        custom_rules: Dictionary of custom validation rules
        
    Returns:
        Dictionary containing consistency check results
    """
    consistency_report = {
        'issues_found': [],
        'summary': {'total_issues': 0},
        'details': {}
    }
    
    # Check date columns
    if date_columns:
        for col in date_columns:
            if col in df.columns:
                future_dates = df[df[col] > datetime.now()][col].count()
                if future_dates > 0:
                    consistency_report['issues_found'].append(
                        f"WARNING: {future_dates} future dates found in {col}"
                    )
                    consistency_report['details'][col] = {
                        'future_dates': future_dates,
                        'min_date': df[col].min(),
                        'max_date': df[col].max()
                    }
    
    # Check numeric columns
    if numeric_columns:
        for col in numeric_columns:
            if col in df.columns:
                # Calculate statistics
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                
                # Identify outliers
                outliers = df[
                    (df[col] < (Q1 - 1.5 * IQR)) | 
                    (df[col] > (Q3 + 1.5 * IQR))
                ][col].count()
                
                if outliers > 0:
                    consistency_report['issues_found'].append(
                        f"WARNING: {outliers} outliers found in {col}"
                    )
                    consistency_report['details'][col] = {
                        'outliers': outliers,
                        'Q1': Q1,
                        'Q3': Q3,
                        'IQR': IQR
                    }
    
    # Apply custom rules
    if custom_rules:
        for rule_name, rule_func in custom_rules.items():
            try:
                result = rule_func(df)
                if result:
                    consistency_report['issues_found'].append(
                        f"Custom rule '{rule_name}' failed: {result}"
                    )
            except Exception as e:
                consistency_report['issues_found'].append(
                    f"Error applying custom rule '{rule_name}': {str(e)}"
                )
    
    consistency_report['summary']['total_issues'] = len(
        consistency_report['issues_found']
    )
    
    return consistency_report