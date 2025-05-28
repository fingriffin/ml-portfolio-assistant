# Fund Metadata Configuration

This folder contains `funds_metadata.yml`, which defines metadata for each fund tracked by the data ingestion pipeline.

Each fund entry uses the following fields:

### Fields
- `ticker`: Yahoo Finance ticker used for data ingestion.
- `name`: Full name of the fund for readability.
- `currency`: Reporting currency of the fund's NAV (e.g. GBP, USD).
- `ocf`: Ongoing Charges Figure (as a percent, e.g. 0.07 means 0.07% per year).
- `source`: Where the data is pulled from (e.g. `yfinance`, `csv`).
- `added`: Date the fund was added to the YAML config (ISO format, e.g. `2025-05-28`).
- `accumulation`: `true` if dividends are reinvested (accumulation class), `false` if distributing.
- `asset_class`: Type of asset (`equity`, `bond` etc.).
- `region`: Broad geographic exposure of the fund (e.g. `US`, `Global`).
- `hedged`: `true` if the fund is currency-hedged to its reporting currency.
- `base_currency`: Currency of the underlying assets (e.g. USD for S&P 500).
- `inception_date`: Fund launch date (ISO format, e.g. `2012-05-22`).
- `frequency`: Frequency of available NAV data (typically `daily`).

To add a new fund, copy an existing block in `funds_metadata.yaml` and update the relevant fields.
