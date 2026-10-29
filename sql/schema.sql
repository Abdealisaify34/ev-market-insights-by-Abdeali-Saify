CREATE DATABASE IF NOT EXISTS ev_market;
USE ev_market;
CREATE TABLE IF NOT EXISTS ev_sales (
  Vehicle_ID INT PRIMARY KEY, Manufacturer VARCHAR(50), Model VARCHAR(50),
  Vehicle_Category VARCHAR(30), Battery_Type VARCHAR(20),
  Battery_Capacity_kWh DECIMAL(6,1), Driving_Range_km INT, Price_USD INT,
  Annual_Sales_Units INT, Customer_Rating DECIMAL(2,1),
  Manufacturing_Country VARCHAR(40), Sales_Year INT);
