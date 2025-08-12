-- Query 1: Roll-up - Total sales by country and quarter
SELECT 
    Country, 
    strftime('%Y-Q%q', InvoiceDate) AS Quarter,
    SUM(TotalSales) AS TotalSales
FROM SalesFact
GROUP BY Country, Quarter
ORDER BY Country, Quarter;

-- Query 2: Drill-down - Monthly sales for United Kingdom
SELECT 
    strftime('%Y-%m', InvoiceDate) AS Month,
    Description,
    SUM(Quantity) AS TotalQuantity,
    SUM(TotalSales) AS TotalSales
FROM SalesFact
WHERE Country = 'United Kingdom'
GROUP BY Month, Description
ORDER BY Month;

-- Query 3: Slice - Electronics sales analysis
SELECT 
    Country,
    SUM(TotalSales) AS ElectronicsSales
FROM SalesFact
WHERE Description IN ('Laptop', 'Smartphone', 'Headphones')
GROUP BY Country
ORDER BY ElectronicsSales DESC;