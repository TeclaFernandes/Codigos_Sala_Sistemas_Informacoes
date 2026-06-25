w = input('Informe a sequencia do automatao: (0s e 1s) ')

M = {}
M['q1'] = {'0': 'q1', '1': 'q2'}
M['q2'] = {'0': 'q1', '1': 'q2'}

s_atual = 'q1'
s_final = 'q1'

for c in w:
    s_atual = M[s_atual][c]

if s_atual == s_final:
    print('Cadeia é aceita')
else: 
    print('Cadeia NÃO aceita')

##########################################
# Teste de cadeia aceita:

# Exe1: 110
# Exe2: 1010
# Exe3: 000

# Teste de cadeia NÃO aceita

# Exe1: 101
# Exe2: 1011
# Exe3: 111
# Exe4: 1101