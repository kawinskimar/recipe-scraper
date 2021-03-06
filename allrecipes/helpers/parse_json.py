#! python

"""This script takes a json file generated by allrecipes scraper and writes an html file
to be picked up by another script and emailed."""

import json

def write_html_files(json_dict, file_path):
    """Funciton takes a dictionary with json data and writes html file
    to be picked up by email script"""

    length = json_dict.__len__()

    for i in range(0, length):
        f = open(file_path + json_dict[i]['title'][0] + '.html', 'w')

        f.write('<html>')
        f.write('<head></head>')
        f.write('<body>')
        f.write('<h1>' + json_dict[i]['title'][0] + '</h1>')
        f.write('<img src="' + json_dict[i]['image'][0] + '" style="zoom:50%">')
        f.write('<p>')
        f.write('<b>Calories per serving:</b> ' + json_dict[i]['cals_per_serving'][0])
        f.write('<br>')
        f.write('<b>Cook time:</b> ' + json_dict[i]['cook_time'][0])
        f.write('<br><br>')
        f.write('<em>' + json_dict[i]['recipe_yield'][0] + '</em>')
        f.write('</p>')
        f.write('<h3>Ingredients</h3>')
        f.write('<ul>')

        for j in range(0, json_dict[i]['ingredients'].__len__()):
            f.write('<li>' + json_dict[i]['ingredients'][j] + '</li>')

        f.write('</ul>')
        f.write('<h3>Directions</h3>')
        f.write('<ol>')

        for k in range(0, json_dict[i]['directions'].__len__()):
            f.write('<li>' + json_dict[i]['directions'][k] + '</li>')

        f.write('</ol>')
        f.write('</body>')
        f.write('</html>')

        f.close()

if __name__ == "__main__":
    file_path = "../recipe_files/"
    json_file = open(r'../recipes.json').read()
    json_data = json.loads(json_file)
    write_html_files(json_data, file_path)

