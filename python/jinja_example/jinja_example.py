# pip install jinja2
from jinja2 import Template

# Simplest use
print(Template('Hello, {{ name }}!').render({'name': 'NanoDano'}))

# Read template from file
#with open("jinja_template.txt") as f:
#    template_text = f.read()

# Another way to read a file
#from pathlib import Path
#template_text = Path('jinja_template.txt').read_text(encoding='utf8')  # 'ascii'

template_text = '{{ greeting.text }}, {{ first_name|upper }} {{ last_name }}!'

class GreetObj:
    pass
greet_object = GreetObj()
greet_object.text = "Howdy"

template = Template(template_text)
output = template.render({'first_name': 'John', 'greeting': greet_object}, last_name='Doe')
print(output)