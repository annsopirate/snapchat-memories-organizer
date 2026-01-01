import os
import shutil

# --- CONFIGURATION ---
SIMULATION = True
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"

def flatten_folders():
    if not os.path.exists(TARGET_FOLDER):
        print(f"Error: Folder not found.")
        print("Please edit the script and set the correct TARGET_FOLDER path.")
        return

    count_moved = 0
    count_deleted = 0
    print(f"--- Flattening Folders (Simulation: {SIMULATION}) ---")

    for month_folder in os.listdir(TARGET_FOLDER):
        path_month = os.path.join(TARGET_FOLDER, month_folder)
        if not os.path.isdir(path_month): continue

        for sub in os.listdir(path_month):
            path_sub = os.path.join(path_month, sub)
            if not os.path.isdir(path_sub): continue

            if len(sub) > 15 and sub[0].isdigit():
                for file in os.listdir(path_sub):
                    src = os.path.join(path_sub, file)
                    dst = os.path.join(path_month, file)

                    if os.path.exists(dst): continue

                    if SIMULATION:
                        print(f"[SIMULATION] Move: .../{sub}/{file} -> .../{month_folder}/")
                    else:
                        try:
                            shutil.move(src, dst)
                            count_moved += 1
                        except Exception as e:
                            print(f"[ERROR] Move failed: {e}")

                if SIMULATION:
                    print(f"[SIMULATION] Remove empty folder: {sub}")
                    count_deleted += 1
                else:
                    try:
                        os.rmdir(path_sub)
                        print(f"[CLEANUP] Removed: {sub}")
                        count_deleted += 1
                    except:
                        pass

    print(f"Done! Moved {count_moved} files, deleted {count_deleted} folders.")

if __name__ == "__main__":
    flatten_folders()