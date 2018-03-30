import sys
sys.path.insert(0, '/var/www/scpsl_serverchecker/')
from app import app as application, db
db.create_all()
