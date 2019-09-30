from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PSUser, PSBadges

engine = create_engine('sqlite:///postsoho.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

