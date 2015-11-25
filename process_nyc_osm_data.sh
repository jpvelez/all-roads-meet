NYC_OSM='nyc.osm.pbf'
if [ ! -f $NYC_OSM ]; then
    curl https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf > $NYC_OSM
fi

python src/parse_osm_data.py $NYC_OSM
