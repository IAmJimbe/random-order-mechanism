def wM(men, women, m_to_w, w_to_m, man_preference, woman_preference):
    w_Mm = 0
    w_Mw = 0
    r_M = ''
    for i in men:
        w_Mm += man_preference[i].index(m_to_w[i]) + 1
        if not r_M or r_M <= man_preference[i].index(m_to_w[i]):
            r_M = man_preference[i].index(m_to_w[i]) + 1

    for i in women:
        w_Mw += woman_preference[i].index(w_to_m[i]) + 1
        if r_M <= woman_preference[i].index(w_to_m[i]):
            r_M = woman_preference[i].index(w_to_m[i]) + 1

    w_M = w_Mm + w_Mw

    if w_Mm > w_Mw:
        d_M = w_Mm - w_Mw
    if w_Mw > w_Mm:
        d_M = w_Mw - w_Mm

    print ("w(M):" + str(w_M))
    print ("r(M):" + str(r_M))
    print ("d(M):" + str(d_M))
