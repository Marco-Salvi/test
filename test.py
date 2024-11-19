import sys
import geojson  # External library that needs to be installed using pip

def write_geojson(output_path):
    try:
        # Define a GeoJSON Point using the geojson library
        point = geojson.Point((12.4924, 41.8902))  # Longitude, Latitude (Rome, Italy)

        # Define a GeoJSON Feature with the point
        feature = geojson.Feature(geometry=point, properties={"name": "Example Point in Italy"})

        # Create a FeatureCollection
        feature_collection = geojson.FeatureCollection([feature])

        # Write the GeoJSON data to the output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            geojson.dump(feature_collection, outfile, indent=4)

        print(f"GeoJSON data has been written to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <output_file_path>")
    else:
        output_file = sys.argv[1]
        write_geojson(output_file)
