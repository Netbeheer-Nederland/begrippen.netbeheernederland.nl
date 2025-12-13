from rdflib import Graph

INPUT_FILE = "begrippenkaders/begrippenkader.ttl"
OUTPUT_FILE = "docs/begrippenkader.ttl"

try:
    g = Graph()
    g.parse(INPUT_FILE, format="turtle")
    g.serialize(destination=OUTPUT_FILE, format="turtle", base="https://begrippen.netbeheernederland.nl")    
    print(f"TTL file generated: wrote {len(g)} triples to {OUTPUT_FILE}")

except Exception as e:
    print("ERROR: The TTL file contains syntax errors.")
    print(e)
    exit(1)
