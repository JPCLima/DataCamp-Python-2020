## Count number of rows in a table
```sql 
SELECT count(*)
    FROM tablename;
```

## Count the number of missing values
Subtract the count of the non-NULL ticker values from the total number of rows; 
alias the difference as missing.
```sql 
SELECT count(*) - count(ticker) AS missing
  FROM fortune500;
```

## Join Tables
```sql 
SELECT company.name
  FROM company
       INNER JOIN fortune500 
       ON company.ticker=fortune500.ticker;
```

## Coaldesce function

Return the first non null value from the columns
```sql 
SELECT coalesce(column_1, column_2)
```

### Using the coalesce
```sql 
-- Use coalesce
SELECT coalesce(industry, sector, 'Unknown') AS industry2,
       -- Don't forget to count!
       count(*) 
  FROM fortune500 
-- Group by what? (What are you counting by?)
 GROUP BY industry2
-- Order results to see most common first
 ORDER BY count DESC
-- Limit results to get just the one value you want
 LIMIT 1;
```

## Count the number by type
```sql 
-- Count the number of tags with each type
SELECT type, count(*) AS count
  FROM tag_type
 -- To get the count for each type, what do you need to do?
 GROUP BY type
 -- Order the results with the most common
 -- tag types listed first
 ORDER BY count DESC;
```


```sql 
-- Select the 3 columns desired
SELECT name, tag_type.tag, tag_type.type
  FROM company
  	   -- Join to the tag_company table
       INNER JOIN tag_company 
       ON company.id = tag_company.company_id
       -- Join to the tag_type table
       INNER JOIN tag_type
       ON tag_company.tag = tag_type.tag
  -- Filter to most common type
  WHERE type='cloud';
  ```

  ## Self Join
  ```sql 
  SELECT company_original.name, title, rank
  -- Start with original company information
  FROM company AS company_original
       -- Join to another copy of company with parent
       -- company information
	   LEFT JOIN company AS company_parent
       ON company_original.parent_id = company_parent.id 
       -- Join to fortune500, only keep rows that match
       INNER JOIN fortune500 
       -- Use parent ticker if there is one, 
       -- otherwise original ticker
       ON coalesce(company_parent.ticker, 
                   company_original.ticker) = 
             fortune500.ticker
 -- For clarity, order by rank
 ORDER BY rank; 
   ```

## Cast the columns
Changing the data type of the coloumns using the CAST()
  ```sql 
-- Select the original value
SELECT profits_change, 
	   -- Cast profits_change
       CAST(profits_change as integer) AS profits_change_int
  FROM fortune500;
```