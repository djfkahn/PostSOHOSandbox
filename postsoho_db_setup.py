import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, \
						Text, LargeBinary, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

## Set Up jobs type
class PSJobType(Base):
    __tablename__ = 'psjobtype'
    id    = Column(Integer, primary_key=True)
    name  = Column(String(30), nullable=False)
    value = Column(String(30), nullable=False)


class PSUser(Base):
    __tablename__ = 'psuser'
    id                   = Column(Integer, primary_key=True)
    name                 = Column(String(80), nullable=False)
    address              = Column(String(250))
    city                 = Column(String(30))
    state                = Column(String(2))
    email                = Column(String(100), key='email')
##    profilePic           = Column(LargeBinary)
##    coverPic             = Column(LargeBinary)
    description          = Column(Text)
    date_of_birth        = Column(Date)
    ratingAverage        = Column(Float)
    numberOfRatings      = Column(Integer)
    rate                 = Column(String(10))
    
    whenUpdated          = Column(DateTime)
    #profile_Facebook
    #profile_LinkedIn
    #profile_Twitter
    #profile_GooglePlus
    #profile_GitHub
    #profile_Behance
    #profile_Dribble
    #profile_Devianart
    #portfolio


## Set Up one-to-many relashiphip between Users and their reviews
class PSReview(Base):
    __tablename__ = 'psreview'
    id             = Column(Integer, primary_key=True)
    user_id        = Column(Integer, ForeignKey('psuser.id'))
    user           = relationship(PSUser)
    reviewer_name  = Column(String(30))
    reviewer_email = Column(String(100), key='email')
    review_text    = Column(Text)
    review_date    = Column(Date)
    review_rating  = Column(Integer)


## Set Up many-to-many relationship betwen Users and Technologies
class PSTechnology(Base):
    __tablename__ = 'pstechnology'
    id   = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class PSTechnologyMap(Base):
    __tablename__ = 'pstechnologymap'
    id      = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('psuser.id'))
    user    = relationship(PSUser)
    tech_id = Column(Integer, ForeignKey('pstechnology.id'))
    tech    = relationship(PSTechnology)


## Set Up many-to-many relationship betwen Users and Tags
class PSTag(Base):
    __tablename__ = 'pstag'
    id   = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class PSTagMap(Base):
    __tablename__ = 'pstagmap'
    id      = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('psuser.id'))
    user    = relationship(PSUser)
    tag_id  = Column(Integer, ForeignKey('pstag.id'))
    tag     = relationship(PSTag)


## Set Up many-to-many relationship betwen Users and Languages
class PSLanguage(Base):
    __tablename__ = 'pslanguage'
    id   = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class PSLanguageMap(Base):
    __tablename__ = 'pslanguagemap'
    id          = Column(Integer, primary_key=True)
    user_id     = Column(Integer, ForeignKey('psuser.id'))
    user        = relationship(PSUser)
    language_id = Column(Integer, ForeignKey('pslanguage.id'))
    language    = relationship(PSLanguage)


## Set Up many-to-many relationship betwen Users and Accreditations
class PSAccreditation(Base):
    __tablename__ = 'psaccreditation'
    id   = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class PSAccreditationMap(Base):
    __tablename__ = 'psaccreditationmap'
    id               = Column(Integer, primary_key=True)
    user_id          = Column(Integer, ForeignKey('psuser.id'))
    user             = relationship(PSUser)
    accreditation_id = Column(Integer, ForeignKey('psaccreditation.id'))
    accreditation    = relationship(PSAccreditation)


## Set Up many-to-many relationship betwen Users and Certifications
class PSCert(Base):
    __tablename__ = 'pscert'
    id        = Column(Integer, primary_key=True)
    name      = Column(String(30), nullable=False)
    authority = Column(String(30), nullable=False)

class PSCertMap(Base):
    __tablename__ = 'pscertmap'
    id       = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('psuser.id'))
    user     = relationship(PSUser)
    cert_id  = Column(Integer, ForeignKey('pscert.id'))
    cert     = relationship(PSCert)


## Set Up many-to-many relationship betwen Users and Badges
class PSBadge(Base):
    __tablename__ = 'psbadge'
    id   = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class PSBadgeMap(Base):
    __tablename__ = 'psbadgemap'
    id       = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('psuser.id'))
    user     = relationship(PSUser)
    badge_id = Column(Integer, ForeignKey('psbadge.id'))
    badge    = relationship(PSBadge)


## Set Up many-to-many relationship betwen Users and Categories
class PSCategory(Base):
    __tablename__ = 'pscategory'
    id    = Column(Integer, primary_key=True)
    name  = Column(String(30), nullable=False)
    value = Column(String(30), nullable=False)
    num   = Column(Integer)

class PSCategoryMap(Base):
    __tablename__ = 'psCategorymap'
    id       = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('psuser.id'))
    user     = relationship(PSUser)
    badge_id = Column(Integer, ForeignKey('pscategory.id'))
    badge    = relationship(PSCategory)


engine = create_engine('sqlite:///postsoho.db')
Base.metadata.create_all(engine)
