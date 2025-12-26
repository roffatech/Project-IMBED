import csv
import random

# To use this code to plot random data points to dummy up a heatmap:
#
# 1. Get a geographical region with min/max latitudes and longitudes
# to define a rectangular region. This region should avoid private residences
# 
# 2. Enter the coordinates from step 1 in the statements below
#
minlat=39.14028
minlon=-86.56559
maxlat=39.14342
maxlon=-86.57194
# 3. Run this script
#
# 4. Get the coordinates from random_coordinates.csv and add them to the 
# table you are using for your heat map
# 

# Generate 200 random coordinates
coords = [
    (random.uniform(minlat, maxlat), random.uniform(minlon, maxlon))
    for _ in range(200)
]

# Save to CSV
filename = "random_coordinates.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latitude", "longitude"])
    writer.writerows(coords)

print(f"✅ Saved {len(coords)} random coordinates to {filename}")
