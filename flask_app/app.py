from flask import Flask, Response, request
from flask import render_template
import csv
from io import StringIO
from crawling_two import crawling_two

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
    
@app.route("/crawl")
def crawl():
    games  = crawling_two()
    search_query = request.args.get('name', '').lower()
    if search_query:
        games = [game for game in games if search_query in game[0].lower()]
        
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Game', 'Alphabet', 'Release Date'])  
    writer.writerows(games)  

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=games.csv"}
    )
    
if __name__ == "__main__":
    app.run(debug=True)