# Simple URL Shortener

This is a basic URL shortener program written in Python. It allows users to shorten long URLs into more manageable short codes and retrieve the original URLs using these codes.

## Features

- Shorten long URLs to 6-character codes
- Retrieve original URLs using short codes
- Local SQLite database storage
- Simple command-line interface

## Requirements

- Python 3.x
- SQLite3 (included in Python standard library)
- * Remember to replace yourusername with your actual GitHub username in the clone URL and issues page link.

Follow the on-screen prompts to:
1. Shorten a URL
2. Expand a shortened URL
3. Quit the program

## How it works

- The program generates a random 6-character code for each new URL.
- URLs and their corresponding short codes are stored in a SQLite database.
- If a URL has been shortened before, the program returns the existing short code.
- When expanding a URL, the program looks up the short code in the database and returns the corresponding long URL.

## Limitations

- This is a basic implementation and not suitable for production use without further development.
- The program uses a local database and does not provide a web interface.
- There's no collision checking for short codes, which could potentially lead to duplicates in a high-volume scenario.

## Future Improvements

- Add web interface using a framework like Flask or Django
- Implement collision checking for short codes
- Add URL validation
- Improve error handling
- Add user authentication for creating and managing shortened URLs

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/url-shortener/issues) if you want to contribute.

