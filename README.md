# Do all roads meet?

This is a simple python implementation of Depth-First Search in order to answer
a simple but ambitious question: can I drive from any intersection in the world
to any other intersection? In other words, *do all roads meet*?

We're going to answer this question using road data from Open Street Map.

## Installation

This project uses python to parse OSM data and run the DFS graph algorithm
on it.

For faster downloads and disk reads, we download data in OSM's [PBF format](http://wiki.openstreetmap.org/wiki/PBF_Format).
PBF uses Google's Protocol Buffer format, so you'll need to install that. We
use the `imposm.parser` python library to read OSM PBF files, which only works
with python 2.7.

To install everything, simply type

`./setup.sh`

## Running the analysis

To run the entire analysis, tyoe

`make planet-dfs`
