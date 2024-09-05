from flask import Flask, Response
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/getcsv")
def getCSV():
    csv = '1,2,3,4,5,6'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})
    

if __name__ == "__main__":
    app.run(debug=True)
