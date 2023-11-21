def solution(survey, choices):
    result = ""
    alpha_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0, }
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            alpha_dict[s[0]] += (4-c)
        elif c > 4:
            alpha_dict[s[1]] += (c-4)
    alpha_list = list(alpha_dict.items())
    for i in range(0, 8, 2):
        if alpha_list[i][1]>=alpha_list[i+1][1]:
            result+=alpha_list[i][0]
        else:
            result+=alpha_list[i+1][0]
    return result