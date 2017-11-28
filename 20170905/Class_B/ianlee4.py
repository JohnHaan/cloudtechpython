company_dict = [
    {'name': 'naver', 'employee': 780},
    {'name': 'ncsoft', 'employee': 2250},
    {'name': 'netmarble', 'employee': 3850},
    {'name': 'com2us', 'employee': 708},
    {'name': 'nexon', 'employee': 4500}
]


def main():
    ncompany_list = []
    
    
    kcompany_list = []
    for i in company_dict:
        if 'n' in i['name']:
            ncompany_list.append(i['name'])
        else:
            pass
    for i in company_dict:
        if i['employee'] >= 2000:
            kcompany_list.append(i['name'])
            
    print(ncompany_list)
    print(kcompany_list)
        
if __name__ ==  '__main__':
    main()
