# python_geocoder

This is a Python Flask application that let's you upload a CSV file with an address column. 
It then gets the latitude and longitude of all addresses in the file and adds the values in new columns on the same file
Then it makes the file available for download (it's supposed to, I might implement this piece later. 
Right now it only just display the CSV as a table on the page)

<h3>Libraries used</h3>
<ul>
  <li>Flask</li>
  <li>pandas</li>
  <li>geopy</li>
</ul>

<h3>How to run...</h3>
<ul>
  <li>From the root folder run: <em>python3 app.py</em> </li>
  <li>Open your browser and go to http://127.0.0.1:5000/ </li>
</ul>
