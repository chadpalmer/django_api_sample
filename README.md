# Django API sample
Sample Django REST api. This simple project uses html5, javascript and css to power the front-end UI while using Django, Django REST framework and Python to power the back end.
#
To get this running locally on your computer, please run the following commands.

First, in the cmd terminal window, cd to the "django_api_sample" project folder that you cloned from github and then run the following command to set up the Python 3 virtual environment.
```
python3 -m venv env
```
Next, activate the new virtual environment by running the following command.
```
source env/bin/activate
```
Next, install libraries and requirements with PIP as follows.
```
pip install -r requirements.txt
```
(NOTE: You might need to adjust your project interpreter setting in whatever app you're using to view the code of this projects as it likely defaults to the system 2.7.x version if you are on a Mac.)

If that is the case, you need to change the project interpreter setting to point to the Python 3 installation in your virtual environment. If you followed the instructions here, the interpreter path will be as follows:
```
/<your_folder_path>/django_api_sample/env/bin/python
```
At this point, you should be ready to run the app locally, but running the following command.
```
python manage.py runserver
```
If you go to the browser of your choice on your computer and copy the URL you see in your cmd window output (likely as follows: http://127.0.0.1:8000/ ), you will see the index page. 
You can play around with the options to see how the UI changes slightly with the choices you make as well as error messages if you don't put a valid integer id in the ID text box under the choose your
axiom radio button.

You can also check out the slightly customized admin at http://127.0.0.1:8000/admin/. You can use the user "admin" and the password "test1234" to play around with your local sqlite3 DB.