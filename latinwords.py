import requests
from bs4 import BeautifulSoup


# Function to remove ":" characters from a word
def remove_colon(word):
    return word.replace(' : ', '')


# Fetch the content of the website
url = "https://personal.math.ubc.ca/~cass/frivs/latin/latin-dict-full.html"  # Replace with the website URL you want to scan
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all text within <strong> tags
    strong_tags = soup.find_all('strong')

    # Extract words between <strong> tags and remove ":" characters
    latin_words = [remove_colon(tag.get_text().strip()) for tag in strong_tags]

    # Remove empty strings
    latin_words = [word for word in latin_words if word]

    # Write the cleaned words to a file
    with open('latinwords.txt', 'w') as file:
        for word in latin_words:
            file.write(word + '\n')

    print("Latin words extracted and saved to latinwords.txt.")
else:
    print("Failed to fetch the website. Please check the URL or try again later.")

# Open the file for reading
with open('latinwords.txt', 'r') as file:
    content = file.read()

# Replace all ":" with ","
modified_content = content.replace(' :', '')

# Open the file for writing (overwrite mode) and write the modified content back to it
with open('latinwords.txt', 'w') as file:
    file.write(modified_content)

print("All occurrences of ':' replaced with ',' in latinwords.txt.")
