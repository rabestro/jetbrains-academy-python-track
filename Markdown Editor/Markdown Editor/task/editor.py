supported_formatters = \
    ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list',
     'link', 'inline-code', 'line-break']

while True:
    command = input('- Choose a formatter')
    if command == '!help':
        print('Available formatters: ' + ' '.join(supported_formatters))
        print('Special commands: !help !done')
    elif command == "!done":
        break
    elif command not in supported_formatters:
        print('Unknown formatting type or command. Please try again')

    if command == 'header':
        level = int(input('- Level:'))
        pass
