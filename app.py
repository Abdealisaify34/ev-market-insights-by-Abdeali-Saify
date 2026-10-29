import os
from flask import Flask, render_template
app = Flask(__name__)
# Paste your Tableau Public "Share > Embed" URLs (the src of the iframe) here or set env vars.
DASHBOARD_URL = os.environ.get("DASHBOARD_URL", "https://public.tableau.com/views/EVMarketInsights/EVDashboard?:showVizHome=no&:embed=true")
STORY_URL = os.environ.get("STORY_URL", "https://public.tableau.com/views/EVMarketInsights/EVStory?:showVizHome=no&:embed=true")
@app.route("/")
def home(): return render_template("index.html", dash=DASHBOARD_URL, story=STORY_URL)
if __name__ == "__main__": app.run(debug=True)
