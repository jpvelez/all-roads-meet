import sys
from imposm.parser import OSMParser

class RoadExtractor():
    road_ways = []

    def ways_callback(self, ways):
        for osmid, tags, refs in ways:
            if 'highway' in tags:
                self.road_ways.append((osmid, tags, refs))

extract = RoadExtractor()
parser = OSMParser(ways_callback=extract.ways_callback)

parser.parse(sys.argv[1])

print extract.road_ways
