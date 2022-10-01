import jinja2, os

# create jinja env that can load template from filesystem
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('.')))

template = jinja_env.get_template('Anschreiben.txt')
 
f = template.render(sex='f', Nachname='meier')

m = template.render(sex='m', Nachname='Müller')

print(f)

print(m)