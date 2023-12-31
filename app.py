from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location':'Bangulur, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location':'Dehli, India',
    'salary': 'Rs. 1,50,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location':'Sans Fransco, USA',
    'salary': 'Rs. $120,000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location':'Remote',
    
  }
]

@app.route("/")
def Hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Jovian')

@app.route("/api/json")
def list_jobs():
  return jsonify(JOBS)


if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)