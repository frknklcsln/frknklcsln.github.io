from flask import Flask, request, jsonify, render_template
from recommendation import recommend_movies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    title = request.form.get('title')
    recommended_movies = recommend_movies(title)
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
