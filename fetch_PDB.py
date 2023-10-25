import requests
from Bio import PDB

# Function to download PDB file by ID
def download_pdb(pdb_id, save_directory):
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    
    if response.status_code == 200:
        pdb_filename = f"{save_directory}/{pdb_id}.pdb"
        with open(pdb_filename, 'wb') as pdb_file:
            pdb_file.write(response.content)
        print(f"Downloaded {pdb_id} to {pdb_filename}")
    else:
        print(f"Failed to download {pdb_id}")

# List of PDB IDs you want to fetch
pdb_ids = ["1q94","1qka","1qr1","1qvo","1slg","1soz","1svz","1sys","1t1w","1u8h"]

# Directory to save the downloaded PDB files
save_directory = "pdb_files"

# Create the save directory if it doesn't exist
import os
os.makedirs(save_directory, exist_ok=True)

# Loop through the list and download PDB files
for pdb_id in pdb_ids:
    download_pdb(pdb_id, save_directory)

