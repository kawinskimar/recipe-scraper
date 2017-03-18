import json

def write_html_files(json_dict, file_path):
    length = json_dict.__len__()

    for i in range(0, length):
        f = open(file_path + '\\' + i + '.csv', 'w')
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

file = open(r'C:\Users\maris\Documents\GitHub\Projects\recipe-scraper\allrecipes\test.json').read()
jsonData = json.loads(file)
