class CSVFile():

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        lista_grande=[]

        my_file = open(self.name)
        for line in my_file:
            lista_piccola=[]
            elements=line.split(',')
            if elements[0]!='Date' :
                data=elements[0]
                valore=elements[1]
                lista_piccola.append(data)
                lista_piccola.append(float(valore))
                lista_grande.append(lista_piccola)
        my_file.close()
        return lista_grande

myobject=CSVFile('shampoo_sales.csv')
myobject2=myobject.get_data()
print(myobject2)
