# Knowledge Card System

## Overview
This project is a cloud-based knowledge card system made for CIS 4517.

The goal of the project is to let users create and store cards that contain text and images.

Each card includes:
- title
- description
- image

The image is stored in AWS S3 and the text data is stored in the database.

This project uses a three-tier architecture:
- frontend with Django templates
- backend with Django views
- storage with SQLite and AWS S3

---

## Features
- create new cards
- upload images
- view all cards
- search cards by text
- search by image
- delete cards
- deployed on AWS EC2

---

## Tech Used
- Python
- Django
- AWS EC2
- AWS S3
- SQLite
- boto3

---

## Files I worked on

### models.py
This file contains the `Card` model.

It stores:
- title
- description
- image url

### views.py
This is where most of the backend logic is.

I wrote the functions for:
- creating cards
- uploading images to S3
- displaying cards
- searching cards
- deleting cards
- image search

### urls.py
This file handles the routes for each page such as:
- home
- create
- delete
- image search

### HTML Templates
I created:
- `home.html`
- `create.html`
- `image_search.html`

These pages are used for displaying cards and forms.

---

## AWS
The images are stored in my S3 bucket called:

`knowledge-cards`

The website is deployed using AWS EC2.

---

## Database
The text information for each card is stored in `db.sqlite3`.

This includes the title, description, and image URL.

---

## Purpose
This project was made to practice cloud computing concepts using AWS and Django.

It includes cloud storage, database storage, and search functionality.




