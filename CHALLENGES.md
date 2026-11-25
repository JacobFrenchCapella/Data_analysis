# Data Analysis Challenges

Complete these in order. Do not skip the written explanations: a good analyst explains what the numbers mean.

## Level 1 — Data inspection
1. Load all four CSV files using pandas.
2. Print the number of rows and columns in each file.
3. Display the first 5 rows of each dataset.
4. Identify missing values in every column.
5. Identify duplicate order IDs.
6. Report the data types and determine which columns should be dates or numeric.

**Deliverable:** A short data-quality report.

## Level 2 — Data cleaning
7. Standardize `status` values so capitalization is consistent.
8. Decide how to handle rows with missing order dates, missing prices, and zero quantities. Explain your decisions.
9. Detect and handle duplicate orders.
10. Find orders whose customer ID does not exist in customers.
11. Check for impossible values (negative quantities/prices, invalid dates).
12. Create a cleaned orders dataset without changing the original CSV.

**Deliverable:** `cleaned_orders.csv` and a list of cleaning decisions.

## Level 3 — Business metrics
13. Calculate total valid orders.
14. Calculate gross revenue from completed orders.
15. Calculate total units sold.
16. Calculate average order value (AOV).
17. Calculate total cost and gross profit using product cost.
18. Calculate profit margin as a percentage.
19. Find the top 10 customers by revenue.
20. Find the 5 best-selling products by units.

**Deliverable:** A metrics summary printed clearly.

## Level 4 — Grouping and joining
21. Join orders to customers and products.
22. Calculate revenue by state.
23. Calculate revenue by product category.
24. Calculate monthly revenue.
25. Find each customer's number of orders and total spend.
26. Identify customers who have never placed a completed order.
27. Calculate return counts and return rates by product.

**Deliverable:** Three summary tables saved as CSV files.

## Level 5 — Analysis and visualization
28. Plot monthly revenue as a line chart.
29. Plot revenue by category as a bar chart.
30. Plot the top 10 customers by revenue.
31. Compare units sold with revenue by product.
32. Identify the strongest and weakest month.
33. Write 5 evidence-based observations. Do not confuse correlation with causation.

**Deliverable:** At least 3 charts and a one-page findings report.

## Level 6 — Final analyst challenge
Pretend the owner asks: "What is happening in my business, and what should I do next?"

Create a report that includes:
- A data-quality section
- At least 6 business KPIs
- Monthly revenue trend
- Best and worst product/category
- Best-performing state
- Customer concentration (how much revenue comes from the top 10 customers?)
- Return-rate analysis
- Three recommendations supported by numbers
- Limitations and assumptions

Your final report should be understandable to someone who does not know Python.

## Optional advanced challenges
- Write a reusable function that accepts any dataframe and returns a missing-value report.
- Add command-line arguments for selecting a date range.
- Export all metrics to JSON.
- Create a SQLite database and query it with SQL.
- Write unit tests for your own cleaning and metric functions.
