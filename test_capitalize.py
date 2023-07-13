from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('The function woks incorrect')
if capitalize('') != '':
    raise Exception('The function woks incorrect!')
