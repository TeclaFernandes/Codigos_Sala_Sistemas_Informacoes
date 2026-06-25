w = input('Informe a sequencia do automato: (a e b) ')

M = {}
M['s'] = {'a': 'q1', 'b': 'r1'}   # Estado inicial 's'
M['q1'] = {'a': 'q1', 'b': 'q2'}  # Estando em 'q1', 'a' continua em 'q1' e 'b' vai para 'q2'
M['q2'] = {'a': 'q1', 'b': 'q2'}  # Estando em 'q2', 'a' vai para 'q1', 'b' continua em 'q2'
M['r1'] = {'a': 'r1', 'b': 'r1'}  # Estando em 'r1', 'a' vai para 'r2', 'b' continua em 'r1'
M['r2'] = {'a': 'r2', 'b': 'r1'}  # Estando em 'r2', 'a' continua em 'r2', 'b' volta para 'r1'

s_atual = 's'
s_final = ['q1', 'r1']

for c in w:
    s_atual = M[s_atual][c]
if s_atual in s_final:
    print('Cadeia é aceita')
else:
    print('cadeia NÃO aceita')

########################################
# Teste de cadeia aceita

# Exe1: aba
# Exe2: babb
# Exe3: ababa
# Exe4: aabba

# Teste de cadeia NÃO aceita

# Exe1: abab
# Exe2: aabbab