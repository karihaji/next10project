import os

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

base_dir = r"c:\Users\user\Desktop\Next100project\assets\logo"

for fn, color in colors.items():
    path = os.path.join(base_dir, fn)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace('fill="#ffffff"', f'fill="{color}"')
        content = content.replace('fill="#FFFFFF"', f'fill="{color}"')
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print("SVG colors updated successfully.")
