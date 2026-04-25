import pandas as pd
import glob
import os

# 1. SET THE PATH (Double-check this folder name!)
path = r'C:\Coding Project'

# 2. Find the files
files = glob.glob(os.path.join(path, "*.xls*"))

print(f"Checking folder: {path}")
print(f"Files detected: {len(files)}")

all_data = []

for f in files:
    # This prevents the script from trying to read its own output
    if "Master_Report" in f:
        continue
        
    try:
        print(f"Reading: {os.path.basename(f)}...")
        df = pd.read_excel(f)
        
        # Only add it if the file isn't empty
        if not df.empty:
            all_data.append(df)
        else:
            print(f"Skipping {os.path.basename(f)}: File is empty.")
            
    except Exception as e:
        print(f"Could not read {os.path.basename(f)}: {e}")

# 3. The Final Merge
if len(all_data) > 0:
    print(f"Merging {len(all_data)} valid datasets...")
    result = pd.concat(all_data, ignore_index=True)
    
    # Save the file
    output_path = os.path.join(path, "Master_Report.xlsx")
    result.to_excel(output_path, index=False)
    
    print("-" * 30)
    print(f"SUCCESS! Open your folder to find: Master_Report.xlsx")
else:
    print("FAILED: Found files, but could not extract any data from them.")