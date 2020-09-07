import re

s = '0123abc'

regex = re.compile('\w?')

# =============================
# matcher的用法
# ============================

# matcher = regex.match(s, 4)
#
# print(type(matcher), matcher)
#
# matcher = re.match('[ab]', s)
# print(type(matcher), matcher)


# =========================
# searcher的用法
#==========================

# searcher = regex.search(s)
# print(type(searcher), searcher)
#
# searcher = re.search('[ab]', s)
# print(type(searcher), searcher)

# =========================
# full match的用法
#==========================

full_matcher = re.fullmatch('\w+', s)
print(type(full_matcher), full_matcher)
full_matcher = regex.fullmatch(s, 4, 5)
print(type(full_matcher), full_matcher)
