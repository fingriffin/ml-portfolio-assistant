""""""
import sqlite3
from pathlib import Path
from sqlite3 import Connection
from typing import Any, Dict, Optional
import yaml
from schema.fund_metadata import FundMetadataSchema

def get_project_root() -> Path:
    """
    Resolves root of project relative to .src.

    :return: The root of the project relative to .src.
    """
    return Path(__file__).resolve().parent.parent

def get_db_connection(db_path: Optional[Path] = None) -> Connection:
    """
    Establishes a connection to the local SQLite3 database for fund data.

    If the database file does not exist, it will be created automatically.

    :param db_path: Optional path to the SQLite3 database file. If None, defaults to 'config/fund_data.sqlite3'.
    :return: A sqlite3 Connection object
    """
    if db_path is None:
        db_path = get_project_root() / "data" / "sqlite" / "fund_data.sqlite3"

    db_path.parent.mkdir(parents=True,exist_ok=True)

    return sqlite3.connect(db_path)

def load_config_funds(config_path: Optional[Path] = None) -> Dict[str, Dict[str, Any]]:
    """
    Loads fund metadata from a YAML configuration file.

    :param config_path: Optional path to the YAML config file. If None, defaults to 'config/fund_metadata.yml' at project root.
    :return: A list of dictionaries, each representing a fund's metadata
    """
    if config_path is None:
        config_path = get_project_root() / "config" / "fund_metadata.yml"

    with config_path.open("r", encoding="utf-8") as file:
        funds = yaml.safe_load(file)

    return funds

def validate_fund_metadata(funds: Dict[str, Dict[str, Any]]) -> None:
    """
    Validates a dictionary of fund metadata entries against the required schema.

    Each fund is expected to be a dictionary with a specific set of required fields and types,
    as defined in FundMetadataSchema.REQUIRED_FIELDS.

    Each fund is also checked for unexpected fields and values of fields.

    :param funds: Dictionary where keys are fund identifiers and values are metadata dictionaries.
    :raises ValueError: If any fund is missing a required field, contains a field of the wrong type,
                        includes an unexpected field or value of the field not defined/implemented
                        in the schema.
    :return: None.
    """
    required_fields = FundMetadataSchema.REQUIRED_FIELDS
    allowed_fields_set = set(required_fields.keys())

    for fund_key, fund_data in funds.items():
        # Check for missing fields and type mismatches
        for field, expected_type in required_fields.items():
            if field not in fund_data:
                raise ValueError(f"Fund '{fund_key}' is missing required field: '{field}'")

            actual_value = fund_data[field]
            if not isinstance(actual_value, expected_type):
                # Support expected_type being a tuple of types
                if isinstance(expected_type, tuple):
                    expected_names = ", ".join(t.__name__ for t in expected_type)
                else:
                    expected_names = expected_type.__name__

                raise ValueError(
                    f"Field '{field}' in fund '{fund_key}' should be of type {expected_names}, "
                    f"but got {type(actual_value).__name__}"
                )

        # Check for unexpected fields
        for field in fund_data:
            if field not in allowed_fields_set:
                raise ValueError(
                    f"Fund '{fund_key}' contains unexpected field: '{field}'. "
                    f"Expected only: {sorted(allowed_fields_set)}"
                )

        # Check for allowed value constraints
        allowed_values = FundMetadataSchema.ALLOWED_VALUES
        for field, valid_options in allowed_values.items():
            if fund_data.get(field) not in valid_options:
                raise ValueError(
                    f"Fund '{fund_key}' has unsupported value for '{field}': {fund_data.get(field)}. "
                    f"Allowed values: {valid_options}"
                )


if __name__ == "__main__":
    data = load_config_funds()
    validate_fund_metadata(data)