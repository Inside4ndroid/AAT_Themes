import os
import json

def generate_manifest(base_path='.'):
    manifest = {}

    # Walk through all directories and files starting from the base_path
    for root, dirs, files in os.walk(base_path):
        # Filter out the .git folder and hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]

        # Relative folder path from the base_path
        relative_path = os.path.relpath(root, base_path)

        # Skip the base directory itself
        if relative_path == '.':
            continue

        # Add the folder as a key and the files inside as values
        manifest[relative_path] = files

    # Write the manifest to a file
    with open('manifest.json', 'w') as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    generate_manifest()