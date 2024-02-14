import random
import string
import requests

# Fetch the content of the website
url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)

# Reading words from local file
file_path = r"C:\Users\os508c\Documents\DevOps\Password Generator\latinwords.txt"

# Open the file for reading
with open(file_path, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Process each line (word) and filter out words with X characters
six_character_words = [line.strip() for line in lines if len(line.strip()) == 6]
five_character_words = [line.strip() for line in lines if len(line.strip()) == 5]

# Select a random word from the list of X-character words
random_word_latin1 = random.choice(six_character_words)
random_word_latin2 = random.choice(five_character_words)

# Process each line (word) and print it
for line in lines:
    word = line.strip()  # Remove any leading/trailing whitespace or newline characters

# Check if the request was successful
if response.status_code == 200:
    # Split the content into a list of words
    wordlist = response.text.splitlines()

    # Filter the word list to include only words with X characters
    six_letter_word = [word for word in wordlist if len(word) == 6]
    five_letter_word = [word for word in wordlist if len(word) == 5]

    # Select a random word from the filtered list
    random_word1 = random.choice(six_letter_word)
    random_word2 = random.choice(five_letter_word)

    # Print the random word
    #print("Random 6-letter Word:", random_word1)
    #print("Random 5-letter Word:", random_word2)
else:
    print("Failed to fetch the wordlist. Please check the URL or try again later.")

# List of ten words
word_list = ['apple', 'banana', 'orange', 'grape', 'melon', 'pineapple', 'kiwi', 'strawberry', 'peach', 'blueberry']


# Function to generate a random password
def generate_password():
    # Select a random word from the list (list of ten words)
    #random_word = random.choice(word_list)

    # Generate a random symbol character
    #symbol = random.choice(string.punctuation)
    symbols = ['!', '#', '.']
    random_symbol = random.choice(symbols)

    # Generate two random numbers
    numbers = ''.join(random.choices(string.digits, k=2))

    # Capitalize the first letter of the selected word
    capitalized_word = random_word1.capitalize()

    # Construct the password
    password = random_symbol + capitalized_word + random_word2 + numbers

    return password

def generate_password2():
    # Select a random word from the list (list of ten words)
    #random_word = random.choice(word_list)

    # Generate a random symbol character
    #symbol = random.choice(string.punctuation)
    symbols = ['!', '#', '.']
    random_symbol = random.choice(symbols)

    # Generate two random numbers
    numbers = ''.join(random.choices(string.digits, k=2))

    # Capitalize the first letter of the selected word
    capitalized_word = random_word_latin1.capitalize()

    # Construct the password
    password_latin = random_symbol + capitalized_word + random_word_latin2 + numbers

    return password_latin

# Generate and print the password
random_password = generate_password()
random_password2 = generate_password2()
print("14 Character Random Generated Password from English Dictionary:", random_password)
print("14 Character Random Generated Password from Latin Dictionary:", random_password2)