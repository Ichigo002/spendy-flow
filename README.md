# spendy-flow
Database holding all user's expenses, incomes, subscriptions, salaries and everything what is related to cash management. Website is only for quick managing database. All features will be included in the future android app to easily manage it without computer becuase you can sometimes do not have any pc.

## How to setup project?
Be sure you've installed on your machine python3
1. Clone repository
2. In *spendy-flow* directory create new virtual environment: `python -m venv .venv`
3. activate it (depends on your OS. For more info look [here](https://python.land/virtual-environments/virtualenv#Python_venv_activation))
4. run `pip install -r requirements.txt` (If installing *mysqlclient* fails, you should install additional dependencies. On linux install: `python3-devel` and `mysql-devel`)
5. SETUP *MARIA-DB SERVER*. If you hasn't made it yet, you need it to do now.
6. go to directory *project* and run `python manage.py migrate`
7. run `python manage.py runserver` and you did it!

## How to setup *maria-db server*?
1. Install maria-db depending on your OS.
2. Make it active and running.
3. Log into maria-db by terminal.
4. Create new database: `CREATE DATABASE spendy_flow_db;`
5. Create new user: `CREATE USER 'django_spendy'@'localhost' IDENTIFIED BY 'django_spendySECRET';` (you can change password if you need)
6. Grant all privileges to newly created db: `GRANT ALL PRIVILEGES ON spendy_flow_db.* TO 'django_spendy'@'localhost';`
7. Refresh to be sure it worked! `FLUSH PRIVILEGES;`
