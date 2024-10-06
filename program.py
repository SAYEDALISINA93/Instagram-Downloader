import instaloader
import os
from dotenv import load_dotenv

def download_posts(username):
    L = instaloader.Instaloader()

    try:
        print("Attempting to log in...")
        # Login or load session
        L.interactive_login(username)  # (ask password on terminal)
        print("Login successful.")

        print("Fetching profile metadata...")
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, username)
        print("Profile metadata obtained.")

        print("Downloading all posts...")
        # downloading all posts
        L.download_profile(profile, profile_pic_only=False)
        print("All posts downloaded.")

        print("Organizing downloaded files...")
        # save downloaded posts in a folder
        os.rename(username, "downloaded_posts")
        # save profile picture in a folder
        os.rename(username + ".jpg", "profile_pic")
        print("Downloaded posts and profile picture organized successfully.")

    except instaloader.exceptions.LoginRequiredException:
        print("Login required. Please check your credentials.")
    except instaloader.exceptions.ConnectionException:
        print("Connection error. Please check your internet connection.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist. Please check the username.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Closing the session...")
        # close the session
        L.close()
        print("Session closed.")

def main():
    load_dotenv()

    while True:
        print("\nMenu:")
        print("1. Download Instagram posts")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your Instagram username: ")
            download_posts(username)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
