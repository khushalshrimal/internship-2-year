# PySpark Sales Analysis

## Objective

Perform sales analysis using PySpark DataFrame API.

## Dataset

sales.csv contains:

- product_id
- product_name
- category
- sales

## Operations Performed

1. Read CSV file into DataFrame
2. Sort products by sales descending
3. Display Top 3 products by sales
4. Filter products with sales > 80000
5. Save filtered results as CSV

## Build Docker Image

```bash
docker build -t sales-analysis .
```

## Run Container

```bash
docker run --rm sales-analysis
```

## Expected High Sales Products

| Product | Sales |
|----------|---------|
| Laptop | 150000 |
| TV | 120000 |
| Mobile | 95000 |
| Bed | 90000 |

## Output Location

```text
output/high_sales_products/
```