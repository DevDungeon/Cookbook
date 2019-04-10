import requests


# GET
response = requests.get('https://www.devdungeon.com/archive') # stream=True
print(response.text)  # whole HTML body
print(response.status_code)
print(response.headers)



# POST
response = requests.post('https://httpbin.org/anything',
                         files={'file': 'The file contents'}, # can pass a list of files
                         data={'form_field_name': 'form_value'},
                         params={'q': 5, 'action': 'delete'})
print(response.text)
# multiple_files = [
#         ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#         ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
# r = requests.post(url, files=multiple_files)


# Or stream data in upload
with open('large-file.txt', 'rb') as file_contents:
    response = requests.post('https://httpbin.org/anything', data=file_contents)
    print(response.text)
