import itertools

class LabeledNodes:

    # instructions: itertools.cycle[int] # 0 Left | 1 Right
    elements: dict[str, tuple[str, str]]
    END = "ZZZ"
    START = "AAA"

    def __init__ (self, s: str) -> None:
        i, e = s.split("\n\n", 1)
        self.instructions = itertools.cycle([0 if char == "L" else 1 for char in i])
        self.elements = {}
        for line in e.split("\n"):
            element, elements = line.split(" = ")
            self.elements[element] = tuple(elements.strip("()").split(", "))

    def count_steps (self) -> int:
        steps, element = 0, self.START
        while element != self.END:
            instruction = next(self.instructions)
            element = self.elements[element][instruction]
            steps += 1
        return steps

"""
Starting at AAA, how many steps are required to reach ZZZ ?
You need to look up the next element based on the next left/right instruction in your input
Repeat the whole sequence of instructions as necessary
"""

example = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
puzzle_input = """LLLLRLRLRRLRRRLRRLRLRRLRLLRRRLRRLRRRLRLLLRLRRLRLLRRRLRRLRLRRLLRRRLRRRLRLRRLRRRLRRLRRLLRRRLLLLRRLRRLRRLRRRLLLRLRLRLRRLRRRLRLRRRLRLRRRLRRLRRLLRRLLRLRRRLRLRRRLLLRLRRRLRLRRRLRRLRLRRLRRRLRRRLRRLLLRRRLRRLRRLRRLRRRLLLRRLRLRRRLLLLRRRLRRLRRRLLRLRLRRLLRRRLLRLRLRLRRLRRLRRRLRRLLRLRRLRRLLLLRRLRLRRLLRRLLRRLRRLRRRLLLRRRR

BRR = (LVC, FSJ)
BHX = (GMG, QTN)
TJD = (HQF, PBJ)
JGN = (JXR, DGK)
NMC = (VPC, CRF)
DVJ = (KMM, DFJ)
LML = (MTG, KNX)
JKL = (LRX, FRD)
FJR = (MHX, SBX)
LMC = (QNB, QCK)
LJF = (KCJ, HCT)
KTL = (XTG, NGM)
GJB = (KTQ, KTQ)
BXR = (TDR, KMK)
GKB = (VXT, NQR)
PJL = (FPL, TFX)
LNZ = (CJC, DQL)
KCG = (KDL, LMF)
PGG = (NDL, XXC)
PMS = (XQM, DFG)
CJF = (MCG, RTJ)
JTH = (PGS, SGZ)
QBS = (JSC, KMT)
DQL = (KRR, PBL)
HSF = (SNP, KJR)
XVQ = (VQR, HSX)
QKF = (PBT, XLC)
DNA = (DQL, CJC)
LNF = (RVC, TJD)
MKT = (LDX, CGC)
BXP = (RGX, TTR)
SBX = (PGT, JGN)
JQK = (HDQ, BHQ)
MHL = (TLX, JDN)
BBD = (QNJ, BRM)
MTT = (BVK, DXB)
FVR = (VLN, PRV)
RVC = (HQF, PBJ)
LDX = (LRS, KBV)
BKF = (PXH, TNB)
BRM = (XTV, NGH)
DDL = (JNG, SFF)
BBT = (BQJ, BCN)
GPK = (CVK, DDL)
TLX = (BDN, XNT)
JHL = (BRX, QBT)
NTL = (HSR, DJD)
XBH = (PJX, JQK)
PPF = (LCT, BJL)
SFF = (FVR, NFG)
HNA = (CTC, BSG)
CNG = (DXM, QFN)
GML = (NRD, TVN)
RHH = (NBT, LJH)
LDM = (DDN, TRN)
XSK = (PLB, NVJ)
NCQ = (MDN, XGT)
FCQ = (HCT, KCJ)
DRC = (JKL, JNM)
SHR = (KLX, VLH)
FTP = (DRN, DKV)
QBF = (GVS, NXK)
GXK = (XDK, LVF)
KMK = (VXV, XCS)
PKK = (QNJ, BRM)
NJH = (TKL, PQK)
BRX = (MNM, HVC)
VTD = (BJK, LML)
QVX = (DVJ, DSF)
GRM = (JCV, SQB)
RDQ = (HCG, XMB)
RGX = (FCN, TPD)
HBH = (FPR, DHX)
PHM = (JSP, RCR)
NBT = (FRG, CMJ)
XRH = (HCB, FBM)
GMR = (FDJ, NJD)
MVG = (RDJ, QSD)
BDL = (JSB, TFN)
VXT = (MBM, JND)
TXC = (QDG, LTV)
SRL = (RRX, NDS)
SGN = (MPL, CBB)
HVH = (SLJ, CBC)
VPC = (CCG, QSJ)
KCJ = (CKC, TTD)
RLT = (LLT, VVL)
RXV = (KXQ, VBR)
FQS = (STP, BHX)
SGC = (RLJ, QGB)
XLX = (HRG, DGV)
XKV = (QQB, TNQ)
SLJ = (GTB, MPF)
PKV = (CQN, THS)
RPP = (QFT, TNK)
DKL = (MFC, MFC)
BCG = (FXM, GPR)
RFV = (DRC, MPD)
VVC = (FGN, CVL)
HQB = (QNT, VVC)
RRP = (VVC, QNT)
TRS = (RCM, GHN)
QBT = (HVC, MNM)
XKS = (SCC, VXX)
TPS = (FMH, KFN)
MTS = (VXT, NQR)
FXM = (LDM, FQT)
LNB = (XJV, SJN)
HVF = (QXC, RBH)
LSG = (QHM, TSM)
JMP = (HBH, NQK)
NGM = (KDP, HHP)
HCG = (SLR, TSC)
HGX = (DFG, XQM)
DLG = (BVN, GMM)
DJD = (VGP, VML)
HBT = (XKL, JBQ)
NVJ = (GKX, PKS)
CPS = (PKJ, RSV)
SKN = (NBT, LJH)
CCK = (TTJ, SLV)
DXM = (CBN, BXR)
RJD = (XJH, SKH)
RDJ = (CNF, TTG)
PKJ = (BCM, XKC)
FQL = (SRV, DFC)
KDS = (MFB, CLQ)
QKR = (VGD, CXK)
XXC = (NFD, SPS)
PSQ = (NJH, BLR)
BLR = (PQK, TKL)
LMX = (DGV, HRG)
GCK = (CSR, CSR)
GKJ = (JHL, PNN)
GVS = (TLN, LJX)
FPR = (JCH, GKD)
VQV = (DGB, GGN)
CPF = (VMH, JQQ)
GKD = (SGF, PHM)
JNM = (LRX, FRD)
CXV = (LNF, HGF)
TNK = (RRD, HKC)
DXX = (LMC, ZZZ)
DGG = (PPF, TRR)
MLH = (TVL, PBR)
LBC = (LJL, FTR)
FVQ = (TBC, LKB)
LTF = (CBC, SLJ)
TVH = (XMS, GJS)
SFB = (TTJ, SLV)
LVF = (MBT, SJB)
XPP = (QDM, PJL)
BVK = (RPV, JMP)
VGD = (MRX, FJR)
FRD = (XBH, CDN)
LKM = (CMF, XNS)
TCJ = (MMS, PGG)
DHQ = (MTT, BKS)
HDQ = (GPH, XKH)
KTJ = (QQT, MKR)
NMQ = (VFK, VSD)
RSK = (QDM, PJL)
XQC = (KFP, HVB)
LQN = (NGM, XTG)
TKG = (XDQ, XDQ)
KBB = (VQR, HSX)
TQQ = (QDG, LTV)
SQN = (TDQ, XKV)
TSM = (TSH, MRP)
KPH = (THS, CQN)
HCB = (DVL, RTV)
MLR = (GHT, NSN)
BFM = (GCK, SLX)
GXQ = (QKM, JJL)
GNF = (HRQ, XTK)
TRR = (BJL, LCT)
AAA = (QNB, QCK)
SDL = (KJX, LSN)
DKV = (KBB, XVQ)
RMR = (MQR, CPR)
MQC = (CBV, SRP)
PRV = (KDS, FBX)
GTB = (CCK, SFB)
SNP = (PXX, SHR)
NTR = (VHT, KXK)
MKJ = (DDL, CVK)
LSQ = (HSF, RMN)
TTJ = (CBH, QKF)
DNH = (MVG, JCJ)
KMM = (KPH, PKV)
NTT = (RQK, PFK)
QMF = (BFM, PJB)
RJB = (RBH, QXC)
LRS = (MJT, BVM)
CJG = (RMR, BMN)
DVQ = (GXM, DDH)
MFC = (LMC, LMC)
XTG = (HHP, KDP)
HKB = (RDQ, TVT)
PKS = (JQM, DGG)
BJK = (KNX, MTG)
TVT = (XMB, HCG)
JNR = (JHG, JLN)
VFK = (XKS, QBH)
NPC = (PKK, BBD)
PXX = (KLX, VLH)
XLC = (NST, BXP)
CBB = (LMX, XLX)
KLX = (MSH, LCF)
CLQ = (JNF, JNC)
TSS = (MKR, QQT)
SSS = (RMQ, RCS)
QSD = (TTG, CNF)
NHG = (DVQ, VNB)
CTC = (VCN, RJD)
THS = (QRH, GPT)
KDR = (RTK, GKJ)
NTD = (CGG, SPN)
GHP = (NCQ, FCD)
KXQ = (RLS, VRM)
GNV = (BQJ, BCN)
DXQ = (QHC, FXN)
RQB = (FVQ, TNF)
CNF = (TXC, TQQ)
BGB = (QQS, LRV)
ZZZ = (QCK, QNB)
NFM = (MGV, VTD)
MFD = (DBF, KSN)
NST = (RGX, TTR)
XJV = (LGL, LGL)
TRQ = (TVH, KJL)
PPV = (CJP, VHH)
DNV = (DBM, VGJ)
JBQ = (MHL, RFN)
HRG = (JFD, VQP)
RMB = (JKJ, JGJ)
RGQ = (RSK, XPP)
KHF = (TJG, KPX)
HPZ = (BSG, CTC)
LFJ = (TSN, NMB)
MBT = (XRC, PJR)
QFN = (CBN, BXR)
QSJ = (BRS, BKF)
XJH = (RSF, VNP)
GST = (LVF, XDK)
DDN = (NMS, RLT)
CXK = (FJR, MRX)
PHH = (FPB, TCJ)
XHV = (KTJ, TSS)
VHT = (NPC, DMG)
RNL = (NHG, DVN)
TKL = (KPN, FKX)
DGB = (GPJ, QMF)
PNN = (QBT, BRX)
TBC = (NTR, FKG)
PGS = (QDT, JQL)
SLX = (CSR, LNB)
BVV = (LVC, FSJ)
JQL = (MLH, GSC)
PXH = (CJF, CKM)
LHM = (DSF, DVJ)
NND = (NTD, DTB)
MFB = (JNF, JNC)
TTR = (FCN, TPD)
HRQ = (JTD, JTD)
SLR = (TXT, JSN)
VQP = (XPK, XGB)
QHM = (MRP, TSH)
RTJ = (PXB, TLP)
QQT = (RRL, QHQ)
CSR = (XJV, XJV)
CJP = (CJG, HQQ)
RMC = (MPD, DRC)
XMS = (LXX, GPN)
HSR = (VGP, VML)
MNM = (VSS, QXR)
SJN = (LGL, LNZ)
KBV = (MJT, BVM)
KFN = (NRC, VSG)
JNC = (RHR, LFJ)
MPF = (SFB, CCK)
QVK = (GNK, BCG)
NJD = (KCG, LDB)
DBM = (MJG, MFD)
NKF = (GGN, DGB)
BCN = (JNR, MHK)
GNK = (FXM, GPR)
KMT = (HFC, CPS)
FDJ = (KCG, LDB)
LVD = (PHH, QDR)
FCN = (VDP, MQC)
QQB = (GJB, GJB)
PLF = (JNL, HBT)
QDM = (FPL, TFX)
GXM = (CLD, NNL)
MRV = (BCG, GNK)
LKB = (NTR, FKG)
TTG = (TQQ, TXC)
GFD = (VSD, VFK)
RCS = (KQQ, DNH)
QXR = (FCQ, LJF)
HMQ = (RJQ, FQL)
VCN = (SKH, XJH)
QQG = (HSR, DJD)
HGF = (RVC, TJD)
XMB = (TSC, SLR)
PJB = (GCK, SLX)
HFC = (RSV, PKJ)
JJL = (GXK, GST)
QTN = (JLV, SGX)
KDP = (GNV, BBT)
VRF = (TFN, JSB)
GPN = (CPF, SRQ)
TSC = (TXT, JSN)
CRF = (QSJ, CCG)
TNF = (TBC, LKB)
VLH = (LCF, MSH)
BCV = (JSC, KMT)
NNL = (KVX, FQS)
RVT = (HCB, FBM)
QHC = (QKV, NCJ)
VDP = (CBV, SRP)
CBV = (VQV, NKF)
CMF = (XHV, TPR)
TRN = (RLT, NMS)
JSB = (XTH, TRS)
CFC = (TVT, RDQ)
KDL = (TKG, TKG)
TTD = (BBC, GHP)
KJR = (PXX, SHR)
MTV = (GVS, NXK)
BVN = (KDR, PVP)
DXB = (RPV, JMP)
FSJ = (QPQ, GML)
PBJ = (LQN, KTL)
PXB = (BDL, VRF)
NDS = (BGB, NGX)
CBN = (KMK, TDR)
NFG = (VLN, PRV)
JTD = (PGS, PGS)
MKR = (QHQ, RRL)
JSN = (RFV, RMC)
CVK = (SFF, JNG)
FGN = (BVQ, XQC)
HHF = (RPS, QQF)
PLB = (PKS, GKX)
BJB = (QMC, GPG)
STP = (QTN, GMG)
DGK = (RKK, BVT)
JJM = (VGD, CXK)
LTS = (QPN, BCL)
LVC = (QPQ, GML)
QNB = (GJN, RVB)
RBH = (HMQ, HPS)
NQK = (DHX, FPR)
MRP = (BDT, SGN)
JQM = (TRR, PPF)
TSH = (BDT, SGN)
JLN = (JCC, FCB)
BRP = (LDX, CGC)
SJC = (HRQ, HRQ)
LJL = (BVB, PPV)
SPN = (SDL, VHM)
SDM = (DDF, LTS)
LJH = (FRG, CMJ)
CMG = (MKD, JGT)
GPR = (LDM, FQT)
QPQ = (NRD, TVN)
JCJ = (RDJ, QSD)
HSX = (CMG, SHF)
VML = (RMB, MHC)
DHX = (JCH, GKD)
MTG = (FPX, SPD)
BDT = (MPL, CBB)
CJC = (PBL, KRR)
JLS = (LJL, FTR)
HQF = (LQN, KTL)
HQQ = (RMR, BMN)
QMC = (RBP, PXD)
RPV = (HBH, NQK)
JHG = (JCC, FCB)
TPD = (VDP, MQC)
BHQ = (XKH, GPH)
XKC = (HDD, GXR)
RPS = (KJP, KJP)
QNT = (CVL, FGN)
JSC = (HFC, CPS)
KXG = (DTB, NTD)
CKM = (RTJ, MCG)
FTD = (KPX, TJG)
VSD = (XKS, QBH)
MCG = (TLP, PXB)
XKH = (HLP, CXV)
TNB = (CJF, CKM)
XTH = (RCM, GHN)
DFN = (GMR, DSS)
LMF = (TKG, XST)
FMH = (NRC, VSG)
XCS = (JTS, GRM)
GVF = (NDS, RRX)
CXM = (HGX, PMS)
VRM = (XJT, DXQ)
JLV = (QVX, LHM)
JCH = (PHM, SGF)
NMS = (VVL, LLT)
BHS = (XJR, LKM)
CKC = (BBC, GHP)
CBH = (XLC, PBT)
PRL = (QFT, TNK)
SDF = (VTD, MGV)
RVB = (MLR, XHT)
GPT = (PLF, MJX)
KRR = (RVT, XRH)
GXR = (BVV, BRR)
NSN = (RGQ, JMQ)
KJX = (TCR, MSL)
PHL = (TSM, QHM)
MQR = (MTS, GKB)
XDK = (SJB, MBT)
NRC = (DGN, BJB)
JQQ = (LBC, JLS)
JTS = (JCV, SQB)
RLJ = (JJM, QKR)
DTB = (CGG, SPN)
BRS = (PXH, TNB)
SRV = (SPC, DNV)
MNP = (JJL, QKM)
KTQ = (XSK, XSK)
FPX = (SJC, GNF)
VBR = (VRM, RLS)
KSN = (HQB, RRP)
RJQ = (SRV, DFC)
BKS = (BVK, DXB)
BVB = (VHH, CJP)
XTK = (JTD, JTH)
PBT = (BXP, NST)
PVP = (RTK, GKJ)
QPN = (BCV, QBS)
QQF = (KJP, HPZ)
QRH = (PLF, MJX)
GHS = (BKN, TPS)
RCM = (MNP, GXQ)
DCT = (DDF, LTS)
JLC = (HGX, PMS)
VNC = (XSK, CXZ)
BQJ = (MHK, JNR)
SHF = (JGT, MKD)
FXN = (QKV, NCJ)
FPB = (PGG, MMS)
JGJ = (KXG, NND)
VBM = (PSQ, QKN)
GKX = (DGG, JQM)
DSF = (KMM, DFJ)
CMJ = (GPK, MKJ)
NCJ = (SDM, DCT)
MKD = (GQG, DHQ)
CFZ = (RQB, SHH)
RQK = (DKL, DKL)
XGT = (HPQ, VRQ)
SRP = (NKF, VQV)
BSG = (VCN, RJD)
XRC = (NFM, SDF)
DVL = (SRL, GVF)
HVB = (HXS, MLD)
MPD = (JNM, JKL)
JSP = (PHL, LSG)
BCR = (XJR, LKM)
PQK = (KPN, FKX)
FCD = (XGT, MDN)
MDL = (JLC, CXM)
FBX = (CLQ, MFB)
VNP = (RGM, GHS)
HMK = (RMN, HSF)
SJB = (PJR, XRC)
JFD = (XPK, XGB)
HHP = (GNV, BBT)
TVN = (VBM, KJN)
DMG = (PKK, BBD)
RGM = (BKN, TPS)
TRF = (KXQ, VBR)
XHT = (NSN, GHT)
DFJ = (KPH, PKV)
KJP = (CTC, BSG)
LLT = (NTS, LVD)
RMN = (SNP, KJR)
GSC = (TVL, PBR)
RSV = (XKC, BCM)
TLP = (VRF, BDL)
GGN = (GPJ, QMF)
XJR = (CMF, XNS)
GQG = (BKS, MTT)
JPN = (MRV, QVK)
RSF = (RGM, GHS)
QQS = (DLG, JPV)
DGV = (VQP, JFD)
JDN = (XNT, BDN)
LMA = (QDT, JQL)
QDG = (QGC, DTX)
HDD = (BVV, BRR)
RRD = (CNG, XLJ)
QBH = (VXX, SCC)
GPH = (HLP, CXV)
CVN = (MRV, QVK)
RLS = (XJT, DXQ)
QKN = (NJH, BLR)
NRD = (VBM, KJN)
NMB = (HVF, RJB)
XNT = (RXV, TRF)
XNS = (XHV, TPR)
SGX = (LHM, QVX)
NTS = (PHH, QDR)
SPS = (LTF, HVH)
KPX = (BCR, BHS)
GNM = (RPS, RPS)
CXZ = (NVJ, PLB)
VVL = (LVD, NTS)
VTC = (NHG, DVN)
PXD = (BHH, SSS)
TVL = (MKT, BRP)
TPR = (KTJ, TSS)
MJX = (JNL, HBT)
BKN = (FMH, KFN)
MBM = (BVC, FTP)
RTV = (GVF, SRL)
GPG = (PXD, RBP)
KXK = (DMG, NPC)
JPV = (GMM, BVN)
LXP = (VPC, CRF)
RMQ = (DNH, KQQ)
DRN = (KBB, XVQ)
MMS = (XXC, NDL)
GMG = (SGX, JLV)
MJT = (KHF, FTD)
XJT = (QHC, FXN)
JMQ = (XPP, RSK)
QCS = (TVH, KJL)
BVC = (DRN, DKV)
SPC = (DBM, VGJ)
SHH = (TNF, FVQ)
VGA = (PLB, NVJ)
RKK = (JPN, CVN)
SCC = (TRQ, QCS)
CDN = (JQK, PJX)
VSS = (LJF, FCQ)
JNF = (LFJ, RHR)
VGP = (MHC, RMB)
VGJ = (MJG, MFD)
QGC = (RHH, SKN)
RKJ = (KTQ, VNC)
DTX = (SKN, RHH)
HPQ = (VDR, SGC)
CCG = (BRS, BKF)
VLN = (FBX, KDS)
BHH = (RMQ, RCS)
BBC = (FCD, NCQ)
JCV = (GNM, GNM)
TNQ = (GJB, RKJ)
QNJ = (NGH, XTV)
GHT = (RGQ, JMQ)
LJX = (CFC, HKB)
TLN = (HKB, CFC)
PFK = (DKL, LFL)
PJR = (SDF, NFM)
JNG = (NFG, FVR)
PJX = (BHQ, HDQ)
VHH = (CJG, HQQ)
RTK = (PNN, JHL)
XGB = (MLN, SQN)
JCC = (NQX, NTT)
BVT = (CVN, JPN)
HPS = (RJQ, FQL)
TCR = (DFN, RHS)
LLA = (SHH, RQB)
NGX = (QQS, LRV)
SLV = (CBH, QKF)
BMN = (CPR, MQR)
XKL = (RFN, MHL)
CGG = (VHM, SDL)
KJN = (PSQ, QKN)
LDB = (KDL, LMF)
SPD = (SJC, GNF)
VDR = (RLJ, QGB)
DDF = (QPN, BCL)
KQQ = (MVG, JCJ)
DSS = (FDJ, NJD)
NFD = (HVH, LTF)
GPJ = (BFM, PJB)
LGL = (DQL, CJC)
TDQ = (QQB, TNQ)
RCR = (PHL, LSG)
SKH = (VNP, RSF)
DGN = (QMC, GPG)
NGH = (RNL, VTC)
TSN = (HVF, RJB)
MGV = (LML, BJK)
QHQ = (LXP, NMC)
KJL = (GJS, XMS)
RBP = (BHH, SSS)
QDR = (FPB, TCJ)
RHR = (NMB, TSN)
NXK = (LJX, TLN)
FCB = (NQX, NTT)
TFN = (TRS, XTH)
MJG = (KSN, DBF)
BVQ = (KFP, HVB)
GMM = (PVP, KDR)
MDN = (VRQ, HPQ)
LTV = (DTX, QGC)
LRV = (DLG, JPV)
MHC = (JKJ, JGJ)
DFC = (DNV, SPC)
LXV = (SHH, RQB)
PBL = (RVT, XRH)
BDN = (RXV, TRF)
JKJ = (KXG, NND)
MSH = (MTV, QBF)
NDL = (SPS, NFD)
FKG = (VHT, KXK)
PBR = (MKT, BRP)
VSG = (BJB, DGN)
RRX = (BGB, NGX)
NQR = (JND, MBM)
MRX = (MHX, SBX)
DVN = (DVQ, VNB)
HKC = (CNG, XLJ)
PGT = (JXR, DGK)
DBF = (HQB, RRP)
FRG = (GPK, MKJ)
DFG = (NMQ, GFD)
QDT = (MLH, GSC)
KVX = (STP, BHX)
LCT = (MDL, KCL)
LSN = (TCR, MSL)
TXT = (RMC, RFV)
MXM = (LXV, CFZ)
TJG = (BHS, BCR)
BCM = (GXR, HDD)
FKX = (NTL, QQG)
SRQ = (JQQ, VMH)
BCL = (BCV, QBS)
LRX = (CDN, XBH)
RHS = (DSS, GMR)
CLD = (FQS, KVX)
XLJ = (DXM, QFN)
KCL = (CXM, JLC)
HXS = (PRL, RPP)
JND = (BVC, FTP)
VQR = (SHF, CMG)
VNB = (DDH, GXM)
QGB = (JJM, QKR)
CVL = (BVQ, XQC)
RFN = (JDN, TLX)
FBM = (DVL, RTV)
TFX = (LSQ, HMK)
XQM = (NMQ, GFD)
BJL = (KCL, MDL)
FTR = (PPV, BVB)
KNX = (FPX, SPD)
MHK = (JHG, JLN)
TDR = (XCS, VXV)
HVC = (VSS, QXR)
QXC = (HPS, HMQ)
RRL = (NMC, LXP)
MLD = (PRL, RPP)
LCF = (MTV, QBF)
VXV = (JTS, GRM)
XTV = (RNL, VTC)
LFL = (MFC, DXX)
CBC = (GTB, MPF)
CQN = (GPT, QRH)
DDH = (NNL, CLD)
GHN = (GXQ, MNP)
JGT = (DHQ, GQG)
HCT = (CKC, TTD)
QCK = (GJN, RVB)
SGF = (JSP, RCR)
MPL = (XLX, LMX)
XDQ = (LXV, LXV)
MLN = (TDQ, XKV)
SGZ = (JQL, QDT)
VRQ = (SGC, VDR)
FPL = (LSQ, HMK)
SQB = (GNM, HHF)
MHX = (PGT, JGN)
QFT = (HKC, RRD)
LXX = (CPF, SRQ)
CPR = (GKB, MTS)
HLP = (LNF, HGF)
GJS = (GPN, LXX)
QKV = (DCT, SDM)
XST = (XDQ, MXM)
VXX = (QCS, TRQ)
KFP = (HXS, MLD)
MSL = (RHS, DFN)
NQX = (RQK, PFK)
CGC = (LRS, KBV)
FQT = (TRN, DDN)
VMH = (LBC, JLS)
VHM = (LSN, KJX)
JXR = (BVT, RKK)
KPN = (QQG, NTL)
QKM = (GST, GXK)
JNL = (XKL, JBQ)
BVM = (KHF, FTD)
XPK = (SQN, MLN)
GJN = (MLR, XHT)"""
assert LabeledNodes(example).count_steps() == 6
print("Part 1:", LabeledNodes(puzzle_input).count_steps())