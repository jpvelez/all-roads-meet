
data/nyc.osm.pbf:
	curl https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf > $@

test-graph:
	cat data/small_graph.txt | src/graph.py
