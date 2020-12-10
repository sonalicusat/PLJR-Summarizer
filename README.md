# PLJR-Summarizer

To run this project first you need to download pip and django. 
# Install PIP on Windows
Open a command prompt and execute **easy_install pip**. This will install pip on your system. This command will work if you have successfully installed Setuptools.

Alternatively, go to http://www.pip-installer.org/en/latest/installing.html for installing/upgrading instructions.

# Install Django on Windows
Django can be installed easily using pip.

In the command prompt, execute the following command: **pip install django** or **python -m pip install django. This will download and install Django.

After the installation has completed, you can verify your Django installation by executing **django-admin --version** or **python -m django --version** in the command prompt.
In Django 1.7, a .exe has been introduced, so just use **django-admin** in place of **django-admin.py** in the command prompt.

***Do not install multiple version of python if you are a beginner try to create a virtual enviornment or you can use anaconda but use anaconda prompt instead of command prompt.***

# Creating a project in Windows
If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, cd into a directory where you’d like to store your code, then run the following command: **django-admin startproject Summarizer**.
This will create a Summarizer directory in your current directory. If it didn’t work, see [Problems running django-admin](https://docs.djangoproject.com/en/3.1/faq/troubleshooting/#troubleshooting-django-admin).

# The development server
Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands: **...\> py manage.py runserver**
You’ll see the following output on the command line:

**Performing system checks...**

**System check identified no issues (0 silenced).**

**You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.**
**December 08, 2020 - 15:50:53**

**Django version 3.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C**

You’ve started the Django development server, a lightweight Web server written purely in Python.

Now’s a good time to note: don’t use this server in anything resembling a production environment. It’s intended only for use while developing.

Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

***Download the codes of this repository or colon it.***

# Copy folders
Copy static and template folder inside the Sumaarizer folder you have created. Replace settings.py, views.py and urls.py which will be in Summarizer folder of Summarizer folder. 

***Now you are raedy to go, you can stop the pervious server by Ctrl + C***

Start the devoplment server again and project should work fine.

I have added all the comments in html and views.py so you can do changes as required. 


