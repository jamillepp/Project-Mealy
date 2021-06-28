from mealy.alphabet import default_ans, default_s

def mealyMachine(s, p, o):
    print(s+p+o)
    if s not in default_s:
        print("Sua pergunta deve iniciar com QQQQOPC")
        return

    ans_group = default_ans[s]
    answers = []
    o_splited = o.split()
    for ans in ans_group:
        for w in o_splited:
            if len(w) > 3:
                if (w in ans["s"] or w in ans["o"]) and ans not in answers:
                    answers.append(ans)
    
    if len(answers) == 0:
        print("Desculpe, não tenho resposta para sua pergunta. Tente perguntar utilizando outras palavras.")
        return
    elif len(answers) == 1:
        ans = answers[0]
        print(ans["s"]+ans["p"]+ans["o"])
        return
    else:
        answers_n = []
        p_splited = p.split()
        for ans in answers:
            for w in p_splited:
                if len(w) > 3:
                    if (w in ans["s"] or w in ans["p"] or w in ans["o"]) and ans not in answers_n:
                        answers_n.append(ans)
        if len(answers_n) == 0:
            for ans in answers:
                print(ans["s"]+ans["p"]+ans["o"]+'\n')
            return
        else:
            for ans in answers_n:
                print(ans["s"]+ans["p"]+ans["o"]+'\n')
            return