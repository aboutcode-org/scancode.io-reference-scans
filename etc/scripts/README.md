To update the README, make the desired modifications in readme.template, then regenerate the README.

How to generate the README file for this repo:

1. Ensure you are in a virtual environment with jinja2 and requests installed
2. Have the staging.scancode.io username and password in the following environment variables: SCANCODE_IO_USER and SCANCODE_IO_PASSWORD, respectively.
3. Run the generate_readme.py script: SCANCODE_IO_USER=\<username\> SCANCODE_IO_PASSWORD=\<password\> python generate_readme.py
