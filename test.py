import sys
from langdetect import detect, DetectorFactory

# For consistent results across runs
DetectorFactory.seed = 0

def process_file(input_path, output_path):
    try:
        # Read the input file
        with open(input_path, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Perform language detection using langdetect
        language = detect(content)

        # Prepare the processed content
        processed_content = f"Detected Language: {language}\n\nOriginal Content:\n{content}"

        # Write the processed content to the output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(processed_content)

        print(f"Processed content has been written to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_file(input_file, output_file)

