Netflix Data Warehouse: ETL Pipeline & Star Schema
Project Overview
This project involves the development of an end-to-end ETL (Extract, Transform, Load) pipeline to migrate raw Netflix media data into a structured Data Warehouse. The goal was to transform a "dirty" flat-file dataset into a professional Star Schema optimized for analytical reporting and data integrity.

Architecture & Design
The data warehouse is built using a Star Schema architecture in SQLite to reduce data redundancy and improve query performance.

Fact Table (fact_netflix): Acts as the central hub containing content details and foreign key references to dimensions.

Dimension Tables (dim_type, dim_rating): Normalized tables that store categorical information, linked to the fact table via Primary Key/Foreign Key relationships.

The ETL Process
1. Extraction
Data was extracted directly from the Kaggle API within a Linux environment.

The raw dataset contained over 8,800 records with significant data quality issues.

2. Transformation
Data Profiling: Identified 2,634 missing entries in the 'Director' column and other null values in 'Cast' and 'Country'.

Data Imputation: Handled missing categorical values by filling gaps with the label "Unknown" to preserve data integrity rather than deleting records.

Standardization: Standardized text formats and removed rows with missing critical ratings.

3. Loading
Processed data was loaded into an SQLite database.

Verified the warehouse functionality using SQL JOIN queries to retrieve human-readable insights from the normalized tables.

Technologies Used
Environment: Kali Linux.

Language: Python (Pandas) for Transformation.

Database: SQLite & DB Browser for SQLite.

Version Control: Git & GitHub.
