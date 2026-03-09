#SC_malaria#
Sickle_cell_freq_het=open('data/Sickle_cell_freq_het.csv','w')
Freq_qq=0.0036 #שכיחות החולים באנמיה חרמשית (HbS,HbS) 
Freq_q=0.0036**0.5 #שכיחות האלל HbS (q)
gen=10
generation=0
Sickle_cell_freq_het.write("generation\tFreq_HbA\tFreq_HbS\tFreq_HbAHbA\tFreq_HbAHbS\tFreq_HbSHbS\n")#שורה ראשונה של הטבלה
