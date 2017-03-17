import json

def to_html_file(json_dict, file_path):
    file = open(file_path, 'w')
    file.write('<html>')
    file.write('<head></head>')
    file.write('<body>')
    
    file.close()

file = open(r'C:\Users\maris\Documents\GitHub\Projects\recipe-scraper\allrecipes\test.json').read()
jsonData = json.loads(file)

