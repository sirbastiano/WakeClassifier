import requests
from tqdm import tqdm

def download_file(url, filename):
    """
    Download a file from the specified URL and save it locally.
    """
    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Total size in bytes
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(filename, 'wb') as file, tqdm(
        total=total_size, unit='iB', unit_scale=True
    ) as bar:
        for data in response.iter_content(block_size):
            bar.update(len(data))
            file.write(data)

# URL of the file to be downloaded
url = "https://zenodo.org/records/10018939/files/xAIWakes.zip?download=1"

# Local filename to save the downloaded file
filename = "xAIWakes.zip"

# Download the file
download_file(url, filename)

print(f"Downloaded '{filename}'.")
