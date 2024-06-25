# Define the path to your text file
file_path = 'perspective_api.txt'

# Open the file and read the API key
with open(file_path, 'r') as file:
    api_key = file.read().strip()

# Print the API key to verify
print(f'API Key: {api_key}')