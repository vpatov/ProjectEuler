def decrypt(ciphertext):
    ans = ''
    for letter in ciphertext:
        if (letter not in [' ','\n',',',"'",'?']):
            ans += chr((((ord(letter) - ord('a')) + 13) % 26) + ord('a'))
        else:
            ans += letter
    return ans


ciphertext = "inf,\n" \
            "v'z va n jrveq cynpr va zl urneg yngrl, \n" \
             "naq v arrg gb svther bhg rknpgyl jung v jnaq nag vs v pna unir\n" \
             "lbh va zl yvsr vs v'z tbvat gb nppbzcyvfu\n" \
             "jungrire gung vf. lbh unir orra bar bs zl\n" \
             "orfg sevragf blre gur cnfg lrne, naq v nz\n" \
             "irel tengrshy gb lbh'ir oebhtug gb zr, ohg v arrg\n" \
             "fbzr fcnpr jvgubhg lbh sbe ng yrnfg\n" \
             "n yvggyr juvyr ybatre, tb v pna cvrpr\n" \
             "gbtrgure jub jr obgu ner frenerngryl, naq qrpvqr jurgure vg'f \n" \
             "cbffvoyr gb unir lbh or cneg bs zl yvsr va gur shgher\n" \
             "\n" \
             "lbh oevatvat zr pbssrr be grkgvat zr\n" \
             "ng gur raq bs gur qnl vf fb njrfbzr ohg v\n" \
             "srry guvf jrveq oneevre orjrra\n" \
             "npgvat abezny naq unccl naq ubj v nz\n" \
             "npgvat, naq vg'f aby snve gb rvgure bs\n" \
             "nf sbe zr gb srry fb hapbzsbegnoyr nppregvat\n" \
             "lbh naq, va ghea, tvivat nal cnegf bs zr onpx\n\n" \
             "guvf fhpxf, v xabj, v whfg arrq n yvggyr gvzr gb pyrne zl urnq\n" \
             "gunax lbh sbe rirelguvat, cbbcurnqrq naq nyy\n" \
             "\n" \
             "v jbhyq fgvyy yvxr gb jevgr gubfr\n" \
             "yrggref gubhtu\n" \
             "hf ortvaavat gb abj\n" \
             "pbhyq lbh cvpx gur qngr?"


print(decrypt(ciphertext))