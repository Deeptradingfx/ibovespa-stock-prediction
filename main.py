import os
import pandas as pd
from datetime import date
from pre_process_ibovespa import maybe_process_ibovespa

raw_file = "COTAHIST_A2017.TXT"
processed_file = "ibovespa_" + str(date.today()) + ".txt"

def main():

	if not os.path.exists(processed_file):
		maybe_process_ibovespa(raw_file, processed_file)

	all_pd_data = pd.read_csv(processed_file, header=0)
	emae4 = all_pd_data[all_pd_data['cod_neg'] == 'emae4']

	print(emae4)

if __name__ == '__main__':
	main()