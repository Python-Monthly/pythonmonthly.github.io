Title: How To Get Pelican Up And Running
Date: 2016-10-22 22:16
Author: Steve Gregg
Category: General
Tags: blog

We will assume that you already have Python, pip and Git installed and running on your particular OS, if not please do so before completing any of the instructions below.


To get Pelican up and running, you will first need to clone our repository

`$ git clone https://github.com/Python-Monthly/Python-Monthly-Website.git`

Go into the project folder

`$ cd Python-Monthly-Website`

The next step is to create a virtual environment within which to run Pelican. This is optional but highly recommended. If you do not have 'virtualenv' installed, do so by typing the following

`$ pip install virtualenv`

Once installed, run

`$ virtualenv venv`

Activate the newly created virtual environment

`$ source venv/bin/activate`

Now we can install Pelican and Markdown

`$ pip install pelican markdown'

You now have everything you need to test and contribute to our site.
