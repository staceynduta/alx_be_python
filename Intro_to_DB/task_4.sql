-- Retrieve detailed schema information for the 'BOOKS' table.
SELECT
    COLUMN_NAME AS Field,        -- Aliased to 'Field'
    COLUMN_TYPE AS Type,         -- Aliased to 'Type'
    IS_NULLABLE AS 'Null',       -- Aliased to 'Null' (using quotes for keyword)
    COLUMN_KEY AS 'Key',         -- Aliased to 'Key' (using quotes for keyword)
    COLUMN_DEFAULT AS 'Default', -- Aliased to 'Default' (using quotes for keyword)
    EXTRA AS Extra               -- Aliased to 'Extra'
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND -- Filter by the specific database name (lowercase as per schema)
    TABLE_NAME = 'Books';               -- Filter by the specific table name (uppercase as created in task_2.sql)