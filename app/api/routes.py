from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Altsongs, altsong_schema, altsongs_Schema, Blusongs, blusong_schema, blusongs_Schema, Countrysongs, countrysong_schema, countrysongs_Schema
from models import Hiphopsongs, hiphopsong_schema, hiphopsongs_Schema, Metalsongs, metalsong_schema, metalsongs_Schema, Rnbsongs, rnbsong_schema, rnbsongs_Schema

api = Blueprint( 'api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return {'digital': 'music'}


# Alternative Songs
# Create Altsong
@api.route('/altsongs',methods=['POST'])
@token_required
def create_altsong(current_user_token):
    altsong_title = request.json['altsong_title']
    altartist = request.json  ['altartist']
    altalbum = request.json['altalbum']
    altyear = request.json['altyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    altsong = Altsongs (altsong_title, altartist, altalbum, altyear, user_token = user_token)

    db.session.add(altsong)
    db.session.commit()

    response = altsong_schema.dump(altsong)
    return jsonify(response)

# Get all Altsongs
@api.route('/altsongs', methods = ['GET'])
@token_required
def get_altsongs(current_user_token):
    a_user = current_user_token.token
    altsong = Altsongs.query.filter_by(user_token = a_user).all()
    response = altsongs_Schema.dump(altsong)
    return jsonify(response)

# Get single Altsong
@api.route('/altsongs/<id>', methods = ['GET'])
@token_required
def get_single_altsong(current_user_token, id):
    altsong = Altsongs.query.get(id)
    response = altsong_schema.dump(altsong)
    return jsonify(response)

# Update Altsongs
@api.route('/altsongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_altsong(current_user_token, id):
    altsong = Altsongs.query.get(id)
    altsong.altsong_title = request.json['altsong_title']
    altsong.altartist = request.json['altartist']
    altsong.altalbum = request.json['altalbum']
    altsong.altyear = request.json ['altyear']
    altsong.user_token = current_user_token.token
    db.session.commit()
    response = altsong_schema.dump(altsong)
    return jsonify(response)
    
# Delete Altsong
@api.route('/altsongs/<id>', methods = ['DELETE'])
@token_required
def delete_altsong(current_user_token, id):
    altsong = Altsongs.query.get(id)
    db.session.delete(altsong)
    db.session.commit()
    response = altsong_schema.dump(altsong)
    return jsonify(response)






# Blues Songs
# Create Blusong
@api.route('/blusongs',methods=['POST'])
@token_required
def create_blusong(current_user_token):
    blusong_title = request.json['blusong_title']
    bluartist = request.json  ['bluartist']
    blualbum = request.json['blualbum']
    bluyear = request.json['bluyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    blusong = Blusongs (blusong_title, bluartist, blualbum, bluyear, user_token = user_token)

    db.session.add(blusong)
    db.session.commit()

    response = blusong_schema.dump(blusong)
    return jsonify(response)

# Get all BLusongs
@api.route('/blusongs', methods = ['GET'])
@token_required
def get_blusongs(current_user_token):
    a_user = current_user_token.token
    blusong = Blusongs.query.filter_by(user_token = a_user).all()
    response = blusongs_Schema.dump(blusong)
    return jsonify(response)

# Get single Blusong
@api.route('/blusongs/<id>', methods = ['GET'])
@token_required
def get_single_blusong(current_user_token, id):
    blusong = Blusongs.query.get(id)
    response = blusong_schema.dump(blusong)
    return jsonify(response)

# Update Blusongs
@api.route('/blusongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_blusong(current_user_token, id):
    blusong = Blusongs.query.get(id)
    blusong.blusong_title = request.json['blusong_title']
    blusong.bluartist = request.json['bluartist']
    blusong.blualbum = request.json['blualbum']
    blusong.bluyear = request.json ['bluyear']
    blusong.user_token = current_user_token.token
    db.session.commit()
    response = blusong_schema.dump(blusong)
    return jsonify(response)
    
# Delete Blusong
@api.route('/blusongs/<id>', methods = ['DELETE'])
@token_required
def delete_blusong(current_user_token, id):
    blusong = Blusongs.query.get(id)
    db.session.delete(blusong)
    db.session.commit()
    response = blusong_schema.dump(blusong)
    return jsonify(response)






# Country Songs
# Create Countrysong
@api.route('/countrysongs',methods=['POST'])
@token_required
def create_countrysong(current_user_token):
    countrysong_title = request.json['countrysong_title']
    countryartist = request.json  ['countryartist']
    countryalbum = request.json['countryalbum']
    countryyear = request.json['countryyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    countrysong = Countrysongs (countrysong_title, countryartist, countryalbum, countryyear, user_token = user_token)

    db.session.add(countrysong)
    db.session.commit()

    response = countrysong_schema.dump(countrysong)
    return jsonify(response)

# Get all Country songs
@api.route('/countrysongs', methods = ['GET'])
@token_required
def get_countrysongs(current_user_token):
    a_user = current_user_token.token
    countrysong = Countrysongs.query.filter_by(user_token = a_user).all()
    response = countrysongs_Schema.dump(countrysong)
    return jsonify(response)

# Get single Country song
@api.route('/countrysongs/<id>', methods = ['GET'])
@token_required
def get_single_countrysong(current_user_token, id):
    countrysong = Countrysongs.query.get(id)
    response = countrysong_schema.dump(countrysong)
    return jsonify(response)

# Update Country songs
@api.route('/countrysongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_countrysong(current_user_token, id):
    countrysong = Countrysongs.query.get(id)
    countrysong.countrysong_title = request.json['countrysong_title']
    countrysong.countryartist = request.json['countryartist']
    countrysong.countryalbum = request.json['countryalbum']
    countrysong.countryyear = request.json ['countryyear']
    countrysong.user_token = current_user_token.token
    db.session.commit()
    response = countrysong_schema.dump(countrysong)
    return jsonify(response)
    
# Delete Country song
@api.route('/countrysongs/<id>', methods = ['DELETE'])
@token_required
def delete_countrysong(current_user_token, id):
    countrysong = Countrysongs.query.get(id)
    db.session.delete(countrysong)
    db.session.commit()
    response = countrysong_schema.dump(countrysong)
    return jsonify(response)






# Hip Hop Songs
# Create Hiphopsong
@api.route('/hiphopsongs',methods=['POST'])
@token_required
def create_hiphopsong(current_user_token):
    hiphopsong_title = request.json['hiphopsong_title']
    hiphopartist = request.json  ['hiphopartist']
    hiphopalbum = request.json['hiphopalbum']
    hiphopyear = request.json['hiphopyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    hiphopsong = Hiphopsongs (hiphopsong_title, hiphopartist, hiphopalbum, hiphopyear, user_token = user_token)

    db.session.add(hiphopsong)
    db.session.commit()

    response = hiphopsong_schema.dump(hiphopsong)
    return jsonify(response)

# Get all Hip Hop songs
@api.route('/hiphopsongs', methods = ['GET'])
@token_required
def get_hiphopsongs(current_user_token):
    a_user = current_user_token.token
    hiphopsong = Hiphopsongs.query.filter_by(user_token = a_user).all()
    response = hiphopsongs_Schema.dump(hiphopsong)
    return jsonify(response)

# Get single Hip Hop song
@api.route('/hiphopsongs/<id>', methods = ['GET'])
@token_required
def get_single_hiphopsong(current_user_token, id):
    hiphopsong = Hiphopsongs.query.get(id)
    response = hiphopsong_schema.dump(hiphopsong)
    return jsonify(response)

# Update Hip Hop songs
@api.route('/hiphopsongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_hiphopsong(current_user_token, id):
    hiphopsong = Hiphopsongs.query.get(id)
    hiphopsong.hiphopsong_title = request.json['hiphopsong_title']
    hiphopsong.hiphopartist = request.json['hiphopartist']
    hiphopsong.hiphopalbum = request.json['hiphopalbum']
    hiphopsong.hiphopyear = request.json ['hiphopyear']
    hiphopsong.user_token = current_user_token.token
    db.session.commit()
    response = hiphopsong_schema.dump(hiphopsong)
    return jsonify(response)
    
# Delete Hip Hop song
@api.route('/hiphopsongs/<id>', methods = ['DELETE'])
@token_required
def delete_hiphopsong(current_user_token, id):
    hiphopsong = Hiphopsongs.query.get(id)
    db.session.delete(hiphopsong)
    db.session.commit()
    response = hiphopsong_schema.dump(hiphopsong)
    return jsonify(response)






# Heavy Metal Songs
# Create Metalsong
@api.route('/metalsongs',methods=['POST'])
@token_required
def create_metalsong(current_user_token):
    metalsong_title = request.json['metalsong_title']
    metalartist = request.json  ['metalartist']
    metalalbum = request.json['metalalbum']
    metalyear = request.json['metalyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    metalsong = Metalsongs (metalsong_title, metalartist, metalalbum, metalyear, user_token = user_token)

    db.session.add(metalsong)
    db.session.commit()

    response = metalsong_schema.dump(metalsong)
    return jsonify(response)

# Get all Metal songs
@api.route('/metalsongs', methods = ['GET'])
@token_required
def get_metalsongs(current_user_token):
    a_user = current_user_token.token
    metalsong = Metalsongs.query.filter_by(user_token = a_user).all()
    response = metalsongs_Schema.dump(metalsong)
    return jsonify(response)

# Get single Metalsong
@api.route('/metalsongs/<id>', methods = ['GET'])
@token_required
def get_single_metalsong(current_user_token, id):
    metalsong = Metalsongs.query.get(id)
    response = metalsong_schema.dump(metalsong)
    return jsonify(response)

# Update Metalsongs
@api.route('/metalsongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_metalsong(current_user_token, id):
    metalsong = Metalsongs.query.get(id)
    metalsong.metalsong_title = request.json['metalsong_title']
    metalsong.metalartist = request.json['metalartist']
    metalsong.metalalbum = request.json['metalalbum']
    metalsong.metalyear = request.json ['metalyear']
    metalsong.user_token = current_user_token.token
    db.session.commit()
    response = metalsong_schema.dump(metalsong)
    return jsonify(response)
    
# Delete Metalsong
@api.route('/metalsongs/<id>', methods = ['DELETE'])
@token_required
def delete_metalsong(current_user_token, id):
    metalsong = Metalsongs.query.get(id)
    db.session.delete(metalsong)
    db.session.commit()
    response = metalsong_schema.dump(metalsong)
    return jsonify(response)






# R&B Songs
# Create Rnbsong
@api.route('/rnbsongs',methods=['POST'])
@token_required
def create_rnbsong(current_user_token):
    rnbsong_title = request.json['rnbsong_title']
    rnbartist = request.json  ['rnbartist']
    rnbalbum = request.json['rnbalbum']
    rnbyear = request.json['rnbyear']   
    user_token = current_user_token.token

    print (f'BIG TESTER: {current_user_token.token}')

    rnbsong = Rnbsongs (rnbsong_title, rnbartist, rnbalbum, rnbyear, user_token = user_token)

    db.session.add(rnbsong)
    db.session.commit()

    response = rnbsong_schema.dump(rnbsong)
    return jsonify(response)

# Get all Rnbsongs
@api.route('/rnbsongs', methods = ['GET'])
@token_required
def get_rnbsongs(current_user_token):
    a_user = current_user_token.token
    rnbsong = Rnbsongs.query.filter_by(user_token = a_user).all()
    response = rnbsongs_Schema.dump(rnbsong)
    return jsonify(response)

# Get single Rnbsong
@api.route('/rnbsongs/<id>', methods = ['GET'])
@token_required
def get_single_rnbsong(current_user_token, id):
    rnbsong = Rnbsongs.query.get(id)
    response = rnbsong_schema.dump(rnbsong)
    return jsonify(response)

# Update Rnbsongs
@api.route('/rnbsongs/<id>', methods = ['POST', 'PUT'])
@token_required
def update_rnbsong(current_user_token, id):
    rnbsong = Rnbsongs.query.get(id)
    rnbsong.rnbsong_title = request.json['rnbsong_title']
    rnbsong.rnbartist = request.json['rnbartist']
    rnbsong.rnbalbum = request.json['rnbalbum']
    rnbsong.rnbyear = request.json ['rnbyear']
    rnbsong.user_token = current_user_token.token
    db.session.commit()
    response = rnbsong_schema.dump(rnbsong)
    return jsonify(response)
    
# Delete Rnbsong
@api.route('/rnbsongs/<id>', methods = ['DELETE'])
@token_required
def delete_rnbsong(current_user_token, id):
    rnbsong = Rnbsongs.query.get(id)
    db.session.delete(rnbsong)
    db.session.commit()
    response = rnbsong_schema.dump(rnbsong)
    return jsonify(response)