# Download NYC Metro Extract OSM data in PBF format.
data/nyc.osm.pbf:
	curl https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf > $@

# Extract road features out of NYC OSM data.
parsed_data: data/nyc.osm.pbf src/parse_osm_data.py
	python src/parse_osm_data.py $<

# Test client for adjacency-list implementation of undirected graph.
test-graph:
	cat data/small_graph.txt | src/graph.py
