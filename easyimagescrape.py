###
#Quick python script for scraping images off of a webcomic. Relies on the webcomic using a numbers format for its pages.
###

import os
import requests

# Define the full URL of the webcomic site, minus the ending filename
# e.g. https://www.webcomic.com/a/comic/page0001.jpg would be "https://www.webcomic.com/a/comic/"
base_url = "https://www.webcomic.com/a/comic/"

# Define the start and end number for the webcomic pages. Try not to leave end_number on 9999...
# if webcomic uses a format that doesn't start with zeros, you'll need to comment out the six lines near the bottom of the script.
start_number = "0001"
end_number = "9999"

# Define the directory to store the downloaded images
if not os.path.exists("images"):
    os.makedirs("images")

# Loop through all dates between the start and end numbers
current_number = start_number
while current_number <= end_number:
    # Generate the image URL for the current date
    # This is the full link the script is searching for. Ensure it matches with a valid url on the site you're scraping from.
    # You may need to change the word 'page' for something else e.g. 'comic'. Again, ensure it matches an actual url
    # Don't forget to change the file extension if necessary!
    image_url = f"{base_url}/page{current_number}.png"

    # Download the image and save it to the images directory
    image_filename = os.path.join("images/", f"page{current_number}.png")
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(image_filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {image_url} to {image_filename}")
    else:
        print(f"Could not download {image_url} (status code {response.status_code})")

    # Move to the next date
    print(f"Current number is {current_number}")
    current_number = str(int(current_number) + 1)
    # if your page numbers don't start with zero, comment out the next six lines. This assumes the numbering system uses a four digit format.
    if (len(current_number) == 1):
        current_number = f'000{current_number}'
    elif (len(current_number) == 2):
        current_number = f'00{current_number}'
    elif (len(current_number) == 3):
        current_number = f'0{current_number}'
    print(f"Next is {current_number}. End number is {end_number}")
