# cost_control 💡

API for an expense management and
expense control system for prisma digital employees to control their monthly budget.

## Getting started 🚀

These instructions will allow you to install correctly the Python web project

### Installation 🔧

1. Init your repository 
 ```- git init
 - git add .
 - git -m commit "my first commit"
 ```
2. Clone the repository 
 ```
 - git clone https://github.com/SantiagoAndresSerrano/cost_control 
 #or download the source code.
 ```
3. Create a Virtual enviorenment
``` - py -3 -m venv venv
 - venv\Scripts\activate
 ```
5. install the requirements
 ``` 
 pip install -r requirements.txt
 ```
6. Run the app
``` 
- python main.py

```

### Deployment 🚀

The API was deployed on heroku, a free service that was made easy for me to use, however I have had experience deploying through AWS services, in RDS (Relational Database Service) S3 and Elastic Bean Stalk technologies.

1. Log in to heroku Account
``` 
- heroku login

```
2. Clone the repository 
``` 
- heroku git:clone -a cost-control-v1

```
3. Deploy changes
``` 
- git add .
- git commit -am "My First Commit"
- git push heroku master

```
4. Open app

``` 
https://cost-control-v1.herokuapp.com/swagger/#/

```

#### built with 🛠️

- **Python** is a high-level language, is an interpreted language where any platform with an interpreter can run it, offers a variety of libraries and frameworks has a large community which allows exponential progress in learning.
- **Flask** is a microframework that allows to develop in an agile and fast way, it includes a development web server, you can run a web server to see the results that are being obtained.
- **SqlAlchemy** one of the features of SqlAlchemy is its ORM model, is a library that allows you to manipulate the tables of a database as if they were objects. It is responsible for making the appropriate translations and has a dependency on the database so you can easily modify the database engine.
- **Flask-Marshmallow** is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow, including URL and Hyperlinks fields for HATEOAS-ready APIs.
- **Flasgger** provides an extension (Swagger) that inspects the Flask app for endpoints that contain YAML docstrings with Swagger 2.0
- **Heroku** is a cloud-based Platform as a Service (PaaS) solution, has the ability to support multiple programming languages and is currently a free service.

##### Architecture
- API REST 

- **Flassger** I used flassger for the documentation of the different proposed endpoints, in order to facilitate the review of them. LINK: https://cost-control-v1.herokuapp.com/swagger/#/ 🔩

The architecture is a REST architecture, which is represented by the following diagram, in this case the client is a web browser, which communicates through HTTP requests (GET, POST, PUT, DELETE) with the API rest represented as an interface and making use of the flassger tool. The API, being a programmable application interface, exposes the required services through the corresponding endpoints, to finally communicate with the database through SQLALCHEMY. 

![Diagrama de arquitectura](https://github.com/SantiagoAndresSerrano/cost_control/blob/master/doc/architecture.png?raw=true "Architecture diagram")


