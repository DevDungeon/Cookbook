import requests, sys


def download_file(url, local_filename=None):
    if not local_filename:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

if __name__ == '__main__':
    print(f"Downloading {sys.argv[1]} to {sys.argv[2]}")
    download_file(sys.argv[1], sys.argv[2])
