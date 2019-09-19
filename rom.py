#モジュールのインポート
import random
import pprint
import csv
import copy
import evaluation

def stableMatching(n, men, women, men_preference, women_preference):
    #M=φとし、全員をフリーとする
    m_to_w = {}
    w_to_m = {}

    #peopleを空集合とする
    people = list()
    all_people = list()
    all_people.append(0)
    present_women = list()
    present_men = list()
    #all_people = m1, w1, m2, w2, w3,....mn, wnと並べ替える
    for i in range(n):
        all_people.append(women[i])
        all_people.append(men[i])
     #while all_people全員がペアになっていない do
    while all_people[-1] != 0:
        #peopleに先頭の人を加える
        people.append(all_people.pop(-1))
        man_preference = copy.deepcopy(men_preference)
        woman_preference = copy.deepcopy(women_preference)
            #if 加えた人が女性w then
        if "W" in people[-1]:
            present_women.append(people[-1])
            #while フリーの女性がいる do
            while len(w_to_m) < len(present_women):
                #任意のフリー女性（最初は加えた女性）をwとする
                woman = [w for w in present_women if w not in w_to_m][0]
                #wの選好リストの先頭の男性をmとする
                man = ''
                while not man:
                    if woman_preference[woman][0] in present_men:
                        man = woman_preference[woman][0]
                    else:
                        woman_preference[woman].pop(0)

                #if mがフリー then
                if man not in m_to_w:
                    #(m, w)をMに加え、mとwを婚約中にする
                    m_to_w[man] = woman
                    w_to_m[woman] = man
                #end if
                #if mが婚約中 then
                else:
                    #mの婚約相手をw'とする
                    another_woman = m_to_w[man]
                    #if mはwよりw'が好き then
                    if man_preference[man].index(woman) > man_preference[man].index(another_woman):
                        #wの選好リストからmを削除する
                        woman_preference[woman].pop(0)
                    #else
                    else:
                        #Mから(m, w')を削除し、(m,w)を加える
                        #w'をフリーに、wを婚約中にし、w'の選好リストからmを削除する
                        del w_to_m[another_woman]
                        w_to_m[woman] = man
                        m_to_w[man] = woman
                        woman_preference[another_woman].pop(0)
                    #end if
                #end if
            #else 加えた人が男性m then
        else:
            present_men.append(people[-1])
            flag = 'true'
            #while ある男性が選好リストをすべて探索しつくすまで do
            while len(m_to_w) < len(present_men) and flag == 'true':
                #任意の男性（最初は加えた男性）をmとする
                man = [m for m in present_men if m not in m_to_w][0]
                #mの選好リストの先頭の男性をwとする
                woman = ''
                while not woman:
                    if not man_preference[man]:
                        flag = 'false'
                        break
                    else:
                        if man_preference[man][0] in present_women:
                            woman = man_preference[man][0]
                        else:
                            man_preference[man].pop(0)
                if flag == 'false':
                    break
                #if wがフリー then
                if woman not in w_to_m:
                    #(m, w)をMに加え、mとwを婚約中にする
                    m_to_w[man] = woman
                    w_to_m[woman] = man
                #end if
                #if wが婚約中 then
                else:
                    #wの婚約相手をm'とする
                    another_man = w_to_m[woman]
                    #if wはmよりm'が好き then
                    if woman_preference[woman].index(man) > woman_preference[woman].index(another_man):
                        #mの選好リストからwを削除する
                        man_preference[man].pop(0)
                    #else
                    else:
                        #Mから(m', w)を削除し、(m,w)を加える
                        #m'をフリーに、mを婚約中にし、m'の選好リストからmを削除する
                        del m_to_w[another_man]
                        m_to_w[man] = woman
                        w_to_m[woman] = man
                        man_preference[another_man].pop(0)
                    #end if
            #end if
    #Mを出力する


    print ("組み合わせ結果:")
    pprint.pprint(m_to_w)
    evaluation.wM(men, women, m_to_w, w_to_m, men_preference, women_preference)

    return(m_to_w)
