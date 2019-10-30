from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_form():
    return """
<html><body>
  <form method="POST" enctype="multipart/form-data">
  <input type="file" name="file-to-upload" />
  <input type="submit" value="Upload" />
</form>
</body></html>
"""

@app.route('/', methods=['POST'])
def process_file_upload():

    print("`request.files` object: %s" % request.files)

    # It will store the file in memory or a temporary location
    # and we need to do something with it, like process the
    # data or store it to disk somewhere.
    uploaded_file = request.files.get('file-to-upload')
    print("Uploaded file object: %s" % uploaded_file)

    print('Uploaded data size: %s' % uploaded_file.content_length)
    print('Mimetype: %s' % uploaded_file.mimetype)
    print('Filename: %s' % uploaded_file.filename)
    print('Name: %s' % uploaded_file.name)
    print('Stream: %s' % uploaded_file.stream)
    print('Headers: %s' % uploaded_file.headers)

    # Save will read() the contents and store to disk.
    # File cursor will be at the end of the data unless reset
    uploaded_file.save('upload.bin')

    # Move the cursor to the beginning so we can do an additional read()
    uploaded_file.seek(0)
    data = uploaded_file.read()
    print('Amount of data read: %s' % len(data))
        
    # Manually close the file if you're done with it
    print(uploaded_file.close())

    return '<html><body>Ok</body></html>'


if __name__ == '__main__':
    app.run(debug=True)