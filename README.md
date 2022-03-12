# DRF_poc 
- This poc contains Django Usermanagement functionality in API format.
- just by going through API links and adding data in those APIs , we can do login, logout , change password .



## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* Virtual Environment

### To install virtual environment on your system use:

**bash**
```
pip install virtualenv
```
**or**
```
pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation and Running :

**bash**
```
git clone https://github.com/himanshugupta0158/django_DRF.git
```
- This will clone whole project

```
virtualenv venv 
```   
**or**
```
virtualenv venv -p python3 #if using linux(for python 3 and above)
```
*NOTE : 'venv' is the name of your isolated virtual environment for python.*
```
venv\Scripts\activate # for windows
```
**or**
```
source venv/bin/activate # for linux
```
# install required packages for the project to run
```
pip install django djangorestframework
```

#### If you are using image data in your database model make sure you install 
```
pip install pillow
```
