file = {'YAHOO': 'YHOO', 'GOOGLE INC': 'GOOG', 'Harley-Davidson': 'HOG', 'Yamana Gold': 'AUY', "Sotheby's": 'BID', 'inBev': 'BUD'}
def ticker(filename):
    while True:
        company_name = str(input('Enter Company name: '))
        for k, v in file.items():
            if company_name == k:
                print('Ticket symbol: ' + v)
        break

ticker(1)

file1 = {'YAHOO': 'YHOO', 'GOOGLE INC': 'GOOG', 'Harley-Davidson': 'HOG', 'Yamana Gold': 'AUY', "Sotheby's": 'BID', 'inBev': 'BUD'}
def symbol(filesymbol):
    while True:
        company_name = str(input('Enter Ticket symbol: '))
        for k, v in file1.items():
            if company_name == v:
                print('Company name: ' + k)
        break

symbol(1)

