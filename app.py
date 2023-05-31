from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': '1',
    'title': 'Web Dev',
    'location': 'Bengalore, India',
    'salary': 'Rs. 10,000'
  },
  {
    'id': '2',
    'title': 'Data Analyst',
    'location': 'Delhi, India'
  },
  {
    'id': '3',
    'title': 'Data Scientist',
    'location': 'Pune, India',
    'salary': 'Rs. 30,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
