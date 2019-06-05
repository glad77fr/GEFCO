import pandas as pd

file = pd.read_excel(r'C:\Users\Sabri.GASMI\Desktop\GEFCO\RDD\RDD_Mapping.xls')
file = pd.DataFrame(file)

metadata = pd.DataFrame(columns=['Table','Séparateur', 'Colonne'])

def extract(data):
    beg=0
    for i,val in enumerate(data.itertuples()):
        print(data.at[i, "TABLE COLONNE"])
        if data.at[i, "TABLE COLONNE"] != "" and pd.isna(data.at[i, "LIBELLE COLONNE"]) :
            metadata.at[beg, 'Table'] = data.at[i, "TABLE COLONNE"]
            metadata.at[beg, 'Séparateur'] = ";"
            beg += 1

extract(file)
print(metadata)