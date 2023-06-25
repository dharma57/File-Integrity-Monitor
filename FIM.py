import hashlib
import os
import time

# Configuration parameters
TARGET_FILES = [r'Path of the file ', 
                r'Path of the file']  # List of files to monitor
CHECK_INTERVAL = 1  # Time interval between integrity checks

def compute_file_hash(file_path):
    """Compute the hash value of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def initialize_fim():
    """Initialize the file integrity monitor."""
    # Create a dictionary to store the initial file hashes
    initial_hashes = {}
    for file in TARGET_FILES:
        if os.path.exists(file):
            initial_hashes[file] = compute_file_hash(file)
        else:
            print(f"Warning: File {file} does not exist.")

    return initial_hashes

def monitor_files():
    """Monitor the integrity of target files."""
    file_hashes = initialize_fim()

    while True:
        for file in TARGET_FILES:
            if os.path.exists(file):
                current_hash = compute_file_hash(file)
                if file_hashes[file] != current_hash:
                    print(f"File {file} has been modified!")
                    # Perform actions based on the modification, e.g., log event, send notification
                    # ...
                    print("file modified")

                    # Update the file hash with the new computed hash
                    file_hashes[file] = current_hash
            else:
                print(f"Warning: File {file} does not exist.")

        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    monitor_files()
