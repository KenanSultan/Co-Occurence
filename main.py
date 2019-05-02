
def create_lines_set(file_name):
    with open(file_name, 'r') as file:
        setirler = [set(i.strip().replace('.','').replace(',','').lower().split(' ')) for i in file]
    
    return setirler

def find_lines(words, file_name):
    setirler = create_lines_set(file_name)
    lines = [str(setirler.index(i)+1) for i in setirler if words.issubset(i)]
    
    return 'Lines: ' + ', '.join(lines)
        

while True:
    file_name = input('\nEnter a file name (q for quit): ')
    
    if file_name == 'q':
        exit()
    elif file_name not in ['einstein.txt', 'pimpernel.txt', 'gettysburg.txt']:
        print('Wrong file name!')
        continue

    words = set(input('Enter space-separated words: ').split(' '))
    print('The co-occurance for: ' + ", ".join(words))
    
    print(find_lines(words, file_name))