import gdown

file_id = "18lzo9iq0aTfsdGwE0gET2vvyItQuuP5k"
url = f"https://drive.google.com/uc?id={file_id}"
output = ".env"
gdown.download(url, output,quiet=False)