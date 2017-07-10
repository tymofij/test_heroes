# Test 'A Tour of Heroes'

This is a tutorial on creating Selenium/Python tests.
Slides: **[Testing front-end applications with Python](Front-end_Testing.pdf)**

We will be testing Angular's [A Tour of Heroes](https://www.npmjs.com/package/angular2-tour-of-heroes)

### Download and run demo app
```
git clone https://github.com/johnpapa/angular2-tour-of-heroes.git toh
cd toh
npm i
npm start
```
### Install requirements and drivers
```
pip install -r requirements.txt
```
[Install Firefox Webdriver](http://selenium-python.readthedocs.io/installation.html#drivers)

### Run tests
```
pytest ugly.py
```
1. ugly.py
2. ugly_implicit_waits.py
3. using_objects.py
4. two_pages.py
