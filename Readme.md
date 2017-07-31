# Logs Analysis
Logs Analysis is a project that utilizes PostgreSQL database and Python3 to query the database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

# Getting Started

## Requirements

- Must have Python3 installed on system
- Must have Vagrant (VM) Installed on system
- Must have PostgreSQL (psql) installed on system

**Note :-** 
If you are on Linux & Mac just run below command with **sudo** to install psql 
> sudo apt install postgresql-client-common    

### Steps To Run The Project

1.  Clone The Repo At [click here](https://github.com/imrshu/Logs-Analysis)
2.	Download newsdata.sql file At [click here](https://drive.google.com/file/d/0B_qzAKxW64G-VFJZLWZ3SHdZUVk/view?usp=sharing)
3.  Copy & Paste newsdata.sql file in project's folder
4.  Take the project's folder to the vagrant directory
5.  Open up the terminal
6.  Run `vagrant up` command to Start your VM Machine
7.  Run `vagrant ssh` command to Log In your VM Machine
8.  Run `cd /vagrant` command to make sure that you are in vagrant folder in VM machine
9.  Change Directory to project's folder that you have pasted in vagrant folder
10. Run `psql -d news -f newsdata.sql` command to connect to the database & load the data
11. Head over to **Views** section to make views in the database
12. Finally Run `python3 app.py` command in terminal to start the application

### Views
```SQL
create view status_error as select date_trunc('day', time) "dates", count(*) as e from log where status= '404 NOT FOUND' group by dates;
```

```SQL
create view requests_sum as select date_trunc('day', time) "dates", count(status) as r from log group by dates;
```


**Note**
- Making Views are compulsory in order to run `app.py` file error free

This Project is a part of FSND udacity.
