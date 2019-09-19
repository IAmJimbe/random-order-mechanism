#モジュールのインポート
import random
import pprint
import csv
import evaluation

def stableMatching(n, men, women, men_preference, women_preference):
    #M=φとし、全員をフリーとする
    m_to_w = {}
    w_to_m = {}

    #whileフリーの男性がいるdo
    while len(m_to_w) < n:
        #任意の男性をmとする
        """print ("進捗:")
        pprint.pprint (m_to_w)"""

        man = [m for m in men if m not in m_to_w][0]
        #mの選好リストの先頭の女性をwとする
        woman = men_preference[man][0]
        #wがフリー
        if woman not in w_to_m:
            #(m,w)をMに加え, mとwを婚約中にする
            m_to_w[man] = woman
            w_to_m[woman] = man
        else:

            #wの婚約相手をm'とする
            another_man = w_to_m[woman]
            #wはmよりm'が好き
            if women_preference[woman].index(man) > women_preference[woman].index(another_man):
                # ある女性に対して男性の選好が現在の選好よりも好ましくない場合
                #wの婚約相手をm'とする
                men_preference[man].pop(0)
            else:
                #Mから(m', w)を削除し、(m,w)を加える
                #m'をフリーに、mを婚約中にし、m'の選好リストからwを削除する
                del m_to_w[another_man]
                m_to_w[man] = woman
                w_to_m[woman] = man
                men_preference[another_man].pop(0)

    #Mを出力する
    print ("組み合わせ結果:")
    pprint.pprint (m_to_w)
    evaluation.wM(men, women, m_to_w, w_to_m, men_preference, women_preference)
    return(m_to_w)
    