import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from postsoho_db_setup import Base, PSBadge, PSBadgeMap, PSUser, PSCategory, PSJobType

engine = create_engine('sqlite:///postsoho.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

## Create some users
x = datetime.datetime.now()
users = [PSUser(name = 'John Dow', rate='$125/hr', ratingAverage=4.4, numberOfRatings=9, whenUpdated=x),
         PSUser(name = 'Jane Smith'),
         PSUser(name = 'Michael Jordan')]

for user in users:
    session.add(user)

session.commit()
users = session.query(PSUser).all()

## Create some Badge
badges = [PSBadge(name = 'Awesome'),
          PSBadge(name = 'Super User'),
          PSBadge(name = 'Stinky')]
for badge in badges:
    session.add(badge)
session.commit()
badges = session.query(PSBadge).all()

## Assign some Badge to users
maps = [PSBadgeMap(user_id=users[0].id, badge_id=badges[0].id),
        PSBadgeMap(user_id=users[0].id, badge_id=badges[2].id),
        PSBadgeMap(user_id=users[1].id, badge_id=badges[1].id),
        PSBadgeMap(user_id=users[1].id, badge_id=badges[2].id),
        PSBadgeMap(user_id=users[2].id, badge_id=badges[0].id),
        PSBadgeMap(user_id=users[2].id, badge_id=badges[1].id)]
for this in maps:
    session.add(this)
session.commit()

## Create some categories
cats = [PSCategory(name='Account Management', value='account-management', num=2),
        PSCategory(name='App Development', value='app-development', num=8),
        PSCategory(name='Back End Developer', value='back-end-developer', num=13),
        PSCategory(name='Blogging', value='blogging', num=4),
        PSCategory(name='Content Creator', value='content-creator', num=7),
        PSCategory(name='Data Processing', value='data-processing', num=2),
        PSCategory(name='Estate & Space Advisory', value='estate-space-advisory', num=0),
        PSCategory(name='Executive', value='executive', num=3),
        PSCategory(name='Front End Developer', value='front-end-developer', num=13),
        PSCategory(name='Graphic Design', value='graphic-design', num=10),
        PSCategory(name='Hiring', value='hiring', num=0),
        PSCategory(name='IT Consultant', value='it-consulting', num=5),
        PSCategory(name='Journalist', value='journalist', num=0),
        PSCategory(name='Legal', value='legal', num=0),
        PSCategory(name='Management', value='management', num=5),
        PSCategory(name='Network Engineering', value='network-engineering', num=1),
        PSCategory(name='Operations Management', value='operations-management', num=2),
        PSCategory(name='PC Technician', value='pc-technician', num=2),
        PSCategory(name='Photography', value='photography', num=9),
        PSCategory(name='PR Specialist', value='pr-spcialist', num=0),
        PSCategory(name='Product Management', value='product-management', num=5),
        PSCategory(name='Production Management', value='production-management', num=1),
        PSCategory(name='Quality Checking', value='quality-checking', num=1),
        PSCategory(name='Recruiting', value='recruiting', num=1),
        PSCategory(name='Sales', value='sales', num=0),
        PSCategory(name='Social Media Marketing', value='social-media-marketing', num=3),
        PSCategory(name='System Engineering', value='system-engineering', num=0),
        PSCategory(name='Training', value='training', num=2),
        PSCategory(name='UX/UI', value='ux-ui', num=6),
        PSCategory(name='Video Production', value='video-prodction', num=6),
        PSCategory(name='Web Design', value='web-design', num=12),
        PSCategory(name='Web Development', value='web-development', num=15),
        PSCategory(name='Web Marketing', value='web-marketing', num=4),
        PSCategory(name='Webmaster', value='webmaster', num=8)]

for cat in cats:
    session.add(cat)
session.commit()

## Create some categories
job_types = [PSJobType(name='Freelance', value='freelance'),
        	 PSJobType(name='FT/PT Job', value='ftpt-job'),
        	 PSJobType(name='Gig', value='gig'),
       		 PSJobType(name='Hourly', value='hourly'),
       		 PSJobType(name='Internship', value='internship'),
       		 PSJobType(name='Non Profit', value='non-profit'),
       		 PSJobType(name='Retainer', value='retainer'),
       		 PSJobType(name='Temp', value='temp')]

for jt in job_types:
    session.add(jt)
session.commit()

