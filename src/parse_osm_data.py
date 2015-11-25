import sys
from imposm.parser import OSMParser

parser = OSMParser()

parser.parse(sys.stdin)
