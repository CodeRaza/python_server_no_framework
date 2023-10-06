# Python Server WithOut Any Framework

## Overview

This project demonstrates creating a basic HTTP server in Python without using any external frameworks. The server serves HTML files, handles GET requests with query parameters, extracts variables from the URL path, and processes simple JSON POST requests.

## Features

- **Serving HTML files over HTTP:** The server can serve HTML files.
- **Extracting query parameters:** It can extract query parameters from GET requests and use them in the response.
- **Extracting variables from the URL path:** The server can extract variables from the URL path to customize responses based on the path.
- **Handling JSON POST requests:** The server can handle JSON POST requests and process the data accordingly.

## Usage

1. Run the Python script to start the HTTP server:
   ```bash
   python server.py

2. Access the root URL: http://localhost:8000/ 
3. Get JSON at /data
4. Get Single User Data: /data?user_id=1
5. Post Data at: /user_data - { "username": "name" }
