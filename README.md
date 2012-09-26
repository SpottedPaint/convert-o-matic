Convert-o-matic
===============

This is a silly test project because I wanted to learn some python so this is really my hello world in python. Although I would like to live in world where this was useful.

Its built using **Flask** http://flask.pocoo.org/ . 
The passenger_wsgi.py is built to work on dreamhost with a virtualenv but guess you could tweak to work wherever if you know what your doing.

If you have any issues with hosting python/flask on dreamhost you can check out there wiki entry http://wiki.dreamhost.com/Flask thats what I did. My main issues were with python paths though :) 

It also uses the very super duper SQLite.

You can see this working in whatever state its in here at http://convert-o-matic.adamwilson.info/

- It uses '%(thing)' % {'thing':value} rather than .format() because the version of python online is 2.5

The folder structure goes like this 
/flask_env
	- all this stuff
	- log.db // the database
	- errors.log
	/tmp
	 	- restart.txt
	
If you want to restart/refresh you can do touch tmp/restart.txt

<pre>
				  .    .          
				 /_\ .-| .-. .-.-.
				'   '`-'-`-`-' ' '
</pre>