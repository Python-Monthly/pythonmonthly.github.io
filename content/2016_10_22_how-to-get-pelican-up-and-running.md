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

Now we can install all the required components for the project

`$ pip install -r requirements.txt`

You now have everything you need to test and contribute to our site. We communicate using Slack.

<a class="typeform-share button" href="https://jay400.typeform.com/to/tfYA6n" data-mode="1" target="_blank">Request an invite</a>
<script>(function(){var qs,js,q,s,d=document,gi=d.getElementById,ce=d.createElement,gt=d.getElementsByTagName,id='typef_orm',b='https://s3-eu-west-1.amazonaws.com/share.typeform.com/';if(!gi.call(d,id)){js=ce.call(d,'script');js.id=id;js.src=b+'share.js';q=gt.call(d,'script')[0];q.parentNode.insertBefore(js,q)}id=id+'_';if(!gi.call(d,id)){qs=ce.call(d,'link');qs.rel='stylesheet';qs.id=id;qs.href=b+'share-button.css';s=gt.call(d,'head')[0];s.appendChild(qs,s)}})()</script><br>
