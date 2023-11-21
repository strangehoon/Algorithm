def solution(survey, choices):
    result = ""
    alpha_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0, }
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            if c == 1:
                alpha_dict[s[0]] += 3
            elif c == 2:
                alpha_dict[s[0]] += 2
            elif c == 3:
                alpha_dict[s[0]] += 1
        elif c == 4:
            continue
        elif c > 4:
            alpha_dict[s[1]] += (c-4)

    if alpha_dict['R']>=alpha_dict['T']:
        result += 'R'
    else:
        result += 'T'

    if alpha_dict['C'] >= alpha_dict['F']:
        result += 'C'
    else:
        result += 'F'

    if alpha_dict['J']>=alpha_dict['M']:
        result += 'J'
    else:
        result += 'M'

    if alpha_dict['A']>=alpha_dict['N']:
        result += 'A'
    else:
        result += 'N'

    return result