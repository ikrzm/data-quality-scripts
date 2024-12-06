import pandas as pd
import numpy as np
from typing import Dict, Any

def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Comprehensive missing value detector that identifies and categorizes missing data.
    
    Args:
        df (pd.DataFrame): Input DataFrame to analyze
        
    Returns:
        pd.DataFrame: DataFrame containing missing value statistics
    """
    # Calculate missing values statistics
    missing_stats = pd.DataFrame({
        'total_missing': df.isnull().sum(),
        'percent_missing': (df.isnull().sum() / len(df) * 100).round(2)
    }).sort_values('percent_missing', ascending=False)
    
    # Add impact assessment
    missing_stats['impact'] = missing_stats['percent_missing'].apply(
        lambda x: 'High' if x > 15 else ('Medium' if x > 5 else 'Low')
    )
    
    # Add additional metadata
    missing_stats['column_type'] = df.dtypes
    missing_stats['total_rows'] = len(df)
    
    return missing_stats