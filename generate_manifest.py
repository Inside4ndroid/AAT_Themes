import os
import json

def generate_manifest():
    # Define the directories to ignore
    ignored_folders = {'.github', '.git'}
    
    # Get a list of all items in the current directory
    root_dir = "."
    folders = [f for f in os.listdir(root_dir) 
               if os.path.isdir(os.path.join(root_dir, f)) and f not in ignored_folders]

    # Create a manifest as a JSON object
    manifest = {
        "folders": folders
    }

    # Save the manifest to a file
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    generate_manifest()
