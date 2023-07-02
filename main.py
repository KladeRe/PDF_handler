import argparse
from PyPDF2 import PdfWriter

def combine_pdfs(output_path, *input_paths):
    merger = PdfWriter()

    
    for pdf in input_paths:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()


def main():
    parser = argparse.ArgumentParser(description='Combine multiple PDF files into one.')
    parser.add_argument('output_file', help='Output file path for the combined PDF')
    parser.add_argument('input_files', nargs='+', help='Input PDF files to combine')
    args = parser.parse_args()

    combine_pdfs(args.output_file, *args.input_files)



if __name__ == '__main__':
    
    main()