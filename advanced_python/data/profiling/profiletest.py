import re
def make_re(pattern):
    return re.compile(pattern)

text = '''The quick brown fox jumps over the lazy dog'''
for x in range(10000):
    re.search('fox', text)
