# Tableau build guide

## Sheets (12 unique visualizations)
1. Bar: Annual_Sales_Units by Vehicle_Category
2. Treemap: sales by Manufacturer (market share)
3. Line: sales by Sales_Year, split by category (growth)
4. Donut/Pie: Battery_Type share
5. Bar: avg Driving_Range_km by category
6. Box plot or bar: Customer_Rating by category
7. Filled map: Manufacturing_Country by sales
8. Scatter: Battery_Capacity_kWh vs Driving_Range_km, colour = Battery_Type
9. Heat map: Battery_Type x Vehicle_Category (avg range)
10. Bar: Top 10 manufacturers by avg rating (Top N filter)
11. Dual axis: avg Price vs avg Range by category
12. KPI tiles: total sales, avg rating, avg range, # manufacturers

## Calculated fields (8)
- `Market Share %` = SUM([Annual_Sales_Units]) / TOTAL(SUM([Annual_Sales_Units]))
- `YoY Growth %` = (ZN(SUM([Annual_Sales_Units])) - LOOKUP(ZN(SUM([Annual_Sales_Units])),-1)) / ABS(LOOKUP(ZN(SUM([Annual_Sales_Units])),-1))
- `Price per km` = SUM([Price_USD]) / SUM([Driving_Range_km])
- `Rating Band` = IF AVG([Customer_Rating])>=4.5 THEN "Excellent" ELSEIF AVG([Customer_Rating])>=4 THEN "Good" ELSE "Average" END
- `Range Class` = IF [Driving_Range_km]>=450 THEN "Long" ELSEIF [Driving_Range_km]>=250 THEN "Medium" ELSE "Short" END
- `Efficiency (km/kWh)` = [Driving_Range_km] / [Battery_Capacity_kWh]
- `Revenue` = [Price_USD] * [Annual_Sales_Units]
- `Is Top 5 Maker` = RANK(SUM([Annual_Sales_Units])) <= 5

## Filters
Year (range), Category, Manufacturer, Battery_Type, Country, Rating slider. Apply "Apply to worksheets > All using this data source".

## Dashboard
Size: Automatic (or build a Desktop + Phone layout). Use floating-free tiled containers, a filter bar on top, KPIs row, 2x2 chart grid. Add Filter actions (click a category to filter all) and a Highlight action on Battery_Type.

## Story (6 scenes)
1. Market overview (KPIs + category sales)  2. Who leads (manufacturer share)  3. Growth 2019-2025
4. Battery technology mix and range  5. Where EVs are made (map)  6. Customer satisfaction and recommendations

## Performance testing checklist (for the documentation)
Rows loaded (2,500), live connection vs extract timing, number of filters, calculated fields, sheets. Screenshot Performance Recording (Help > Settings and Performance > Start Performance Recording).
