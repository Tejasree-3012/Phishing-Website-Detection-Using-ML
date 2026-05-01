Optimizing tool selection...Reviewing the repository files to craft an accurate README.

Read [](file:///c%3A/Users/Bhavya%20Chandrika/PhishingApp/phishing_detection.py)

Read [](file:///c%3A/Users/Bhavya%20Chandrika/PhishingApp/README.md)

Read [](file:///c%3A/Users/Bhavya%20Chandrika/PhishingApp/app.py)

## PhishingApp

A simple Flask web app for detecting suspicious URLs and analyzing text-based files for phishing-like patterns.

### Overview

This project provides:

- URL scanning via heuristic analysis
- File scanning for `.txt`, `.csv`, and `.html` files
- A web interface powered by `Flask`
- Basic phishing indicators such as IP-based domains, suspicious keywords, hidden script/form patterns

### Files

- app.py — Flask application and upload handling
- phishing_detection.py — phishing detection logic for URLs and file content
- index.html — web UI template
- files — upload/storage folder for scanned files

### Features

- URL phishing detection
- File content analysis for embedded forms, scripts, passwords, IPs
- User-friendly web interface
- Simple heuristic rules for quick scanning

### Installation

1. Install Python 3.8+.
2. Install requirements:
   - `pip install flask`
3. Run the app:
   - `python app.py`

### Usage

1. Open the app in your browser at `http://127.0.0.1:5000/`
2. Enter a URL and submit to check it
3. Or upload a `.txt`, `.csv`, or `.html` file to scan its content

### How it works

- `predict_phishing(url)` checks for:
  - IP address in the URL
  - `@` symbol
  - long URL length
  - many subdomains
  - suspicious keywords like `login`, `verify`, `update`, `banking`, `account`

- `analyze_file_content(file_content)` checks for:
  - embedded HTML forms
  - script tags
  - password verification/update prompts
  - raw IP addresses

### Notes

- This is a proof-of-concept and not a replacement for production phishing protection.
- Use it as a learning tool or base for extending detection logic.
- The app saves uploaded files into files and validates allowed extensions.

### Optional Improvements

- Add more phishing detection rules
- Improve file analysis with HTML parsing
- Add logging and persistent scan history
- Deploy as a production Flask app with a proper secret key and secure file handling