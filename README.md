# importing_sheet

This project imports a spreadsheet, displaying its items.

USING:  
PostgreSQL 10.8  
Python 3.7.3  
Django 2.2.9  
Django-Import-Export 2.0.1  
     

A) Considering that POSTGRES is already properly installed and configured, just perform the following instructions:  
(feel free to choose other names, but don't forget to change in settings.py - DATABASES)

create database importing;  
create user importinguser with password 'importing123';

alter role importinguser set client_encoding to 'utf8';  
alter role importinguser set default_transaction_isolation to 'read committed';  
alter role importinguser set timezone to 'UTC';

grant all privileges on database importing to importinguser;

alter database importing owner to importinguser;

create extension if not exists "uuid-ossp";


B) Create and activate VIRTUALENV:  
(Choose the way you like best)


C) Install requirements.txt:  
- pip install -r requirements.txt 


D) Create tables in the database:

- python manage.py makemigrations
- python manage.py migrate
