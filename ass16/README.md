# Employee Salary Processing Using PySpark RDD

## Objective

Process employee data using PySpark RDDs and Docker.

## Operations Performed

1. Read employee CSV data into an RDD.
2. Sort employees by salary in descending order.
3. Calculate department-wise salary totals.
4. Identify top 3 highest-paid employees.
5. Save top 3 employees to output file.

---

## Dataset

employees.csv

```csv
id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000
```

## Build Docker Image

```bash
docker build -t employee-rdd .
```

## Run Docker Container

```bash
docker run --rm employee-rdd
```

## Output

### Sorted Employees

Employees are displayed in descending order of salary.

### Department Salary Totals

IT : 170000
HR : 85000
Finance : 130000

### Top 3 Employees

Saved in:

```text
output/top3_employees/
```

## Technologies Used

- Python 3.12
- Apache Spark 3.5.6
- PySpark RDD
- Docker
- Java 21