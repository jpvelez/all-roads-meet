import sys
import csv
from imposm.parser import OSMParser

class RoadExtractor():
    intersection_coords = []
    road_ways = []

    def coords_callback(self, coords):
        for osmid, lat, lon in coords:
            self.intersection_coords.append((osmid, lat, lon))

    def ways_callback(self, ways):
        for osmid, tags, refs in ways:
            if 'highway' in tags:
                self.road_ways.append((osmid, tags, refs))

# Parse intersection coordinates and road ways from OSM data input.
extract = RoadExtractor()
parser = OSMParser(coords_callback=extract.coords_callback, ways_callback=extract.ways_callback)
parser.parse(sys.argv[1])

# Print out features for inspection.
# for ix, road in enumerate(extract.intersection_coords):
#     print road
#     if ix == 30:
#         break

# Save intersections to disk.
writer = csv.DictWriter(open(sys.argv[2], 'w'), fieldnames=['osmid','lat','lon'])
writer.writeheader()
for osmid, lat, lon in extract.intersection_coords:
    writer.writerow({'osmid': osmid, 'lat': lat, 'lon': lon})
