userslist = {
    'joao':'10293',
    'pedrinho':'espanca_idosa_na_rua',
}

username = input('')
password = input('')


if username not in userslist:
    raise ValueError('O nome não está na lista de usuários')
if userslist[username] != password:
    raise ValueError('Senha incorreta')

userslist['meudeus'] = 'meusenhor'

print(userslist['meudeus'])