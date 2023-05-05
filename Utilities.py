import csv



def ReadCSV_Dict (document_name, translate):
    list_dict = []
    list_dict_return = []
    with open(document_name) as csv_data:
        read_dict = csv.DictReader(csv_data)
        for row in read_dict:
            list_dict.append(row)
    headers = list(list_dict[0].keys())
    for d in list_dict:
        c=0
        aux_d={}
        for k, v in d.items():
            if translate[c]==0: #string
                aux_v = v
            elif translate[c]==1: #int
                aux_v = int(v)
            elif translate[c]==2: #float
                aux_v = float(v)
            aux_d[k]=aux_v
            c+=1
        list_dict_return.append(aux_d)

    return list_dict_return



def Top (list_top, n_top, key_sort,rev = False):
    list_top.sort(key=lambda x: x.get(key_sort),reverse=rev)
    list_return = []
    for i in range(n_top):
        list_return.append(list_top[i])
    return list_return

