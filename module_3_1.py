calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(word):
    count_calls()
    return len(word), word.upper(), word.lower()

def is_contains(word, selection):
    count_calls()
    word = word.lower()
    for i in selection:
        if word == i.lower():
            return True
    return False

print(string_info('Recommended'))
print(string_info('Visual Studio Code'))
print(string_info('First Second'))
print(is_contains('Distribution', ['working', 'DistRibuTion', 'Distribution', 'Tools']))
print(is_contains('Renderer', ['Process', 'Window', 'Chromium']))
print(calls)