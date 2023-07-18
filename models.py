from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'




    # Create Classes for each music genres

# Alternative Songs

class Altsongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    altsong_title = db.Column(db.String(150), nullable=True, default='')
    altartist = db.Column(db.String(150), nullable = True, default = '')
    altalbum = db.Column(db.String(150), nullable = False)
    altyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, altsong_title, altartist, altalbum, altyear, user_token, id = ''):
        self.id = self.set_id()
        self.altsong_title = altsong_title
        self.altartist = altartist
        self.altalbum = altalbum
        self.altyear = altyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.altsong_title} has been added to the database'
    
class AltsongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'altsong_title', 'altartist', 'altalbum', 'altyear']

altsong_schema = AltsongSchema()
altsongs_Schema = AltsongSchema(many=True)






# Blues Songs

class Blusongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    blusong_title = db.Column(db.String(150), nullable=True, default='')
    bluartist = db.Column(db.String(150), nullable = True, default = '')
    blualbum = db.Column(db.String(150), nullable = False)
    bluyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, blusong_title, bluartist, blualbum, bluyear, user_token, id = ''):
        self.id = self.set_id()
        self.blusong_title = blusong_title
        self.bluartist = bluartist
        self.blualbum = blualbum
        self.bluyear = bluyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.blusong_title} has been added to the database'
    
class BlusongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'blusong_title', 'bluartist', 'blualbum', 'bluyear']

blusong_schema = BlusongSchema()
blusongs_Schema = BlusongSchema(many=True)






# Country Songs

class Countrysongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    countrysong_title = db.Column(db.String(150), nullable=True, default='')
    countryartist = db.Column(db.String(150), nullable = True, default = '')
    countryalbum = db.Column(db.String(150), nullable = False)
    countryyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, countrysong_title, countryartist, countryalbum, countryyear, user_token, id = ''):
        self.id = self.set_id()
        self.countrysong_title = countrysong_title
        self.countryartist = countryartist
        self.countryalbum = countryalbum
        self.countryyear = countryyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.countrysong_title} has been added to the database'
    
class CountrysongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'countrysong_title', 'countryartist', 'countryalbum', 'countryyear']

countrysong_schema = CountrysongSchema()
countrysongs_Schema = CountrysongSchema(many=True)






# Hip Hop Songs

class Hiphopsongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    hiphopsong_title = db.Column(db.String(150), nullable=True, default='')
    hiphopartist = db.Column(db.String(150), nullable = True, default = '')
    hiphopalbum = db.Column(db.String(150), nullable = False)
    hiphopyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, hiphopsong_title, hiphopartist, hiphopalbum, hiphopyear, user_token, id = ''):
        self.id = self.set_id()
        self.hiphopsong_title = hiphopsong_title
        self.hiphopartist = hiphopartist
        self.hiphopalbum = hiphopalbum
        self.hiphopyear = hiphopyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.hiphopsong_title} has been added to the database'
    
class HiphopsongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'hiphopsong_title', 'hiphopartist', 'hiphopalbum', 'hiphopyear']

hiphopsong_schema = HiphopsongSchema()
hiphopsongs_Schema = HiphopsongSchema(many=True)






# Heavy Metal Songs

class Metalsongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    metalsong_title = db.Column(db.String(150), nullable=True, default='')
    metalartist = db.Column(db.String(150), nullable = True, default = '')
    metalalbum = db.Column(db.String(150), nullable = False)
    metalyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, metalsong_title, metalartist, metalalbum, metalyear, user_token, id = ''):
        self.id = self.set_id()
        self.metalsong_title = metalsong_title
        self.metalartist = metalartist
        self.metalalbum = metalalbum
        self.metalyear = metalyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.metalsong_title} has been added to the database'
    
class MetalsongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'metalsong_title', 'metalartist', 'metalalbum', 'metalyear']

metalsong_schema = MetalsongSchema()
metalsongs_Schema = MetalsongSchema(many=True)






# R&B Songs

class Rnbsongs(db.Model):
    id = db.Column(db.String, primary_key = True)
    rnbsong_title = db.Column(db.String(150), nullable=True, default='')
    rnbartist = db.Column(db.String(150), nullable = True, default = '')
    rnbalbum = db.Column(db.String(150), nullable = False)
    rnbyear = db.Column(db.String, nullable = True, default = '')      
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, rnbsong_title, rnbartist, rnbalbum, rnbyear, user_token, id = ''):
        self.id = self.set_id()
        self.rnbsong_title = rnbsong_title
        self.rnbartist = rnbartist
        self.rnbalbum = rnbalbum
        self.rnbyear = rnbyear        
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())
   
    def __repr__(self):
        return f'User {self.rnbsong_title} has been added to the database'
    
class RnbsongSchema (ma.Schema):
    class Meta:
        fields = ['id', 'rnbsong_title', 'rnbartist', 'rnbalbum', 'rnbyear']

rnbsong_schema = RnbsongSchema()
rnbsongs_Schema = RnbsongSchema(many=True)
