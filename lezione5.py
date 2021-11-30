class CSVFile():

    def __init__(self, name):
        try:
            aper=open(name, 'r')#self.name
            aper.read()[0:1]
            self.name = name
        except:
            print('Il file non esiste')
        
    
    def get_data(self):
        try:
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
        except AttributeError: #scegliere tra i due:
            print ('No')

myobject=CSVFile('shampoo_sales.csv')
myobject2=myobject.get_data()
print(myobject2) 

