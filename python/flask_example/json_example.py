from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_json():
    print('Request is JSON? %s' % request.is_json)
    print('JSON data: %s' % request.get_json(force=True))
    return '<html><body>Ok</body></html>'

"""
# You can test the endpoint with a curl POST like this:
curl -X POST http://localhost:5000/ \
    --header "Content-Type: application/json" \
    --data "{\"x\": 1, \"y\": 2}"
"""

if __name__ == '__main__':
    app.run(debug=True)
