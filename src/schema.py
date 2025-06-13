"""Defines the schema for fund data used throughout the project."""

class FundMetadataSchema:
    # Required fields and their dtypes
    REQUIRED_FIELDS = {
        "ticker": str,
        "name": str,
        "currency": str,
        "ocf": (float, int),
        "source": str,
        "added": str,
        "accumulation": bool,
        "asset_class": str,
        "region": str,
        "hedged": bool,
        "base_currency": str,
        "inception_date": str,
        "frequency": str
    }

    # Required fields for SQL table creation
    REQUIRED_FIELDS_SQL = {
        "ticker": "TEXT PRIMARY KEY",
        "name": "TEXT",
        "currency": "TEXT",
        "ocf": "REAL",
        "source": "TEXT",
        "added": "TEXT",
        "accumulation": "BOOLEAN",
        "asset_class": "TEXT",
        "region": "TEXT",
        "hedged": "BOOLEAN",
        "base_currency": "TEXT",
        "inception_date": "TEXT",
        "frequency": "TEXT",
        "last_updated": "TEXT"
    }

    # Logical constraints based on what's been implemented
    ALLOWED_VALUES = {
        "currency": ["GBP"],
        "source": ["yfinance"],
        "accumulation": [True],
        "asset_class": ["equity","bond"],
        "base_currency": ["USD","GBP","Multi","EUR"],
        "frequency": ["daily"]
    }