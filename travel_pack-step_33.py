# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TravelPack
import sys, os, json, datetime, uuid

def main():
    if len(sys.argv) < 2 or sys.argv[1] != "unzip":
        print("Usage: python TravelPack.py unzip <archive_name>")
        return
    
    archive_path = sys.argv[1]
    
    def safe_unzip(archive):
        try:
            import zipfile
            with zipfile.ZipFile(archive, 'r') as zf:
                for member in zf.namelist():
                    if not os.path.exists(member):
                        zf.extract(member)
        except Exception as e:
            print(f"Error unzipping {archive}: {e}")

    safe_unzip(archive_path)
    
    # Check if TravelPack.py exists in current directory, if so run it
    main_script = "TravelPack.py"
    if os.path.exists(main_script):
        exec(open(main_script).read())
    else:
        print("TravelPack.py not found.")

if __name__ == "__main__":
    main()
