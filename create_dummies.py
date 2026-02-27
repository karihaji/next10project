import os
import base64

# 1x1 transparent PNG
png_b64 = b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
png_data = base64.b64decode(png_b64)

# 1x1 white JPG
jpg_b64 = b"/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="
jpg_data = base64.b64decode(jpg_b64)

work_dir = r"c:\Users\user\Desktop\Next100project"

logos = [
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

images = [
    "integrity_duotone_dummy.jpg",
    "challenge_duotone_dummy.jpg",
    "humanity_duotone_dummy.jpg",
    "innovation_duotone_dummy.jpg",
    "mission_duotone_dummy.jpg",
    "amusement_duotone_dummy.jpg",
    "revolution_duotone_dummy.jpg",
    "unison_duotone_dummy.jpg",
    "next10_all_dummy.jpg"
]

os.makedirs(os.path.join(work_dir, "assets", "logo"), exist_ok=True)
os.makedirs(os.path.join(work_dir, "assets", "image"), exist_ok=True)
os.makedirs(os.path.join(work_dir, "css"), exist_ok=True)

for l in logos:
    with open(os.path.join(work_dir, "assets", "logo", l), "wb") as f:
        f.write(png_data)

for i in images:
    with open(os.path.join(work_dir, "assets", "image", i), "wb") as f:
        f.write(jpg_data)

print("Dummy files generated.")
