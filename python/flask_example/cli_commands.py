import click
from flask import Flask

app = Flask(__name__)

# List commands with: `flask`

# This is the simplest form of a command you can make
# Run with: `flask my_simple_command`
@app.cli.command('my_simple_command')
def my_custom_command_handler():
    print('My custom command has been triggered.')

# This command has nice help description along with an argument
# Run with: `flask greet NanoDano`
@app.cli.command("greet", help="Greet someone")
@click.argument("name", default='Guest')
def hello(name):
    print(f'Hello, {name}')

# This command takes 
# Run with one of the following:
# `flask greet`
# `flask greet --help`
# `flask greet NanoDano
# `flask greet NanoDano --greeting Howdy`
@app.cli.command("greet", help="Test command, please ignore")
@click.argument('name', )
@click.option('--greeting', prompt='What greeting should we use?')
def greet(name, greeting):
    print(f'{greeting}, {name}.')


if __name__ == '__main__':
    app.run(debug=True)