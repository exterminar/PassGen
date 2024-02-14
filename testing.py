import requests
import random

# Fetch the content of the website
url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)

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
    print("Random 6-letter Word:", random_word1)
    print("Random 5-letter Word:", random_word2)
else:
    print("Failed to fetch the wordlist. Please check the URL or try again later.")
