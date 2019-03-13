### It is an Log Analysis Project 

# By Jyothi Sri

This web application is a project for the Udacity [Full Stack Nano Degree Course](https://www.udacity.com/course/full-stack
-web-developer-nanodegree--nd004).


### Needs for log analysis project 
	
	* Vagrant and Virtual box we need to install
	* And finally README file for describing about our project in brief to understand our project
	
	
### Log analysis project consists of following files

	* Log_Analysis2.py - where querries are written 
	* views2.sql - where views are created
	* README.md - for describing about our project in brief to understand our project
	* outcomes.txt - where our output is shown
	
	
### Required Skills for developing
	
	1) Python

	2) Vagrant

    3) VirtualBox

    4) Postgresql

		
### Commands for installation 
	
	
	* We should create vagrant file using command `vagrant init ubuntu/xenial64`
	
	* To connect virtual machine by using command `vagrant up`
	
	* To login virtual machine by using command 	`vagrnat ssh`
	
	* Exit directories by using command `cd ..` and again exit `cd ..`
	
	* To move vagrant path by using command `cd /vagrant`
	
	
### Commands for running project

	* We have to open our project folder
	
	* Open command prompt in your project folder
	
	* `vagrant init ubuntu/xenial64` for creating vagrant file 
	
	* `vagrant up` for connecting to virtual machine
	
	* `vagrnat ssh` for loging into virtual machine
	
	* `cd ..` and `cd ..` for exiting directories
	
	* `cd /vagrant` for moving into vagrant path
	
	* For listing out files in our folder by using command `ls`
	
	* `psql` - connect to postgresql database if postgres database is installed
	
	* If not installed use command for installing `sudo apt-get install postgresql`
	
	* If an error occurred like `unable to locate..`
	
	* Run `sudo apt-get update`
	
	* Again run `sudo apt-get install postgresql`
	
	* `sudo su - postgres` for connecting to postgres server
	
	* Connecting to database postgres `psql`
	
	* `\du` for getting users it displays user with postgres
	
	* We need to create user named as vagrant using command `create user vagrant with superuser createrole createdb replication bypassrls;`
	
	* Again run `\du` it displays two users with postgres and vagrant
	
	* And we need create database named with news by using `create database news;`
	
	* It displays ``CREATE DATABASE``
	
	* `\q` for exiting database
	
	* `logout`
	
	* `ls` for displaying list of files
	
	* And we need to copy `newsdata.sql` file to our project folder
	
	* Run `psql -d news -f newsdata.sql` for dumping newsdata.sql into database named with news
	
	* Run `psql -d news -f views2.sql` for dumping views2.sql into database named with news
	
	* And we need to update by using command `sudo apt-get update`
	
	* It asks to install python like 
	
			The program 'python' can be found in the following packages:
			 * python-minimal
			 * python3
			Ask your administrator to install one of them
			
	    so use command for installing `sudo apt-get install python`
	
	* And we need to install pip also by using `sudo apt-get install python-pip`
	
	* When we run our python file after installing above it displays `No module named psycopg2`
	
	* For installing psycopg2 module use `pip install psycopg2`
	
	* Finally run `python Log_Analysis2.py`
	