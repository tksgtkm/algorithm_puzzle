
caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

def pleaseConformOpt(caps):
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # この処理によって、最後の区間の識別ができるようになる。
    caps = caps + ['END']

    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # 最適化していないコードでは下記の処理を二箇所に記述したが、
            # このコードでは一箇所の記述で済んでいる。
            intervals.append((start, i - 1, caps[start]))

            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == 'flip':
            print('People in positions', t[0], 'through', t[1], 'flip your caps')

# 1パスアルゴリズム
def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps')

pleaseConformOpt(caps)

pleaseConformOnepass(caps)
