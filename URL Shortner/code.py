import string
import random
import sqlite3

# Initialize database
conn = sqlite3.connect('url_shortener.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY, original_url TEXT, short_code TEXT)''')

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def shorten_url(original_url):
    # Check if URL already exists in database
    c.execute("SELECT short_code FROM urls WHERE original_url=?", (original_url,))
    result = c.fetchone()
    
    if result:
        return result[0]
    
    # Generate a new short code
    short_code = generate_short_code()
    
    # Insert the new URL and short code into the database
    c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, short_code))
    conn.commit()
    
    return short_code

def get_original_url(short_code):
    c.execute("SELECT original_url FROM urls WHERE short_code=?", (short_code,))
    result = c.fetchone()
    
    if result:
        return result[0]
    else:
        return None

# Example usage
while True:
    choice = input("Enter 1 to shorten a URL, 2 to expand a short URL, or 3 to quit: ")
    
    if choice == '1':
        original_url = input("Enter the URL to shorten: ")
        short_code = shorten_url(original_url)
<<<<<<< HEAD
        # enter the domain name that is ours and need to shorten it , before running change it , else the domain name will be printed as : albinmanuvel.com
        print(f"Shortened URL: http://yourdomain.com/{short_code}")
=======
        print(f"Shortened URL: http://Albinmanuvel.com/{short_code}")
>>>>>>> 22376a8835691a90e25b9eea4abe9c2c40f7d2a8
    
    elif choice == '2':
        short_code = input("Enter the short code: ")
        original_url = get_original_url(short_code)
        if original_url:
            print(f"Original URL: {original_url}")
        else:
            print("Short code not found.")
    
    elif choice == '3':
        break
    
    else:
        print("Invalid choice. Please try again.")

conn.close()
