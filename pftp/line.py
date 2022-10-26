# 1, 2行目はリスト
cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B',
        'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]

# 関数名と引数のリスト
def pleaseConform(caps):
    # 変数の初期化
    start = 0
    forward = 0
    backward = 0
    intervals = []

    # FやBの区間を計算する
    # 1からlen(caps) - 1の値の範囲までを計算する
    for i in range(1, len(caps)):
        # caps[start]と異なるcaps[i]が見つかるまで計算する
        # if caps[start] != caps[i]がtrueだと区間が一つ終わり、このiから新しい区間となる
        if caps[start] != caps[i]:
            # 求まった区間はstartで始まり、i - 1で終わる
            # 開始位置、終了位置、'F'か'B'の区間を格納する
            # cap1の例：(2, 4, 'B') -> 要素の2番目から4番目までが'B'の区間として格納される。
            intervals.append((start, i - 1, caps[start]))
            # 前向き区間か後ろ向き区間の種類に応じて区間の個数を増やす
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            # 新区間はiから始まるので、startにiを設定する
            start = i

    """
    インデントのループが終了するが、実は全区間の計算はできていない。
    最後の区間がまだintervalsに追加されていない。
    cap1の場合、i=12のとき、start=11でcaps[i]は'F'でループが終わる。
    cap2の場合、i=12のとき、start=9でcaps[i]は'F'でループが終わる。
    したがって、最後の区間をループの外で追加する必要がある。
    """
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward = 1
    else:
        backward += 1
    # どちらの区間を逆向きにするか決定する。
    # 小さい方の集合を選ぶ。
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    # intervalsの区間tについてイテレーションし、前向きか後ろ向きかで選ばれた種類の区間に対して命令を表す。
    # t[0]：区間開始 t[1]：区間終了 t[2]：種類
    for t in intervals:
        if t[2] == flip:
            print('People in positions', t[0], 'though', t[1], 'flip your caps.')

pleaseConform(cap1)
