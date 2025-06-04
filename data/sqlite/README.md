# Vanguard Fund Database Schema

This SQLite3 database stores price and metadata for all tracked Vanguard funds, using two tables:

---

## `fund_metadata`

Stores **static fund information** used to describe and organize funds, syncs to config/funds_metadata.yml.

| Column           | Description                                                        |
|------------------|--------------------------------------------------------------------|
| `fund_id`        | Unique ID.                                                         |
| `ticker`         | yfinance-compatible ticker (e.g. `VUAG.L`).                        |
| `name`           | Full fund name.                                                    |
| `currency`       | Trading currency (e.g. `GBP`).                                     |
| `base_currency`  | Currency of underlying assets (e.g. `USD`).                        |
| `ocf`            | Ongoing Charges Figure (percentage, e.g. `0.07`).                  |
| `source`         | Where this data came from (e.g. `yfinance`).                       |
| `added`          | Date this fund was first added to tracking (`YYYY-MM-DD`).         |
| `accumulation`   | True if accumulating (vs. distributing).                           |
| `asset_class`    | Fund type: `equity`, `bond`, etc.                                  |
| `region`         | Exposure region (e.g. `Global`, `US`, `Europe ex-UK`).             |
| `hedged`         | True if currency-hedged.                                           |
| `inception_date` | Fund inception date.                                               |
| `frequency`      | Update frequency (e.g. `daily`, `weekly`).                         |
| `last_updated`   | When this metadata row was last updated (for syncing with config). |

---

## `fund_prices`

Stores **weekly or daily price history** for each fund.

| Column        | Description                          |
|---------------|--------------------------------------|
| `fund_id`     | Matches the `fund_metadata.fund_id`. |
| `date`        | Date of NAV (Net Asset Value).       |
| `nav`         | The NAV value (float).               |
| `updated_at`  | Timestamp of ingestion/update.       |

Primary key: `(fund_id, date)`

---

This database is **not version controlled** — see `.gitignore`.