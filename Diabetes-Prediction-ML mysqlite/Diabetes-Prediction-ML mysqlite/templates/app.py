from flask import Flask, jsonify
 app = Flask(name)
 Student = [
 {
 'id': 1,
 'firstName': 'Aditya',
 'lastName': 'Malviya',
 'age': '24'
 },
 {
 'id': 2,
 'firstName': 'Aman',
 'lastName': 'Mehta',
 'age': '25'
 },
 {
 'id': 3,
 'firstName': 'Nuclear',
 'lastName': 'Geeks',
 'age': '26'
 }
 ]
 @app.route('/Student/', methods=['GET'])
    def get_Student():
    return jsonify({'tasks': Student})
 if name == 'main':
   app.run()