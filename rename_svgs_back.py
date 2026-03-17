import os

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

for orig, current in target_names.items():
    p = os.path.join(base_dir, current)
    if os.path.exists(p):
        os.rename(p, os.path.join(base_dir, orig))
