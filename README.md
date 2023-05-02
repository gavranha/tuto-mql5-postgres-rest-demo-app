# Python Flask app

This is a very basic demo app implementing a REST API. It is a companion to a tutorial that helps in setting up a dev environment for Postgresql as the source database for an Expert Advisor wrote in MQL5.

Thus, it is not a real app. It is just a functional REST interface built upon the Flask framework. Its purpose is to help you test database connection, database initialization, and perform some CRUD operations.

## How to use this app
It is highly recommended that you use a Python Virtual Environment to avoid messing with your system Python installation. But it is optional.

In this DIR run

```
pip install -r requirements.txt
```

Then

```
flask --app demoapp run --debug
```

This command should start the development server and the app will be ready to receive requests on the configured REST endpoints.

Do not forget to **change the host on db.py** according to your environment.

## Development Help Scripts

Please take a look at the /dev_help_scripts dir. There you will find a bunch of Python scripts like:

*psycopg-connect* to test the connection

*insert_accs* and *insert_deals* to insert 'accounts' and 'deals'

*get_accs* to get 'accounts'

*accs.json* and *deals.json* to help in checking the returning json string format


All of them should help you with troubleshooting if any tutorial step does not work well as expected.

It is worthy noting that you can write this demo REST interface in any language you are more familiar with. I chose Python because I'm used to it and also because Python is already installed in the default WSL/Ubuntu.

The focus of the tutorial is the MQL5 code.