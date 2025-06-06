

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '849c426b62df4e5a872102602240109'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                

    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run()
