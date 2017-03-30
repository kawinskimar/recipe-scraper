import os, glob

os.chdir('../recipe_files')
for file in glob.glob('*.html'):
    test_subject = os.path.splitext(file)[0]
    rec_file = open(file, 'rw+')
    html = rec_file.read()
    rec_file.close()
    
    print test_subject
    print '\n\n'
    print html
    print '\n\n'
