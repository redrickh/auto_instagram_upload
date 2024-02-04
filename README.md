# Instagram Auto-Post README

This Python script is used to automate the process of uploading posts on Instagram. It allows you to upload a file from your local system to your Instagram account directly.

## Prerequisites
You need Python 3.x and pip (Python package installer) installed on your machine. It's advisable to use a virtual environment for the Python project.

Also, make sure to install the necessary Python libraries: Selenium and WebDriver Manager. You can install these using pip:

```bash
pip install selenium webdriver_manager
```

## Usage
Create a text file named "cookies_insta.txt" with the cookies saved from a valid Instagram session. These are used to authenticate your session.

Use the \`upload_instagram_post\` function to start the process:

```python
upload_instagram_post("<path_to_your_file>", "<your_post_description>")
```

Replace \`<path_to_your_file>\` with the path of the file you want to upload and \`<your_post_description>\` with the caption for your post.

## Function description

### \`import_cookies\`
This function is used to import cookies for the Instagram session from a text file. It takes two parameters - driver (the webdriver object) and cookie_file (the file from which cookies are to be read).

### \`upload_instagram_post\`
This is the main function that handles the post upload. It takes two parameters - file_path (the path to the file you want to upload) and description (the caption for your post).
- Initializes the Chrome webdriver with specific options.
- Loads the Instagram page and imports the cookies.
- Goes through a series of steps to find and click the appropriate buttons and input elements to upload the post.
- In the process, handles various expected and unexpected conditions and exceptions.

## Note
This script uses browser automation and interacts directly with Instagram's front-end web elements, so it might break if Instagram updates or changes its website structure or elements. Make sure to regularly update the element tags or XPaths used in the script to prevent such issues.

To run the script, use:

```python
python <script_name>.py
```

Please replace \`<script_name>\` with the name of the script file.
