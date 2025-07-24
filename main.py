# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
    SELECT *,
    CASE
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""", conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
    SELECT CAST(SUM(priceEach * quantityOrdered) AS INTEGER) AS total
    FROM orderDetails
""", conn)['total']

# I couldn't get this test passing for the total price.

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)

conn.close()


# cursor = conn.cursor()

# # Show all table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("All tables:", tables)

# # Check which table has 'orderDate' by showing column names
# for table_name in tables:
#     table = table_name[0]
#     cursor.execute(f"PRAGMA table_info({table});")
#     columns = cursor.fetchall()
#     print(f"Columns in {table}:", [col[1] for col in columns])
