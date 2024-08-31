#!/usr/bin/python3
# Dolphin-UltraCopy 0.3
# Release: 28 Aug 2024
#
# Author: ernzo (https://github.com/ernzo)
# Repository: https://github.com/ernzo/Dolphin-UltraCopy
#
# This script is an Action for Dolphin that uses CopyQ to Paste the clipboard content with Ultracopier.
#
# All details and Installation instructions in the README.MD file.
#
import subprocess
import sys
import urllib.parse
import os

def start_copyq():
    """Ensure CopyQ is running."""
    try:
        result = subprocess.run(['pgrep', 'copyq'], capture_output=True, text=True)
        if result.returncode == 0:
            print("CopyQ is already running.")
        else:
            subprocess.Popen(['copyq'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("CopyQ started.")
    except Exception as e:
        print(f"Exception starting CopyQ: {e}")

def get_clipboard_data():
    """Retrieve clipboard data from CopyQ."""
    try:
        result = subprocess.run(['copyq', 'read', '0'], capture_output=True, text=True)
        if result.returncode == 0:
            data = result.stdout.strip()
            if data:
                print(f"Clipboard Data Retrieved: {data}")
                return data
            else:
                print("Clipboard empty.")
                return None
        else:
            print(f"Error running CopyQ command: {result.stderr.strip()}")
            return None
    except Exception as e:
        print(f"Exception retrieving clipboard data: {e}")
        return None

def uri_to_path(uri):
    """Convert file URI to local file path."""
    if uri.startswith('file://'):
        return urllib.parse.unquote(uri[7:])
    return uri

def format_sources(sources):
    """Format list of source paths."""
    return ' '.join(f'"{source}"' for source in sources)

def main():
    """Execute copy operation."""
    if len(sys.argv) != 2:
        print("Usage: paste-clipboard-ultracopier.py <destination_directory>")
        sys.exit(1)

    destination = uri_to_path(urllib.parse.unquote(sys.argv[1]))
    if not os.path.isdir(destination):
        print(f"Error: {destination} is not a valid directory.")
        sys.exit(1)

    start_copyq()

    clipboard_data = get_clipboard_data()
    if clipboard_data:
        sources = [uri_to_path(source) for source in clipboard_data.split('\n') if source.strip()]
        sources_formatted = format_sources(sources)

        command = f'/usr/bin/ultracopier cp {sources_formatted} "{destination}"'
        print(f"Executing command: {command}")

        try:
            # Run the command and capture both stdout and stderr
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"UltraCopier command output:\n{result.stdout}")
            if result.returncode == 0:
                print("UltraCopier command executed successfully.")
            else:
                print(f"UltraCopier command failed with return code: {result.returncode}")
                print(f"Error output:\n{result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"Exception executing UltraCopier command: {e}")
            print(f"Error output:\n{e.stderr}")
    else:
        print("No valid clipboard data found.")

if __name__ == "__main__":
    main()
