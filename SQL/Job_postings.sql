-- Create Database
CREATE DATABASE IF NOT EXISTS job_postings_db;
USE job_postings_db;

-- Drop table if exists (for fresh reloads)
DROP TABLE IF EXISTS job_postings;

-- Create Job Postings Table
CREATE TABLE job_postings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_id VARCHAR(255) NOT NULL UNIQUE,  -- Adzuna unique ID
    title VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    category VARCHAR(100),
    location VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    contract_time VARCHAR(50),            -- full-time / part-time
    salary_min DECIMAL(12,2),
    salary_max DECIMAL(12,2),
    created DATE,
    description TEXT,
    url VARCHAR(500)
);

-- Indexes for faster queries
CREATE INDEX idx_title ON job_postings(title);
CREATE INDEX idx_company ON job_postings(company);
CREATE INDEX idx_location ON job_postings(location);

