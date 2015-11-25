
data/nyc.osm.pbf:
	curl https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf > $@

parsed_data: data/nyc.osm.pbf src/parse_osm_data.py
	python src/parse_osm_data.py $<

test-graph:
	cat data/small_graph.txt | src/graph.py
