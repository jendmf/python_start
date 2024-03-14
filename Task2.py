translations = {'hello': 'привіт', 'goodbye': 'до побачення', 'cat': 'кіт', 'dog': 'собака'}
text = input('Enter word ').lower()

if text in translations:
    print(translations[text])
else:
    print('Not found')
