# Follow-Back
A simple Python program to check Instagram follow-backs.

## Description
This script reads data from two JSON files, `followers.json` and `following.json`, to determine which users you are following that are not following you back on Instagram. It outputs the number of such users and lists their usernames.

## Prerequisites
- Python 3.x
- Access to your Instagram account

## Usage
1. Clone the repository:
    ```sh
    git clone https://github.com/divinewton/Follow-Back.git
    cd Follow-Back
    ```

2. Ensure you have the required JSON files (`followers.json` and `following.json`) in the same directory as the script.
    These files can be downloaded from Instagram using the guide [here](https://help.instagram.com/181231772500920?helpref=about_content#download-a-copy-of-your-information-in-accounts-center).

3. Run the script:
    ```sh
    python followedback.py
    ```
