from pdfid import pdfid

def main():
    filenames = ["./test"]
    oParser = pdfid.GetOTPParser()
    (options, args) = oParser.parse_args()
    options.scan = True
    options.json = True
    list_of_dict = pdfid.PDFiDMain(filenames, options)
    print(list_of_dict)


if __name__ == '__main__':
    main()