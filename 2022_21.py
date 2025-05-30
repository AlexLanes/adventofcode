import functools, operator

class MonkeyMath:

    type Expression = tuple[str, str, str]
    "`(digits or name, operator, digits or name)`"
    jobs: dict[str, Expression]

    OPERATORS = { "+": operator.add, "-": operator.sub,
                  "*": operator.mul, "/": operator.floordiv }

    def __init__ (self, s: str) -> None:
        self.jobs = {}
        for line in s.split("\n"):
            name, expression = line.split(": ", 1)
            if expression.isdigit(): expression += " + 0"
            left, operator, right = expression.split(" ", 2)
            self.jobs[name] = (left, operator, right)

    @functools.cache
    def value (self, job: str) -> int:
        assert job in self.jobs
        left, operator, right = self.jobs[job]
        return self.OPERATORS[operator](
            int(left) if left.isdigit() else self.value(left),
            int(right) if right.isdigit() else self.value(right),
        )

example = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
puzzle = """lsdv: fbnj * rhjt
jggb: rdpd + cqzw
ctqr: hnbn / zprm
qpmw: 5
vqhj: tbhz * jflr
hppq: 3
zlmd: wjnh * grdc
wzfm: dmgm * pjwp
nfqq: dlgl + mcpl
hqdz: gjpf + cqdg
dthw: 1
htrz: 5
tzgs: fzzb + lzbt
ddzz: rdfd * zqmg
mvdj: fgfh + smrh
htvq: 2
btjd: djln + njrn
nzlc: qmsl + dvww
cpvb: 4
srmr: ccht - vwwb
crqf: 3
hdvj: 3
rnmb: 2
bvcl: nlzn + rsdg
tsnj: 3
ztnv: cfjj + bftm
fqqn: 11
smrz: 5
rwgc: 2
vjvf: 3
cmhc: 3
sgmj: fntf * dfhf
nmlw: drfc * wtsv
hbjp: nfqt + cvnr
hjpm: 2
fbmg: vvzl * fdnq
bgct: hqhz + jqjp
ssvr: qbcs - sgqw
sfhw: smrz * cmhc
vmtf: 18
nvhf: 2
gtgq: 9
hznc: 5
nwpt: wdbj * gbsh
rgsh: nlwr / gjqf
mmln: vdrh * ssrb
pbsj: srdn * lqvh
bjcm: 12
nrjp: 3
pzjq: 17
rhtt: 14
fvgc: 3
cfqw: cqmq + mmqt
mgcc: jtwt + btvv
ntgb: 5
ctcv: tccv + qqww
mwpd: hqrq / wbfm
vfmw: mgzf + gdsg
lzmp: mcvt * gqwb
bpnl: 7
bmww: hpfb * cgzn
nlgt: 4
lfzz: 6
zdpj: rlff * jcnq
brwl: zlms * gnmt
ntnh: nmlw * tjmv
tdqg: 5
nqfj: jpnn + wnlv
wmpp: 5
pfws: 1
hhrv: 5
fpbs: jbcp - gcbr
wdmq: 2
nsjp: 13
pzjc: 2
vgwt: 2
wdqp: zlct + tptm
brzv: 11
svth: cprz - wbwf
vlfj: hhcb * qgfd
qvng: ttww * wfzb
fbjz: jndl + hglp
wcwf: mvrm + mbdv
zqlz: 9
dzdr: 12
zmlj: bccn - rmpd
hpzc: gwld * gdpb
jpnn: gwqz + vhzq
zdll: mnff + dpct
lhrf: jdnj - vhnt
zfbp: 2
vdzj: 3
fdgm: whpw + vqzs
dcgf: 4
gpsn: 1
vqvw: gchp * jtjm
jhfj: gjqs + jflt
bfpw: 3
root: wrvq + vqfc
wsrh: 2
qwgb: 3
fgfh: mzvl * bfcf
gdcz: 11
vsqs: 4
gzvj: dtjb * hhss
pwbl: zzrq / cmmf
dtjb: 2
lqpb: mztw + pcts
wnbq: dhzm + fwsl
fdcb: 15
fhzp: zcrh / lszr
ltcm: wggp + mpdj
zbdv: 4
bqwc: rdcz + jnlf
fncz: wnbq + qdjv
jfgd: 9
jvms: 12
tlwj: twct - wjlf
sqwp: 2
tgcb: 3
lpnr: sndd * jnfv
qzft: 1
hsvm: 4
gjtm: fvfz * rhfn
vzdj: qznh + qzlb
nzdt: cqbd * scms
nhlz: 17
qsgd: 3
wgpb: 4
sqtp: 3
rlll: fbjz - vnlv
jllr: jqnj * bpnl
vprp: 3
hhwm: 19
lvsn: mfcv * nbmn
shqc: 3
cgbw: dqhs + bczr
twvf: mtlr * rcpn
wblz: gnjz + pjqp
tsws: 3
nfbd: 15
dvjn: qlqp * pzlm
slgz: swfz * dczm
ldfr: jghq + cgbl
drfc: 2
rlzc: 16
qhbd: 2
bdwn: 7
fddg: nrbm + ptjr
jccb: 5
dzhn: 5
ndrh: 1
jmbq: 5
crdh: 19
cpjd: rrss + gbhg
bhqb: pbdt + ctpp
fjnp: 11
wbvl: 4
twlg: ncqs + bnfb
jphj: rsvb + cnpc
dclr: ntjt + nqpg
dnds: svpm + rmrw
ngvp: 13
bqds: dlbh * tfzs
zvlg: dvjn * rzsr
snnw: hdgl - mzhd
nmtq: 2
jffl: 8
ngdt: 2
vsqz: tzft + nhlw
tvlp: 16
tljj: nsjq * lrwg
zlct: mfhl * dqgg
lcmv: hthq + mpsz
cdlz: lzjv * mnjr
hlgn: 2
ddrv: wntb + wdcc
hdjz: vtgb * hhcs
rhqb: lpvc + bfcd
ttrm: 20
jsnn: gfwl + jwfj
jdft: 5
dfsz: ljcf * pcst
cjzd: qnms - shgz
grmn: 4
ftwj: 6
mlhq: 20
vdwt: 20
bznb: tbqp + rhrm
jhgl: 6
mdnc: wrql + pjln
hzrb: 2
mpsz: zjpq + vvzh
flnw: sbsc + zrbs
mrgd: 4
fzvh: 6
mswm: 2
jnbr: mtdm * wcrz
nlhg: bbvv + cjlp
qtmt: qsjz - htrl
lgzd: tzgs + pcgg
vqfc: vhhd * qbpd
mtbz: thsv * znbp
ltll: 4
vqqp: bwhz / lrsc
nvdb: 5
sbvv: mjtq * vqpd
vwjh: 8
htzg: 2
jzsg: 14
vzwv: 13
wbzd: hwvf + hwpv
qcht: 2
hwtn: 4
njqt: drht + ttgg
nlff: rjzt * rhtt
bpmm: 3
gnlf: gndr / vrhb
nfqz: tgcb * vhfn
gcrt: nnrf * qjqv
rhrm: zqlz + mrms
drvj: 6
czjf: qlnd + jdjd
gwsb: 5
nwpc: 18
wcrz: qdfv * zcwn
wcml: 5
bwrd: 2
sjnl: 5
stqg: fgtl / lwzn
fbvd: zmzz + gctj
lnzz: pdsf * qpvq
zfpm: jgrm + vqww
vbdt: 17
srsz: 5
tljr: hzsz * bhqb
dfcq: jczd * gpzv
smhr: 3
qczw: cngh * hntn
rmjf: 4
spdg: gldd + zflj
bqjb: 5
gfdn: 12
vtnj: qczw + fjmd
dnrr: 1
trpw: vsqs * vcfs
pppw: mmwr * vqts
tnzm: prlm + mhps
flmf: 14
ngpq: pwzl * mjzl
wthl: vnpt + grgh
mjms: nhgn + htjg
gndr: fdrs * hljd
qsvb: 4
mrzl: 4
lmhr: 20
dpjz: zbhn * gbhl
ldgf: 5
tzcw: hjbq + qpng
pwzl: 3
vjzr: 2
fjgp: cswl * fltg
bvpn: wcpj * fbvd
lqjd: 1
bfzv: lgzd + tvtb
blqp: mqzn / csbf
rcbw: 6
qcsh: 2
dfvf: mtvf + zcrl
gslf: 2
vmqj: 2
rmrw: nbwr * ncdl
flhn: 2
rhjp: vfzb * ptqj
lmdd: 9
czqr: 2
ddrl: 4
sqbh: 5
jfrt: 7
nsrb: 6
wjqr: vlbq * cbmz
pgsd: 4
mvrb: 7
lsqv: hhjr + mnjm
bfnl: 4
phbz: gnrz + gbtq
lfct: 3
rmlz: rdzt + gcbs
frdc: 9
mqfc: 5
sjfb: qjwg * vmqj
rjwb: fjhh + rbcq
cfwj: nfvl * czrg
crmj: 8
zcrl: 12
hslb: 15
sjbc: zznc * dsdr
lspf: 2
zgdb: jtcn + lrcv
wplt: 3
zrjt: 4
mhgs: 6
zngj: 3
fqsn: 10
vrmq: zdll + qvdj
dfjg: 17
gpwb: hcjb * rdjn
cmqg: glqp * bmqs
mbcr: tszr * npbn
hfjw: tcrl * zsgb
mdwt: tzhb * vlvh
ptpj: 4
nmlh: dwrd * ftjw
scms: 9
bwhj: 5
rvfv: zcfc * sqwp
zlfw: 14
pfjr: 4
qdsb: flmf / cbcv
nrbm: vmpc * fsfs
bgmd: fjgp + qnzd
prlm: 13
rlvq: qwdp + slgl
nngm: dnjc - nrnm
vzdl: 2
rmpd: zswh + jbsn
jwtr: sgsq * qvwz
nncj: 2
fgjj: mswm * czjf
qppr: 5
wfzl: 3
wmfj: cnch + mqgh
bcnq: wjqp + ptdh
ztzs: wjhl * lpdv
wcpc: jprs + mzth
lnwt: 2
rfjz: cqjp + fbnt
ffnf: 7
gmmf: 3
jzdb: cnfh * ttpt
tsth: 3
bnfb: 4
jnpv: 3
dbbm: 3
qcls: 8
fsqs: ppvm * fqlm
tdnc: 4
hrwn: vgcc + swct
bgrf: 4
bvqn: 4
rmbp: lzgt * zwtr
hwdm: 11
fjbr: 20
hjhz: wzzb * nwpt
tjfg: 13
pfhl: qpfn * jfhb
brzb: nvhg * vfpl
nlwd: 2
nvzq: 14
wwvq: 2
tnvr: wqtz + bcnq
gzvv: 2
cztp: 3
mmlt: 2
tspz: 2
vnpt: 18
tlvd: 11
tchw: 2
ljzd: zmtt + swss
sqzt: 17
hpzr: 4
lnfv: 2
hwzm: jzln - zcsf
dqsh: mwbn + rccq
tnmf: wclb * fqqn
frtf: nfrh + dpfh
rpll: 3
zrpq: 19
jzhj: cftm + hlrd
nhqv: 3
wfnj: 2
lpwp: ttmt + ntgw
hnbn: zvpb * wfrt
cfrn: 3
sndd: 3
dcbs: stvs + svcb
jbsn: bhwn + ncph
tzhb: 3
nhlc: rjjp * mngf
vsgq: nlgt + cthr
dpct: 5
zbjf: pfbw + ljqq
mwjd: 3
bsjp: 10
rhgf: 2
dhwp: 3
prqw: zqzw - vtzh
flbr: 13
qsjl: 3
ppgl: mldj + hbmd
snqz: 5
zcvf: 2
wvht: wdvs * mlzb
rnqp: lpbn - stgl
hrfq: qbvs * mmlc
fzjb: pssn * hfmp
htjg: shzr * fpbs
fdvq: wfnj * jmsb
jhrd: srzr + hqbd
sgqc: spjr - bqds
nsmt: fbnq + ldgf
fscw: vfdp - mtjt
jnjh: dhhr / mfcb
mnjm: sgqc * fgdl
lgpl: 2
phhh: 3
jjsm: rflb + vzqp
lbjs: 4
sdgj: djwb + mncd
wzzb: 2
hswr: nvhf * mfrv
wqft: 3
grbd: 2
czgp: 5
srln: dnds / wfln
nhpp: cdlz * btjd
sgqw: 5
bdsr: 3
hwdq: 5
qdfl: 4
pqzw: 2
zmzz: zftm + tcns
cwlv: hwdm + rnww
zsgl: 15
zcwp: mbzq * ghvr
znch: cmdc * jffl
hdjm: 2
rqnf: 2
rbrt: 2
shgz: hvwv * wtfp
nlnh: pmlv + pqbs
zrbs: vmgh * qstv
fqlw: 12
wgvv: 12
qchc: bfjm + fdcb
mqhs: 3
wzbf: pgnb + tnrb
sprd: 20
bnmw: ggmg + nmbs
tzvt: wvwq * flzt
vmtn: bdwn * ghhp
gzwf: 7
jmcr: gsll + fhtb
cfpc: jgtg * qbgs
dswv: 3
pqgp: qltn * qsmm
fdwc: 11
dvnq: tnmf * fgdj
jzln: smtq + crpf
cbnw: djfd + whps
zftm: rqrc + jrhr
pfvl: 3
rsqh: 9
qjnn: 2
njlh: gfjt * ngdt
nmnb: 2
ggln: bpfp + nnwf
wsqn: 5
btbz: jsvf * dlqj
qdfv: jpvq * chvd
fwvr: fbcr + cvzz
wzzh: 2
lppp: 7
fltg: cmsb * zfqj
hpbm: dfsz + hsjd
jwvn: 2
pwrq: 3
pstd: 5
hhfl: 3
zgbn: 2
nfvl: 3
dzlb: 3
lwmv: 4
bczr: zcdw * lhhn
ctqd: fcdp + lvpn
grvm: 4
bcwc: 4
fmsl: 3
lqnd: 8
jbbg: mwcv * gbvg
pjlz: trrw * dlgb
jgtg: 11
tmjj: jvnc * slnn
zcfc: 17
ncrr: 2
prrv: 2
drln: 2
zvbb: 2
lqqm: 8
rgtq: 2
cbzq: 4
bfnt: dngt * gcnf
nfrh: ptbd * dqdg
wrql: 19
cgfz: 3
mvtb: 2
dsvj: 17
bbqp: 11
srdf: qdfl + jgtd
pwwv: 2
vdql: 6
zsgs: 4
qbvm: 2
qznh: 19
pdps: 16
nsjq: hnvh + hzpq
psrb: qwrr + jssl
hvwz: 7
fhtz: 5
sdqh: ntvd * tsnj
lvrt: 16
zhwg: 2
wmcn: 1
vmdd: vmtf - fcvb
pwwj: 4
cqpz: 13
hhnw: 5
mncd: 6
vzvq: qwrm * rjsf
vggd: mrtc * dfnw
cpgd: 2
wfzb: pllp * gwvn
rhbn: qwjn * dtgc
hjzt: pspj + tsws
dlbc: 2
nhqc: gtqj + lthp
lgrj: rcbw + rdql
wjhd: 2
sblh: 2
sqsq: npns + mmls
jlmv: 8
spbh: wgdg - jrdz
lzjv: 4
zvqb: btgw / cdnh
zsll: 5
pvfw: fwhz / vqps
tfjc: 2
bnfc: 5
sbzc: 5
mnqr: 2
fchm: 3
vvnq: jtqm * cnhs
ljnf: 18
ztth: 3
rddg: fggl / gqtm
wdww: ztmd + hpbz
pvgl: 2
ljcf: 2
gnmt: 2
zphw: 3
tnnq: 5
qqww: 6
jgtd: 3
wjjw: 2
vhzq: fzmz + fpqz
gncw: lwzq + bbqp
ntjt: 1
mzvl: wwvq * ffcm
nlmc: 3
ptdh: nbsz + whhs
nqqj: 2
tdfg: lzct * dvrq
vwdd: 5
rjjp: bdlm / qtbl
cwbp: 3
mqnl: 2
hdhf: sfhw - zgqb
hhpw: wwqg * nstf
rspb: 8
hlrd: qmnw * dgcf
nbnn: 1
lfzj: wvpr + dcgf
hpwd: hchv - dzct
vqvc: 2
vwjw: jpjh * rqjm
ggmg: hsjv + dvnq
mqhz: 2
hrsc: 3
dhqp: mvdj * ptqd
wdqs: mfmg + fnrp
twmt: bvpn - qjfm
zjsg: vrmq * mqwh
mwzp: 5
jdvv: wjwj - wgsg
hrsb: ctqd * tlfc
njsq: 7
lwzq: 4
vdsp: lwnl + dqbf
lnsg: qwvg - jhfj
glzw: 5
lbvg: 3
fjsj: 3
qlnd: cjbl / ntfl
cnch: jvms + wvzw
szmm: 2
hhcb: lqvn + pclq
cdvh: 2
nhpb: 5
lnwp: 4
gdvc: fffh + qtch
nzjr: bsbh / cpjq
nchc: 4
hhmm: 5
jjgb: 5
njts: mdsg * tmhv
fgtp: 1
hjcb: rgtq * bvcl
mjfv: 17
hnvh: nfvs + cqzf
jqjt: 4
vbhj: pprq * qcht
lmjv: vnwf * zlfg
zqwb: 7
jmmb: hpbm - znzr
cmnj: 7
tljf: grqw * ltmw
hhzt: fjvc + fjbd
rpds: bnrz * ztlt
zggl: ptdw * brzv
swnn: 2
pdzh: 10
ctzd: wmsm + llcm
bdwl: jghw + wrzb
wqzr: 16
vnzj: 3
rvtm: 5
nnth: smlw / jwvn
wjwj: qwgr - btzm
glsz: grlp + sprd
jgwc: 4
lqvh: jvgm + cpzt
wdsc: 19
hfnp: 5
lstb: 5
wcvp: 16
sqml: rzvs * crqf
vfgh: nvzz * hwdq
hlns: 4
rjpg: chvl / rpjh
cwcl: mwht + zsbl
dbjr: 2
gchb: dvvw + ltfz
smzb: 7
gpff: mhts * zjpt
nhfh: nmnl * jhlq
qsjz: jnbr / vdql
chfw: 6
dlld: cwnw + nsms
fzmg: ddzz - nqvg
qdjv: rtlz + trzz
cjpq: 1
dsfr: 3
nzmm: zjsg + mvwp
mhts: 3
tlst: 14
htzl: 6
lfvr: vgbp + ztzs
qhpz: vqzf + mtbt
rsvm: jdnm / qbgh
rctz: nlff - tmtt
sqsp: nhlz + bnps
pmrw: jhqw * cqjr
cprz: gqcz * czqr
dbrn: bjps + cglv
pvdv: ghhh + dthw
dwqh: zrjt * ljhb
vfpl: 2
pgzc: 5
bctn: 10
ltpn: 2
zhlv: pgzc * cdhq
nrtv: rpds / dpgd
mbml: 3
jjbg: wcwf * hnqd
pspj: zwvq * zgcd
lfvh: lztb + mcwn
lhjg: rhqb * vzgn
flpq: sqsp + hlsw
vwmc: 3
ldpb: fqdv * btfv
qljf: vsqz * fqbq
qqtb: 2
fzzc: bjft * wqft
hhzz: zrbr * swgr
lnhs: wmqg * lnsg
qhrw: nbbd + wdww
btfh: ddld / hnwb
cftm: vltg + pvbv
vggb: 5
gtfh: qlws + hswr
ngmt: 2
rnnw: 3
rrzf: 3
hsjd: 5
ztwp: 7
lgqj: 2
tdlb: 5
hngp: pbcl - rdvw
jqwc: 2
cjpm: 2
trnv: fzmq - nnrg
qvjr: 4
tgwq: wtzb * bdwl
gmnm: bgrf * mhjh
jflt: 20
clpr: 1
mffv: 3
twbf: zmcp * mcgf
gltg: 2
twlj: wzzh * tbgb
clnc: lnwt * rjfg
chpw: gvps - zqnh
ncqs: 3
wjrc: 2
vgwz: bttm * srmr
dnlp: 3
zrhf: 17
ggsd: bsfb + sjmn
sblg: zmdz * fwcg
qmnw: nccc * lnwp
rjqn: zjtw * zbqq
qwns: 4
tjwr: 7
msqj: dfqj + frjv
dbgf: zfgr + tdnc
crtd: 3
wvdf: 2
gcrm: zvsp + lmbb
drcm: zlfw / lgpl
ggjc: rhfq * nnth
gspp: 3
vlss: vlfj + ntnh
lmtj: 2
hvrt: 2
fwwc: 3
gjqs: spbp + sjdf
sgsq: 7
gjjr: 5
spbp: jwzv + jqwp
lmdt: 5
drht: gzsf - lrjw
tppd: 1
ghqm: mdvm + qmfh
nvhq: qnqn * shmr
vzgn: 3
rhdw: 5
fgjg: 2
pcst: vvvd + ghzz
mzsl: 5
qgqm: 5
clhs: 1
nbvq: 3
zdth: 12
nmbs: pgsd * btlj
pqgg: 16
hbmn: 5
wqzs: 13
mdsg: 5
gwvn: gfdm + mqfc
gssj: phbz * hgfb
bpbg: 3
tgnd: 3
vfzb: zphw * gzvj
npgg: rmtg - tfds
scjq: nzlc + lfgz
bhwn: vhzc + pjzp
hcjb: rcwt + tcvf
hmvz: vgrl + snld
lmlr: rhjp + jdjj
cvgg: 7
vzqp: 3
szhw: 16
fdvt: 2
tnqh: gfrr * hbmn
qzrb: dlhf + rlhb
jnfm: tbpn + wzbf
qfzn: scjn + fnjd
rrss: 4
wwns: ntgv / dljq
mwlc: pzzz + qzft
mrcv: 2
bcfl: wfjj + rszh
gbbb: mmlt + mbjv
tmnj: twvf + gftm
ncsj: 2
ltfv: 13
htws: 16
ttzq: 5
mlzb: ngmt * dtgs
lzfq: fbqg + hhpw
bwbs: djcb + djrz
bnhf: pndl + hgrz
vcml: 17
ltmw: 19
znhq: 4
cdhq: qgrz + dnbf
vlbq: 4
dqbf: njqt * nrjd
hmtw: 15
rsjr: 3
pmfm: vlmf * dqlb
grgh: 3
brsm: 1
slfp: djth + tggp
fdnq: 3
jzzz: 3
wwqt: pvsn * wrgm
djwg: 3
humn: 1117
psmj: bnhf * qjnn
bpfp: zvsq * rpsz
ffjp: dswv * lmsr
zqph: vfgh * jzzz
tdwz: mwlc + zdpn
bsfb: gjrh * hqbp
bqzg: 4
hmtv: 16
ptjw: nnzn * vtmb
mfrb: 3
gjfj: tmnj - cnfv
brhg: 4
qthb: 14
gvps: ggqq * lmdt
sbsc: rffb / vtlh
nnrn: qvzq + zdsb
ptpz: 2
tblc: cldl + jgnq
zmtt: vlhh + mlpt
cpls: hqnb * gftf
dtfd: 5
trrw: 9
dtfg: wrjg * bhfp
bwwn: twmt / qsnb
nnwf: glsz + zgwd
jrtt: 18
mmlr: 5
jqjc: jdvv + hqnp
fmcs: 1
jdbc: 2
hmjj: 2
lfpl: 5
ghhh: wbfj + jqwc
mjtg: 5
hqbp: 3
qtjv: ncrr * rqds
hcvp: jmff * mspf
zqbt: 2
pjgn: 5
cldl: 3
tmhc: ztlf * vzfm
gpqs: 7
wcpj: 2
dndd: 2
bbbt: rjjh * sbfq
mtbt: brzb + spwp
dvwz: vdwt - cvfp
nrpv: mrfp * pdfb
smrh: vqft * mgcc
tjmd: 8
wfdd: 6
qhhc: bgdq - ngvp
ptgv: 8
rqcw: bqgc * ddrl
wjhl: wdrp * ggtb
lzwm: smzv + qzwr
nbvh: 4
fhhg: 5
mtfd: 2
rplb: 2
vnwf: 5
phfv: 2
fzzb: fqgc * tggm
cqsv: 4
lrlg: 4
rdfd: ljdg - gcvz
flzt: pfhl + vdsz
wdvs: srmn + wdcj
wfbd: 2
mdsn: 5
lsbm: zpgp / drvj
mztw: 4
rzqg: 2
cqhh: gfgz + wzrm
wqfw: whsh * bzgs
hfvs: 3
rpqt: 3
zjhw: fngt + btfh
bfsz: jjws * htmh
zjpq: nqqj * hhwm
hzpq: 2
vnlv: 14
dngt: 3
rnjz: 6
jwtp: 2
fwcg: bbqh * hwsp
fzmf: lsqv + mdzm
bqgc: fcht * jlfd
fgfw: 9
pcgg: 2
bztn: 2
hvdd: 2
lbwd: 4
prdw: grvm * zzsb
rdcz: mmnb * spfb
gbhg: rpqt + qsgc
vmcg: 2
wcch: tbdt + vqmr
mwtz: 6
bnrw: 3
qhrf: hdvj * swnn
njrn: znmr + vwdd
hfbw: 4
fcdp: 1
gftf: 2
wvfb: bbrj * srhp
pnpf: vwmc + pwwj
rshh: 7
gggl: mjtg * ptpz
ntnp: 2
qjtb: 3
sfzl: fpls + hdzc
tppj: 2
vpcr: lscj / qdsf
hpfb: brhq - qnnw
qlrn: nbbh * qsjl
pvbv: smst + cgvj
tbdt: sqml * rgtw
bgmm: jzsg - pznf
brhq: mlgr * shqc
vlzt: qwgb * srzl
mbvl: ntzh + jtmr
mhsw: 14
tmzj: zrsm - vpps
ghvr: 4
rrwf: zvlg + dfft
gqwb: pwrq + rjfd
rqvh: cpwj / zgfg
wpwn: vmbn * ggcl
cdqj: cnhp / pqzw
mtzv: 3
lshh: pzjc * wcqm
srzr: hcvp + vrpz
tjhm: 2
zrjj: hlpl - vcbj
fwhz: tgnd * ltcf
fnmg: mrwq / lmtj
vdvh: 10
sphp: 5
cbmz: 2
gvwr: 3
ptqj: 13
rrlj: dbbm * hrfq
djln: 8
pjdp: 1
shhb: brtq * dgmg
rvfp: srsz * qtvp
brtq: crmj + hvzr
wwwh: 3
cqzw: 16
sbfq: 3
crlj: 2
gqdd: cztp * fjsj
lsqm: 5
hbls: glzw * sqbh
jsln: nhms * wzzm
hchv: zpth * mrth
ztlf: gpff + tsjz
whsh: llsn * bgfg
jmnc: nvzb + qdvd
fgtl: humn - hdqv
hgfb: 2
bpbb: 3
ncfq: lmms - hblt
gwvc: 1
mmtz: pqgp - pzfp
mplq: 3
qrjq: 2
jfqn: phgd + jfqt
nbjt: gnrm * lrms
jrgc: 2
wbgn: chgv * qqgw
dcvd: 13
gqhp: zdgw * cjvs
wdcj: hlns + nstd
hntn: 4
bnps: jnjn * nshp
mnff: qvqf + fznm
hdpt: 9
dvjf: 16
sdww: 2
hdqv: qlrn / mqhs
fmbp: 3
ptfz: 2
cstz: hhzt * srzb
vcpc: 5
cnhp: 16
htzj: dsmw + jwhg
ltlj: zpnn + pfdm
mtdm: 12
pccn: gcrt + lnzz
dsdl: nvhq * mplq
gldd: 6
gjmv: 2
cwnw: fcfj * sfbd
mmls: 2
lmvs: 2
dhqb: vlmq * bvqn
wgfr: 2
twct: zdlz + prqw
zttc: lfzj - bbdb
cnpc: 12
zpgp: jqrm + wdqp
bbqh: 2
fqbq: zwcs * crtd
gpgr: hvtl / mqhz
bmnn: 4
vmgh: 2
pdfq: zfrf * rhdw
bcmv: 4
bzhj: bfdj * gvgd
qpfn: 12
qlqb: cpgd + vdrj
hpgl: 12
dqsl: chfw + ncjj
ljqq: wffb + gbrf
rqsq: 4
ppnz: htmm + ptpj
ztqj: bjfb + slvp
zgrz: 3
qmwh: gpph * blnh
fwsn: vlhn + clnh
gbbv: snbs + nmlh
rcws: 4
cmsb: 2
whth: 8
hljd: 11
zmsm: 7
lfrc: 3
crpf: zsgl + ddrv
zlms: nhsm + tljj
rjdv: 1
vjdw: tqrv + fdvq
rtlj: bfpw * ftqq
jrdz: lsdv * rbrt
dnhs: gtfh + ptfz
cdnh: 5
mgzr: hpzc + btst
hcjz: 3
bpqr: 3
sjgq: 17
dlvs: 17
zqpc: wbst * gslf
qzwr: 3
ngqq: vsrl + vpvn
hwvf: 4
ntwg: 3
lpdv: 2
jvzj: spbh * hltz
gdsg: 9
dgvh: 5
jwfj: dpjd * jqjr
lwhf: 9
rcpt: 7
zhhs: dmzf * fwwc
wlzb: 7
rztl: 2
qvwz: 7
hwzn: fqhh + vdzm
pjzp: 1
cpcl: 5
zzlm: 7
qgwd: 1
scgl: 1
bnrz: 2
nhnw: 6
vvrw: sqtp * pvgl
hvzr: gnbt * vdzj
dfsj: vwwf + wgvf
mmlc: 2
zwpl: 2
jhqw: 5
jdjj: mbmf * ctzd
rhfq: 2
cwhv: zjhb / tblc
ccht: hcht * dfvf
rnrc: 4
cnzj: 6
nfqt: tprh * hczj
cjmm: rhcj + rjpq
bgfg: 3
rfht: 14
dqhd: fcnq - tcll
rjfg: frzq + qwbj
fdqm: 11
vczr: 3
qnzd: ttvq * pmrw
pzfp: rlvq * mrcc
dnzt: 5
lhcc: 2
jpbz: 3
hwsp: pvgq + fqsn
bmlm: jhlv + nnmf
cvnl: gdvc * lbpb
wsln: 2
vtmd: wjmn * nwsn
mfmg: dnhs * hrcm
qqwb: 2
zjtw: ldnp + wwwh
bfdj: rrjg - lsbm
vnpz: 8
fjbd: tlvd + ggfm
hqbd: fdjw + vlzt
msgc: fftr + nztt
htmm: 7
jgtm: wcch + tvwt
qmdl: dnlp * qbbc
cstb: mbml * gtqt
hldw: 2
ssrb: tswc + mcch
tfcp: 4
pptf: fmsl * qrjq
wzzm: fppz + htpq
prrf: 5
bvgd: 4
fpfs: 4
qmhr: wqzg / hwfc
plzp: 2
hcsb: pbsj * vlss
hjwr: whhb - mdvl
lzqz: 19
prhc: sblg + zhhs
fjmm: njlh / nbzs
nlqn: 5
rvgj: 3
ffcm: bcqz + ngns
rccj: wbzd * lndf
vqbb: grhh * tvss
dsrp: mnpm * grsr
dlhf: ltfw + pvdv
jftc: lfpv + ssfh
tlfv: nlwd * prvd
nmvl: 4
jrhr: crqh * hmjj
nwml: 2
dqlb: 2
zczz: 5
cdqd: 5
lthp: cnzn * hpcr
hvwv: 2
ppzr: 1
zsrf: ptgv + nndc
gdwf: rzdt + vnzb
vdng: 15
wbmp: zbjf * wjjw
mwht: vjwl * vfzd
gwgd: 1
zjtz: 11
nrjd: 3
wswz: vmcg * gpqs
zpnn: gdfl / wfns
gqcz: gqhc + gzmv
ddsb: wsrh * tvsr
fhwv: 12
mhfr: 5
nvwq: pfsd * npgg
mwbn: rgsh * jfrt
hqrq: 14
bddl: vcml * qgvr
djrz: gcrm * zqwb
gtps: jqvj * jjgb
snbs: 1
smlc: zsll * ngch
rjqb: qcvr * lmgd
pclq: 8
mbmw: cwhv + nmdr
csmj: 2
vwqv: 2
fjvc: nfgm + rbwj
jsdg: cnbw * wfvn
mzth: zvqb + qbsz
tgqn: lpnr + zggl
znmr: ltfv * rsjr
rdql: flpq - qhdf
gwtn: 2
ntnn: 7
ntgw: qtmt * zgrz
bfjm: mzfb * pcdj
mdqj: 7
qnms: lmlr + btmb
mmnb: mzsl + fgtp
jjmz: 3
jtcn: grhd * bdtv
jtmr: fbrm * tfcp
mvhq: hrwl * qfth
srmn: 4
spwf: vqvw / pptf
qwbj: 4
nrcm: dlcg + fdpp
qgnl: jsfs * nbzh
pptn: 2
vgjd: lcmv + pdfq
pdjl: 8
lrch: bdpf + jqdc
zzrq: bmnn * dwqh
qhhq: rwff * jgwb
mbzq: wgvv + fwhl
hrpj: 3
srbd: gscl * zvmw
chnb: 2
vnwq: clnc / qbvz
gcbn: mqzj * nwml
qrnz: 4
rwff: 3
hsjv: 16
mlnd: hcvl * nggv
dtvc: 5
dvrq: bpht - lmdd
hjtg: 3
ljvf: 5
dbct: 2
fbps: 3
lrtz: 2
gmzj: gjbw + qlcr
ntzh: drjw * ztwp
tggz: jfvh + tmjj
phlg: 3
zjpt: 2
lwnl: 10
htnt: 3
nmnl: 2
hblt: fbhg * jphj
lfnr: 7
bgtw: 5
npns: 5
zgdw: vqzb + gggl
tccv: sqjf + ttzq
fzcm: bgct * bjtg
zbvc: rnrc * qchc
wgmv: 15
chgp: 2
pnbj: fzll * rddg
pgnb: lgfp * trpl
mmwb: 2
qjhb: 1
zqwr: 9
wrzb: vbdt * tspz
rpsz: 20
jtlq: 3
zglq: 2
qjqv: hzwb + djjp
hwlj: 3
gwjb: cwlv / brlf
tcll: 3
npgz: 4
bgwt: 16
stsc: 3
ttfz: jhlc + lpwp
hrcm: qcls * fppd
dlgb: jzhj + rtdq
wjnh: 2
qrmf: 5
hszr: bgmm * zhbb
vtgb: 3
gcnf: 3
vzzf: cljv + trlc
rwft: 6
fzrz: crld + rspb
rzhb: vczr * nvdb
mnjr: vsnb + zbdv
svwb: dpzj * dqwn
qdlz: wmrw * hsqn
jqgc: 9
pqbr: bgwt * fzzc
zdbz: 4
fpls: jttv / wgfr
jsfs: 4
bllb: fchm * wrjs
jrzh: gftv * wqws
zrsm: hjqt / mzff
blnh: 2
mzgb: 2
twgf: rhhw * jmjc
nvzv: cllh * rnvq
fmqm: mspt * lnfv
jmff: 2
gtrz: 18
cswl: 13
tcnb: ftqg / prch
phgd: vwjw * zhrf
zvnz: 5
vrjd: hdpt - gqtj
cqdg: nvgb * dnnr
sqtd: cbzq + rbwc
jlfd: zzlm + npgz
tqgm: hswj * cqpz
pjln: 2
lrms: 2
wqws: 3
pqbj: qrvg * vvzd
qpzz: zsrf * chnb
ljdc: hzrb * stsc
dtgs: 3
vlvh: 5
vmbn: hbls - szmm
gctj: bwbs / pcmv
mmht: 1
qnsd: lzfq + pqbj
qhdf: dgvh * zqgh
zvmw: smlc - fbps
mcch: 17
mzld: zqcv + hdjz
lbft: 2
hjqt: vpmq * wmfj
fbnq: 4
tjpf: 12
tptm: nthq + qpgt
dnnr: 9
gdfl: dlzp * hbpc
njjp: 2
cfrr: 4
whhs: dtdb * hfbw
ncjt: qmfq * rhdd
jfqt: 14
gwnb: 5
spsj: scls * dcnz
jqrm: wcpc - hwzn
jjrg: hrhf - tjwr
mmfh: 6
wfln: 11
lmzh: jpsf + ngnp
pdfb: fjbr + grmt
ldbb: 4
lngb: mwjd * nlmc
dfqj: 14
zrqn: 11
wrgm: 4
npcj: lfpl * lfvh
nfgm: 1
hvwq: 7
vdgf: rppj + fdch
svlq: 2
fhsm: vqhl * vzvl
mvrm: 10
bgbm: cjzd - nhpp
lpzz: 3
ghcp: gfnw * strd
slnm: 1
ftqq: wqfw + qtmq
dzwt: 5
tqrv: cbsd + bqcz
jghw: hbjt * qwcb
zhmp: 3
tljh: 2
wlrg: 8
ndvr: jjbg + qhrf
bjzv: fcvv * vzwv
jvgm: plwf * vgmc
gjpf: 1
jrvg: 3
brgf: fjmm * mcvf
lrsc: 5
nwsn: ggjc / sdww
cllh: 3
rrlf: 3
ncph: pctb * bwwt
rjww: 4
gvtz: cqsv * wpwn
rhpf: lwcq * hrsc
wbfj: lsqm * hwlj
nvgn: 3
spwp: phgs + dpbv
wfmv: tzrq + tpmj
mgzf: 2
llcm: nrcm * gspp
pfsd: 3
fcnq: 14
bwdb: 3
nrnm: 3
zbbq: 11
nfnp: 4
djjs: 14
hcvl: 2
djfd: mjvv * pqln
fjrm: ztnv - slft
cwgn: 6
szpp: 4
smzp: 5
pcmn: lsbv * hppq
tqsz: 2
chcn: dmjj + vdgf
zrbr: 2
lsrp: dndd * rvfv
ctvz: 7
mnpl: 4
qlpq: hjsn * npcj
gnrm: dlvs - zpln
fngt: 9
hczj: 3
jvnc: 2
dhzm: frpb * cstz
brlf: 2
mljs: 2
znbg: hpwn * fnfd
fjhh: qsrb * hpch
ftnh: 4
zzrp: 2
lbmh: jjsm + jnsg
sdgt: rsvm + rctv
nmrr: bpvb * flbr
nbzt: gbbb - rtjl
crqh: sqlf * lgqj
qpvq: 4
gcbs: wgmv + lfzz
bjtg: 7
mbmf: 7
shnd: 3
wggp: 4
zzsb: 4
llsn: 3
jczd: 2
fwlg: 2
vhzc: hvrt * lmrg
tswc: dlvr * phvv
gjtd: 7
rgvc: 20
bhhc: 3
pdsf: mhtj + sjbc
lzgt: 14
nbzh: ptfb / wfvq
vwwf: nvgn * mgmt
vhhd: hncl * dhtv
hnwf: brlh * ldgn
ztlt: qjhb + fwgh
zmcp: 4
ptbd: 6
clpj: wlfq + mtbz
hsrh: ccjp * scjq
vmjm: 3
mzff: 3
zfvc: cfrr * vzbf
qgfd: mffv * wmms
dzzz: pfws + lbmh
rlfd: 4
jpjh: 3
sltm: 2
btlj: cthh / rhgf
pmlv: nljr + jgdz
bmnc: vnzj * czfh
jnmt: 17
mmpl: ppgl * fgzq
fnfd: mlnd * dfdf
bwhz: czsl * nbzt
zpth: swhh + grwn
czfh: tdfg - pzjq
dlpl: 16
lflp: 3
qnng: fhtz * zsjf
njvw: frdc + nmnb
hzwb: mzfq + znch
wdzn: 4
hnqd: 2
vjwl: njts + ldpb
hqnp: bnmw / vqvc
hfbs: ngqq * vbgw
hfmp: 20
twjp: 6
hwpv: 4
dswn: jwnh * vpzc
btqv: zctl * sgmj
rpbv: 3
nvzb: ngpq / rgcb
msmp: tnqh * dsbp
tfds: 2
bbrj: hpgl * bqws
phhc: 5
vltg: 2
pqsv: fwhv * vplf
djcb: jvzj - pnbj
grqw: 5
stgl: 5
gtqt: 3
qhth: 1
gswt: 5
mpdj: 3
pmdg: bjtf * nwst
mhtj: 5
lrbf: 2
wvsb: 8
bntn: fzcm / wmpp
qttd: 4
dpbv: 11
swss: 16
wnld: 3
wtzv: rwts + rgvc
dbnv: hjcc + wfgm
nbzs: 2
qwgr: rlzc + cfpc
svgg: 5
zqcv: 16
qsnb: 2
dhtv: qgpc + znbg
rsvv: 5
cfmt: bcwc * bcwt
cwqw: sbmb + rnbq
thjc: 5
ptfb: nvtb * ttmh
vhlg: jwwl * cgfz
btst: vtmd + hbrt
wjqp: ctcv - zhwg
dpzj: 4
bnpz: wnsj + htws
wnwr: 12
hswj: 4
wntb: hmvz + hwjf
dsdr: 2
mspf: gtrz + rbtv
ndsl: 2
btlz: 6
jhlq: 3
nbmn: 3
fjwh: qqgj + tgwq
zdlz: hjpn + zfpz
gzmv: mdwt + vwnt
scnw: 2
zhzv: 1
hjpn: 19
wbst: tsth + nvhw
hcht: 2
fpts: 13
ttmt: vmhr * gvwr
qgdg: rrbq + ftnh
zhbb: 3
zvzp: dbct * vfmw
zmnc: blgq * jmsj
dzhs: fdgm * mvtb
zbzf: 2
rmrq: 2
blsc: 15
mtlr: 2
pqtw: 2
ddld: vhjj * rcwh
nlwr: cfjg * nrtv
lmcp: 7
fhlf: lbvg * smzb
tlvp: qrfn * cjmm
cnzn: gmmf * zgbn
qzdz: bstz + gtps
fsdr: 2
nvhw: 4
wfgm: dmsg * bctn
fjhb: 10
zbvt: mrbd * rcpt
cthr: 2
cmdn: rccj / qbvm
mfhl: 2
vfzd: lvsn + bjjn
vbhz: 2
gfsz: 18
hpcr: 5
wzdq: wzfm - mtns
rqds: fgfw + dsrp
njww: 2
gtzc: tmzj * dmqf
lqcs: 3
smvl: jrvg * rfjz
gwzt: cfnp * bmpt
vqrv: gjvm * bgmd
ddfg: fgzp * mmgv
nhmc: 4
pbcl: lrbh * fscw
fhtb: csmj * gwjb
dpjd: 4
rpjh: 2
vmhr: 9
fqgc: ftft + nwcj
vqpd: 2
twqj: 10
swct: 4
mnsg: dsmg + mtmt
gnrz: hmtg + pqsv
mlgr: jpbz * gnlb
cqbd: qghp + ncvm
zglh: pcls + gtgq
jwnh: 5
jqjp: 4
mbdv: 1
qzjs: 7
prch: 2
wmms: rvfp + fmvq
snnd: gfrh * lfvr
zdng: vwhr * rrlf
mtlh: wdsc + jrqq
dgcf: vtwl * qwcd
fznm: 5
nblb: fqlw * svhg
ttmh: 2
rcbp: nblb + wphd
rnmv: 2
hthq: smhr * czmb
mjzl: hjwr + fmqm
fppd: 8
hhht: vggd - dqsh
jwnm: 17
jcnf: 2
zdvc: vqct * qbrt
swfz: szmt / tlts
gjqf: 2
mrgl: mdqj + mrcv
hlfj: zbrw * dszl
mcvt: tpls * qjtb
qcvr: 7
bgzn: 11
nvtb: mdsn + hhzz
rbcm: 10
nndc: bpmm * ffnf
ngcl: vtnj + wrvm
fbhg: rrzf * qgnv
bftm: 1
tqcd: dcwb * zdfc
qlst: 3
bbvv: 3
lhhn: tjmd - ppzr
hjsn: 2
tnrb: zlcj * bsjp
pzvh: jlmv + wsqn
tbqp: gvbg + scgm
hpwn: vqrv + tbgr
bphs: 5
zdgw: 5
qtch: 6
fppz: bhhc * phlg
rhvm: 9
dtdb: 8
mjtf: 5
ssvc: 3
wbwf: hbcp + qnng
fdch: fqlf * dbgf
fqlm: srpb * bgbm
csbf: 7
lvzd: drln * rzhb
jbcp: gdrp + vnpc
qnnv: 3
bqtw: phqc + dpsd
hsqn: plzp + svgg
stlb: 8
vqct: 18
cthh: vrmh - scgl
qmfh: 1
gvgd: 3
mbjv: jljp - rfht
pfjv: nvrw + nhnw
sfgd: 2
zsgb: 2
bzgs: 2
bwwt: 4
wtsv: tggz - lfpt
cmmf: 2
rptl: 8
gchp: 2
tfvh: 3
bjtf: 2
pcdj: 2
ttfg: 7
cjrp: bczv * cwbp
dthv: 5
dlcg: zttc * wvdf
cgbl: mtfd * zpmb
rcwh: 11
pntb: 5
hhcs: 7
vwhr: 3
pctb: 4
wfvn: 6
trpl: phhc + zhhb
htdq: 4
jssh: 2
qspp: 3
fmqs: vlrb * dswn
cncl: fpts * hrnp
sjtq: rlll + bzjj
btfv: 7
vdzm: cngl * zmnv
lvfn: svlq * fwsv
mtjt: gbgz * cnls
htrl: 19
lrcv: qhlj * bgfz
pllq: 2
nrld: 4
zggd: vzbw / rcmw
phzb: 2
grdc: dlpl * wcqs
rdjn: tflt / rwgc
cdgb: rrwf * ghlw
slfz: hpqf + qgwd
zdsb: 17
qwrr: zgdw + bddl
dqqp: bmnc + btbz
lmnb: 7
hpdt: jqfp * zdbz
jnjn: 3
rnvq: lbwd + ztnh
nfvs: 4
chrl: lnlp + blgw
dtzf: lzqz * bztn
dgmg: 13
nqvg: dtjc * pptn
qvfn: 2
vtzh: dbjr * ltlj
fwrl: twgf / zzrp
zrdm: zhzv + mhgs
btvv: 3
jbpc: 4
gcvz: 1
vtwl: 2
zbqq: 2
tvwt: 3
bczv: 2
lpht: ftbg - bpbg
rstq: 3
dvww: zdth + wvlh
mmbj: qhhq * wjqr
jtmm: zpzh * bgtw
vqzs: qvlh * jwqq
dwcq: 8
cbcv: 2
hdmm: mzwg + qljf
wgvf: wqzr + gpvl
vtlh: 9
cfmz: ltwl * bzzn
njpd: ndvr + qlqz
dsmg: dhwp + cwgn
qtbl: 2
gbrf: lrrv / fpfm
fggq: 6
rpwb: 2
wfrt: hjzt / fgjg
chrw: 5
pncj: pdbq + znhq
qwdp: fglh * wdhv
dzpv: 3
cnhs: 5
hphj: gtzc + ggsh
mrbd: 4
dlcl: 2
ptjr: mmht + sfzl
lbpb: 2
nmgc: 3
nmdr: fjwh + dwnm
jrqq: hhrv * stlb
tvhj: 4
gfmv: mjfv * csdr
lvwt: bgbl * rmbz
rlvj: 5
hglp: hlpf * hvwz
cjtb: mmtz / htdq
trzz: ltcm * nrjp
rrjg: lmzh / wdgp
nccc: 2
jslp: 2
whpw: tqzq + fwnr
lmsr: 2
bfdw: bmvt + ptjw
bzjj: bmlm * tppj
dmsg: 10
zqzw: gcfr * spbs
lfpv: 5
pssn: prrv + rlfd
frpb: 2
mfcv: 2
mcpl: 17
rhfn: nzmm + gwzt
vqts: 5
jwbw: cdjs + tjpf
snsl: zhmp * fwrl
rjwz: rshh * mljs
gpmp: dvwz * bjzv
nggv: 3
ptqs: 4
nztt: whth + pjdp
ngnp: jcsn + grzl
pwhn: gshr + hndq
wdgp: 3
pvzc: 4
sbmb: cgjm * jssh
cqjp: fsdr * dbrn
smvw: 2
gjpc: mtlh * djwg
jwhg: 15
djjt: 2
mrth: 3
pcvt: sdgj + bsss
nfbw: cmqg - gwsl
zvfn: pqgf + njpd
pbsb: 7
vlrb: vqqp / spdg
chgv: zsgs + wmcz
jljp: dzzz * bsrc
jdnm: jggb + jsnn
srhp: nfbt * lpht
tggm: 2
fsfs: tlwj / pdmd
rhcj: swqs * ncfq
dnjc: qdsb * bwjh
dpfh: bgpq + pclf
jnlf: psrb + hqdz
wrvq: cfqw * mbmw
zpmb: dzdr - gwgd
ztmd: zjhw * nchc
hndq: qmdl / dzpv
dnfh: 2
tcrl: zgdb + ttzr
hvtl: cgsf * hldw
qbrt: 8
qjcj: 2
hlpl: vdpl * mmlr
ccjp: wmcb * jqjc
jhlc: brwl - qlqb
fbnj: zczj + crdh
wcqs: 2
rjsf: 3
cngl: 3
qbgh: 2
bwrb: 11
wvwq: 2
fhgm: 19
scgm: 1
mlqb: scnw * tgqn
fgzp: 2
tjmv: nvzv + ptnf
dqdg: gtpp * nzdj
gfwl: cgqf * jsgm
wrjs: 5
bmtd: 5
ffds: 2
qlcr: hngp / wsfc
sqjf: mmsv * gnwd
rcpn: dfsj + twbf
qmgs: hdhf + mzld
lhnz: 6
hwwc: 4
snrd: cmsc * qsgr
dqgg: fncz + qhpz
snld: 20
lszr: 3
dvmz: 3
jgwb: 5
wvlh: tfjc * rcbp
rzdt: sfgd * fsgb
fwhv: nhqv * pdgb
wnvw: 1
lsbv: 5
rqrc: jgwc * btns
tmtt: mcmr + ssjp
dlzp: 3
nbmm: 2
qlpd: rlpl * tnnq
mldj: vrdm + lhzr
grlp: wnld * lzzt
gbtq: pvzc * twlj
dbqz: 18
sfdg: 11
qhlj: 9
nvrw: 7
rbwc: tfrs + mvbr
csbg: ffjh + dnrr
vjbf: 3
bbvj: bllw - wdzn
svcb: 13
vlhg: 2
frnm: 2
srdn: 17
svpm: prsf * hghl
prvd: 3
dfdf: qsgd * chpw
qrvg: 18
jcnq: 2
qfth: 5
tbpn: lsrp * hzcl
vnpc: wthl * qnnv
zgcd: 7
cglv: 20
lrzq: lnhs + dbnv
slvp: nqwn - hsrh
jhlv: 3
zvsq: gqdd - rnnw
chsv: gmzj * ffds
dtvh: 11
rlff: 13
vwwb: qljv * wplt
wfns: 2
ncdl: 3
jmbb: 4
mrms: 7
bjmf: 5
gpph: fdqm * fvgc
clcp: bqzg * gdcz
cgjm: jllr + zrjj
fpfm: vdvh - djsg
qstv: lrgw / zcvf
psgp: 3
vhfn: ndrh + nhdt
dpgd: 2
jtjm: ztth * bcfl
rtdq: lqcs * snvr
hpqf: 6
rflb: 3
ttzr: jrbc * rfgs
rpwv: 5
rbcq: wvgz + nsmt
lvpn: vbhz * cczj
qmsl: cjwz * gwtn
bttm: 2
jcsn: cpsr * mdwj
lnlp: snmc + msqj
ttww: wnvw + lqpb
smzv: 6
rcwt: 12
zlfg: 5
ljdg: vnvt * ltpn
cflf: 4
vgbp: rjwb - prdw
crgr: 3
whlw: twqj * nzcc
mrcc: 2
jssl: gnlf * ccqw
lrwg: lmnt / ltll
nfbt: 4
fftr: nsjp + cqhh
pqst: drjj * bnhd
zcns: dnfh * tvlp
pclf: tnzm * fpfs
mtvf: 7
rvsd: ntsm * lhcc
lhzr: qlpd + jsln
lrlm: btqv / fggq
wzsw: 2
hcpq: mrgd * mnpl
bsss: 1
gtbg: 2
vpqh: lvwt * qspp
vcfs: ftpd + jcnf
tzhz: 15
zznc: 7
btgw: tfgm + smvl
jmsb: ccdh + pncj
bgqr: jtmm * lwmv
mwlg: 2
ttpv: 4
jgts: 3
nwst: 4
brmb: 3
mtns: 5
ndgq: lrwz + wjhd
mdvv: 3
cpsr: pmjb + ghds
gpzv: 4
smtq: gjtm / pqtw
qpst: tcnb + csbg
grhd: 2
cjwz: tljf + ljfd
dmqf: smzp + sqfn
jmsj: 9
drjj: 2
hlpf: 9
wdbj: 5
ltcj: 3
clsc: vlhg * bqtw
jgnq: 4
wzpn: 5
nqpg: vwjh * htjj
slgl: zqbt * sqrw
gdjz: 3
bzzn: gbbv + fhsm
rqpn: htzj * pwwv
ptqd: cdns + hpwd
ntvd: 2
qlqz: lfct * nbvq
wbfm: 2
qbmw: rqnf * vdsp
gsll: 5
mmwq: 1
dsmw: 4
mmqt: 3
grsr: pdps + rvgj
gtpp: 2
cpjq: 5
ftjw: 2
jfbn: 6
grhh: lmjv + nrvz
hbjt: nhcj * wjns
vvzl: 3
jmjc: ssvr + mzgs
scjn: slfz * bllb
jwwl: hjhz - snnw
jdnj: frtf + spbb
hgrz: 2
lqjr: ljvf * tjhm
rwpt: 13
pmhj: 5
cbsd: pdjl * qrnz
dlzr: fqmz + cgbw
qgrz: qfdw + ctqr
qrfn: 5
qtvp: 16
fqmz: nhfh * nhzb
cfrt: 3
rtjl: bwhj + lshh
nfww: dsdl + cfmz
rdzt: 2
rwts: fdwc * dzwt
jfvh: tzhz + lvrt
gtnb: zglq * zdgh
jdvg: 4
mjvv: lppp + bnfl
lndf: 2
rjjh: 13
vlhh: 3
ljtg: 2
mqgh: whjb * qttd
zgqb: 2
qvqf: 1
tcns: jsdg + bnsw
ncvm: szpp * prhc
htmh: 4
hctq: 3
rddl: chrw + pllq
qqdh: 8
dnbf: tcbp * szhw
bmqs: 7
pljt: 4
csdr: 2
htzm: bjmf * zjsh
swhh: chgp * fnmg
vnzb: ztml * lgzh
bwcw: 11
rtdh: zrhf * wqvl
lsnr: 19
npzc: zlmd + hslb
mrfp: 2
snhl: lsbn / wllt
ttgg: 7
wmcb: 2
strd: 3
gfdm: 6
fcht: 2
ggfm: gpsn + vrjd
hchc: 3
vzbf: rjwz * gltg
fzll: 3
qzql: vmjm * fjrm
vqzb: 3
lrrv: pbsb * mbvl
vsrl: dtvc + gjtd
frzq: dzbs + tppd
ftqg: vjzr * spsj
mlpt: 5
jwqq: 4
srzl: 9
pqln: rhpc * zvnz
svpg: 3
fqff: mlqb - cfwj
fsgb: fhhg + bvvd
fdpp: pnhw * fmbp
vhjj: 4
qpng: ftwj * cflf
sldc: 9
qfdw: lghp - sqgq
swgr: qtcj * nnzl
prtm: cfmt - ggln
jtsf: rbcm * qsvb
zswh: 8
zsbl: gdrl * djjt
grwn: 3
wvmh: 3
spjr: czfg * nzzw
vqmr: 1
pfsc: 5
lwcq: 3
bgdq: ddtd + qggg
fgdv: bcsr / dwcq
czsl: gjjr * vqhb
lzct: wswz / qqtb
zgwd: 4
bjjn: dlfr + wvsb
whhb: jcrq * wwns
hrwl: 16
gqhc: rstq * qgdg
rhwc: 5
mspt: nnrn + wfmv
wsgl: fhgm * gzvv
cmtb: 5
cvwh: 5
bmpt: qcsh * dzth
jwzv: gwnb + wzdq
cpwj: rrlj + hlfj
bzcn: 3
qdsf: 3
swqs: mrpn + jfbb
bpvb: 17
zcsf: mbcr / btlz
nbbd: fwsn / dfcq
fjmd: qgpp * twlg
bcsr: zvfn * qmhr
nhgn: wdqs * spwf
rjpq: sdgt * hhmm
lpbn: tmhc + lpzz
rzsr: 3
jnfv: cvnl - fjnp
jhfc: hqpg * mrgl
dqwn: 4
hdgl: 14
jndl: mnwr * tqsz
ntht: lzmp + zczz
mcwn: 6
ddtd: 5
qdvd: lrlm * fbtp
vgcc: 7
zfnn: jmfq - vcpc
pprq: 3
zzfd: 2
hqpg: rgjq * jwnm
ltfz: fmcs + cdqd
snmc: 2
dmgm: 2
nthq: tzvt + slgz
wnlv: 13
ljfd: pgvm + cwcc
zwcg: chrl * smvw
cjvs: zdqj + wlzb
grzl: tqcd + mmwb
qvlh: 2
cczj: bcth + rhvm
fwnr: ggjq * ttpv
bjps: 9
qrvb: 8
jsgm: 15
hnwb: 2
nvhg: hctq + bntn
wffb: rlvj * vwqv
czmb: zlqd - vqbb
jtnt: ljzd + vhpm
zcrh: ssvc * pcvt
gtbb: 2
vnzw: 2
rsjh: 3
trmb: sldc + tvlt
hhss: wfdd + nhpb
cgvj: 3
bgfz: 15
tszr: tgfh - npzc
fqjw: qgjv * cmdn
qltn: vpcr - mmbj
rlmn: 5
pcls: grmn * nmgg
vhpm: brsm + rwft
tflt: wzsw * gdwf
zdqj: 4
vrdm: mlhq * phqn
pjqp: 10
fqhh: vmsl / fzvh
dszl: 18
srpb: wvfb + qzdz
pqgf: rmlz * snqz
vrmh: cvwh * jgts
cmjs: nncj * cmnt
vrpz: 5
htpq: 2
czfg: 5
rdpd: htgt + hmgf
ggrc: 5
mdzm: nwmb + fzjb
ndzt: sbvv + cstb
hjcc: 5
vvvd: 2
gbhl: 5
chgz: ffnz + njsq
qlmv: dtvh * tgwj
jtdw: 4
fbcr: 17
qbpd: dhqp + fgdv
mjtb: dsjp * tvnz
cfnp: mthr + bgzn
wrvm: nhqc * pzvh
zqgh: 2
dghn: 3
rcsd: qgzm + jhgl
pgvm: 4
cnfh: 2
tdgg: tlvp + gpwb
zcfd: dzlb + qrfl
lgfp: 13
mfcb: 2
gssz: rqpn + tspr
qvds: rpll * zbzf
dhhr: mvhq + rgct
wmcz: zjtz * ldlc
vlmf: 9
qlws: 3
bpld: 6
cnfv: gcbn - slfp
wgqb: dlbc * rjjl
mlct: mvrb + nfqz
fqlf: wpnb + cwcl
gwld: 3
nlzn: pcth + tdst
vjqg: 4
dbsc: rhpf + nvzq
rcmw: 2
zprm: lsfg + cpcl
vpmq: 3
pdbq: 2
mhps: vzzf / jwtp
vmpc: 2
rmtg: 19
wsfc: 2
lrjw: 2
ttjz: 2
thsv: 3
mqzn: dqqp + mltb
wpnb: lgrj * jpmg
cngh: 12
hncl: 5
dzcv: hwhg * sphp
gsrs: mdvs - pmhj
vdrj: cfrt * qscs
tvsr: 13
fwsv: 8
ndtw: clcp * qzql
ppvm: hphj + dhqb
wmrw: 5
qbsz: lvzd * lqjr
pbzg: 19
wnsj: 12
zctl: 2
pndl: 5
cjbl: chsv - blqp
zjhb: tljr - bzhj
rjjl: snrd - bpqr
slnn: dtfd * rhwc
stvs: zvbb * tjts
qnnw: wlrg * mwlg
spbs: 10
zqnh: tsnb * nbvh
mngf: ljnf + sqtd
mqwh: 6
rgcb: 3
vsgp: hdmm * jccb
gnlb: 11
hbmd: prtm / clmp
hdzc: 1
dqhs: zfvc / zpdj
vcbj: 11
hjbq: 2
bjjl: hfnp * tdwz
vbgw: 11
tlts: 2
jwcl: 2
mvwp: zhlv + nfww
bllw: 15
qsmm: 2
ffmc: vcqh / jbpc
frjv: 10
fvzj: svwb + zqjz
hmgf: 2
jrbc: 5
pbrs: 12
tpls: 2
rbwj: fbmg - vzdl
dlbh: vsgq + hdqt
vrhb: 5
rndh: lcrj * hzmz
gmhr: 2
bbdb: 1
cncr: 6
jprs: ptqs * brgf
rtlz: lwhf * dnzt
vlmq: msmp + gwqp
dpsd: ncsj * ghqm
zpzh: 2
gfrr: jgtm / zszj
wqtz: qpzz + bpbb
hpch: 2
zvpb: vmdd * ntnp
glqp: 4
fbqg: mjtb + fzmg
jjpc: jmnc * wfbd
wwqg: 7
qcwj: qvds * fhzp
vzvl: 5
chvd: 8
fggl: lgqq * rzqg
zpln: 4
hlsh: 4
ggcl: 3
wzrm: njvw + sfdg
bsjq: sjnl + jtdj
ghlw: lmnb * nfbd
zvsp: msgc + jtsf
rddz: 17
pcdv: gwrv / zwpl
gzsf: 12
hrhf: sdqh * qphf
cfjj: 16
fdjw: tdqg * pbrs
wqvl: 3
vtmb: 3
prsf: mmpl - znpj
pdmd: 2
hpbz: rhbn * hrwn
bhfp: gfmv - crgr
bvvd: clpr + hvwq
bdlm: mtwg * mlct
sfbd: 5
hwjz: ntwg * lzwm
pdtq: jfbn * mwtz
clnh: rcws * vhsd
qvzq: hpfs + qmlq
rfgs: 2
fgdl: 4
gpjt: 12
zdjf: mfrs + gpgr
tbgr: lflp * bpmp
ntgv: gtgs * hcjz
qgpc: nnpm * zmlj
tfrs: ggbm + cmnj
nnzl: 3
qbbc: qzrb + rctz
gdpb: hznc * grbd
ffnz: 4
rdvw: gpmp + dzhs
cljv: nvwq / gdjz
phvv: 4
rgtw: 2
lgzh: 5
wvzw: ggrc * srdf
gqtm: 2
tsnb: 2
zjhg: 2
qphf: 6
wvpr: cncr + sqzt
jtqm: msrh * czgp
mtvt: 5
hmtg: 5
tpmj: 12
zlqd: tnvr * hsvm
rffb: ddfg + zwcg
bfcd: 9
zvms: zvzp * prmc
csjl: 3
pvgq: bwrb + qqdh
fpwc: lfqp + zggd
nzns: 9
zmdz: 2
ghqf: qpmw + bpld
sqrw: pppw + vjqg
qbcs: jdbc * jftc
mdvl: 8
qlqp: rmbp + mjjz
blgq: 2
zbgj: ggvz / twjp
vqft: zcwp + wmcv
vnvt: vffm + hpzr
fzmz: 4
lmbb: psgp * jnpv
vffm: 2
mnpm: 2
bqcz: 3
znbp: 6
fglh: djrd * rddz
srzb: 2
qtmq: 11
wjmn: 2
ghhp: 3
vfdp: nlnh / pstd
cdns: jmbb * nwbd
cdqr: qvfn * trnv
lfgz: 8
gftm: mtzv * bnrw
dmjj: tdgg - cdgb
mltb: rjpg * whlw
qbgs: 3
rhhw: 2
sqgq: 3
zfrf: hwzm + vdqw
gnbt: 3
hbrt: 7
gshr: bpgc + vsgp
dtgc: zrdm + rqsq
vpps: 6
ngch: 2
hwjf: 4
ltwl: 3
mwcv: rjqb - tjfg
zfgr: 15
zwtr: 2
qlll: 4
qscs: 11
dmzf: ndgq * jtlq
cqmq: wbvl * fvzj
gjbw: jwtr * gfsz
dvvw: 3
plwf: jjpc - gvtz
jpvq: 4
dfhf: 3
cqzf: 17
tdst: hpdt + mgzr
nnvm: jrjt + rwpt
vdsz: bsjq + snhl
nstf: vnpz - lqjd
ldgn: 2
fbrm: 2
dcwb: htzg * cpls
ppzg: 7
fpqz: 3
vvzh: vjdw * thwr
nzdj: 5
prnl: 2
zfpz: hlgn * nrpv
nwzg: bwwn + ngcl
tvnz: 8
bhmf: qhhc + ctrj
wclb: 2
qghp: ndzt * rcsd
phqn: 10
jqfp: 16
nrbd: bmww + mhdj
gnwd: 8
tbgb: 3
hltz: 2
spfb: 6
ntfl: 2
ggjq: 2
gjrh: 3
jgdm: 3
cgqf: 5
qqgw: lfrc + bfnl
vqww: 4
pfbw: jzdb * qlll
rnww: 3
zsjf: 2
bfcf: gtnb * mvqh
bgpq: 3
zpdj: 2
gwrv: vbhj * lvdw
rtdp: 3
zdgh: 4
lvdw: ldbb * gtbb
btmb: pwhn + qbmw
lztb: 1
jqdc: 4
zhrf: 5
gbsh: 5
qgcr: fpwc + qvng
mzfb: 4
pbdt: blcr * jrgc
nhlw: 5
wrjg: 2
nnmf: 4
czrg: 2
bsbh: qgqm * dlzr
bcwt: cjtb + fmqs
ffjh: cdbc * mtvt
cncq: 17
cvfp: 1
lscj: fgjj + jnfm
mthr: 4
crld: hjpm * bhdl
lmrg: 3
ggbm: wvmh + qvjr
jqvj: qnsd + pccn
hzsz: fsqs - hcsb
btns: snsl / ltcj
hbpc: 4
fqdv: 7
nsms: znbw * hjtg
ccdh: gwsb * sbzc
znzr: 2
pcdc: jjrg * jjmz
cqjr: 9
jtdj: 2
bmbf: ggsd * pfvl
wmqg: 4
jpsf: hhht / wnwr
tlfc: 3
fgdj: 2
gqtj: 3
gdrq: gssj / njww
hwfc: 2
cmsc: 2
cpzt: chcn - nrbd
snvr: 15
tlwv: 20
fwhl: dlcl * pnpf
rppj: cbnw * hmtv
ftft: 10
tgzw: 2
cjlp: rmrq + pwzz
tjts: rnmb * ppzg
lmms: ndtw + qgnl
bdtv: znmw + pqgw
jcrq: 7
mcgf: 2
nfnq: dvmz * zrqn
phmc: 1
drgm: vpqh * lrzq
jrbs: hchc + cpvb
qwwd: mnsg + zmsm
qwcb: 2
bccn: vmtn * fjhb
ctrj: 4
bpfb: 6
nbwr: jrzh / nsrb
pznf: 3
qsrb: lstb * dzhn
lrgw: ntht * ncjt
qvdj: zbvt - cjpq
lfpt: 16
dwnm: drcm * hbjp
sqfn: hwjz - lrlg
ftpd: 5
fzmq: wzpn * nmbf
mzgs: jjbz * clpj
zszj: 2
drjw: 3
jwjz: 8
bhzz: 20
bdpf: rnmv + jdft
wfvq: 2
tspr: lqnd * rptl
nzlm: 2
zjsh: vppd + pfsc
tcvf: bpfb + dcvd
vwnt: sgjn + ghcp
wgdg: flnw / rztl
wdrp: 3
qjwg: jhrd / wsln
crhd: cfrn + dpjz
gdrp: nzns - gtbg
rctv: hjcb + fzmf
lptv: 2
vmsl: nfqq * vzvq
ggqq: 5
wdcc: qpst * qrmf
znmw: jdgf + dghn
blcr: 4
ztml: hfjw - bfdw
djwb: 4
qljv: 3
lcsb: jfgd * jwcl
wmsm: 16
lstt: 4
vvzd: jrbs + bjcm
mqzj: rpwb * lvfn
ssjp: zdpj + dbqz
cnls: zbbq + bfzv
rqjm: 3
zqmg: 2
gdrl: qfzn + gssz
rjpd: 2
mjjz: 1
jflr: zbgj * zfbp
ttvq: 9
blgw: cdqj * fhwv
zfqj: cncq * gqcr
lmgd: wzmc * nmgc
qmlq: zbvc / bvgd
gfqf: 8
lndg: ntrn + gchb
zbrw: stqg + vvnq
shzr: 2
phqc: 5
vplf: 6
rlpl: gncw + rnqp
qgjv: 9
rnbq: bwcw * ffmc
nljr: nwzg * gcdm
qfpq: 2
vdqw: dcbs + cjrp
dsjp: tfvh * jqjt
mhdj: ztqj - mjms
vpft: 17
zwvq: gmnm - thjc
vpzc: 5
sjmn: qppr * mnqr
cnbw: 10
jqwp: mdvv * rpbv
zdpn: bcmv * nmvl
rhdd: 5
dzth: pcmn + ctvz
phgs: cdvh * tzpz
dnzs: jtdw + zqwr
sqlf: 19
vqhb: tlst / hvdd
wvgz: 4
fffh: jnmt + hlsh
tgwj: 2
jrjt: bbvj * hwwc
ftbg: 14
rlnp: 4
grmt: 3
znbw: jqgc * ttfg
qqgj: qjcj * rtdh
prmc: rnjz * hwtn
pcmv: 2
gdpp: 1
hbcp: 5
jgdz: pjlz / tchw
fcvv: 3
smst: 8
nhzb: rmjf * dthv
mnwr: 5
jtwt: lfnr + jgdm
jghq: bwdb * mfrb
zqhg: 11
nshp: 2
pqgw: bphs + phzb
gfnw: 2
qtcj: 2
dzbs: zzfd * shnd
vgmc: rsqh * jnjh
wjns: rjdv + tlfv
rgct: phhh * wgqb
szmt: jfqn * bwrd
hdqt: 5
wfjj: 6
vjsd: nwpc + pntb
vcqh: sctr / bnfc
fbtp: 2
mvbr: 5
sctr: rvsd * thrd
mfrv: 4
hlbh: 13
qgpp: 7
rsdg: pqbr / wdmq
gtgs: qthb / tljh
gfgz: 14
hzcl: 4
mjtq: brmb + lstt
mmgv: jtnf - nmrr
zwcs: 7
hghl: 2
nvgb: 5
dlfr: rtdp * ntgb
jsvf: bnpz - mhfr
qpgt: zrpq * dbsc
bnfl: lsnr * bfnt
vzbw: lrcz + dnzs
jnsg: 1
qsgc: ddsb - cvgg
cdjs: zdng + gjmv
zjbh: jtnt - srjj
bpgc: shhb + rmcr
nhms: 11
jjbz: 2
nwcj: 3
bwjh: 11
sjdf: wgpb * pqph
jmfq: 16
ssfh: wmcn + qzjs
zczj: qqwb * vnwq
mvqh: 2
tvss: 9
ncjj: 5
bcth: 2
ztnh: 3
mcvf: 2
rrbq: 2
nzzw: hrsb / vjvf
svhg: 2
hlsw: cmtb * lspf
ljhb: 2
rlhb: mmfh * nfnp
ldlc: 3
lrbh: 9
vhsd: cdqr + htzm
lzzt: 2
hpfs: 3
tmhv: 4
qzlb: dqsl * lrbf
vpvn: 1
tvtb: hvgj * lndg
zmnv: 17
vdrh: 3
cqhd: 2
hrnp: gqhp / hhnw
cgzn: gjfj * rsjh
gcbr: 11
lmnt: glpq * frnm
rjfd: 10
rgjq: 2
tcbp: 2
mgmt: lcsb - nmpm
fdrs: 5
mzwg: wvht + lqqm
hwhg: 3
ptdw: 4
mrpn: 6
gtvh: 2
ljtb: 3
vsnb: 2
cvzz: 12
gvbg: vnzw * jmbq
pfdm: 5
czts: 19
dscj: hfwv * mwzp
wphd: tzcw - wfzl
dsbp: pbzg * lptv
wtzb: 5
jdnb: qlmv + ljdc
pqbs: qhrw + lhrf
lpvc: cnzj + qwwd
rmcr: zdvc - srbd
clbh: jmmb + zdjf
dlvr: 2
dlgl: pfjv * tgzw
dnwb: 20
nbbh: bmbf + wcvp
spbb: fwlg * mwpd
pvsn: 4
dzct: 12
brlh: jdvg + dzcv
hhjr: vqhj / nrld
pzzz: blsc * htvq
vpqg: rqvh - rtlj
tvlt: hlbh * vgwt
hvgj: 5
bgbl: qhth + pdzh
rzvs: 2
mmsv: 4
wjlf: gpjt + slnm
bjft: 8
jttv: nvcg * phfv
bjfb: drgm + dhng
zflj: 1
cjwd: 2
fmvq: 3
vzfm: 7
vqhl: 2
qwjn: 3
nvzz: 2
hfwv: lrch * cjwd
mmwr: rjqn / jslp
srjj: 9
fwsl: nnvm + qmgs
gjvm: 2
gscl: 4
hqhz: 16
pzlm: 3
lghp: bhzz * ttjz
tprh: 5
bpht: nfnq * lrtz
rhpc: ghqf + nzlm
dwrd: 3
qwrm: 2
ltcf: tvvv + fzrz
jdgf: 4
gftv: gdrq * qfpq
nnzn: pcdv - gcjv
nwmb: ldfr * pwbl
vdpl: rlmn + hzrw
rdzw: 2
bwmf: 4
gnjz: 1
sgjn: 4
jhfv: 4
tbtp: jhfv * zmnc
mdvm: 6
fnjd: lmhr * zjbh
pwzz: 11
rmbz: 3
qmfq: 2
nnrf: 2
tfgm: nzjr * rdzw
mdvs: lbft * hpqc
ggvz: wbmp * csjl
jjws: 4
hzrw: 2
vfqc: 4
lqvn: 3
pdgb: 3
pmjb: dtzf + fqjw
lsbn: brhg * ppnz
mtmt: bwmf + ljtb
rszh: htzl + trmb
qnqn: 5
mtwg: 2
mjgr: 15
qbvs: hcpq + gdpp
ngns: phmc + qmwh
lsfg: 3
clmp: 2
mfrs: rddl * ntnn
fcfj: sjtq * mjtf
bqws: 3
bsrc: 7
wmcv: zcns + snnd
ggsh: qhbd * ttfz
tqzq: prrf * rvtm
tzft: tvhj * ljtg
tzpz: 17
vqzf: fddg + tbtp
gtqj: 1
thrd: hdjm * gswt
pnhw: mhsw + mjgr
mzfq: jwjz + zngj
jtnf: vpqg * pdtq
wcqm: 4
cwcc: vfqc * crlj
fvfz: 2
zgfg: 6
lrcz: rjww + chgz
zbhn: 3
nrvz: cjpm * qlst
ltfw: bqjb * rpwv
msrh: mdnc + ndsl
pllp: 2
nmbf: 3
gtsq: bhmf + dtfg
tsjz: 1
qwcd: hrpj * vjbf
djsg: 3
qrfl: lngb + zfpm
nbsz: pqgg + dclr
mrtc: pljt * sltm
gcdm: 4
znpj: bjjl + qtfn
vgrl: sqsq * flhn
ctpp: qtjv / cqhd
fwgh: rplb * zqhg
rbtv: wcml * sjgq
fbnt: wwqt + mmln
chvl: clbh * rjpd
ntrn: 2
bqmn: prnl * hszr
pcth: gfqf * hnwf
tfzs: 2
qgvr: 2
bnsw: dscj + pcdc
vhnt: zqpc + vjsd
qwvg: svpg * nngm
qggg: htrz * hmtw
bcqz: nqfj + wtzv
gpvl: lbjs * qwns
glpq: fdvt * czts
tzrq: mzgb * bdsr
htjj: rqcw / pmdg
nmgg: 2
ttpt: 19
qjfm: lmvs * cncl
hqnb: 4
dljq: 3
rsvb: gtvh + zglh
zcwn: 2
cgsf: gfdn + rndh
wlfq: 13
djth: 6
pjwp: 17
nmpm: 5
jfbb: 1
vppd: 2
npbn: lhnz * dsfr
wllt: 2
tvvv: nhlc - jmcr
zdfc: 4
rhjt: 3
tgfh: bfsz * dvjf
fntf: qdlz + lhjg
tggp: 13
thwr: nbjt - mmwq
shmr: 3
djrd: 5
mzhd: 3
dhng: wbgn + gzwf
pqph: 2
mdwj: 3
jpmg: qrvb * fvtp
cdbc: 2
whps: gjpc * bqmn
hzmz: 5
gwqp: bgqr + qgcr
fnrp: hfbs + clsc
scls: 2
trlc: 9
nhdt: rlnp + nbmm
jqnj: 7
mhjh: 4
nhsm: jrtt * dnwb
bpmp: cmjs / zjhg
ghds: vpft * lmcp
whjb: 5
jqjr: bznb + djjs
zlcj: fwvr + clhs
wzmc: 4
nhcj: 3
lfqp: trpw + zcfd
zqjz: 12
bstz: wsgl + fqff
dfft: psmj + pqst
htgt: 5
qgzm: 1
wtfp: vhlg + cwqw
gwsl: htnt * bzcn
tbhz: 2
bmvt: crhd * hhfl
gfrh: 5
qbvz: 2
lzbt: 3
gcjv: 5
dcnz: dsvj - nhmc
zhhb: 12
ghzz: 5
qsgr: pjgn + ffjp
mrwq: qlpq / nlqn
gbgz: 5
gcfr: hfvs * vprp
gqcr: 2
bhdl: vggb * rsvv
wdhv: 3
lrwz: 5
slft: 4
ldnp: 8
vqps: 3
wgsg: bmtd * njjp
dlqj: nmtq * nfbw
cmdc: 4
dtjc: 3
wqzg: mqnl * vgjd
gfjt: vgwz / wjrc
djjp: pmfm + vvrw
dfnw: srln + zvms
lgqq: fhlf + tqgm
cmnt: jhfc + dqhd
lcrj: 5
smlw: dfjg * sblh
nstd: 3
gbvg: 5
vlhn: bbbt * ttrm
nnrg: 4
nzcc: 3
rjzt: 17
nnpm: dlld + wspn
ggtb: 2
bnhd: nbnn + tdlb
jfhb: 10
hpqc: 8
cfjg: 2
jdjd: sjfb + jbbg
nvcg: gtsq + nlhg
dczm: 2
gwqz: 17
lwzn: 3
qgnv: 5
fgzq: 2
wspn: pvfw * svth
jgrm: 3
fvtp: 6
qtfn: vzdj * wqzs
ccqw: 4
cvnr: gsrs + vdng
ptnf: 10
mcmr: wblz * gmhr
btzm: pfjr * mrzl
ntsm: tlwv + zfnn
rccq: bqwc + qcwj
fcvb: 5
pcts: cpjd + zqph
zcdw: jdnb + gwvc
nqwn: nzdt * jwbw
nwbd: 10"""

assert MonkeyMath(example).value("root") == 152
print("Part 1:",  MonkeyMath(puzzle).value("root"))