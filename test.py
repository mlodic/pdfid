import pprint
from pdfid import pdfid

pp = pprint.PrettyPrinter(indent=4)

TEST_FILENAME = "./JavaScriptClock.pdf"

def analyze_pdfs_by_filenames(filenames):
    # 1. Setup
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True

    # 2. Actual analysis
    list_of_dict = pdfid.PDFiDMain(filenames, options)

    return list_of_dict

def analyze_pdfs_by_buffer(filenames, file_buffers):
    # 1. Setup
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True

    # 2. Actual analysis
    list_of_dict = pdfid.PDFiDMain(filenames, options, file_buffers)
    return list_of_dict

def disarm_pdfs_by_buffer(filenames, file_buffers):
    # 1. Setup
    options = pdfid.get_fake_options()

    options.disarm = True
    # If you want to return the disarmed buffer 
    # instead of the results dict, set this to True
    options.return_disarmed_buffer = True

    # 2. Actual analysis + disarm
    disarmed_pdf_buffers = pdfid.PDFiDMain(filenames, options, file_buffers)
    return disarmed_pdf_buffers

def main():
    filenames = [TEST_FILENAME]
    file_buffers = []
    for filename in filenames:
        with open(filename, "rb") as f:
            file_buffers.append(f.read())

    # 1. Analyze PDF from filenames
    print("STARTING ANALYSIS 1")
    results_1 = analyze_pdfs_by_filenames(filenames)
    pp.pprint(results_1)

    # 2. Analyze PDF from buffer
    print("STARTING ANALYSIS 2")
    results_2 = analyze_pdfs_by_buffer(filenames, file_buffers)
    pp.pprint(results_2)

    # 3. Disarm PDF from buffer and return disarmed buffer
    print("STARTING DISARM")
    disarmed_pdf_buffers = disarm_pdfs_by_buffer(filenames, file_buffers)
    print(f"{disarmed_pdf_buffers['buffers'][0][:100]=}")

    # 3.1 Analyze PDF from disarmed buffer
    print("STARTING DISARMED ANALYSIS")
    results_3 = analyze_pdfs_by_buffer(filenames, disarmed_pdf_buffers['buffers'])
    pp.pprint(results_3)

if __name__ == '__main__':
    main()