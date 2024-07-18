
from flask import Flask, render_template, request

# Sample data for testing (replace with API integration)
transport_options = [
    {
        "type": "train",
        "origin": "New York City",
        "destination": "Washington, D.C.",
        "travel_time": "2 hours 30 minutes",
        "cost": 40
    },
    {
        "type": "bus",
        "origin": "Los Angeles",
        "destination": "San Francisco",
        "travel_time": "6 hours",
        "cost": 30
    },
    {
        "type": "flight",
        "origin": "Chicago",
        "destination": "Denver",
        "travel_time": "2 hours",
        "cost": 80
    },
    # Include donkey, ferry, and bike options here
]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        travel_dates = request.form.get("travel-dates")
        transport_types = request.form.getlist("transport-types")
        
        # Filter transport options based on user selections
        itinerary = []
        for option in transport_options:
            if option["type"] in transport_types and option["origin"] == origin and option["destination"] == destination:
                itinerary.append(option)
                
        return render_template("results.html", itinerary=itinerary)
    else:
        return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)
