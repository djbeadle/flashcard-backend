"""
This is the entry point to your application. The environment variable FLASK_APP
is set to the name of this file (excluding the extension, .py)
"""

from app import create_app
import os

print('Firing things up')
app = create_app(os.getenv('FLASK_ENV') or 'development')

# Uncomment the following line to run your application in Pythonista for iOS
app.run(host="0.0.0.0", use_reloader=False)
