import jinja2


# standard Python
name = 'Uwe'
print(f'Hello, {name}')


# Jinja2 way
environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")

print(template.render(name="World"))
