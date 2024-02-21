from flask import Flask, render_template, request, redirect
import requests
import datetime

date = datetime.datetime.now()
today = date.strftime("%d %B %Y")
year = date.strftime("%Y")
app = Flask(__name__)
URL = "https://newsapi.org/v2/everything?q="
API_KEY = "9c3b907e3b7f474e856709302ed7f8f1"


@app.route('/search', methods=["GET", "POST"])
def search_news():
    if request.method == "POST":
        query = request.form.get('search')
        response = requests.get(f"{URL}{query}&apiKey={API_KEY}")
        data = response.json()
        send_data = data["articles"]
        return render_template("index.html", data=send_data, date=today, year=year)
    return redirect("/")

@app.route('/')
def home():
    response = requests.get(f"{URL}India&apiKey={API_KEY}")
    data = response.json()
    len_of_data = len(data["articles"])
    send_data = data["articles"]
    return render_template("index.html", data=send_data, lenData=len_of_data, date=today, year=year)

if __name__ == '__main__':
    app.run(debug=True)