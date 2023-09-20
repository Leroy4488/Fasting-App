from flask import Flask, request
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


def is_valid_time(time):
    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False


@app.route("/meal-time", methods=["POST"])
def meal_time():
    time = request.form.get("time")  # Expecting time as "HH:MM"
    if time == "24:00":
        time = "00:00"
        today = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    elif is_valid_time(time):
        today = datetime.now().strftime("%Y-%m-%d")
    else:
        return "Not Valid"

    last_meal_time = f"{today} {time}:00"  # Constructing full datetime string

    fasting_window = 16  # Fasting schedule

    # Calls function
    next_meal_time = calculate_next_meal(last_meal_time, fasting_window)

    # Format output
    next_meal_date = datetime.strptime(next_meal_time, "%Y-%m-%d %H:%M:%S").date()
    today_date = datetime.now().date()
    when = "Today: " if next_meal_date == today_date else "Tomorrow: "
    next_meal_hour = datetime.strptime(next_meal_time, "%Y-%m-%d %H:%M:%S").strftime(
        "%H:%M"
    )

    return f"{when} {next_meal_hour}"


def calculate_next_meal(last_meal_time, fasting_window):
    last_meal_datetime = datetime.strptime(last_meal_time, "%Y-%m-%d %H:%M:%S")
    next_meal_datetime = last_meal_datetime + timedelta(hours=fasting_window)
    next_meal_time = datetime.strftime(next_meal_datetime, "%Y-%m-%d %H:%M:%S")
    return next_meal_time


if __name__ == "__main__":
    app.run(debug=True)
