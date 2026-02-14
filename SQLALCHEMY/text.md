# SQL Basics

SQL is the language used to talk to databases.

## Core Concepts

*   **Database**: A container for tables. You make one, then "use" it.
*   **Table**: Like a spreadsheet. It stores data in rows and columns.
*   **Column**: A specific attribute (e.g., Name, Age). It has a defined type.
*   **Row**: A single record of data (e.g., "Mike, 21").

## Data Types

*   `INT`: Whole numbers.
*   `VARCHAR(size)`: Text with a maximum length.
*   `CHAR(size)`: Text with a fixed length.
*   `FLOAT`: Decimal numbers.
*   `DATE` / `DATETIME`: Dates and times.

## Key Rules (Constraints)

*   **Primary Key**: A unique ID for every row. No duplicates allowed.
*   **Unique**: Ensures values in a column are different for every row.
*   **Not Null**: The column cannot be empty.
*   `DEFAULT`: A fallback value if none is provided.
*   `AUTO_INCREMENT`: Automatically numbers new rows (1, 2, 3...).
*   `CHECK`: custom rule (e.g., Age must be positive).

## Basic Actions

1.  **Create**: Make new databases or tables.
2.  **Insert**: Add new rows of data.
3.  **Select**: Read or "query" data to see it.
4.  **Update**: Change existing data.
5.  **Delete**: Remove data.
6.  **Alter**: Change the structure of a table (like adding a column) later on.
7.  **Drop**: Delete a table or database entirely.
