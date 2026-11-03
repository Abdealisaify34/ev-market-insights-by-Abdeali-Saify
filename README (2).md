# EV Market Performance Insights — SQL + Tableau + Flask

**Live app:** https://ev-market-insights-e7fx.onrender.com/

An end-to-end EV market analytics project. A dataset of electric vehicles is stored in **MySQL**, analysed with **SQL**, visualised in an interactive **Tableau** dashboard and story, and published through a responsive **Flask** web app deployed on **Render**.

The project covers EV **sales**, **battery technology**, **driving range**, **customer ratings** and **manufacturing by country**.

> **Important:** This repository hosts the website and the supporting data/SQL pipeline. The embedded Tableau views are loaded from Tableau Public's servers, so an internet connection is required to see them.

## Features

- Interactive Tableau dashboard and Tableau Story embedded in a Flask web page
- MySQL schema and a data-loading script (pandas → MySQL)
- SQL analysis using `GROUP BY`, subqueries and window functions
- Reproducible dataset generator (2,500 rows, 12 columns)
- Tableau packaged workbook included (`EV Market Insights.twbx`)
- Environment-based configuration of the Tableau URLs
- Render.com deployment using Gunicorn

## Tech stack

| Layer | Technology |
| --- | --- |
| Database | MySQL |
| Analysis | SQL (aggregation, subqueries, window functions) |
| Data prep | Python, pandas |
| Visualisation | Tableau (Dashboard + Story), Tableau Public |
| Web app | Python, Flask, HTML/CSS |
| Deployment | Gunicorn, Render.com |

## Project structure

```text
ev-market-insights-by-Abdeali-Saify/
├── app.py                    # Flask app (serves the embedded dashboard and story)
├── generate_dataset.py       # Builds data/ev_market.csv
├── load_to_db.py             # Loads the CSV into MySQL
├── requirements.txt
├── Procfile                  # web: gunicorn app:app
├── EV Market Insights.twbx   # Tableau packaged workbook
├── README.md
├── data/                     # Generated dataset (ev_market.csv)
├── sql/                      # schema.sql and queries.sql
├── docs/                     # Tableau build guide (TABLEAU_GUIDE.md)
├── static/                   # CSS and static assets
└── templates/                # Jinja templates (index.html)
```

## Dataset

`generate_dataset.py` creates `data/ev_market.csv` with **2,500 rows and 12 columns**, covering sales years **2019–2025**.

> The data is **synthetic** (generated with realistic ranges and a fixed random seed of 42). Replace it with a real dataset, for example from Kaggle, if one is available.

| Column | Description |
| --- | --- |
| `Vehicle_ID` | Unique row identifier |
| `Manufacturer` | Maker (Tesla, BYD, Tata Motors, MG Motor, Hyundai, Nissan, BMW, Volkswagen, Ola Electric, NIO, Ather, Ashok Leyland) |
| `Model` | Generated model code |
| `Vehicle_Category` | Hatchback, Sedan, SUV, Electric Bus, Electric Truck or Two-Wheeler |
| `Battery_Type` | NMC, LFP, NCA, Solid-State or Sodium-Ion |
| `Battery_Capacity_kWh` | Battery capacity in kWh |
| `Driving_Range_km` | Driving range in km |
| `Price_USD` | Price in US dollars |
| `Annual_Sales_Units` | Units sold |
| `Customer_Rating` | Rating between 2.5 and 5.0 |
| `Manufacturing_Country` | Country of manufacture |
| `Sales_Year` | Year of sale (2019–2025) |

## Pipeline

1. **Generate the dataset**
   ```bash
   python generate_dataset.py
   ```
   Creates `data/ev_market.csv`.

2. **Create the database and table**
   ```bash
   mysql < sql/schema.sql
   ```

3. **Load the data into MySQL**
   ```bash
   DB_URL=mysql+pymysql://user:pass@host/ev_market python load_to_db.py
   ```

4. **Run the SQL analysis** — execute `sql/queries.sql` for the `GROUP BY`, subquery and window-function queries.

5. **Build the Tableau workbook** — in Tableau, choose *Connect → MySQL → `ev_sales`*, then build the sheets, the dashboard and the story. See `docs/TABLEAU_GUIDE.md`.

6. **Publish to Tableau Public** and copy the embed URL (the `src` of the iframe from *Share → Embed*) for the dashboard and the story.

7. **Run the web app** with the embed URLs configured (see below).

8. **Deploy on Render.**

## Run locally

### 1. Prerequisites

- Python 3.10 or newer
- MySQL (only needed if you want to rebuild the database and run the SQL queries)
- An internet connection to load the Tableau Public visualisations

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Tableau URLs (optional)

The app reads two environment variables and falls back to defaults in `app.py`:

| Variable | Purpose |
| --- | --- |
| `DASHBOARD_URL` | Tableau Public embed URL for the dashboard |
| `STORY_URL` | Tableau Public embed URL for the story |

macOS/Linux:

```bash
export DASHBOARD_URL="https://public.tableau.com/views/<workbook>/<dashboard>?:showVizHome=no&:embed=true"
export STORY_URL="https://public.tableau.com/views/<workbook>/<story>?:showVizHome=no&:embed=true"
```

Windows PowerShell:

```powershell
$env:DASHBOARD_URL="https://public.tableau.com/views/<workbook>/<dashboard>?:showVizHome=no&:embed=true"
$env:STORY_URL="https://public.tableau.com/views/<workbook>/<story>?:showVizHome=no&:embed=true"
```

### 5. Start the application

```bash
python app.py
```

Then open http://127.0.0.1:5000/.

## Deploy to Render.com

1. Push the project to GitHub (do not commit virtual environments or secrets).
2. In Render, create a **New → Web Service** and connect the repository.
3. Set **Runtime** to Python.
4. Set **Build Command** to:
   ```bash
   pip install -r requirements.txt
   ```
5. Set **Start Command** to:
   ```bash
   gunicorn app:app
   ```
   (The included `Procfile` contains the same command.)
6. Under **Environment**, add the two variables:

   | Key | Value |
   | --- | --- |
   | `DASHBOARD_URL` | Your Tableau Public dashboard embed URL |
   | `STORY_URL` | Your Tableau Public story embed URL |

7. Click **Deploy**. Render will publish the app at a public `onrender.com` URL.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Home page with the embedded Tableau dashboard and story |

## Troubleshooting

- **Tableau view doesn't appear:** confirm the workbook is published publicly on Tableau Public, check your internet connection, and make sure the URL is the embed URL (`...?:showVizHome=no&:embed=true`).
- **Wrong or default dashboard shows:** set `DASHBOARD_URL` / `STORY_URL`, then restart or redeploy the app.
- **`python` or `py` not found:** install Python and make sure it is on your PATH.
- **Database load fails:** check the `DB_URL` credentials and that the `ev_market` database exists (run `sql/schema.sql` first).
- **Render deployment fails:** check the build and runtime logs, and make sure `requirements.txt` and `Procfile` are in the repository root.

## Author

**Abdeali Saify** — [GitHub: Abdealisaify34](https://github.com/Abdealisaify34)

## License and data

This repository contains the web application code, SQL scripts and a synthetic dataset. The embedded visualisations are hosted on Tableau Public and are subject to Tableau's terms and policies.
