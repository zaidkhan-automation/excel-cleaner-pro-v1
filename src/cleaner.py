"""
cleaner.py
Core cleaning functions for Excel Cleaner Pro v1.
"""

import pandas as pd
import re

def remove_duplicates(df: pd.DataFrame, subset=None, keep: str = 'first') -> pd.DataFrame:
    """Remove duplicate rows. If subset is None, checks all columns."""
    return df.drop_duplicates(subset=subset, keep=keep).reset_index(drop=True)

def handle_missing(df: pd.DataFrame, strategy: str = 'fill', fill_value='', columns=None) -> pd.DataFrame:
    """
    Handle missing values.
    strategy: 'drop' | 'fill' | 'fill_column_mode'
    """
    df_copy = df.copy()
    cols = columns if columns is not None else df_copy.columns.tolist()

    if strategy == 'drop':
        return df_copy.dropna(subset=cols).reset_index(drop=True)

    elif strategy == 'fill':
        return df_copy.fillna(fill_value)

    elif strategy == 'fill_column_mode':
        for c in cols:
            try:
                mode = df_copy[c].mode().iloc[0]
                df_copy[c] = df_copy[c].fillna(mode)
            except Exception:
                df_copy[c] = df_copy[c].fillna(fill_value)
        return df_copy

    return df_copy

def standardize_text(df: pd.DataFrame, columns=None, lowercase=True, strip=True) -> pd.DataFrame:
    """Clean text: trim spaces, lowercase, remove extra spaces."""
    df_copy = df.copy()
    cols = columns if columns is not None else df_copy.select_dtypes(include=['object']).columns.tolist()

    for c in cols:
        def clean_cell(x):
            if pd.isna(x):
                return x
            s = str(x)
            if strip:
                s = s.strip()
            s = re.sub(r'\s+', ' ', s)
            if lowercase:
                s = s.lower()
            return s

        df_copy[c] = df_copy[c].apply(clean_cell)

    return df_copy

def format_numbers(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    """Convert numbers stored as text into numeric (remove commas, symbols)."""
    df_copy = df.copy()
    cols = columns if columns is not None else df_copy.columns.tolist()

    for c in cols:
        try:
            df_copy[c] = df_copy[c].astype(str).str.replace(r'[^0-9.\-]', '', regex=True)
            df_copy[c] = pd.to_numeric(df_copy[c], errors='ignore')
        except Exception:
            continue

    return df_copy

def parse_dates(df: pd.DataFrame, columns=None, dayfirst: bool = False) -> pd.DataFrame:
    """Try parsing columns into datetime."""
    df_copy = df.copy()
    cols = columns if columns is not None else df_copy.columns.tolist()

    for c in cols:
        try:
            df_copy[c] = pd.to_datetime(df_copy[c], errors='ignore', dayfirst=dayfirst)
        except Exception:
            continue

    return df_copy

def clean_pipeline(df: pd.DataFrame,
                   remove_dup=True,
                   missing_strategy='fill',
                   fill_value='',
                   text_standardize=True,
                   parse_date_columns=None,
                   format_number_columns=None) -> pd.DataFrame:
    """Pipeline that runs common cleaning steps in sequence."""
    df_out = df.copy()

    if remove_dup:
        df_out = remove_duplicates(df_out)

    if text_standardize:
        df_out = standardize_text(df_out)

    if format_number_columns:
        df_out = format_numbers(df_out, format_number_columns)

    if parse_date_columns:
        df_out = parse_dates(df_out, parse_date_columns)

    df_out = handle_missing(df_out, strategy=missing_strategy, fill_value=fill_value)

    return df_out