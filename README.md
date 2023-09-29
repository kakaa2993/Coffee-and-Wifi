<h1 align="center"> Coffee and Wi-Fi(☕+📶) </h1>

https://user-images.githubusercontent.com/43291919/208074983-476e1437-0c6e-4647-82ab-27c3a7085ba1.mp4

![Languages](https://img.shields.io/github/languages/count/kakaa2993/Coffee-and-Wifi?color=%234d41c0)
![Top Language](https://img.shields.io/github/languages/top/kakaa2993/Coffee-and-Wifi?color=%234d41c0)
![Repository Size](https://img.shields.io/github/repo-size/kakaa2993/Coffee-and-Wifi?color=%234d41c0)
![Made By](https://img.shields.io/badge/made%20by-kakaa-%234d41c0)

<br>

## About The Website:
This website is a collection of cafes ☕ with data on power sockets 🔌  available, wifi 📶 speed, and coffee quality, and you can also add more cafe stores to the database.

<br>

## The technologies Used:
- <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML5</a> & <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS3</a> for the structure and the styling.  
- <a href="https://getbootstrap.com/">Bootstrap 5</a> for the UI.  
- <a href="https://docs.python.org/3/library/csv.html">CSV</a> for the Database.  
- <a href="https://flask.palletsprojects.com/">Flask</a> for the Backend.  
- <a href="https://palletsprojects.com/p/jinja/">Jinja2</a> for the Templating.

<br>

## Run the website:
Regular web servers can't run Python applications, so a special server type was used(Web Server Gateway Interface 'WSGI') to run Python applications.
The most popular: <a href="http://www.gunicorn.org/">gunicorn</a> ( run on Linux only!!!)

<br>

**To run the website:**

* 1 - install the requirements by
```
pip install requirements.txt
```
* 2 - run the webiste
```
gunicorn main:app
```

<br>

> - **Note: You must be in the same directory of the `main.py` file to run the previous command.**

<br>

Made by Belamiri Zakarya  :wave: [Get in touch!](https://github.com/kakaa2993)
