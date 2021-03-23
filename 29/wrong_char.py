chars = ['A', 'f', '.', 'Q', 2]

def get_index_different_char(chars):
    alphanum = [[i, x] for (i, x) in enumerate(chars) if str(x).isalnum()]
    anti_alphanum = [[j, k] for (j, k) in enumerate(chars) if not str(k).isalnum()]

    return alphanum[0][0] if len(alphanum) == 1 else anti_alphanum[0][0]


print(get_index_different_char(chars))
