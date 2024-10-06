# Instagram Downloader

This project is a simple Instagram downloader that allows you to download all posts and profile pictures from a specified Instagram account. The project uses the `instaloader` library to interact with Instagram and download the content.

## Features

- Login to Instagram using your credentials.
- Download all posts from a specified Instagram account.
- Save the downloaded posts and profile picture in organized folders.

## Requirements

- Python 3.6+
- `instaloader` library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/instagramDownloader.git
cd instagramDownloader
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required libraries:

```sh
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory of the project and add your Instagram credentials:

```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## Usage

1. Run the program:

```sh
python /Users/alisina/Documents/Projects/Others/instagramDownloader/main/program.py
```

2. Follow the on-screen instructions to download posts from a specified Instagram account.

## Error Handling

The program handles the following exceptions:

- `LoginRequiredException`: Raised when login is required. Check your credentials.
- `ConnectionException`: Raised when there is a connection error. Check your internet connection.
- `ProfileNotExistsException`: Raised when the specified profile does not exist. Check the username.
- `FileNotFoundError`: Raised when a file is not found.
- `Exception`: Catches any other unexpected errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
