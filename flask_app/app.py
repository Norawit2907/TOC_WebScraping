from flask import Flask, Response, request
from flask import render_template
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
        
    game_list = [{'game': game[0], 'alphabet': game[1], 'release_date': game[2]} for game in games]
    
    return game_list
    
if __name__ == "__main__":
    app.run(debug=True)
