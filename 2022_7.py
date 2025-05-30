from __future__ import annotations
from functools import cached_property
from pathlib import PurePath
from typing import Generator

class File:

    path: PurePath
    size: int

    def __init__ (self, path: PurePath, size: int) -> None:
        self.size = size
        self.path = path

    def __repr__ (self) -> str:
        return f"""<File "{self.path}" | {self.size} size>"""

    def __hash__ (self) -> int:
        return hash(self.path)

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

class Dir:

    path: PurePath
    parent: Dir | None
    files: list[File]
    dirs: list[Dir]

    def __init__ (self, path: PurePath, parent: Dir | None = None) -> None:
        self.files, self.dirs = [], []
        self.path, self.parent = path, parent

    def __repr__ (self) -> str:
        return f"""<Dir "{self.path}" | {len(self.files)} files | {len(self.dirs)} dirs>"""

    def __hash__ (self) -> int:
        return hash(self.path)

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

    @cached_property
    def size (self) -> int:
        files = sum(file.size for file in self.files)
        return files + sum(d.size for d in self.dirs)

    def all_dirs (self) -> Generator[Dir, None, None]:
        yield self
        for d in self.dirs:
            yield from d.all_dirs()

class Parser:

    root: Dir
    lines: list[str]
    index: int

    TOTAL_SPACE = 70_000_000
    SPACE_NEEDED = 30_000_000

    def __init__ (self, s: str) -> None:
        self.root = Dir(PurePath("/"))
        self.index = 0
        _, *self.lines = s.split("\n")
        self.parse()

    def end (self) -> bool:
        return self.index >= len(self.lines)

    def line (self) -> str:
        return self.lines[self.index]

    def handle_ls (self, root: Dir) -> None:
        self.index += 1 # consume `$ ls`
        while not self.end() and not self.line().startswith("$"):
            left, right = self.line().split(" ")
            path = root.path / right

            if left == "dir": root.dirs.append(Dir(path, root))
            else: root.files.append(File(path, int(left)))

            self.index += 1 # next

    def handle_cd (self, root: Dir) -> Dir:
        line = self.line()
        self.index += 1 # consume `$ cd`

        if line.endswith(".."):
            assert root.parent
            return root.parent

        _, _, name = line.split(" ")
        index = root.dirs.index(Dir(root.path / name))
        return root.dirs[index]

    def parse (self) -> "Parser":
        root = self.root

        while not self.end():
            match self.line():
                case line if line == "$ ls": self.handle_ls(root)
                case line if line.startswith("$ cd"): root = self.handle_cd(root)
                case _: raise Exception(f"Line not expected '{line}'")

        return self

    def sum_dirs_at_most (self, size=100_000) -> int:
        return sum(
            d.size
            for d in self.root.all_dirs()
            if d.size <= size
        )

    def smallest_dir_to_space_needed (self) -> Dir:
        unused_space = self.TOTAL_SPACE - self.root.size
        space_to_free = self.SPACE_NEEDED - unused_space
        ordered_size_dirs = sorted(self.root.all_dirs(), key=lambda d: d.size)

        for d in ordered_size_dirs:
            if d.size > space_to_free:
                return d

        raise Exception("Not Found")

