import os
import json

def generate_manifest():
    # Get a list of all items in the current directory
    root_dir = "."
    folders = [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f))]

    # Create a manifest as a JSON object
    manifest = {
        "folders": folders
    }

    # Save the manifest to a file
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    generate_manifest()
