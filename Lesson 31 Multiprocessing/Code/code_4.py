# Real-world use case: Image Processing (CPU-bound task)
# Comparing single-process vs multi-process for resizing images

import concurrent.futures
import os
import time
from PIL import Image, ImageFilter

# Image paths from raw folder
RAW_FOLDER = r'D:\Desktop\Python_Programs\Lesson 31 Multiprocessing\Code\img\raw'
PROCESSED_FOLDER = r'D:\Desktop\Python_Programs\Lesson 31 Multiprocessing\Code\img\processed'

def get_image_paths():
    """Get all valid image paths from raw folder (skip files smaller than 1KB)"""
    valid_paths = []
    for f in os.listdir(RAW_FOLDER):
        if f.endswith(('.jpg', '.jpeg', '.png')):
            full_path = os.path.join(RAW_FOLDER, f)
            # Skip files smaller than 1KB (not valid images)
            if os.path.getsize(full_path) > 1024:
                valid_paths.append(full_path)
    return valid_paths

def process_image(image_path):
    """CPU-bound task: Resize and apply filters to an image"""
    img = Image.open(image_path)
    
    # Resize to smaller dimensions
    img = img.resize((400, 300), Image.Resampling.LANCZOS)
    
    # Apply multiple filters (CPU-intensive operations)
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img = img.filter(ImageFilter.SMOOTH)
    
    # Save processed image
    filename = os.path.basename(image_path)
    output_path = os.path.join(PROCESSED_FOLDER, filename)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    img.save(output_path, quality=85)
    
    return output_path

def main():
    image_paths = get_image_paths()
    print(f"Found {len(image_paths)} images to process")
    
    print("=" * 60)
    print("CPU-BOUND TASK: Image Processing")
    print("=" * 60)
    
    # Method 1: Sequential (Single Process)
    print("\n[Method 1] Sequential Processing (1 process)...")
    start_time = time.perf_counter()
    
    for img_path in image_paths:
        process_image(img_path)
    
    sequential_time = time.perf_counter() - start_time
    print(f"Time taken: {sequential_time:.2f} seconds")
    
    # Clean up processed images for fair comparison
    import shutil
    if os.path.exists(PROCESSED_FOLDER):
        shutil.rmtree(PROCESSED_FOLDER)
    
    # Method 2: Multiprocessing (Multiple Processes)
    print("\n[Method 2] Parallel Processing (4 processes)...")
    start_time = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(process_image, image_paths)
    
    parallel_time = time.perf_counter() - start_time
    print(f"Time taken: {parallel_time:.2f} seconds")
    
    # Results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Sequential (1 process):  {sequential_time:.2f} seconds")
    print(f"Parallel (4 processes):  {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x faster")
    print("=" * 60)

if __name__ == "__main__":
    main()