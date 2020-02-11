from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from flask import Flask, jsonify, request
import config

app = Flask(__name__)
app.config.from_object(config)
api = Api(app)

# connect db
sql_connect = "mysql+pymysql://root:password@ip:3306/test"

engine = create_engine(sql_connect)
DBSession = sessionmaker(bind=engine)
# create object base
BaseModel = declarative_base()


#Definition object
class User(BaseModel):
    # tablename
    __tablename__ = "user"
    # Table Structure
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    age = Column(Integer)

#Initialize the database
def init_db():
    BaseModel.metadata.create_all(engine)

#Delete all data tables
def drop_db():
    BaseModel.metadata.drop_all(engine)

@app.route('/users', methods=['GET'])    
def get():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    #  create session:
    session = DBSession()
    # Create a Query query, filter is a where condition, and finally call one () to return the only row, if all () is called to return all rows:
    users = session.query(User).all()
    # Print type and object's name property:
    test = []
    for u in users:
        results = 'id:'+str(u.id),'name:'+str(u.name),'age:'+str(u.age)
        #print (results)
        test.append(results)
    # close session:
    session.close()
    print (test)
    res = results[1]
    resp=jsonify(test)
    resp.status_code=200
    return resp
    return jsonify({'result': result})
    
@app.route('/users/add', methods=['POST'])    
def post():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    input_body = request.get_json()
    name_input = input_body['name']
    age_input = input_body['age']
    # Create a session object, equivalent to a cursor in MySQLdb
    session = DBSession()
    # Create a new User object:
    new_user = User(name=name_input, age=age_input)
    # Add to session:
    session.add(new_user)
    # Submit to database
    session.commit()
    # Close session
    session.close()
    return jsonify({'result': result})

@app.route('/users/delete', methods=['DELETE'])    
def delete():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    input_body = request.get_json()
    id_input = input_body['id']
    # Create Session
    session = DBSession()
    # What data is deleted
    user = session.query(User).filter(User.id == id_input).one()
    session.delete(user)
    # submit data
    session.commit()
    # Close session
    session.close()
    return jsonify({'result': result})
    
@app.route('/users/update', methods=['PUT'])    
def update():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    input_body = request.get_json()
    id_input = input_body['id']
    name_input = input_body['name']
    age_input = input_body['age']
    # Create Session:
    session = DBSession()
    # Can perform multiple data updates
    user = session.query(User).filter(User.id == id_input)
    user.update({User.name: name_input})
    user.update({User.age: age_input})
    # submit data
    session.commit()
    # Close Session
    session.close()
    return jsonify({'result': result})
    
@app.route('/users/patch', methods=['PATCH'])    
def patch():
    result = [{'msg': 'success'}, {'stat': '200 ok'}]
    input_body = request.get_json()
    id_input = input_body['id']
    age_input = input_body['age']
    # Create Session:
    session = DBSession()
    # Can perform multiple data updates
    user = session.query(User).filter(User.id == id_input)
    user.update({User.age: age_input})
    # submit data
    session.commit()
    # Close Session
    session.close()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
