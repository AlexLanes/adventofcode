import string
from itertools import batched

class Compartment:

    left:  set[str]
    right: set[str]

    def __init__ (self, compartment: str) -> None:
        middle = len(compartment) // 2
        self.left = set(compartment[: middle])
        self.right = set(compartment[middle :])

    def __repr__ (self) -> str:
        return str(self.__dict__)

    def duplicate (self) -> str:
        duplicates = self.left.intersection(self.right)
        assert len(duplicates) == 1
        return duplicates.pop()

    def intersection (self, s: set[str]) -> set[str]:
        return self.right.union(self.left).intersection(s)

class Rucksack:

    compartments: list[Compartment]
    priorities: dict[str, int]

    def __init__ (self, s: str) -> None:
        self.compartments = [
            Compartment(compartment)
            for compartment in s.split("\n")
        ]
        self.priorities = {
            letter: priority
            for letter, priority in zip(string.ascii_letters, range(1, 53))
        }

    def sum_priorities (self) -> int:
        return sum(
            self.priorities[c.duplicate()]
            for c in self.compartments
        )

    def sum_priorities_of_group (self) -> int:
        assert len(self.compartments) % 3 == 0
        _sum = 0
        for c1, c2, c3 in batched(self.compartments, 3):
            intersection = c1.intersection(c2.intersection(c3.left | c3.right))
            assert intersection
            _sum += self.priorities[intersection.pop()]
        return _sum

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
puzzle_input = """shzsFcPssFhjFssBzdpRcNHNZrpdJdJVJZ
fwvMCntfCCbSbSbtDgDNrDtDtJHZVH
GbCwwbwwnGrLhBzjFFFsWPhL
PpCqRsqqmmtCwMJC
LHFrLLHDSNHlfWNhDzmjzzJlJzPJMvPJjQ
SGSWDNrhZhPDSWDZLgVVRgbRppgpGVnpnn
GRRjbVjmJZlgMRzzrN
FpDptHpfHfnpPTvDFTWpFPnPcMfNCClNrzcVcrMMzVsCZlsZ
TFTQDnvLHPFDtVbLwbjdGjdwwJ
lhljvvhCjjzhjszzBPmnmGVZMGzG
FbTcTwbtSFdtcMPnTBPQVnnBZT
SFMpHDtNDSSbSdwppvgJWjJCJJgWgvlJHH
wzNCWpzCzJnWWpRRNdJrgHLhjfbLrHrchV
lBMStmPmmLQDPQZlshrdhgrfrcrrddgHgs
mvGDGQSvDPBlGMLGCvCWpNvpzRWFwqRw
stBttBThtDZqPWssPWZp
gRggwwggCGFSBBvPRpHZZrHdZLZq
ccFJGCNJmmGQzbTDhnQhBBnB
HJqMqtZbJMmJTqtLtVMqhpfphNdQfhfzzjhhlHll
rWSBrnwFwWCvwWCwBgPgCgzjQccQhhgRzcdQzjfcNfzR
CWBCwCvCvvwssWLMtJJGMdMZJsGV
nFwSFQwsNrrsssSwCrhrCNnfcCRgJRMJTJcMfRzMCMCRvW
DdbGdLZLttllWWvTzgzzgR
ZqGzPdLtDjBjDZGPZVmnhQFwqrFQhVFnss
sNNpCjttjsJjSpgpWjslCTnqqSVffrnhSfDhmhrhfm
dBwcGzbPBHbbwZcwJbcTTFDFFFDVrdVmFdnDqf
HzGcczQPHGwzPzGHRctWlvRgtvJlvNlJvRNj
cFNCFdvcCHvFBCZcwBfRSpttGhDmCghGShmSRt
QjLnTTzQVzTTnLMqhDgPhGDDSjGPrgSh
TTJGnJJlLQdNWZWJNBJZ
WHBpHcMDZHLDbHLtGCnmRmLNGmRqvsCC
PzTFzPPTJzrSbGsvnmqfsqfqRz
dJSQQdVFQgjTrjQPWcWHbBVcZVccZtWp
JDtnRtJzNzTTNlHc
rQPJFrLPGMMwrGPFwjFMVLjSTWHdWBTdSWdWZlcWTHlZ
MGFrCvLLwrwPFVVhvLMGGtnqfsmRJgDnqbRgfbqmfC
jnTtFjcSSvctJjznzvFmpqqPMqQDRVpRqPzqQzVQ
bhHBfrWpfHsfGNllRrRCPqDCqPqq
gsGZZpbWgbwHWGNgfZNjvLSTTjtnTgjSSSSJmL
RLQNdVNnRQdQHVVLGpspNqvtsqptqpTtsp
MlRWwbRBBFMFjCTFTTFDvj
WmlWBmBwwmrndnmLRHRQ
WnftJWlfnWSHGCjWWWSCFqFGBDqBwMcDmmMmGmqD
pTNhpTrPhhhRPzbhrppLhThLgqDmwccwqPBmMMqnFBcwwmBB
ZrhQTpzdjSVVtnvZ
jgtnJtBjtlTdJBZJVQBngQGDCGWpPGCcPWCbWdWMbcpP
wHstNNttSHPDmHcMCp
rrFFSvLLNfsFtNSqrtfrhsNjjVTBVgVvnTBvTQvjTgjVZz
qhZwlqFqFwlJwrDHqHcDvgcNzv
RCCTQmjCbQTBtRTbjJRDpBrgDHPPpPDvHccDPc
VmjVWstQJhlJlGVJ
GggpGwZmgvgJMvbJFQQDbDFbBbFCQDCW
rtrLzNLtNSPnNqDSQDcQCWlqBQ
VtzdRPtztLtVRtZmmMTRwCGZpMwp
vtvqjsCqtshfjcWFHWGjGFJj
zGrnzDDMpPcTHcSTVTJP
DbDwMbZRDrZdBBnMznZMGZDfwtlgQhsqCttClsqvsLfCff
JLzLtLsrzsQdvrWRwMHwcc
qPmCTzlPjljjFTZmWwcwwvHMMRWwHvMm
PFqZnVCqTCNjCzNgQsbGBLzLQQ
CBnppDHllVpPCBshBHpjDTSmZcSrfwvmJcDDTJfw
dFRLdLFQzNSTBTSNmBJv
FzFFzRMBFWtQlPlsjjPVMnhC
CVCfwnfdVvBdBbTNTT
LNzsHPNWsDjTZqDHqT
PtLgQsGQLSzWLstPgGWcgQLSNrpplffrnrNhpVCwlGVlrwMn
jPPVqPsHffzVnHzvSgMcCJGGMSVCll
pdbpDpBLNmNNppJgcvgSllGjDSGQ
hrbBwLpjLhhhNZLhNrhZZLHzfsztFzzsrtHfRFnFfRHf
tdjBdbmSfdHBdHHmZlWjFrnlWQlqvMFvFn
pDNDJhLhPVPLLLJphJLwNcwnQTcWWTqTrqMWTZvqMrlvFM
gpVLhNwpgZJCghCLDNwphgmsBdzHHHmSstmfggzdbR
TfMpfMBVftLMDBSjWDHgzHbgwLgHHvdzggzs
QJnZcFFnZRHdHjJvwgdg
RjjRRnmNmmZNjZqZnQcVffBrWqVTqrtffTSTVV
fZTdTVcVjrjdBzdTnGtgnnGSHHNFGn
thMWPtPMslmGnWnNnS
thvbMvQMRphhLCjrzBjZVdcQfC
MpmgZFgMGdrFrBCVnJ
JsbJlTTlvLQbVffRRvBBRVjd
LWlbhHlJhLTJmmGcMMHNmNgN
bhvmhPrbhqNqQRRGzQjVvvRL
wTwBZDBTwwggfnngcDfdsVVFQCdzCzDVRsFdQs
pngWMcgzMgpZWncnMpWNrbNHrNbmHhltWlbl
nPndBjLPscWSccBVGnScsSzMdhMppMthdMgpMgrzvhhp
CCFTFDwqZqCCJmhvpDzztVzDNztp
qQFJTbRVbmCfwTwfmnnssWBGnLnWlRLSGn
JRlJDSvLRRCdvmDSvdlbZNVBSWZGNgWsZGNgZBVs
QrjPMqMnLzzjLjFnNNgBpsgtgGGGVZ
hrjrFqjqFrQfMHPhQzDvvCLJdwwwmvbJbwDH
HDGrDDDpNsGQNdZQ
jpjgtgjSjpjllfZZtZsvNdtshqqq
cbgMfjclWTJcMwjWJfpfmVPLPBnVBHnmVbnmLBbD
rPrMZNsNrsvrwqvFFFdgQWNzLJJzRW
pStppStHmcmHpgVSllVcbVbWWDdLFhdbzdRRFhJFLLRF
cltCHmCBmtSlgjpllgGvTwPZPMfZvPsCMCwZvC
FRQQMdlFMDWRFQRQMQQDWdFbSSSVJSBbJSlBVVBnPJnzJL
rsftPfhsrgwznSzzHSLgJG
fhNsjrjhvsTTvdjcCRMRMRPcCW
tRtJttHFrjtDQHHBQMMBgMBSghhZQb
vqWPLpLvqrmPdmqwvqfmPhNBBBlSnbwbgnlnlhNSZZ
pGpdfzLLspddmqsqPvfvvPpGTVcJJCDRjHrccRtDjcRDFD
GJMHCdTMWJRhSTlhhSPllt
fVvqpfBFrqvqNzzgVDFrpDPmSVtQSlSmhjwltlRtmVhn
pzpBNDBzfDrsNsDRJJRdCssMLdLZWZ
hFfvWWvdpCwwcwFhphpcZCMmllHLfmbQlbrQLBJmGgQrQm
nVSNGjGzzSVNTsjzSJrbSrHBSHlrrmQHJB
PttTNsTRVnNjNqRnzRzRWCCCcpMCWGPMwwFZvFwW
DvZbFnDDsqDBwwRQgNBm
HhWpWWRMWChlChdHLlGlGtQtggSNPSSpgPmNgPJQtw
CMlWGMhhCVHlLCdHTHdrGHdbzjVqnzcvqqjRjFbbzbFFqR
ZZgCNqqBmjZsNgZCqJgNBdrLFHbBrWlPdHWFbPnHPW
TVwTDfzDwSDzmcSTcrzdbllnHPHdFlLzbF
tvDQwVtVvDVmtRsNMgRpJg
BBpDCpNJnmnpnDDmDGGmtTzqHcGTvTTjTbGjHLVcLb
swNNhPwwHzTVwwHw
rPRlPRhSQmmBDpnNfl
pbRhffPzcPDmfcNTpVBLpBjMGBGjZLLg
ssrCsqrszgJjZMqZLQ
SzCwnsllCrssvdrvwzPmDmPPbFRbSThPTPDD
QWLfcfczQQpcDTpLPfdZRRvRRVqbFWvZbvtqvv
NsGGJBhCmNdZVqsbdssZ
rMwwwBBJMrdzPfQMpzMnLQ
rdtCQhrCtQQprtTWQCHFjPgGBPdFPgvBqRRPqB
lsVsSnVSbLmmgBcgTLTFGgvq
wTTDTszsbzMDppJrJhDQ
ZlmsGLBVCBBZFCFFHqcHVvQhqVQSSHpH
dbbTRMrRwwzDfrTbFtMvcptvHFQQpqtc
gdJTDWgfwDwTwmgmNPnNsgFBlZ
PWhWhGFzzzrLdHCPccbJQJcHPD
NRpVTpTgRWVlHJNHMcHQMb
pSRSpVSZWRSTZjgTRTWnFLdZLrrndhdzZvtvzn
LgctLgVBVLhlPjqRhBLVcVlhbDDcGnNGfwCrbNDnrGbGCJNw
HmppHMWWmQmMqZZHWQrDDfDCffJrDGJrCb
qpWZsZZZMZWTLPhTRgTtThRP
hfhQfFQWzBfhfTQdmzdLDtDjtvHLjt
qsgpcqMNRmgpqsCwpCmZDvjwvdddHZHvZDtrrd
SgmNmqScbTSJbhJQ
dvMTQvTnZJsrQdbbSvMVZMblDwlflfDGgwwHcfGjPfjjrG
FqBLpBpFpFzRzqNFmgjGlDRHcwPPGwgcgs
tLNtWshsLLqWMJhTQVVbhvJd
bgZLMZgzbbLCcPCbMZbcNMgBqSTqSWVtSzvvTTBTqBvRBW
FhQpJQnGrlhGlrnTqRtTRJqSwDwtVR
FqlnnFnqFHnGHHdNZdbZbCNMdPLMPb
HHFnbftcfnfbbTbTnHTNVZZzJlPQlFrFzVJFZsdr
mvpGCBgwqCvLCqvMQWWzsQQWlPzwzsrV
hpGSGgqSvqbHcnhfVfct
lGVrnHsGcnVHzscrlGjHcrHqqWPlJCPJClTLLqCSPLPdqS
fRbwbtMQZtMMRFMSqfJTTWCTJPJCmd
ggdvtvdbVVGnpDGg
BnBjTcbnvhjjlMnNJJfnDnQDGdNDfP
qwFqVSWwqLpWFmFVCSqFpDDCJNJRQTRfRDGPfdfDQN
zwHwWVVWWFSqqwWTLqzzztHMvBhlcghblMlcttMllh
PFFNPNPmlFllbctNLmcjBstrsVrQHJSSHHSnnB
fddfDhdwGhTWWTDMwMggssjsjndsBsjsnSrVqSVV
MCvvTWvRMwCvGPpzCcmbplpCVC
thTqlPPTNbGNhGdqRRhRrNtFWnDnvvFZDpnFvfQDZtvWvv
HcMzVcVVcHrgHzcMcmmgfQvFQnMjnWDjfnvjQFfQ
VSmHJLHBJrTrJTlT
NjnsHjLLjNRddNdBFBSR
ftsbqfDcDqsrDtqsfSVBhJVFJgdBRVFS
wvDqwtDlsDDczjzjHvLzLQQM
qDwstwDtRfpJfVhBVZBMvnlRvv
zSFzQHFWdgZBVTZhTzrp
NHdggjGjWHQFPWHNPPbpJfPDtCwCtqDqJfbt
pvnbqHvnTvlCCpjsBsMGBGWWPp
RJSJhJCRVJmJwScrhSJdfwFsBGhZBjhGFFFFGgFPGhZW
cdRrdmwtfcdSmLtcSCQlvQNqQTlqqvtTlv
rnSlSrgWjVGpTTRhSffpRd
HtgHPsNNgNHszPcTBphMdhHhBcTc
JNNbZPZZsszNmtDbPgsmJlwFvWVnCwrlmWlnjnGvCC
WrVBVgVGGQCrSTTqvVjDqDjv
FmwRRwwRQhhLFMjFMzdqSSzS
RcJtbnnLtQWrGHcfrP
vpzssjmVjVZWNZzzQwtQwccpQhgtQCct
qDdfLMnMrrTbBLqTqltlTfbGQnghgRwggGgRnhhccCJJcG
MtdLfSSSddMftlrjjzsSWVSjFvjNvs
qTRPpRPzJglzGJzpGRHWHljwDtbwffjtbhjfwNfHmwwf
SZLVdsvrrdFdBcdZvsBdDCNtbmftNwfNbNhCNvtz
MLzzddLsQRppRlQGPq
PDDpdJgtpppGgttgdGdgJFzLjVcvVnnCTrVrRPTLvwnTTC
ZSbHBsSNlZcsfNnnvRrnVjrHwvCC
NmSmsfsfhmzcDmctJW
NbrLfrrLqpqWQHtBzbFttJgcgB
CmwjPPjjjShPvljwvwwjPBFttBtcHzFJcHTRHJRRmT
CCljjDGhvPCVdVSCdPvrrNfnnQsGqMpqqMqnFW
bdPdbcDZlddsZbHjrrgrmZmCZhCGjv
BffLfLVFVMMBRfwMpfzhFGFhGWvWvrhNvvNj
RMBpRSnffBJjSbJqdPHsDcbqtl
BgwGwDDZttDDTNND
WzNNnFRWFtTFlFsh
WJjPpPqqzWRbrqnNqvVvgvvdcBwgdrVBZG
FFbMVMFPvJppgvcvrZMjHlCJWHmHHBlqhCmqChCl
RGQVdVVLnLsQnQnnqWBlBmDRBDWWlhBD
SftLzQndGfVgFfjvvM
npvLlFLTWWqdLnJCmBmmpjQjjmjB
tfgDwzwVVVVtgtrsJtrbjSPQjQmjNBCNBNhPHDHC
ggVzVtMRgzMrvJLqFnnRnnRT
gZFZssWgNZTDwHDWzsFwWDQMMpqqpBPMjFtMPSQFqqqM
vrmvhdnVvQpftStnMN
JCdLddhhdJdcCdrrmCGhlgNsWDWDwWsgwHgHLZHW
vSsSGjSPvjvRSGpFprFbqFpppRfp
ZdmlndtBZbwrwfpWFn
JmdHdBBHtgllZldBhJZldLLBjPVQTfvGPNzQQSjjzPgTGNTs
TjTjBjVrTsLRRrMBsMMgzLqGGqgQHQdCQGgpgd
nbZcmNnPNcbNftvhlhZpgQgCqdSpgCHCqPFzSH
WfcNvtmmNmQlvNcbsWWjMwMVMRDVMDJM
hHHnfZSwHDgHcfclSGSnvrnvBCvWWntvzvzbWWVq
dTJTmspFTsFdRRLvtvLzvvVqtPVtrb
VFMNFpRJNTppTpsJVRcMGgfGfgZwghgGfcGh
lLGvwsMJLCMVnTrCrVdHRd
tbzqtDNNBpNWBtqzfRrFFnrVTTdrQVSVGp
tztfzmfzzPDzgWNNBbhGMlJLsvhJJjGJhGmM
rHrVJQVQVJLggDQQLbTvdCCSTdWLLLbCbS
pNtnwPthmZGRpmPFtqbMSzqffFSdTvbSzW
GpvvshwtmwsZDljjssHjVBVj
SmhJdtJhhzQSrzVhtQbtBRNfnFNSnDNGRfFGGMgR
lHwqPjqwTjLHCWLvPpvNrNMvnNGNfNGNBffGRN
lCrPTrwpPZWlqPlqpWWqZjsmJzbzVtVhhdsJcQdddZVJ
QqpCWHdQdVQlWcQCqcfRjnZZZPDnSPqPhhqZ
tmmzgWGgwJwwStSZZDRnZssR
GbFbLLvgmMMwGgmLCrppQrWVlWrFTHHd
qdqCgSVdVSVqfwsdZhpJspZsph
RjZBbmRlrlmmJwLNNNhLpwhB
vZlRrtTZCzCMfSPT
JBjhCNwjrlJlHJJRsscZrTcvLLgTsLPP
dDztmntCSgbLgqTzgc
fGVWnSMFtVGMNNNQllBjWHJC
dSDhVVdVZtnSgHQGThQvFNQQqF
LcfLRpMpcBpbrJfsbsscBNWRNPRGHvqPdTGPGqPWFH
spmrCcrdJJpLLmcmLLLDlzSzCCjVwZVtgnSZzn
ZJtgPTHtZPZQGbtNzzprVWWVrbrpCD
BRlfcRmBhSMVBqSVfBvNWrDrjWCjjzprCDCl
LfMRSmfqfSLcnnMqVSfccnhZwJFHZFTGZQGFLggwZTZGPJ
BChWddRRRcfmDbfhDP
MgpMFFsvMfGwvLgPjQPzPPmDcztDtw
NFgJpqvpLgqFnWWVNSfnNSCR
zMMMRmMfJpfhpzQJLMVtjtjPntgBtlZlVgJP
SdNbZvZbvbHTNbZbSWTdrTVBglBDlWBjDPDgntPqBDPt
rrNcrFwNdSrfzwMzZMLQQs
JPmCSfHTGJdTCbHgpgqLgRhghhffhg
ZWSSFVSVFQghQvwpphgh
lsDtZjVMMSdCNdbGCbjb
PBQPvDvVVRvQDqLDzJTlzwjz
tGcZTcdgGcncdrFrsTjzJSJqJqqwHSzzSZwq
CgtgdFgcFCMnMgsGFGGQWPQpQTCBvbNpNVVWVT
FHVFWMHMgVhnLWWMpnppfcdZNcPplnfn
RSvSCBSqGgDRjqCpPlPpppTpPjlcNP
zRzsGgJDqJwLVWVFwM
ThhWhNthVWTWqbWbFWbTdBtWSdMlHSlGlCGCdsCMClmnSlMn
DPPpvvfDHfLgDHvzpvPDsssMsmmzsMcClScMMcGG
rgPLHHJJHgZfvvZQQZfrpfFqBBwFBTNTBNBwtthQwVqt
JJgSWDSmSDQCFrhbRLSwLS
VznqzVNsMsZLdqslbRChtbHdHRrwHb
LVfNLMsLTmWDpBpf
cbTsnNpcnnchllFQlMRgJhRP
WddmdMVSBMWSBWjwCJVCPRwPFCQRRC
DWSSfjdSrTpDnHHMbZ
fgsVqqwQQtHhCrDfJH
pvbnBZWBbvWbTdthrJbDmqrmHq
TvZSNSNNSvFMBpqpnLnTBZBFGQwlQFggcFzcVGRlswsRll
zfMcQHzPtRNvlllc
BLnMhbZMLJLNNVtCdNgZgt
BJGFpqMBhBLLMqnwBhbrbhLssjFzssjfDzsmFmjmQFQPjT
JPBJPnpBFrqBJHtjlCjHJcCthM
wQZggQWQGfZFVmmGfDRjlvvNcvlNDhcNttlctt
SfmWfwVFwVGZWQVGSTdTbBpTPSqBbLnnrn
RJqBRJbqpqqJGvqHMmcfczfcjvHQfm
llgVnSWSlsssTnlWjhTcsZMcZcZMZMcccMNmcH
TnFhhllnWCnVCTllLnhhVSrbDDPrdpjRRqjBPRBBpbFJ
mRwRRNDjNTqwDNjNnNRTsQLcQWpQWZJLlLpQWs
PMFGCSzzgbBVzCGShVQZcgWsQLLftttQtlZZ
SlGVldCGGbBPMhPCVSBrNNdjRqjDrNmDnmrRwN
mqGGqGHnqGBCMrnGCbbbLgTTFFNNghHNTj
SdRfcsDPPcDdRzWPWltSlscwTSbShhgpQhgbFLbTQFjwhN
DPWWZzzztsDDtfzlscsPdcWZnVMNVqqGJnBrVqCrMrVvZnBJ
ZgglFCrrrlrWCJswHmwRVmFSwSsP
zhzqBLcjjnpzMzjhTtcqnVGbwssVRmqbHNPbwPsVNH
ftBjzLtptRWdvZlQQZQf
nGpsMncVRMGSnfsBllZdppwrTljZrQ
gcgHmtbCthHWhwBFBWZBlWlWrd
bCDDqHhcqbbtqcqtvJMzsGRsvVfPsfnzJV
TclPvSGZsPZRjhjWDgjp
JtnwHFtJqtwfQfgWgRWhdhjtgdRM
JBwnHwgFFqVJrsGmPvNTPsVvSN
ZJnfZNnDNZJLzNntDtDNNzNWTVBPrrvRRGdBcVRfPPcvfdMr
CFgjFmggQSQQmSggVMMvRdTvBVRjrdrc
mbsqQFqFgwwmgmSbwQWWLDWzpLcLnzZzLbLL
PnwSFSLSTwbbHdtstW
RrDZVVfJNZCmDCfVDVlblZHbddtHScbWbMjt
NmzqhzCCqmzffhCCqrhhLLnPvpnTPPgpGTTBSL
ShhfLSDDFMPQddpMrDgNbjzffqqqzgcjbqZR
sCstmwJwVBtmTltVmTVbRbcbcRvqvrZvBRvZbR
VwCnwnVrrrWShWPHHDdQFL
pbpDpWjZMmFCmmmb
jTjtJLJgJncCFmnJFC
LvhvhTQhBSdRNtLNsSszlGrHSGjZDlGf
JrhvTNJJhhCrtVtcrNLwDBSBwqzDwQVbBLQS
RnCgHmHHGMdPsGMfDlDqlSQbQnQQDbzD
RdPMPsmWHmjfMffPcCWrptcprpFTFrFp"""

assert Rucksack(example).sum_priorities() == 157
assert Rucksack(example).sum_priorities_of_group() == 70
print("Part 1:", Rucksack(puzzle_input).sum_priorities())
print("Part 2:", Rucksack(puzzle_input).sum_priorities_of_group())