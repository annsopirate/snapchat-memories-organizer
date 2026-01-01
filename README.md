# Snapchat Memories: Complete Workflow (Downloader + Organizer + Overlay Merger)

**⚠️ NOTE ON OS COMPATIBILITY**

This guide is written for **Windows**. 
However, the Python scripts provided here are **cross-platform** and will work on macOS and Linux. 
If you are on Mac or Linux, you can use these scripts, but you will need to adapt the terminal commands (specifically for installing/running ExifTool and FFmpeg) to your operating system.

**This repository provides a complete workflow to download your Snapchat Memories, fix their metadata (dates), organize them into folders (Year/Month), and merge the "overlay" text/stickers back onto your photos and videos.**

It is designed as an extension to the [Snapchat Memories Downloader by Manuel Puchner](https://github.com/ManuelPuchner/snapchat-memories-downloader).

**Note:** All steps following the first one are optional. You can stop whenever you are satisfied with the result.

## Prerequisites

1.  **Python 3.x** installed (Ensure "Add Python to PATH" is checked during installation).
2.  **ExifTool** (for fixing dates).
3.  **FFmpeg** (only if you want to merge overlay text onto images/videos).

---

## Step 1: Download your Memories and fix date metadata (ExifTool)

First, use the original downloader to get your files.
Follow the instructions here: [ManuelPuchner/snapchat-memories-downloader](https://github.com/ManuelPuchner/snapchat-memories-downloader).

Once done, you will have a `snapchat_memories` folder containing thousands of files (images, videos, and JSON files) and folders named after dates/UUIDs.

Now, you will need Exiftool for the date metadata.

### Installation of Exiftool

1.  Download the **Windows Executable** for ExifTool.
2.  **Helpful Video:** Watch this tutorial on how to install it: [https://www.youtube.com/watch?v=Ku1Nx-kl7RM](https://www.youtube.com/watch?v=Ku1Nx-kl7RM).
3.  **Troubleshooting:** If you get an error like `Could not find C:\Program Files (x86)\Exiftool\exiftool_files\perl5*.dll`, you must copy the `exiftool_files` folder into the same directory as the `exiftool.exe`.

Snapchat exports often lack proper internal date tags. This causes files to appear with "Today's date" in your gallery. Since the filenames contain the correct date, we use ExifTool to fix this. *This corresponds to steps **9. Adding location metadata** and **12. Correct the FileCreatedTimestamp** in the original downloader's README.*

## Step 2: ⚠️ SAFETY BACKUP

**Before proceeding, make a copy of your `snapchat_memories` folder to a separate drive or location.**

While the scripts below are designed to be safe, mistakes happen (e.g., incorrect paths). Having a clean backup ensures you never lose your original data if something goes wrong during sorting or merging.

---

### ⚠️ IMPORTANT INSTRUCTIONS FOR EACH SCRIPT BELOW:

1. **DOWNLOAD & PLACE:** Download the scripts and place them in the **root folder** of the project (the same folder where the scripts of the **first step** are located). Do **not** put the scripts inside the `snapchat_memories` folder itself.
2. **EDIT THE PATH:** In every script, look for `TARGET_FOLDER = r"C:\YOUR\PATH\HERE"`. You must change this to the actual location of your memories folder.
3. **SIMULATION MODE:** By default, scripts are in **Simulation Mode** `(SIMULATION = True)`. Run them once to see what they would do. Change to `False` to execute them for real.

---

## Step 3: Sort files into folders

`sort_photos.py` moves files into folders named "Month Year" (e.g., "January 2018") based on the date found in their filename.

**Setup:**
1. Download `sort_photos.py`.
2. Edit the file: Change `TARGET_FOLDER` to your memories path.
3. Change `SIMULATION = False` when ready.

**Command to run in your terminal:**
```bash
python sort_photos.py
```

---

## Step 4: Rename Content

Sometimes, the downloader does not give you a single video or photo, but creates a directory containing multiple files (usually the main media + an overlay image).

**The Problem:** The files *inside* these directories often have random, illogical filenames (e.g., a long string of random letters and numbers) that do not match the directory's name.

**The Solution:** This script renames the files inside to match the parent folder's name (which contains the correct date, e.g., `20180803_...`).

**Setup:**

1. Download `rename_content.py`.
2. Edit the file: Change `TARGET_FOLDER` to your memories path.
3. Change `SIMULATION = False` when ready.

**Command to run in your terminal:**

```bash
python rename_content.py
```

---

## Step 5: Merge Overlays (FFmpeg)

This script finds folders containing exactly one media file (JPG/MP4) and one Overlay (PNG). It merges them into a new file ending in `_FUSION`. It handles resizing automatically to prevent the text from being zoomed in/cut off.

**Requirement:** You must download FFmpeg (Windows Build). Extract the files from the bin folder and place these in the same folder where you run the scripts. You can follow this video if you need help: [https://www.youtube.com/watch?v=JR36oH35Fgg](https://www.youtube.com/watch?v=JR36oH35Fgg)

**Setup:**

1. Download `merge_overlays.py`.
2. Edit the file: Change `TARGET_FOLDER` to your memories path.
3. Change `SIMULATION = False` when ready.

**Command to run in your terminal:**

```bash
python merge_overlays.py
```

---

## Step 6: Cleanup PNGs
Once merged, you might want to delete the transparent overlay files (.png) to save space and to clean up the repositories.

**Setup:**

1. Download `delete_pngs.py`.
2. Edit the file: Change `TARGET_FOLDER` to your memories path.
3. Change `SIMULATION = False` when ready.

**Command to run in your terminal:**

```bash
python delete_pngs.py
```

---

## Step 7: Extract Files from Subfolders

This moves the files (original + fused) out of their dated sub-folders and places them directly into the "Month Year" folder. It deletes the sub-folder if it becomes empty.

**Setup:**

1. Download `flatten_folders.py`.
2. Edit the file: Change `TARGET_FOLDER` to your memories path.
3. Change `SIMULATION = False` when ready.

**Command to run in your terminal:**

```bash
python flatten_folders.py
```

---

And, that's it. I hope everything worked out for you and that you didn't encounter any problems. If you need help, you can send me a message on Reddit, and i will try to help you: u/lord_annso. Thank you for your trust!

