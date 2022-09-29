def solution(s):
    s1 = re.sub('%%','pct_var',s)
    s2 = re.sub('%[bcdefgnosx]','{}',s1)
    s3 = re.sub('pct_var','%',s2)
    return s3

#You should select python3 instead of javascript