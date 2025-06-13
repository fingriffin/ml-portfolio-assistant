from schema import FundMetadataSchema

class DatabaseStatement:
    @classmethod
    def create_metadata_table(cls, table_name: str = "fund_metadata") -> str:
        """
        Generates a SQL CREATE TABLE query using the required fields from FundMetadataSchema.

        :param table_name: Name of the table to create.
        :return: SQL statement string.
        """
        columns = ",\n    ".join(
            f"{field} {dtype}" for field, dtype in FundMetadataSchema.REQUIRED_FIELDS_SQL.items()
        )
        return f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {columns}\n);"

    @classmethod
    def query_fund_metadata(cls, ticker: str, table_name: str = "fund_metadata") -> str:
        """
        Generates a SQL statement to query fund metadata for a given ticker.

        :param ticker: ticker for fund.
        :param table_name: Name of the metadata table.
        :return: SQL statement string.
        """
        return f"SELECT * FROM {table_name} WHERE ticker = '{ticker}'"

    @classmethod
    def upsert_fund_metadata(cls, table_name: str = "fund_metadata", *, do_update: bool = False) -> str:
        """
        Generates a parameterized SQL INSERT or REPLACE statement for fund metadata.

        :param table_name: Target table name.
        :param do_update: If True, replaces existing row.
        :return: SQL statement string with '?' placeholders.
        """
        fields = list(FundMetadataSchema.REQUIRED_FIELDS_SQL.keys())
        placeholders = ", ".join(["?"] * len(fields))
        columns = ", ".join(fields)

        if do_update:
            return f"REPLACE INTO {table_name} ({columns}) VALUES ({placeholders})"
        else:
            return f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    @classmethod
    def get_all_tickers(cls, table_name: str = "fund_metadata") -> str:
        """
        Generates a SQL SELECT statement to select all tickers from given table.

        :param table_name: Target table name.
        :return: SQL statement string.
        """
        return f"SELECT DISTINCT TICKER FROM {table_name}"

    @classmethod
    def remove_fund_metadata(cls, ticker, table_name: str = "fund_metadata") -> str:
        """
        Generates a SQL DELETE statement for given ticker.

        :param ticker: Target ticker.
        :param table_name: Target table name.
        :return: SQL statement string.
        """
        return f"DELETE FROM {table_name} WHERE ticker = '{ticker}'"