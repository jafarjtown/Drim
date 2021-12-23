

def Check(text, rules):
    tl = list(text.split(' '))
    rule = []
    for r in rules.all():
        n = r.forbiden_words.all()
        for i in n.all():
            rule.append(i.word.lower())
    for t in tl:
        if t.lower() in rule:
            return True
    return False