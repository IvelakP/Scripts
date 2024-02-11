import os
import subprocess
import platform

def open_image(image_path):
    """
    Open the specified image using the default image viewer based on the operating system.

    Args:
    - image_path (str): Path to the image file.

    Raises:
    - Exception: If an error occurs while opening the image.
    """
    try:
        if platform.system() == 'Windows':
            os.startfile(image_path)
        elif platform.system() == 'Darwin':
            subprocess.call(['open', image_path])
        elif platform.system() == 'Linux':
            subprocess.call(['xdg-open', image_path])
        else:
            print("Unsupported platform. Cannot display image.")
    except Exception as e:
        print(f"Error opening image: {e}")

def get_new_name(folder_path, base_name, extension):
    """
    Generate a new filename to avoid naming conflicts in the specified folder.

    Args:
    - folder_path (str): Path to the folder containing the images.
    - base_name (str): Base name of the image file.
    - extension (str): File extension of the image.

    Returns:
    - new_name (str): New base name for the image.
    """
    new_name = base_name
    counter = 1

    while os.path.exists(os.path.join(folder_path, f"{new_name}{extension}")):
        new_name = f"{base_name}{counter}"
        counter += 1

    return new_name

def process_images(folder_path):
    """
    Process images in the specified folder, allowing the user to delete, rename, or skip each image.

    Args:
    - folder_path (str): Path to the folder containing the images.
    """
    try:
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        for image in images:
            image_path = os.path.join(folder_path, image)
            print(f"Processing: {image}")

            # Display the image using the default image viewer
            open_image(image_path)

            # Ask for user input
            action = input("Program can be terminated with (T). Do you want to (D)elete, (R)ename, or (S)kip this image? ").lower()

            try:
                if action == 'd':
                    os.remove(image_path)
                    print(f"Deleted: {image}")
                elif action == 'r':
                    base_name, extension = os.path.splitext(image)
                    new_name = input("Enter the new base name for the image: ")
                    
                    # Preserve the original file extension
                    new_name = get_new_name(folder_path, new_name, extension)
                    new_path = os.path.join(folder_path, f"{new_name}{extension}")
                    os.rename(image_path, new_path)
                    print(f"Renamed and saved as: {new_name}{extension}")
                elif action == 's':
                    print("Skipped.")
                elif action == 't':
                    print("Exiting the program")
                    return
                else:
                    print("Invalid action. Skipping.")

            except FileNotFoundError:
                print(f"File not found: {image}")
            except PermissionError:
                print(f"Permission error. Unable to perform the action on: {image}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Skipping.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    process_images(folder_path)