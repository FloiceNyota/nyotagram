# NyotaGram

#### Created on 29 Oct 2021
#### By Floice Nyota Ndiiya

---
# Description  
This is a Clone for the popular photo-sharing  Instagram. It's Responsive for both Desktop version and Mobile version

---
## User Stories  
User Can :-

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it. 

---
## Access the website
Need the latest browser to be able to View

Follow this link 

It is hosted by heroku

---

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  
 ```bash 

```
##### Install and activate Virtual Enviroment envgallery  
 ```bash 
cd nyotagram  && python3 -m venv envnyotagram && source envnyotagram/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

  Create .env file
```bash
  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True 
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

  EMAIL_USE_TLS=True
  EMAIL_HOST='smtp.gmail.com'
  EMAIL_PORT=587
  EMAIL_HOST_USER='email'
  EMAIL_HOST_PASSWORD='email-password'
```

 ```bash 
python manage.py makemigrations instaclone
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py server 
```
##### Test Application  
 ```bash 
 python manage.py test instagram
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Pythonp, Django Framework

* Heroku 
  
  
## Bugs  
* have to press enter for the like button to work
  
## Contact Details
nyotafloice@gmail.com

@FloiceNyota (Twitter)

@Floice `Nyota Slack Moringa`

---

### License
This Project is under the [MIT](LICENSE) license
