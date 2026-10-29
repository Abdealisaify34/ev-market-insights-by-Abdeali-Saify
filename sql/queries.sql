-- 1 Sales by category
SELECT Vehicle_Category, SUM(Annual_Sales_Units) total_sales FROM ev_sales GROUP BY 1 ORDER BY 2 DESC;
-- 2 Top 5 manufacturers + market share
SELECT Manufacturer, SUM(Annual_Sales_Units) sales,
 ROUND(100*SUM(Annual_Sales_Units)/(SELECT SUM(Annual_Sales_Units) FROM ev_sales),2) share_pct
FROM ev_sales GROUP BY 1 ORDER BY 2 DESC LIMIT 5;
-- 3 Battery technology distribution
SELECT Battery_Type, COUNT(*) models, ROUND(AVG(Driving_Range_km)) avg_range FROM ev_sales GROUP BY 1;
-- 4 Avg rating by category
SELECT Vehicle_Category, ROUND(AVG(Customer_Rating),2) avg_rating FROM ev_sales GROUP BY 1;
-- 5 Year-over-year growth
SELECT Sales_Year, SUM(Annual_Sales_Units) sales,
 ROUND(100*(SUM(Annual_Sales_Units)-LAG(SUM(Annual_Sales_Units)) OVER (ORDER BY Sales_Year))
 /LAG(SUM(Annual_Sales_Units)) OVER (ORDER BY Sales_Year),1) yoy_pct FROM ev_sales GROUP BY 1;
-- 6 Production by country
SELECT Manufacturing_Country, COUNT(DISTINCT Manufacturer) makers, SUM(Annual_Sales_Units) sales FROM ev_sales GROUP BY 1 ORDER BY 3 DESC;
-- 7 Top-rated manufacturers (window rank)
SELECT Manufacturer, ROUND(AVG(Customer_Rating),2) r, RANK() OVER (ORDER BY AVG(Customer_Rating) DESC) rnk FROM ev_sales GROUP BY 1;
