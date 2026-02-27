import os
from collections import Counter
from pathlib import Path

def scan_directory(path_to_scan):
    print(f"--- Scanning: {path_to_scan} ---")
    
    # Initialize our counters
    extension_counter = Counter()
    total_files = 0
    total_size = 0

    try:
        # Walk through the directory
        for root, dirs, files in os.walk(path_to_scan):
            for file in files:
                total_files += 1
                file_path = Path(root) / file
                
                # Get extension (e.g., '.xls', '.doc')
                ext = file_path.suffix.lower()
                if not ext:
                    ext = "[No Extension]"
                
                extension_counter[ext] += 1
                
                # Try to get file size
                try:
                    total_size += file_path.stat().st_size
                except:
                    pass

        # Print the Report
        print(f"\n[DONE] Scan Complete!")
        print(f"Total Files Found: {total_files}")
        print(f"Total Size: {total_size / (1024*1024):.2f} MB")
        print("\n--- Breakdown by File Type ---")
        
        for ext, count in extension_counter.most_common():
            print(f"{ext:15} : {count} files")

    except Exception as e:
        print(f"[ERROR] Error scanning directory: {e}")

if __name__ == "__main__":
    # For now, we scan the current project folder
    target = os.getcwd()
    scan_directory(target)
