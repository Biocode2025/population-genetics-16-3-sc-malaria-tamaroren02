#SC_malaria#
Sickle_cell_freq_het=open('data/Sickle_cell_freq_het.csv','w')
Freq_qq=0.0036 #שכיחות החולים באנמיה חרמשית (HbS,HbS) 
Freq_q=0.0036**0.5 #שכיחות האלל HbS (q)
gen=500
generation=0
Sickle_cell_freq_het.write("generation\tFreq_HbA\tFreq_HbS\tFreq_HbAHbA\tFreq_HbAHbS\tFreq_HbSHbS\n")#שורה ראשונה של הטבלה
while gen > 0 :
    Freq_p = 1 - Freq_q #שכיחויות בדור הנוכחי
    Freq_pp = Freq_p**2 
    Freq_pq = 2*Freq_p*Freq_q
    Freq_qq = Freq_q**2
    Sickle_cell_freq_het.write("%d\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\n" %(generation, Freq_p, Freq_q, Freq_pp, Freq_pq, Freq_qq))#כתיבה לקובץ
    #לדור הבא#
    new_Freq_qq = 0 #מתים
    new_Freq_pp = Freq_pp*0.98
    new_Freq_q = Freq_q/(0.98*Freq_p+2*Freq_q)
    new_Freq_p = 1-new_Freq_q
    new_Freq_pq = 2*new_Freq_p*new_Freq_q
    #עדכון נתונים#
    Freq_p= new_Freq_p
    Freq_q= new_Freq_q
    gen-=1
    generation += 1
Sickle_cell_freq_het.close()
