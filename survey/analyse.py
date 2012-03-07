import csv
f = open('gameplaySurvey.csv', 'r')
h = f.readline()
h = h.split(',')
r = csv.reader(f, delimiter=',')
games = {}
for e in h:
    tmp = e.split('_')
    if len(tmp) > 1:
        if tmp[0] not in games:
            games[tmp[0]] = {}
        games[tmp[0]][tmp[1]] = []
for row in r:
    if len(row) == len(h):
        for i,e in enumerate(row):
            if i > 0: #and e != '':
                tmp = h[i].split('_')
                if e != '':
                    games[tmp[0]][tmp[1]].append(e)
                else:
                    games[tmp[0]][tmp[1]].append('x')

for g,v in games.iteritems():
    i_verygood = set()
    for i,e in enumerate(v['HowGood']):
        if e == "Very good":
            i_verygood.add(i)
    for c in ['Skill','Deductive','Inductive','DecisionMaking','Predict','MapGame']:
        if not c in v:
            continue
        m = 0.0
        n = 0
        m_verygood = 0.0
        n_verygood = 0.0
        m_good = 0.0
        for i,e in enumerate(v[c]):
            if e == 'x':
                continue
            try:
                k = int(e)
            except:
                if e == 'both':
                    k = 0
                elif e == 'bestplay':
                    k = 1
                elif e == 'person':
                    k = -1
                elif e == 'game':
                    k = 1
                elif e == 'map':
                    k = -1
            m += k
            n += 1
            if i in i_verygood:
                m_verygood += k
                n_verygood += 1
            else:
                m_good += k
        m /= n
        m_verygood /= n_verygood
        m_good /= (n - n_verygood)
        v[c].append({'mean': m, 'mean_verygood': m_verygood, 'mean_good': m_good, 'n': n})

#print games
for g,v in games.iteritems():
    print '=================='
    print g
    for c in ['Skill','Deductive','Inductive','DecisionMaking','Predict','MapGame']:
        if not c in v:
            continue
        print c,
        for k,vv in v[c][-1].iteritems():
            if type(vv) == float:
                print '[%s: %.3f],' % (k,vv),
            else:
                print '[%s: %d],' % (k,vv),
        print ''

