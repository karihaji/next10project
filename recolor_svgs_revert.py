import os
import shutil

colors = {
    "catchlogo (1).svg": "#607894",
    "catchlogo (2).svg": "#005f6b",
    "catchlogo (3).svg": "#dea876",
    "catchlogo (4).svg": "#0077b6",
    "catchlogo (5).svg": "#766a8a",
    "catchlogo (6).svg": "#967117",
    "catchlogo (7).svg": "#ff806e",
    "catchlogo (8).svg": "#a7a7a7",
    "NEXT10.svg": "#093065",
}

# The names we want to keep (replacing the old dummy pngs)
target_names = {
    "catchlogo (1).svg": "integrity_logo_dummy.svg",
    "catchlogo (2).svg": "challenge_logo_dummy.svg",
    "catchlogo (3).svg": "humanity_logo_dummy.svg",
    "catchlogo (4).svg": "innovation_logo_dummy.svg",
    "catchlogo (5).svg": "mission_logo_dummy.svg",
    "catchlogo (6).svg": "amusement_logo_dummy.svg",
    "catchlogo (7).svg": "revolution_logo_dummy.svg",
    "catchlogo (8).svg": "unison_logo_dummy.svg",
    "NEXT10.svg": "next10_logo_dummy.svg",
}

base_dir = r"c:\Users\user\Desktop\Next100project\assets\logo"

# 1. Revert to white and rename to replace dummy names
for fn, color in colors.items():
    path = os.path.join(base_dir, fn)
    target_path = os.path.join(base_dir, target_names[fn])
    
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Revert colors back to white
        content = content.replace(f'fill="{color}"', 'fill="#ffffff"')
        
        # Save as the dummy name but with .svg extension
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        # Remove the original catchlogo files
        os.remove(path)

# 2. Cleanup old .png dummies
png_dummies = [
    "integrity_logo_dummy.png",
    "challenge_logo_dummy.png",
    "humanity_logo_dummy.png",
    "innovation_logo_dummy.png",
    "mission_logo_dummy.png",
    "amusement_logo_dummy.png",
    "revolution_logo_dummy.png",
    "unison_logo_dummy.png",
    "next10_logo_dummy.png"
]

for dummy in png_dummies:
    dummy_path = os.path.join(base_dir, dummy)
    if os.path.exists(dummy_path):
        os.remove(dummy_path)

print("SVGs reverted to white, renamed to replace dummies, and old PNG dummies removed.")
