#!/usr/bin/python3
import requests
from google_play_scraper import app
import os


def main():
    system_username = os.getlogin()
    print_banner()
    print("\U0001F449 Please type or paste the package name of the app")
    package_name = input("you want to download: ")
    print(" ")
    app_info = get_app_info(package_name)
    
    if app_info:
        download_and_save_apk(app_info, system_username)
    else:
        print(f"App with package name '{package_name}' not found on Google Play Store.")

def print_banner():
    banner = '''
========================================================================                                 
=        #    #   ##       ### ### ###  #                              =
=       # #  # #  # #       #  # # # #  #                              =
=       ###  ###  # #       #  # # # #  #                              =
=       # #  # #  # #       #  # # # #  #                              =
=       # #  # #  ##        #  ### ###  #####                          =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                         =
=     x        Android APPs Downlaoder       x                         =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                         =
=                                                                      =
=   Written by Learn Tech With Deepak                                  =
=   Youtube Channel: @learntechwithdeepak                              =
=   YouTube: https://www.youtube.com/channel/UCq6THg2VnvaKWnOPF7FGmLw  =
========================================================================   
    '''
    print(banner)
    print(" ")

def get_app_info(package_name):
    try:
        app_info = app(
            package_name,
            lang='en',    # Language (optional)
            country='us'  # Country (optional)
        )
        return app_info
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def download_and_save_apk(app_info, system_username):
    app_url = app_info.get('url')
    app_name = app_info.get('title', 'UnknownApp')

    if not app_url:
        print("App URL not found.")
        return

    response = requests.get(app_url)
    if response.status_code == 200:
        with open(f'{app_name}.apk', 'wb') as apk_file:
            apk_file.write(response.content)
            print(f"\U000F60A Congratulations! Mr. {system_username} ):")
            print(f"'{app_name}' is Downloaded Successfully.....")
            print(" ")
            print("Thanks You! Mr. {system_username}")
    else:
        print("Failed to download APK....")

if __name__ == "__main__":
    main()
