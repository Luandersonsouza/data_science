import pandas as pd
import matplotlib

data_set = pd.read_csv("venv/raw_data/ABONOP_122021.csv", sep=";" , encoding='ISO-8859-1')
#filtering columns of interest
data_set_columns = [ 'Nome','CPF','Situação servidor','Quantidade de anos no Serviço público',
			'Quantidade de meses no Serviço público','Ano/Mês inicial do abono de permanência','Val']
#print(data_set.columns.values)
#print(data_set.head())


data_set_selected = data_set.filter(items = data_set_columns)
#print(data_set_selected.head())


column_name = data_set_selected['Nome']
#print(column_name.value_counts().sort_index())


column_number_of_months_in_the_public_service = data_set_selected['Quantidade de meses no Serviço público']
#print(column_number_of_months_in_the_public_service.value_counts().sort_index())


#generate the grafo for column number of months in the public service
print(column_number_of_months_in_the_public_service.hist())