example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
puzzle = """$ cd /
$ ls
53302 chvtw.czb
240038 dwhl.nrn
124868 dwhl.vvb
dir fml
dir jbgpgvj
dir qjphltd
dir wlfprc
dir zqvh
dir zzmgz
$ cd fml
$ ls
dir bztjtqg
176916 crgzcmrt.jlr
199024 gpnmqlr.rdb
dir lwpbbb
dir nsdgz
186077 sfrlrc.jtj
$ cd bztjtqg
$ ls
dir dwhl
dir lwtrqrqq
dir nsdgz
105281 qlsr
$ cd dwhl
$ ls
dir fqdzv
198583 mmrplb.ncb
42601 qmdjhrsg
68484 rnmsmcqn.cwf
dir wlfprc
$ cd fqdzv
$ ls
140953 mfprqmdp.pnl
$ cd ..
$ cd wlfprc
$ ls
180121 swjgs.glp
$ cd ..
$ cd ..
$ cd lwtrqrqq
$ ls
224392 swjgs.glp
$ cd ..
$ cd nsdgz
$ ls
5704 chvtw.wzb
158254 gppbtqsw.mrr
192803 pltnst.mnt
265646 pst.njs
dir qzdb
$ cd qzdb
$ ls
171982 jcjcv
125788 tfr.hlv
$ cd ..
$ cd ..
$ cd ..
$ cd lwpbbb
$ ls
dir chvtw
88879 dtgbns.jfw
dir fgfm
dir nsdgz
216019 wlfprc.bhp
$ cd chvtw
$ ls
67998 mfprqmdp.pnl
$ cd ..
$ cd fgfm
$ ls
85968 mfprqmdp.pnl
$ cd ..
$ cd nsdgz
$ ls
171874 pfwzjm.wbv
110070 vdpnmst.wjm
$ cd ..
$ cd ..
$ cd nsdgz
$ ls
dir cqwh
33973 dwhl.clh
dir rdcmr
140633 sfrlrc.jtj
dir stqhwh
24695 vdpnmst.wqp
222421 wlfprc.dcf
225333 zfq
$ cd cqwh
$ ls
220212 bbpbg.sch
dir dwhl
203595 nsdgz.fcc
123921 nwjds
145468 sqg.dpb
199052 wvqphtff.stc
$ cd dwhl
$ ls
51966 hfhlcjp.mtn
23657 hhflcsql.pns
241753 mwbgzn.fpn
247935 srdgnb.zbj
$ cd ..
$ cd ..
$ cd rdcmr
$ ls
215436 crgzcmrt.jlr
116617 ndwd.drq
$ cd ..
$ cd stqhwh
$ ls
28083 cfmcj.plz
dir chvtw
229939 hwf.wzr
dir twfztmq
219525 vdpnmst.mcb
dir wlfprc
$ cd chvtw
$ ls
120506 lspn
214538 mfprqmdp.pnl
$ cd ..
$ cd twfztmq
$ ls
231371 mbsrnbww
$ cd ..
$ cd wlfprc
$ ls
dir dncq
dir fmqzns
$ cd dncq
$ ls
40876 swjgs.glp
$ cd ..
$ cd fmqzns
$ ls
23604 chvtw.bhw
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jbgpgvj
$ ls
121937 crgzcmrt.jlr
$ cd ..
$ cd qjphltd
$ ls
85066 chvtw
dir dwhl
dir fcqfgnvh
238098 hbzf.wgc
dir ltm
dir mbbvp
118907 mfprqmdp.pnl
dir mgnl
dir nhmqcpdl
147292 qtjcqtwt.vtn
dir tvplqllb
$ cd dwhl
$ ls
dir cgrdfzc
197650 chvtw.bfz
109566 dwhl.vww
dir jgzjzvh
80828 sfsz
154910 vdpnmst.fmz
dir zfrpc
$ cd cgrdfzc
$ ls
145237 ffzd
dir jqwgwcm
72905 sztrgnwr.gqw
58294 vdpqccdl.ddc
$ cd jqwgwcm
$ ls
115858 nsdgz.zdf
$ cd ..
$ cd ..
$ cd jgzjzvh
$ ls
dir chvtw
$ cd chvtw
$ ls
dir zmwmcgcr
$ cd zmwmcgcr
$ ls
dir wjq
$ cd wjq
$ ls
121465 rbg.plr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zfrpc
$ ls
dir cqv
dir llwsnsd
dir qrmg
$ cd cqv
$ ls
dir vdpnmst
$ cd vdpnmst
$ ls
170492 qsvf
273024 sfrlrc.jtj
$ cd ..
$ cd ..
$ cd llwsnsd
$ ls
42903 dwhl.shp
179054 fvwwghsb.dll
dir glhdqhf
dir wblwwf
dir wlfprc
dir zrjzmj
$ cd glhdqhf
$ ls
70524 pzll.cjc
29836 wlfprc.bns
$ cd ..
$ cd wblwwf
$ ls
209990 jcfss
$ cd ..
$ cd wlfprc
$ ls
97159 djqs.gqb
$ cd ..
$ cd zrjzmj
$ ls
164830 fwrpcrbg.pvg
83144 vszfdj
$ cd ..
$ cd ..
$ cd qrmg
$ ls
42025 nsdgz.sjw
114620 swjgs.glp
269872 tgptmhz.zch
$ cd ..
$ cd ..
$ cd ..
$ cd fcqfgnvh
$ ls
126854 gbbfpz.rjv
dir gbzslwz
dir nsdgz
200981 pmswh.nbz
45443 tdqwszvc
227183 vdpnmst.tbt
$ cd gbzslwz
$ ls
dir njzvwjh
$ cd njzvwjh
$ ls
44070 lvsjfvll.bfc
$ cd ..
$ cd ..
$ cd nsdgz
$ ls
dir cmfz
116103 fztsf.lvz
59406 mfprqmdp.pnl
dir wlfprc
$ cd cmfz
$ ls
37680 ncshvdst
$ cd ..
$ cd wlfprc
$ ls
273982 jcvqttf.fqz
$ cd ..
$ cd ..
$ cd ..
$ cd ltm
$ ls
19761 mfprqmdp.pnl
$ cd ..
$ cd mbbvp
$ ls
12482 wnv.vps
46227 zlnlzzn
$ cd ..
$ cd mgnl
$ ls
dir bpc
dir chvtw
240396 dwhl
115971 hbbnwwh
33819 mfprqmdp.pnl
218670 nnbjb
dir qwjp
107343 tmhp.jst
dir vfrbjgdm
dir ztpggl
$ cd bpc
$ ls
dir chvtw
63061 dwhl.ftj
dir dzlv
119367 gmp.fdd
dir hdvdfnw
dir nsdgz
dir pds
48753 sfrlrc.jtj
186706 vdpnmst.lnb
182938 wlfprc.dvf
$ cd chvtw
$ ls
29411 sfrlrc.jtj
$ cd ..
$ cd dzlv
$ ls
140503 vdpnmst.dtl
$ cd ..
$ cd hdvdfnw
$ ls
36521 crgzcmrt.jlr
dir hsjb
231528 mnl.scm
dir pczq
$ cd hsjb
$ ls
204248 swjgs.glp
$ cd ..
$ cd pczq
$ ls
18842 qzwd.tfn
$ cd ..
$ cd ..
$ cd nsdgz
$ ls
dir bpgdn
106092 nsdgz.vqs
71032 pgbvnv
47006 pthbb.znn
dir rll
dir wlfprc
$ cd bpgdn
$ ls
54889 wlfprc
$ cd ..
$ cd rll
$ ls
135900 shgfznp
$ cd ..
$ cd wlfprc
$ ls
dir dwhl
160547 vddtj.jrh
114072 vdld.ndv
258527 wlfprc.lgg
$ cd dwhl
$ ls
9122 nvptwfp.qhh
$ cd ..
$ cd ..
$ cd ..
$ cd pds
$ ls
174820 svq.gmz
133508 zhpcdqnr.pmf
$ cd ..
$ cd ..
$ cd chvtw
$ ls
dir vhspmg
$ cd vhspmg
$ ls
dir flzpg
$ cd flzpg
$ ls
205811 sdtgsjsd
262847 zbmsmzq.wwt
$ cd ..
$ cd ..
$ cd ..
$ cd qwjp
$ ls
dir crzqrz
dir gwwrhjh
232315 mfprqmdp.pnl
dir nsdgz
248778 qfsds.rhh
252980 vdpnmst.qgj
$ cd crzqrz
$ ls
202759 srdgnb.zbj
$ cd ..
$ cd gwwrhjh
$ ls
dir lvnsvm
$ cd lvnsvm
$ ls
191751 tdrrztrn.rfb
$ cd ..
$ cd ..
$ cd nsdgz
$ ls
273767 chvtw.gzr
244356 pww.qgb
$ cd ..
$ cd ..
$ cd vfrbjgdm
$ ls
dir chvtw
132015 cznw.mfc
dir fnw
dir gvddj
dir jdzsng
204950 lmprp
dir nsdgz
187795 whd.qlv
$ cd chvtw
$ ls
dir bfwl
dir fvfmzg
dir mzmdjhjq
153152 srdgnb.zbj
239385 stcfdsv.fjj
dir vdfw
93411 vdpnmst
186283 wlfprc.hbq
dir wvgj
$ cd bfwl
$ ls
dir frrsl
1168 sch
dir vnzvmpmg
dir wlfprc
$ cd frrsl
$ ls
164016 btzft.qdc
$ cd ..
$ cd vnzvmpmg
$ ls
dir hfnjf
$ cd hfnjf
$ ls
267448 dqts.pgp
$ cd ..
$ cd ..
$ cd wlfprc
$ ls
dir hsbg
dir mgzvqhtr
dir nbbdv
88560 wflghrq.lws
$ cd hsbg
$ ls
191520 cmdshfgh
283887 crgzcmrt.jlr
dir dwhl
$ cd dwhl
$ ls
103303 vdpnmst
$ cd ..
$ cd ..
$ cd mgzvqhtr
$ ls
159296 dvlhwsj.gvl
$ cd ..
$ cd nbbdv
$ ls
dir hnv
$ cd hnv
$ ls
138102 wlfprc
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fvfmzg
$ ls
205962 ltzsj
$ cd ..
$ cd mzmdjhjq
$ ls
178012 dwhl.dfd
155247 mmmlqppm.hcz
85643 npllz.ltb
122027 nsdgz.ngz
dir wlfprc
dir zrmt
$ cd wlfprc
$ ls
171189 rgsbqlw
$ cd ..
$ cd zrmt
$ ls
dir dwhl
$ cd dwhl
$ ls
75018 qbwm
$ cd ..
$ cd ..
$ cd ..
$ cd vdfw
$ ls
77110 ffsvhm
dir lmplrbzc
dir ttq
$ cd lmplrbzc
$ ls
dir mmf
$ cd mmf
$ ls
127691 sfrlrc.jtj
$ cd ..
$ cd ..
$ cd ttq
$ ls
dir qwfvql
202107 rpgqwfb
dir zhfg
$ cd qwfvql
$ ls
dir tbldv
276153 vdpnmst
$ cd tbldv
$ ls
65603 mfprqmdp.pnl
218354 wdbprnm
$ cd ..
$ cd ..
$ cd zhfg
$ ls
dir wlfprc
$ cd wlfprc
$ ls
dir dggm
273082 mfprqmdp.pnl
$ cd dggm
$ ls
197043 chm
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wvgj
$ ls
163854 pcmbb.gwc
$ cd ..
$ cd ..
$ cd fnw
$ ls
84321 bjnn.mqc
dir dmcbshg
dir mdvt
$ cd dmcbshg
$ ls
dir fsh
$ cd fsh
$ ls
dir cgstfrbl
$ cd cgstfrbl
$ ls
227959 vdpnmst
$ cd ..
$ cd ..
$ cd ..
$ cd mdvt
$ ls
dir mts
dir pwrvqrjc
dir qwrh
52239 sfrlrc.jtj
$ cd mts
$ ls
242122 mfprqmdp.pnl
$ cd ..
$ cd pwrvqrjc
$ ls
40460 crgzcmrt.jlr
173816 jzhvzrnv
56851 swjgs.glp
218509 wlfprc.cvr
$ cd ..
$ cd qwrh
$ ls
240079 lzwbvw.zvf
$ cd ..
$ cd ..
$ cd ..
$ cd gvddj
$ ls
dir cgbpbw
24565 chvtw.czc
244373 nsdgz.mzj
281443 srdgnb.zbj
63755 swjgs.glp
dir vdpnmst
247101 wlfprc.nzd
dir zlh
$ cd cgbpbw
$ ls
dir bcbgqzj
dir dwhl
dir nhtz
dir nlnbr
$ cd bcbgqzj
$ ls
199932 vdpnmst.zvh
$ cd ..
$ cd dwhl
$ ls
116043 nsdgz.ttd
$ cd ..
$ cd nhtz
$ ls
196534 cthbt.tjj
$ cd ..
$ cd nlnbr
$ ls
dir chvtw
dir dwhl
75467 lhzhvn
dir ncmpwvrd
dir vdpnmst
160988 wlfprc
$ cd chvtw
$ ls
119163 sfrlrc.jtj
226449 srdgnb.zbj
$ cd ..
$ cd dwhl
$ ls
dir dwhl
$ cd dwhl
$ ls
283831 ptssf
$ cd ..
$ cd ..
$ cd ncmpwvrd
$ ls
169547 chvtw.hnh
142447 wlfprc.pds
$ cd ..
$ cd vdpnmst
$ ls
276326 jslgmcp.mmz
$ cd ..
$ cd ..
$ cd ..
$ cd vdpnmst
$ ls
36500 dwhl
186159 nwwhrf
$ cd ..
$ cd zlh
$ ls
245705 chvtw.jgd
$ cd ..
$ cd ..
$ cd jdzsng
$ ls
48648 dnzlvjr
63253 fnzfrtrp.bll
9962 zcgg.ldc
$ cd ..
$ cd nsdgz
$ ls
188613 cvvr
$ cd ..
$ cd ..
$ cd ztpggl
$ ls
dir vbrtv
dir vdpnmst
236782 vqm.zdj
$ cd vbrtv
$ ls
35655 rswctm
$ cd ..
$ cd vdpnmst
$ ls
143090 crgzcmrt.jlr
242681 mfprqmdp.pnl
146639 vdpnmst
63563 vdpnmst.flr
$ cd ..
$ cd ..
$ cd ..
$ cd nhmqcpdl
$ ls
dir dwhl
dir nsdgz
dir tgwtvm
$ cd dwhl
$ ls
253652 swjgs.glp
$ cd ..
$ cd nsdgz
$ ls
208378 crgzcmrt.jlr
$ cd ..
$ cd tgwtvm
$ ls
dir jptp
dir qdjl
dir qngflrgr
$ cd jptp
$ ls
103248 chvtw.pgr
65015 pvz
$ cd ..
$ cd qdjl
$ ls
149177 chvtw.rzd
$ cd ..
$ cd qngflrgr
$ ls
98041 drfl.jfq
238883 jjzqzmm
$ cd ..
$ cd ..
$ cd ..
$ cd tvplqllb
$ ls
107011 chvtw.mdn
91988 dwhl
84875 ftwz.fzj
dir hpfr
dir wdgzsg
$ cd hpfr
$ ls
dir bbgbnr
dir dwhl
131524 fdpg
dir jvddlfsf
250910 mfprqmdp.pnl
174858 qpl.qtm
271840 sjncl.cjb
dir wlfprc
$ cd bbgbnr
$ ls
139093 chvtw
21309 crgzcmrt.jlr
dir nsjfgmrs
22977 qqt.mvb
129496 srdgnb.zbj
$ cd nsjfgmrs
$ ls
dir ppwm
167856 tvsqvsrf.plp
dir vztfzgrd
$ cd ppwm
$ ls
161664 ssl.fnd
$ cd ..
$ cd vztfzgrd
$ ls
213100 fwjrgdbb
$ cd ..
$ cd ..
$ cd ..
$ cd dwhl
$ ls
124522 gtmgtq
$ cd ..
$ cd jvddlfsf
$ ls
78145 zpcc.wzt
$ cd ..
$ cd wlfprc
$ ls
143769 mfprqmdp.pnl
$ cd ..
$ cd ..
$ cd wdgzsg
$ ls
209123 chvtw.lpr
191060 fqzjpnfb.lmd
dir gbcqgszh
dir jzhvmj
17755 mfprqmdp.pnl
dir mvvltrs
204706 wfmttzc.cdb
dir wlfprc
$ cd gbcqgszh
$ ls
263162 crgzcmrt.jlr
277604 rddzmchb.fwr
$ cd ..
$ cd jzhvmj
$ ls
2388 dnqs
249647 sfrlrc.jtj
276429 vcn
dir wlfprc
$ cd wlfprc
$ ls
179811 mfprqmdp.pnl
$ cd ..
$ cd ..
$ cd mvvltrs
$ ls
171792 bzq
dir chvtw
41358 crgzcmrt.jlr
86479 ddsjsbp
dir dqvlqnn
227156 srdgnb.zbj
dir thwdjln
dir wjl
dir wlfprc
$ cd chvtw
$ ls
61085 crgzcmrt.jlr
72256 rbnvsbm
154180 wmwnpf
$ cd ..
$ cd dqvlqnn
$ ls
42736 chvtw.wcd
$ cd ..
$ cd thwdjln
$ ls
114664 hdjvgpr
51273 pdsgj.tvr
$ cd ..
$ cd wjl
$ ls
49897 swjgs.glp
$ cd ..
$ cd wlfprc
$ ls
dir chvtw
222869 zffqnb.plq
$ cd chvtw
$ ls
84667 mfprqmdp.pnl
$ cd ..
$ cd ..
$ cd ..
$ cd wlfprc
$ ls
180812 cjbjffhs.rlc
dir dwhl
dir rvgrjsps
229144 vql.lww
210367 wlfprc.ghn
$ cd dwhl
$ ls
220631 sbrdjv.cdt
24851 swjgs.glp
$ cd ..
$ cd rvgrjsps
$ ls
62849 wrlzz.nwn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wlfprc
$ ls
88598 chvtw.vvq
222226 mssqb.gwc
54178 zjttbct.rft
$ cd ..
$ cd zqvh
$ ls
124084 wmswcs.wcd
$ cd ..
$ cd zzmgz
$ ls
143006 bbttfvt
dir vdpnmst
$ cd vdpnmst
$ ls
dir chvtw
107664 crgzcmrt.jlr
175290 dmp.hqm
dir dwhl
dir jtbh
dir lwbqctd
203538 swjgs.glp
dir vdpnmst
140212 wlfprc
26253 wlfprc.vqs
$ cd chvtw
$ ls
57311 chvtw.tmb
183900 vdpnmst.wfl
$ cd ..
$ cd dwhl
$ ls
46475 lpdfsdb.cgj
32915 vlhhrq.zld
$ cd ..
$ cd jtbh
$ ls
255372 chvtw.tmh
149848 gndwds.mzn
273202 wlfprc.ghc
$ cd ..
$ cd lwbqctd
$ ls
dir dbfbfjjw
dir qbn
dir qqqfdrst
dir zhzrhzcv
$ cd dbfbfjjw
$ ls
29216 mfprqmdp.pnl
17937 vhvbcmlh.wdf
87790 vqzhr.bsl
$ cd ..
$ cd qbn
$ ls
dir bdg
79958 mbzc.qbv
218421 nsdgz
$ cd bdg
$ ls
103738 crgzcmrt.jlr
179430 dwhl.gmw
118482 dwhl.ztl
dir gmlqjh
dir phvf
264818 zzjwzlrn
$ cd gmlqjh
$ ls
116934 wlfprc.rmt
$ cd ..
$ cd phvf
$ ls
dir dqbjm
43516 vdpnmst
$ cd dqbjm
$ ls
180654 lvdwvp.mjp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qqqfdrst
$ ls
58625 nsdgz.bmt
33328 sfrlrc.jtj
$ cd ..
$ cd zhzrhzcv
$ ls
119179 dhcfzq
270185 gtmphbt
$ cd ..
$ cd ..
$ cd vdpnmst
$ ls
180546 chvtw
dir htgbz
133410 lwdm.snh
134253 swjgs.glp
$ cd htgbz
$ ls
75079 nsdgz.vlj"""

assert Parser(example).sum_dirs_at_most() == 95_437
print("Part 1:", Parser(puzzle).sum_dirs_at_most())

assert Parser(example).root.size == 48381165
assert Parser(example).smallest_dir_to_space_needed().size == 24933642
print("Part 2:", Parser(puzzle).smallest_dir_to_space_needed().size)