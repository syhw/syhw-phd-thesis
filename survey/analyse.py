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

print ""
print "=================== latex table ==================="
print ""
print "\\begin{tabular}{|l|cccccc|}"
print "\\hline"
print "Game & Virtuosity & Deduction & Induction & Decision-Making & Opponent & Knowledge\\\\"
print " & (sensory-motor) & (analysis) & (abstraction) & (acting) & -1: subjectivity & -1: map \\\\"
print " & [0-2] & [0-2] & [0-2] & [0-2] & 1: objectivity & 1: game \\\\"
print "\\hline"

for g,v in games.iteritems():
    l = []
    n = 0
    for c in ['Skill','Deductive','Inductive','DecisionMaking','Predict','MapGame']:
        if not c in v:
            l.append(' X ')
            continue
        if v[c][-1]['n'] > n:
            n = v[c][-1]['n']
        l.append('%.3f' % (v[c][-1]['mean']))

    print "%s (n: %d) & %s \\\\" % (g, n, " & ".join(l))
    
print "\\hline"
print "\\label{surveygamers}"
print "\\end{tabular}"
print ""
    

print "=================== HTML table ==================="
print ""
print "<table>"
print "<tr>"
print "<th> Game </th><th> Virtuosity </th><th> Deduction </th><th> Induction </th><th> Decision-Making </th><th> Opponent </th><th> Knowledge </th>"
print "</tr>"
print "<tr>"
print "<th> </th><th> (sensory-motor) </th><th> (analysis) </th><th> (abstraction) </th><th> (acting) </th><th> -1: subjectivity </th><th> -1 map </th>"
print "</tr>"
print "<tr>"
print "<th> </th><th> [0-2] </th><th> [0-2] </th><th> [0-2] </th><th> [0-2] </th><th> 1: objectivity </th><th> 1: game </th>"
print "</tr>"

for g,v in games.iteritems():
    l = []
    n = 0
    print "<tr>"
    for c in ['Skill','Deductive','Inductive','DecisionMaking','Predict','MapGame']:
        if not c in v:
            l.append(' X ')
            continue
        if v[c][-1]['n'] > n:
            n = v[c][-1]['n']
        l.append('%.3f' % (v[c][-1]['mean']))

    print "<td>%s (n: %d) </td><td> %s </td>" % (g, n, " </td><td> ".join(l))
    print "</tr>"
    
print "</table>"
    
