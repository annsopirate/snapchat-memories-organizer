import os
import subprocess

# --- CONFIGURATION ---
SIMULATION = True
TARGET_FOLDER = r"C:\Users\YourName\Desktop\snapchat_memories"
FFMPEG_PATH = os.path.join(os.getcwd(), "ffmpeg.exe")

def merge_overlays():
    if not os.path.exists(FFMPEG_PATH):
        print("ERROR: ffmpeg.exe not found!")
        print("Please place ffmpeg.exe in the same directory as this script.")
        return

    print(f"--- Merging Started (Simulation: {SIMULATION}) ---")
    count = 0

    for root, dirs, files in os.walk(TARGET_FOLDER):
        medias = []
        overlays = []

        for f in files:
            name, ext = os.path.splitext(f)
            if "_FUSION" in name: continue
            
            if ext.lower() == ".png": overlays.append(f)
            elif ext.lower() in [".jpg", ".jpeg", ".mp4", ".mov"]: medias.append(f)

        if len(medias) == 1 and len(overlays) == 1:
            media_f = medias[0]
            overlay_f = overlays[0]
            
            path_media = os.path.join(root, media_f)
            path_overlay = os.path.join(root, overlay_f)
            
            name_no_ext, ext_media = os.path.splitext(media_f)
            final_name = f"{name_no_ext}_FUSION{ext_media}"
            final_path = os.path.join(root, final_name)

            if os.path.exists(final_path):
                try: os.remove(final_path)
                except: pass

            print(f"[DETECTED] {media_f} + {overlay_f}")

            if SIMULATION:
                print(f"   -> [SIMULATION] Would create: {final_name}")
            else:
                filter_cmd = "[1:v][0:v]scale2ref[ovr][base];[base][ovr]overlay=0:0"
                cmd = [FFMPEG_PATH, "-y", "-i", path_media, "-i", path_overlay, "-filter_complex", filter_cmd, "-map_metadata", "0", "-c:a", "copy", final_path]
                
                if ext_media.lower() in [".jpg", ".jpeg"]:
                     cmd = [FFMPEG_PATH, "-y", "-i", path_media, "-i", path_overlay, "-filter_complex", filter_cmd, "-map_metadata", "0", final_path]

                try:
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"   -> [SUCCESS] Created: {final_name}")
                    count += 1
                except Exception as e:
                    print(f"   -> [ERROR] {e}")

    print(f"Done! {count} fusions created.")

if __name__ == "__main__":
    merge_overlays()