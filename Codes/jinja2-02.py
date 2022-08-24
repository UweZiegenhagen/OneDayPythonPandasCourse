import pandas as pd # data wrangling
import jinja2 # template engine
import os # for file-related stuff
 
# create jinja env that can load template from filesystem
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('.')))
 
df = pd.read_excel('Daten.xlsx')
template = jinja_env.get_template('template.xml')
 
with open('FertigesXML.xml','w') as output:
    output.write(template.render(data=df))