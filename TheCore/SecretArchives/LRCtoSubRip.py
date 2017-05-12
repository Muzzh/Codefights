def lrc2subRip(ly, song):
    import re

    def modtime(s):
        p = r'((?:\d\d:)?\d\d:\d+)\.(\d\d)'
        g = re.search(p,s)
        print int(g.group(1)[:2])
        if int(g.group(1)[:2]) >= 60:
            reduced = int(g.group(1)[:2])
            h = str(reduced / 60)
            reduced = str(reduced%60)
            if int(reduced) < 10:
                reduced = '0' + reduced
            sec = g.group(1)[2:]
            new = re.sub(p, ''.join(r'0%s:%s%s,\g<2>0'), s) %(h,reduced,sec)
        else:
            new = re.sub(p, r'00:\1,\g<2>0',s)
        return new

    for i in range(len(ly)):
        ly[i] = modtime(ly[i])

    times = []

    for i in range(len(ly)):
        if i == len(ly) -1:
            times.append(ly[i][1:13] + ' --> ' + song + ',000')
        else:
            times.append(ly[i][1:13] + ' --> ' + ly[i+1][1:13])
        ly[i] = ly[i][15:]
    ans = []

    for i in range(len(ly)):
        ans.append(str(i+1))
        ans.append(times[i])
        ans.append(ly[i])
        if i != len(ly)-1:
            ans.append('')
    return ans

    
