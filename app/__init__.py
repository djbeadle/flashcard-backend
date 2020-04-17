from flask import Flask, Blueprint
from flask_restful import Api
import sqlite3

try:
  from config import config, DevelopmentConfig, ProductionConfig
except ModuleNotFoundError as e:
  print('')
  print('ERROR: You forgot to make a copy of the "config-example.py" file called "config.py"')
  print('       Your application will NOT work until you do so.')
  print('       (or maybe you tried to run __init__.py instead of myapp.py)')
  print('')

"""
If you have another file in this directory and want to import it you must
prefix the import statement with the directory 'app'.

ex:
from app.db_operations import create_db
"""

def create_app(config_name):
    """Application factory that returns a fully formed instance of the app

    The application context doesn't exist when this file is running, so 
    instead of being able to access values defined in the file config.py 
    the normal way as follows which uses the 'current_app' proxy:
    
    ~~~python
    from flask import current_app
    current_app.config['KEY_NAME']
    ~~~
    
    We have to manually access the config file as follows:

    ~~~python
    from config import config
    config[config_name].KEY_NAME
    ~~~
    
    Args:
      config_name (str): The name of the configuration to use
    
    """

    app = Flask(__name__, static_url_path="/static")
    print(f'Using the {config_name} config.')
    
    db = sqlite3.connect(config[config_name].DB)
    cur = db.cursor()
    
    try:
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                source TEXT,
                image_url TEXT,
                tags TEXT
            );
        """)
        db.commit()
        db.close()
    except Exception as e:
        print(e)
        print("Database already exists!")
    
    # Select the desired config object from FLASK_ENV environment variable
    try:
      app.config.from_object(config[config_name])
      config[config_name].init_app(app)
    except Exception as e:
      print('')
      print('An error occurred initalizing the app. Be sure to set the environment')
      print('variables FLASK_ENV=(development|production) and FLASK_APP=application.py')
      print('')
      raise e
    

    from app.landing import landing_bp
    app.register_blueprint(landing_bp)
    from app.api import api_bp
    app.register_blueprint(api_bp)

    return app
