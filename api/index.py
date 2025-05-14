from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'q-vercel-python.json')
with open(file_path, 'r') as f:
    student_data = json.load(f)

@app.route("/api", methods=["GET"])
def get_student_marks():
    names = request.args.getlist("name")
    marks = []
    for name in names:
        mark = next((item['mark'] for item in student_data if item['name'] == name), None)
        marks.append(mark)
    return jsonify({"marks": marks})
  
if __name__ == '__main__':
    app.run(debug=True)
