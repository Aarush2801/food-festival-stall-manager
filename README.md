# Food Festival Stall Manager

A Python-based desktop application designed to manage food festival stall information efficiently. The project provides a graphical interface for adding, viewing, modifying, and deleting stall records, along with a mechanism to import structured data from Excel into an SQL database.

---

## Overview

Managing stall information during large school or community events can be error-prone when done manually. This project digitizes the process by combining a relational database with a simple GUI, making stall data easy to store, retrieve, and update in real time.

The system is intended for event organizers and student executive members who need quick access to stall details without direct interaction with the database.

---

## Features

- Import stall data from Excel (.xls) files into an SQL database  
- Centralized storage of stall, food item, and team information  
- Graphical user interface built using Tkinter  
- Add, delete, modify, and view stall records  
- Simple login screen for controlled access  

---

## Tech Stack

**Language**
- Python

**Libraries and Tools**
- Tkinter (GUI)
- sqlite3 (database)
- PyMySQL (SQL interface)
- xlrd (Excel file handling)

---

## Project Structure

- Excel-to-SQL data import script for structured data storage  
- SQL database with predefined tables for stall and team details  
- Tkinter-based application for managing and querying records  

---

## How It Works

1. Stall data is prepared in an Excel file (.xls format)  
2. The data is imported into an SQL database using Python  
3. The GUI allows users to interact with the data:
   - Add new stalls  
   - Update existing records  
   - Delete stalls  
   - View all stored information  

---

## Usage

1. Install required dependencies:
   ```bash
   pip install pymysql xlrd

