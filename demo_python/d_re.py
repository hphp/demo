import re

def d_search():
    r = 'dsfdsaaa'
    match_g = re.search(r'.*aaa$', r)
    if match_g:
        print match_g.group(0)

def d_match():
    r = 'dsfdsa.a.a'
    match_g = re.match(r'.*aaa$', r)
    match_g = re.match(r'd.*a\.a\.a.*', r)
    if match_g:
        print match_g.group(0)

d_match()
