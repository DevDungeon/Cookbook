from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_json():

    print('Data object type: %s' % type(request.get_data()))
    print('Data: %s' % request.get_data())
    return '<html><body>Ok</body></html>'

"""
# You can test the endpoint with a curl POST like this for text:
curl -X POST http://localhost:5000/ --data "{\"x\": 1, \"y\": 2}"
# or like this for binary
curl -X POST http://localhost:5000/ --data-binary @my-binary-file.bin
cat my-binary-file.bin | curl -X POST http://localhost:5000/ --data-binary @-
"""

if __name__ == '__main__':
    app.run(debug=True)
