# Inventory Management Web Application
An inventory management Web Application using Flask

## Clone this repository and running on your local system.
git clone https://github.com/arjunsugumar24/flask-Inventory

we need Python in our system, and run below commands:

- pip install Flask
- pip install Flask-SQLAlchemy
- pip install Jinja2
- pip install SQLAlchemy

## Setup Db Connection URL.

https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format

for postgresql
app.config["SQLALCHEMY_DATABASE_URI"] =  "postgresql://postgres:admin@localhost:5432/pythonDb"

for mysql
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/arjundb'

## Running the app

1) run the file python file

D:\Arjun\realProject\flask-Inventory>python app.py

![Step-1](https://user-images.githubusercontent.com/105728946/232997839-f3617af5-a026-4df6-a298-ff36fe465142.png)

2) Check your DB for table auto created with proper colum

![Step-2](https://user-images.githubusercontent.com/105728946/232998355-2e28e1a4-7afe-4022-8e62-957cf322c9e0.png)

3) Click product nav bar and add some products

![Step-3](https://user-images.githubusercontent.com/105728946/232998527-795adca9-ba81-4994-90bf-f1d868d96269.png)

4) reate some locations and Add Product Movements

![Step-4](https://user-images.githubusercontent.com/105728946/232998774-62f1914f-8253-4282-b8da-7347ced37d32.png)

5) After Making Product Movements Check Report Tab

![Step-5](https://user-images.githubusercontent.com/105728946/232999179-ec5cef3c-acba-449e-9feb-c85e0d2c8a1c.png)

6) Check your DataBase value

![Step-6](https://user-images.githubusercontent.com/105728946/232999388-582b5bc7-c7c0-4a17-b471-ba678545dc03.png)

