from pdfminer.high_level import extract_text
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Extract text from PDF.')
parser.add_argument('--pdf', type=str, default='UEDC.pdf', help='Path to the PDF file')
parser.add_argument('--out', type=str, default='UEDC.txt', help='Path to output text file')
args = parser.parse_args()

# Extract text from the PDF and write to output file
text = extract_text(args.pdf)
with open(args.out, 'w') as f:
    f.write(text)
