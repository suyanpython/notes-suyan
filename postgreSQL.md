For detailed documentation on all supported PostgreSQL functions:
https://www.postgresql.org/docs/current/functions.html

Data Analysis with PostgreSQL function reference
---------------------------------------------------------------------

String Manipulation Functions
FUNCTION                                    RESULT
---------------------------------------------------------------------
lower ( 'PostgreSQL' )                      postgresql

upper ( 'PostgreSQL' )                      POSTGRESQL

left ( 'PostgreSQL', 4 )                    Post

right ( 'PostgreSQL', 3 )                   SQL

substring ( 'PostgreSQL', 5 , 3 )           gre

length ( 'cats and dogs' )                  13

position ( 'a' in 'cats and dogs' )         2

replace ( 'cats and dogs', 'and', '&' )     cats & dogs

trim ( '   cats   ' )                       cats


Pattern Matching Functions
OPERATOR                                    MATCHES
---------------------------------------------------------------------
name LIKE 'a%'                              abraham, abed
name LIKE '%a'                              Marcia
name LIKE '%a%'                             Iman, Lucia, allen
name LIKE 'a_'                              al
name LIKE '__a'                             Ana, lua
name LIKE '_a_'                             Ian
name LIKE '_a%'                             Tarick, Yasu
name LIKE 'A__%'                            Anya, Ami
name LIKE 'A%'                              Alice
name ILIKE 'A%'                             Alice, alice


Date and Time Series Data Functions
FUNCTION                                    RESULT
---------------------------------------------------------------------
date_trunc( 'day', current_timestamp )      2024-06-13 00:00:00+00
date_trunc( 'hour', current_timestamp )     2024-06-13 17:00:00+00
date_trunc( 'year', current_timestamp )     2024-01-01 00:00:00+00
EXTRACT ( day from current_timestamp )      13
EXTRACT ( hour from current_timestamp )     17
EXTRACT ( year from current_timestamp )     2024
EXTRACT ( ISODOW from current_timestamp )   6,7 (Saturday, Sunday)
TO_CHAR ( current_timestamp,
    'FMDay, DD HH12:MI:SS' )                Thursday, 13 06:59:02
TO_CHAR ( current_timestamp,
    'FMMonth DD, YYYY' )                    June 13, 2024
TO_CHAR ( current_timestamp,
    'HH12:MI AM, FMDay' )                   06:59 PM, Thursday


CASE statements
FUNCTION
---------------------------------------------------------------------
SELECT
    customer,
    quantity,
    CASE 
        WHEN quantity >= 10 THEN '10% discount'
        WHEN quantity >=2 THEN '5% discount' 
        ELSE 'no discount'
    END AS notes
FROM orders;

SELECT
    reviewer, rating,
    CASE rating
        WHEN 5 THEN 'excellent'
        WHEN 4 THEN 'good'
        WHEN 3 THEN 'okay'
        WHEN 2 THEN 'bad'
        WHEN 1 THEN 'terrible'
        ELSE NULL
    END AS rating_translation
FROM reviews;



---------------------------------------------------------------------
CHAPTER 2

Rounding Functions
FUNCTION                                    RESULT
---------------------------------------------------------------------
ROUND ( 123.4567 )                          123
ROUND ( 123.4567, 3 )                       123.457
ROUND ( 123.4567, -2 )                      100
CEIL  ( 123.4567 )                          124
FLOOR ( 123.4567 )                          123
TRUNC ( 123.4567, 3 )                       123.456
TRUNC ( 123.7 )                             123


Data Type Casting Functions
FUNCTION                                    RESULT
---------------------------------------------------------------------
RIGHT ( 1234, 2 )                           error    
CAST ( 1234 AS text )                       ‘1234’    text
RIGHT ( CAST ( 1234 AS text ), 2 )          ‘34’      text
CAST( RIGHT(CAST(1234 AS text), 2) AS int)  34        integer
1 + 2                                       3         integer
1 / 2                                       0         integer
CAST (1 AS numeric) / 2                     0.5000    numeric
ROUND (CAST (1 AS numeric) / 2, 1)          0.5       numeric


Functions for Working with NULL Values
FUNCTION                                                RESULT
---------------------------------------------------------------------
SELECT * 
FROM table_name 
WHERE column_name IS NULL;

SELECT * 
FROM table_name 
WHERE column_name IS NOT NULL;

COALESCE ( null, 'world' )                              world
COALESCE ( 'hello', 'world')                            hello
COALESCE ( null, null, null, null, 'hello', 'world' )   hello
COALESCE ( null, null, null, null )                     null
COALESCE ( nickname, first_name )
COALESCE ( null, 'Michael' )                            Michael
COALESCE ( 'Mike', 'Michael' )                          Mike

NULLIF ( 'hello', 'hello' )                             null
NULLIF ( 'hello', 'world' )                             hello



---------------------------------------------------------------------
CHAPTER 3

Central Tendency Functions
FUNCTION                                    
---------------------------------------------------------------------
SELECT 
    AVG(my_values) AS mean,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY my_values) AS median,
    MODE() WITHIN GROUP (ORDER BY my_values) AS mode
FROM my_data;


Standard Deviation Functions
FUNCTION                                        RESULT
---------------------------------------------------------------------
SELECT 
    MAX(my_values) - MIN(my_values) AS range,   -- range
    VARIANCE(my_values) AS variance,            -- variance of a sample
    VAR_SAMP(my_values) AS var_samp,            -- variance of a sample,
    VAR_POP(my_values) AS var_pop,              -- variance of a population,
    STDDEV(my_values) AS stddev,                -- standard deviation of a sample
    STDDEV_SAMP(my_values) AS stddev_samp,      -- standard deviation of a sample
    STDDEV_POP(my_values) AS stddev_pop         -- standard deviation of a population
FROM my_data;


Percentile Rank Functions
FUNCTION                                    
---------------------------------------------------------------------
SELECT 
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY my_values) AS q1,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY my_values) AS q2, --median
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY my_values) AS q3,
  PERCENTILE_CONT(1.00) WITHIN GROUP (ORDER BY my_values) AS q4  --max
FROM 
  my_data;
    
WITH quartiles AS (
  SELECT 
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY my_values) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY my_values) AS q3
  FROM my_data
  )
  SELECT 
    (q3 - q1) AS iqr,
    (q1 - 1.5 * (q3 - q1)) AS low_outlier_limit,
    (q3 + 1.5 * (q3 - q1)) AS high_outlier_limit
  FROM quartiles;
    

Aggregate Values with Window Functions
FUNCTION                                    
---------------------------------------------------------------------
SELECT employee, department, salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg_salary,
    COUNT(employees) OVER (PARTITION BY department) AS count_same_dept,
    MAX(salary) OVER (PARTITION BY department) AS max_salary_same_dept,
    MIN(salary) OVER (PARTITION BY department) AS min_salary_same_test,
    SUM(salary) OVER (PARTITION BY department) AS sum_salary_department,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_salary_by_department,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS denserank_salary_by_department,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS percentrank_salary_by_department
FROM 
    employees;
    

Moving Window Functions
FUNCTION
---------------------------------------------------------------------
AVG(sales) OVER 
    (ORDER BY month_num ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
    AS 3_month_moving_avg
  
SUM(sales) OVER 
    (ORDER BY month_num ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
    AS running_total




