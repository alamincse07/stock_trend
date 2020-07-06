
```javascript
cd YOUR_PROJECT_DIRECTORY_PATH/

virtualenv --no-site-packages env
(sometimes, you need to specify python version depending on the os..as --python=python3) 

source env/bin/activate

pip install -r requirements.txt

export FLASK_APP=app

export FLASK_ENV=development # enables debug mode

python3 app.py 

To run in Gunicorn, gunicorn -b:8080 app:app --log-level debug

You can use the POSTMAN collection to run all the tests, or use a CURL example at the bottom of this document.
```
