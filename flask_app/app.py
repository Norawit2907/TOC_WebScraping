from flask import Flask, Response, request, jsonify
from flask import render_template
from crawling_two import crawling_two
from io import StringIO
import csv

app = Flask(__name__)
games = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/getcsv")
def getCSV():
    global games
    if not games:
        return 'Unauthorized' , 401
    search_query = request.args.get('name', '').lower()
    if search_query:
        search = [game for game in games if search_query in game[0].lower()]  
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Game', 'Release Date', 'Picture Link'])  
        writer.writerows(search)  

        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-disposition":
                    "attachment; filename=games.csv"}
        ) 
    else:
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Game', 'Release Date', 'Picture Link'])  
        writer.writerows(games)  

        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-disposition":
                    "attachment; filename=games.csv"}
        )

@app.route("/crawl")
def crawl():
    global games
    games  = crawling_two()
    search_query = request.args.get('name', '').lower()
    if search_query:
        search = [game for game in games if search_query in game[0].lower()]
        game_list = [{'game': game[0], 'release_date': game[1], 'pic_link': game[2]} for game in search]    
        return jsonify({'game': game_list, 'search_name': search_query})
    else:
        game_list = [{'game': game[0], 'release_date': game[1], 'pic_link': game[2]} for game in games]    
        return jsonify({'game': game_list, 'search_name': search_query})

  
if __name__ == "__main__":
    app.run(debug=True)