import sae
from django_book import wsgi

import os
import sys 

app_root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(app_root, 'reportlab'))

application = sae.create_wsgi_app(wsgi.application)
