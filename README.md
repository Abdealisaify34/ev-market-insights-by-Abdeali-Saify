# EV Market Performance Insights (SQL + Tableau + Flask)
Interactive Tableau dashboard and story, backed by a MySQL database and embedded in a Flask web app.

**Live demo:** <add Render URL>  |  **Tableau Public:** <add URL>

## Pipeline
1. `python generate_dataset.py` -> `data/ev_market.csv` (2,500 rows, 12 columns; synthetic, replace with real data if available)
2. Create DB and table: `mysql < sql/schema.sql`
3. `DB_URL=mysql+pymysql://user:pass@host/ev_market python load_to_db.py`
4. Run `sql/queries.sql` for the SQL operations (GROUP BY, subquery, window functions)
5. Tableau: Connect > MySQL > `ev_sales`. Build sheets, dashboard, story (see docs/TABLEAU_GUIDE.md)
6. Publish to Tableau Public, copy the embed URL into `DASHBOARD_URL` / `STORY_URL`
7. `pip install -r requirements.txt && python app.py`
8. Deploy on Render: build `pip install -r requirements.txt`, start `gunicorn app:app`, add the two env vars.
