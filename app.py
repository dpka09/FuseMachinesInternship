from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:asad1234@127.0.0.1:5432/postgres'
db = SQLAlchemy(app)


@app.route('/')
def start():
    return "Welcome to my page"

class Info(db.Model):
    __tablename__="info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    address = db.Column(db.String(40))
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer)

    def create(self):
        db.session.add(self)                       
        db.session.commit()                            #adding data to database
        return self
    
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone
    
    def __repr__(self):
        return '' % self.id

db.create_all()  ##to create table

class InfoSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Info
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=True)
    age = fields.Number(required=True)
    phone = fields.Number(required=True)      

#DESIGNING ENDPOINTS FOR CRUD
#GET Operation

@app.route('/Info', methods=['GET'])
def index():
    get_info = Info.query.all()   #in form of list 
    Info_schema = InfoSchema(many=True)    #json to object viveversa
    info = Info_schema.dump(get_info)
    return make_response(jsonify({ "info":info}))


#POST Operation

@app.route('/Info', methods = ['POST'])
def create_info():
    data = request.get_json()
    Info_schema = InfoSchema()
    info = Info_schema.load(data)    ##json to object
    result = Info_schema.dump(info.create())
    return make_response(jsonify({"info": result}),200)

#UPDATE Operation

@app.route('/Info/<id>', methods = ['PUT'])
def update_Info_by_id(id):
    data = request.get_json()
    get_info = Info.query.get(id)
    if data.get('name'):
        get_info.name = data['name']
    if data.get('address'):
        get_info.address = data['address']
    if data.get('age'):
        get_info.age = data['age']
    if data.get('phone'):
        get_info.phone= data['phone']    
    db.session.add(get_info)
    db.session.commit()
    Info_schema = InfoSchema()
    infos = Info_schema.dump(get_info)
    return make_response(jsonify({"info": infos}))

#DELETE Operation

@app.route('/Info/<id>', methods = ['DELETE'])
def delete_Info_by_id(id):
    get_info = Info.query.get(id)
    db.session.delete(get_info)
    db.session.commit()
    return make_response("",204)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
