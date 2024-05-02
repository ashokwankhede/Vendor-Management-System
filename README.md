# Vendor-Management-System
# Django REST API Setup

This repository contains a Django project with a RESTful API using Django REST Framework.

## Prerequisites

- Python (version 3.9+ recommended)
- Django
- Django REST Framework

# Setup Instructions

## Create a Virtual Environment:
- python -m venv env_name

## Install Dependencies:
- pip install django
- pip install djangorestframework

## Superuser Creation and Token Generation
To create a superuser and generate a token, execute the following commands:
After creating the superuser, visit [http://localhost:8000/api/generate-token/](http://localhost:8000/api/generate-token/) to generate a token using username and password.

