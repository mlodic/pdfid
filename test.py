from pdfid import pdfid


def main():
    filenames = ["./test"]
    options = pdfid.get_fake_options()
    options.scan = True
    options.json = True

    # Analyze PDF from filenames
    list_of_dict = pdfid.PDFiDMain(filenames, options)
    print(list_of_dict)

    # Analyze PDF from buffer
    file_buffers = []
    for filename in filenames:
        with open(filename, "rb") as f:
            file_buffers.append(f.read())
    list_of_dict = pdfid.PDFiDMain([], options, file_buffers)
    print(list_of_dict)

if __name__ == '__main__':
    main()