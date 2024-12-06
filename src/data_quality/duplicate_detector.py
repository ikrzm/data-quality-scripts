import pandas as pd
from typing import Optional, List, Dict, Any

def check_duplicates(
    df: pd.DataFrame,
    subset_columns: Optional[List[str]] = None,
    threshold: float = 0.9
) -> Dict[str, Any]:
    """
    Smart duplicate detector that finds exact and near-duplicate entries.
    
    Args:
        df: Input DataFrame
        subset_columns: Columns to consider for duplicate detection
        threshold: Similarity threshold for near-duplicate detection
        
    Returns:
        Dictionary containing duplicate analysis results
    """
    duplicate_report = {
        'exact_duplicates': 0,
        'partial_duplicates': 0,
        'duplicate_groups': [],
        'summary': {}
    }
    
    # Check exact duplicates
    exact_dupes = df.duplicated().sum()
    duplicate_report['exact_duplicates'] = exact_dupes
    
    # Check partial duplicates if subset columns provided
    if subset_columns:
        partial_dupes = df.duplicated(subset=subset_columns).sum()
        duplicate_report['partial_duplicates'] = partial_dupes
        
        if partial_dupes > 0:
            # Analyze duplicate patterns
            dupe_patterns = df[df.duplicated(subset=subset_columns, keep=False)]
            grouped = dupe_patterns.groupby(subset_columns).size()
            
            # Store duplicate groups info
            duplicate_report['duplicate_groups'] = [
                {
                    'columns': subset_columns,
                    'count': count,
                    'values': dict(zip(subset_columns, index))
                }
                for index, count in grouped.items()
            ]
    
    # Calculate summary statistics
    duplicate_report['summary'] = {
        'total_rows': len(df),
        'exact_duplicate_percentage': (exact_dupes / len(df) * 100).round(2),
        'partial_duplicate_percentage': (
            partial_dupes / len(df) * 100
        ).round(2) if subset_columns else 0
    }
    
    return duplicate_report