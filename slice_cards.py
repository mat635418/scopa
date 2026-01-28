from PIL import Image
import os

# Path to the full sheet you downloaded
sheet_path = "Carte_full.jpg"

# Output directory
out_dir = "cards"
os.makedirs(out_dir, exist_ok=True)

# Load sheet
sheet = Image.open(sheet_path)

# Determine grid size
# The Piacentine sheet has 5 columns (suits) and 8 rows (values 1–10 minus 8/9?)
cols = 5
rows = 8

w, h = sheet.size
card_w = w // cols
card_h = h // rows

# Suits order & values order you want to assign
suits = ["denari", "coppe", "spade", "bastoni", "extra"]
values = [1,2,3,4,5,6,7,10]  # Piacentine omit 8 & 9

index = 0
for r in range(rows):
    for c in range(cols):
        if r >= len(values): 
            continue
        value = values[r]
        suit = suits[c]

        # Crop
        box = (c * card_w, r * card_h, (c+1) * card_w, (r+1) * card_h)
        card_img = sheet.crop(box)

        # Save
        filename = f"{suit}_{value}.png"
        path = os.path.join(out_dir, filename)
        card_img.save(path)
        print(f"Saved {path}")
