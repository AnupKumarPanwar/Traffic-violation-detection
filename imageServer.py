from flask import Flask, send_file

app = Flask(__name__)

@app.route('/get_image/<name>')
def get_image(name):
	filename='./uploads/'+name
	return send_file(filename, mimetype='image/jpeg')

if __name__ == '__main__':
   app.run(debug = True, port=5001)