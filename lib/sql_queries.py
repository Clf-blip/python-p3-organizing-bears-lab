# lib/sql_queries.py
# lib/sql_queries.py

# 1. names + ages of all female bears
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

# 2a. names in alpha order (original variable name)
select_all_bears_names_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

# 2b. exact-spelled alias the tests also ask for
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

# 3. youngest bear
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age ASC
LIMIT 1;
"""

# 4. oldest bear
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# 5. all living bears (name + age)
select_name_and_age_of_bears_that_are_alive = """
SELECT name, age
FROM bears
WHERE alive = 1;
"""

# 6. names + temperaments, sorted
select_bears_names_and_temperaments_alphabetically = """
SELECT name, temperament
FROM bears
ORDER BY temperament, name;
"""

# 7. living bears ordered youngest→oldest (new variable the tests now need)
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age ASC;
"""
