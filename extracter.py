from pdf_to_txt import convert_pdf_to_txt

def data_printer(factura):

    string = convert_pdf_to_txt(factura)
    lines = list(filter(bool,string.split('\n')))
    custData = {}
    for i in range(len(lines)):
        if 'EMAIL:' in lines[i]:
            custData['Name'] = lines[i+1]
        elif 'FACTURA' in lines[i]:
            custData['BillNumber'] = lines[i+1]
        elif 'Vencimientos:' in lines[i]:
            custData['price'] = lines[i+2]
        elif 'Banco:' in lines[i]:
            custData['paymentType'] = lines[i+1]

    return custData

if __name__ == '__main__':
    # "FA20150518.pdf"
    custData = data_printer(input('Input path'))
    custData['Name'] = custData['Name'].replace("Â", "")
    print custData['Name']

    custData['paymentType'] = custData['paymentType'].replace("Â", "")
    print custData['paymentType']
