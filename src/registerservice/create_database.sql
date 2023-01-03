-- Create the Escaperoom database
-- CREATE DATABASE Escaperoom;

-- Use the Escaperoom database
USE Escaperoom;

-- Create the Groups table
CREATE TABLE Groups (
    groupname VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);


CREATE TABLE Teams (
    Id INT PRIMARY KEY IDENTITY,
    TeamName VARCHAR(80) NOT NULL,
    ContactName VARCHAR(80) NOT NULL,
    Email VARCHAR(80) NOT NULL,
    PasswordHash VARCHAR(128) NOT NULL
);
