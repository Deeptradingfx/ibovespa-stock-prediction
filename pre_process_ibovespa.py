def maybe_process_ibovespa(file, output_file):

	f = open(file)

	# Create Output file
	w = open(output_file, mode='w', newline='\n')

	header = ["date", "cod_bdi", "cod_neg", "tp_merc", "nome_res", "especi", "prazo_t", "mod_ref", "pre_abe",
			  "pre_max", "pre_min", "pre_med", "pre_ult", "pre_ofc", "pre_ofv", "tot_neg", "vol_tot",
			  "pre_exe", "ind_opc", "dat_ven", "fat_cot", "pto_exe", "cod_isi", "dis_mes\n"]

	w.write(";".join(header))

	for line in f:
		registro = line[0:2]
		if registro == "00":
			# Header
			nome_arq = line[2:15]
			cod_orig = line[15:23]
			date_ger = line[23:31]
			reserva  = line[31:245]


		elif registro == "01":
			# Cotacoes historicas por papel

				date = line[2:10]
				cod_bdi = line[10:12]
				cod_neg = line[12:24]
				tp_merc = line[24:27]
				nome_res = line[27:39]
				especi = line[39:49]
				prazo_t = line[49:52]
				mod_ref = line[52:56]
				pre_abe = line[56:69]
				pre_max = line[69:82]
				pre_min = line[82:95]
				pre_med = line[95:108]
				pre_ult = line[108:121]
				pre_ofc = line[121:134]
				pre_ofv = line[134:147]
				tot_neg = line[147:170]
				vol_tot = line[170:188]
				pre_exe = line[188:201]
				ind_opc = line[201:202]
				dat_ven = line[202:210]
				fat_cot = line[210:217]
				pto_exe = line[217:230]
				cod_isi = line[230:242]
				dis_mes = line[242:245]

				content = [date, cod_bdi, cod_neg, tp_merc, nome_res, especi, prazo_t, mod_ref, pre_abe, pre_max, pre_min,
						  pre_med, pre_ult, pre_ofc, pre_ofv, tot_neg, vol_tot, pre_exe, ind_opc, dat_ven, fat_cot, pto_exe,
						  cod_isi, dis_mes, "\n"]

				w.write(";".join(content))
	w.close()