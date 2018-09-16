## Movies Trailer Website
Webpage for Udacity Web Full-stack Nanodegree created by Valesca Fortunato

## Install

Make sure you have Python v2.7 installed on your computer (if you don't, [here's the link](https://www.python.org/downloads/) to download it). You must also install the [Flkask Python Package](http://flask.pocoo.org/) to run this program. To do so, follow these steps:

1. Run command promt (as admin)
2. Navigate to the directory that holds your Python scripts. For example:

    ```
    cd C:\Python27\Scripts
    ```
    
3. Type the following into command prompt:

    ```
    pip install flask
    ```
    
Then open the entertainment_center.py file in IDLE and click Run -> Run Module (or press F5)

To run the Flask API in our Windows environment, I recommended [this guide](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/). 

## Components
- media.py: contains the Movie Class
- entertainment_center.py: contains the script which initializes the movie array and opens the webpage
- fresh_tomatoes.py: library file which contains code for generating a movie trailer page

## API Resources
The API is version 1.0 and return a JSON with the movies title, storyline, poster and URL's trailer

GET /api/v1/

## License
This project was created by [Valesca Fortunato](http://www.github.com/valescaf).

Licensing terms for this project can be found in the [license](https://github.com/valescaf/movie_trailer_python_udacity/blob/master/LICENSE) file included in this repo.
