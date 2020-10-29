# Week 9 Lab — APIs with Flask

## 0. Get the flask web server running!

1. Make sure you have flask installed into your class conda environment:
  `$ conda install -n musa509week6 flask`
2. Activate your class environment
  `$ conda activate musa509week6`
3. Put the Mapbox credentials into the directory. Download here: <https://canvas.upenn.edu/courses/1533813/files/90068242/download?download_frd=1>.
3. Start up the Flask server
  `$ python lab_app.py`
4. Open up `http://127.0.0.1:5000/` in your browser

## 1. Welcome someone and tell them the time

Using the `/<string:name>/` syntax, welcome someone when they load the page and tell them the time.

You can get the current time with the following code. It will format it in a human readable format. Read more about `datetime` formats in [`datetime` documentation](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior).

```python
from datetime import datetime
curr_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
```

**Write your answer in the `lab_app.py`.**

If there are syntax errors in your code before you save it, your webserver may crash. Just start it up again with `$ python lab_app.py`

## 2. Let's add some HTML bling to the response

Add more styling to your HTML output.

Here are some HTML tips:
* Put text between `<b>your text here</b>` tags to make things bold
* Put text between `<h1>your text here</h1>` to make a big header
* To color text, use this: `<span style='color: #990000;'>your text here</span>`
* Put text blocks between `<p>...</p>` tags to create separate paragraphs/blocks.
* More tips here: <https://www.w3schools.com/html/html_styles.asp>

**Write your answer in the `lab_app.py`.**

## 3. Static Map Generation

Let's give the user a map for their location. Let's assume they know their lng/lat. E.g., Meyerson Hall's lng/lat is: `(-75.1927637, 39.9522314)`.

In a new endpoint called `/map`, parse `lng` and `lat` query strings and fill in the function. Finally, return a webpage that has the map and a nice message for the user.


## 4. Turn an address into a static map

1. Use the Mapbox geocoding API to get a lng/lat for an address
2. Use the function for \#3 to create a map from this
