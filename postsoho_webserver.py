import datetime
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from postsoho_db_setup import Base, PSJobType, PSUser, PSReview, \
     PSTechnology, PSTechnologyMap, \
     PSTag, PSTagMap, \
     PSLanguage, PSLanguageMap, \
     PSAccreditation, PSAccreditationMap, \
     PSCert, PSCertMap, \
     PSBadge, PSBadgeMap, \
     PSCategory, PSCategoryMap

engine = create_engine('sqlite:///postsoho.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def landingPage(): 
    categories = session.query(PSCategory).all()
    job_types = session.query(PSJobType).all()
    users = session.query(PSUser).all()
    for user in users:
    	if datetime.timedelta.total_seconds(datetime.datetime.now()-user.whenUpdated) < 1000:
    		print user.name
    return render_template('landingpage.html', \
    					   categories=categories, \
    					   job_types=job_types, \
    					   users = users)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

