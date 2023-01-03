-- noinspection SqlNoDataSourceInspectionForFile

-- Create the Escaperoom database
-- CREATE DATABASE Escaperoom;

-- Use the Escaperoom database
USE Escaperoom;



CREATE TABLE Teams (
    Id INT PRIMARY KEY IDENTITY,
    TeamName VARCHAR(80) NOT NULL,
    ContactName VARCHAR(80) NOT NULL,
    Email VARCHAR(80) NOT NULL,
    PasswordHash VARCHAR(128) NOT NULL
);


---


DECLARE @DatabaseName nvarchar(50)
SET @DatabaseName = N'users'

DECLARE @SQL varchar(max)

SELECT @SQL = COALESCE(@SQL,'') + 'Kill ' + Convert(varchar, SPId) + ';'
FROM MASTER..SysProcesses
WHERE DBId = DB_ID(@DatabaseName) AND SPId <> @@SPId

SELECT @SQL
EXEC(@SQL)

drop database users

---

CREATE TABLE Teams (
    Id INT PRIMARY KEY IDENTITY,
    TeamName VARCHAR(80) NOT NULL,
    ContactName VARCHAR(80) NOT NULL,
    Email VARCHAR(80) NOT NULL,
    PasswordHash VARCHAR(128) NOT NULL
);
