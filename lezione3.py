#inizializzo lista vuota
values=[]
#apro e leggo il file
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    elements=line.split(',')
    if elements[0]!='Date' :
        value=elements[1]
        values.append(float(value))
my_file.close()
#stampo i valori
print('La somma è {}'.format(sum(values)))