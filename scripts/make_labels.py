import os


base_path = r"C:\Users\Jeevan kumar\Desktop\Geospatial_Project"
folders = ["oceanData", "road_and_shore"]

for folder in folders:
    img_dir = os.path.join(base_path, folder, "images")
    lbl_dir = os.path.join(base_path, folder, "labels")
    
    os.makedirs(lbl_dir, exist_ok=True)
    
    # Get all images to ensure we create a label for every single one
    images = [f for f in os.listdir(img_dir) if f.endswith('.png')]
    
    for img in images:
        label_name = img.replace(".png", ".txt")
        label_path = os.path.join(lbl_dir, label_name)
        
        # Format: class x_center y_center width height
        with open(label_path, "w") as f:
            f.write("0 0.5 0.5 0.1 0.1\n") 


    print(f"Success! Created {len(images)} labels in {folder}")
