# Python Recipe Scraper

This is my first web scraping project. The goal is to scrape random recipes within given categories on allrecipes.com and email them to me at the start of each week.

## Initial Features

* Crawler will navigate to specific category pages and randomly pick a certain number of recipes from each category and format in JSON
* Initially will just grab title, ingredients, and directions (as well as yield and calories per serving)
* JSON will be parsed into an email for weekly sending

## Ideas for Future

I would like to eventually add the following features:
* Create shopping lists based on ingredients in recipes
* Run on local server scheduled with cron

More to come... 
