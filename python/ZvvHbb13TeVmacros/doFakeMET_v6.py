from ROOT import *
from array import *
from math import *
import copy

precut  = 90
cut     = 130
gROOT.SetBatch()

range_ = 1000

newHCSV = TLorentzVector()
j1 = TLorentzVector()
j2 = TLorentzVector()

def redoHCSV(old_tree,HCSV_pt,HCSV_eta,HCSV_phi,HCSV_mass):
    i1 = old_tree.hJCidx[0]
    i2 = old_tree.hJCidx[1]
    j1.SetPtEtaPhiM(old_tree.Jet_pt[i1],old_tree.Jet_eta[i1],old_tree.Jet_phi[i1],old_tree.Jet_mass[i1])
    j2.SetPtEtaPhiM(old_tree.Jet_pt[i2],old_tree.Jet_eta[i2],old_tree.Jet_phi[i2],old_tree.Jet_mass[i2])
    newHCSV         = j1 + j2
    HCSV_pt[0]      = newHCSV.Pt()
    HCSV_eta[0]     = newHCSV.Eta()
    HCSV_phi[0]     = newHCSV.Phi()
    HCSV_mass[0]    = newHCSV.M()


def redoJetArray(old_tree,idx,nJet,nhJCidx,naJCidx):
    tmpJet_pt            = old_tree.Jet_pt[idx]
    tmpJet_rawPt         = old_tree.Jet_rawPt[idx]
    tmpJet_eta           = old_tree.Jet_eta[idx]
    tmpJet_phi           = old_tree.Jet_phi[idx]
    tmpJet_btagCSV       = old_tree.Jet_btagCSV[idx]
    tmpJet_id            = old_tree.Jet_id[idx]
    tmpJet_puId          = old_tree.Jet_puId[idx]
    tmpJet_mass          = old_tree.Jet_mass[idx]
    tmpJet_leadTrackPt   = old_tree.Jet_leadTrackPt[idx]
    tmpJet_leptonPtRel   = old_tree.Jet_leptonPtRel[idx]
    tmpJet_leptonPt      = old_tree.Jet_leptonPt[idx]
    tmpJet_leptonDeltaR  = old_tree.Jet_leptonDeltaR[idx]
    tmpJet_vtxPt         = old_tree.Jet_vtxPt[idx]
    tmpJet_vtxMass       = old_tree.Jet_vtxMass[idx]
    tmpJet_vtx3DVal      = old_tree.Jet_vtx3DVal[idx]
    tmpJet_vtxNtracks    = old_tree.Jet_vtxNtracks[idx]
    tmpJet_vtx3DSig      = old_tree.Jet_vtx3DSig[idx]
    tmpJet_chEmEF        = old_tree.Jet_chEmEF[idx]
    tmpJet_neEmEF        = old_tree.Jet_neEmEF[idx]
    tmpJet_chHEF         = old_tree.Jet_chHEF[idx]
    tmpJet_neHEF         = old_tree.Jet_neHEF[idx]
    tmpJet_chMult        = old_tree.Jet_chMult[idx]
    tmpJet_mult          = old_tree.Jet_mult[idx]

    i = idx
    while (i<nJet[0]-1 and old_tree.Jet_pt[i+1]>tmpJet_pt):
        old_tree.Jet_id[i]       = old_tree.Jet_id[i+1]
        old_tree.Jet_puId[i]     = old_tree.Jet_puId[i+1]
        old_tree.Jet_pt[i]            = old_tree.Jet_pt[i+1]
        old_tree.Jet_rawPt[i]         = old_tree.Jet_rawPt[i+1]
        old_tree.Jet_eta[i]           = old_tree.Jet_eta[i+1]
        old_tree.Jet_phi[i]           = old_tree.Jet_phi[i+1]
        old_tree.Jet_btagCSV[i]       = old_tree.Jet_btagCSV[i+1]
        old_tree.Jet_mass[i]          = old_tree.Jet_mass[i+1]
        old_tree.Jet_leadTrackPt[i]   = old_tree.Jet_leadTrackPt[i+1]
        old_tree.Jet_leptonPtRel[i]   = old_tree.Jet_leptonPtRel[i+1]
        old_tree.Jet_leptonPt[i]      = old_tree.Jet_leptonPt[i+1]
        old_tree.Jet_leptonDeltaR[i]  = old_tree.Jet_leptonDeltaR[i+1]
        old_tree.Jet_vtxPt[i]         = old_tree.Jet_vtxPt[i+1]
        old_tree.Jet_vtxMass[i]       = old_tree.Jet_vtxMass[i+1]
        old_tree.Jet_vtx3DVal[i]      = old_tree.Jet_vtx3DVal[i+1]
        old_tree.Jet_vtxNtracks[i]    = old_tree.Jet_vtxNtracks[i+1]
        old_tree.Jet_vtx3DSig[i]      = old_tree.Jet_vtx3DSig[i+1]
        old_tree.Jet_chEmEF[i]        = old_tree.Jet_chEmEF[i+1]
        old_tree.Jet_neEmEF[i]        = old_tree.Jet_neEmEF[i+1]
        old_tree.Jet_chHEF[i]         = old_tree.Jet_chHEF[i+1]
        old_tree.Jet_neHEF[i]         = old_tree.Jet_neHEF[i+1]
        old_tree.Jet_chMult[i]        = old_tree.Jet_chMult[i+1]
        old_tree.Jet_mult[i]          = old_tree.Jet_mult[i+1]
        i += 1

    old_tree.Jet_pt[i]            = tmpJet_pt
    old_tree.Jet_rawPt[i]         = tmpJet_rawPt
    old_tree.Jet_eta[i]           = tmpJet_eta
    old_tree.Jet_phi[i]           = tmpJet_phi
    old_tree.Jet_btagCSV[i]       = tmpJet_btagCSV
    old_tree.Jet_id[i]            = tmpJet_id
    old_tree.Jet_puId[i]          = tmpJet_puId
    old_tree.Jet_mass[i]          = tmpJet_mass
    old_tree.Jet_leadTrackPt[i]   = tmpJet_leadTrackPt
    old_tree.Jet_leptonPtRel[i]   = tmpJet_leptonPtRel
    old_tree.Jet_leptonPt[i]      = tmpJet_leptonPt
    old_tree.Jet_leptonDeltaR[i]  = tmpJet_leptonDeltaR
    old_tree.Jet_vtxPt[i]         = tmpJet_vtxPt
    old_tree.Jet_vtxMass[i]       = tmpJet_vtxMass
    old_tree.Jet_vtx3DVal[i]      = tmpJet_vtx3DVal
    old_tree.Jet_vtxNtracks[i]    = tmpJet_vtxNtracks
    old_tree.Jet_vtx3DSig[i]      = tmpJet_vtx3DSig
    old_tree.Jet_chEmEF[i]        = tmpJet_chEmEF
    old_tree.Jet_neEmEF[i]        = tmpJet_neEmEF
    old_tree.Jet_chHEF[i]         = tmpJet_chHEF
    old_tree.Jet_neHEF[i]         = tmpJet_neHEF
    old_tree.Jet_chMult[i]        = tmpJet_chMult
    old_tree.Jet_mult[i]          = tmpJet_mult

    if nJet[0]>0 and old_tree.Jet_pt[nJet[0]-1]<15: nJet[0]=nJet[0]-1

    CSVs=[]
    for i in range(nJet[0]):
        if abs(old_tree.Jet_eta[i])>2.4 or old_tree.Jet_pt[i]<15: continue
        CSVs.append((old_tree.Jet_btagCSV[i],i))

    CSVs.sort(reverse=True)
#    print CSVs
#    print old_tree.nJet,old_tree.nhJCidx,old_tree.naJCidx

    hJCidx =0
    aJCidx =0
    count=0
    for CSV,i in CSVs:
#        print count,i
        if (count<2):
            if hJCidx<old_tree.nhJCidx:
                old_tree.hJCidx[hJCidx] = i
                hJCidx+=1
            else:
                print "Warning hJCidx:",hJCidx,old_tree.nhJCidx,count
        else:
            if aJCidx<old_tree.naJCidx:
                old_tree.aJCidx[aJCidx] = i
                aJCidx+=1
            else:
                print "Warning aJCidx:",aJCidx,old_tree.naJCidx,count
        count+=1

    nhJCidx[0] = hJCidx
    naJCidx[0] = aJCidx


def redohJCidx(old_tree):
    maxCSVidx = -1
    maxCSV = -20
    for i in old_tree.aJCidx:
        if old_tree.Jet_btagCSV[i]>maxCSV:
            maxCSV      = old_tree.Jet_btagCSV[i]
            maxCSVidx   = i
    if(maxCSVidx>=0):
        old_tree.hJCidx[0] = old_tree.hJCidx[1]
        old_tree.hJCidx[1] = maxCSVidx


def smartFit(histo,default,formula="gaus(0)+gaus(3)+gaus(6)+gaus(9)"):
    a_=0.25
    b_=1
    c_=5

    function = TF1("function",formula,-c_,c_)
    function.SetParameters(*default)
#    for i in range(function.GetNpar()):
#        if ((i)%3)==0:
#            function.SetParLimits(i,0,1)
#        elif ((i-2)%3)==0:
#            function.SetParLimits(i,0,999999)

    for i in range(function.GetNpar()):
        if not i in [0,1,2]:
            function.FixParameter(i,function.GetParameter(i))
        else:
            function.ReleaseParameter(i)
            if ((i)%3)==0:
                function.SetParLimits(i,0,1)
            elif ((i-2)%3)==0:
                function.SetParLimits(i,0,999999)
            elif ((i-2)%3)==0:
                function.SetParLimits(i,0,999999)
    histo.Fit(function,"","",-a_,a_)

    for i in range(function.GetNpar()):
        if not i in [3,4,5]:
            function.FixParameter(i,function.GetParameter(i))
        else:
            function.ReleaseParameter(i)
            if ((i)%3)==0:
                function.SetParLimits(i,0,1)
            elif ((i-1)%3)==0:
                function.SetParLimits(i,-1,1)
            elif ((i-2)%3)==0:
                function.SetParLimits(i,0,999999)
    histo.Fit(function,"","",-b_,-a_)

    for i in range(function.GetNpar()):
        if not i in [6,7,8]:
            function.FixParameter(i,function.GetParameter(i))
        else:
            function.ReleaseParameter(i)
            if ((i)%3)==0:
                function.SetParLimits(i,0,1)
            elif ((i-1)%3)==0:
                function.SetParLimits(i,-1,1)
            elif ((i-2)%3)==0:
                function.SetParLimits(i,0,999999)
    histo.Fit(function,"","",-c_,-b_)

    for i in range(function.GetNpar()):
        if not i in [9,10,11]:
            function.FixParameter(i,function.GetParameter(i))
        else:
            function.ReleaseParameter(i)
            if ((i)%3)==0:
                function.SetParLimits(i,0,1)
            elif ((i-1)%3)==0:
                function.SetParLimits(i,-1,1)
            elif ((i-2)%3)==0:
                function.SetParLimits(i,0,999999)
    histo.Fit(function,"","",-c_,c_)

    for i in range(function.GetNpar()):
        function.ReleaseParameter(i)
        if ((i)%3)==0:
            function.SetParLimits(i,0,1)
        elif ((i-2)%3)==0:
            function.SetParLimits(i,0,999999)

    histo.Fit(function,"","",-c_,c_)
#    function.Draw("same")
    return function

#def smartFit(histo,formula="(1+[4]*x**[5])*(exp([0]+[1]*x)+exp([2]+[3]*x))",min_=-.,mid_=60.,max_=1000.):
#    function = TF1("function",formula,min_,max_)
#    function.SetParameters(6.58,-0.032,13.32,-0.102,0,0,0)

#    for i in range(function.GetNpar()):
#        if not i in [0,1,2,3]:
#            function.FixParameter(i,function.GetParameter(i))
#        else:
#            function.ReleaseParameter(i)
#
#    histo.Fit(function,"","",mid_,max_)

#    for i in range(function.GetNpar()):
#        if i in [0,1,2,3]:
#            function.FixParameter(i,function.GetParameter(i))
#        else:
#            function.ReleaseParameter(i)

#    histo.Fit(function,"","",min_,mid_)

#    for i in range(function.GetNpar()):
#            function.ReleaseParameter(i)

#    histo.Fit(function,"","",min_+20,max_)
#    histo.Fit(function,"","",min_+10,max_)
#    histo.Fit(function,"","",min_,max_)
#    return function

def getJetIdx(nJets,nGenJets,Jet_pt,Jet_mcIdx,GenJet_wNuPt):
    idx=int(-1)
    diff=-1
    ndiff=0
    for i in range(nJets):
#        if Jet_mcIdx[i]<0 or Jet_mcIdx[i]>=nGenJets: continue
#        if Jet_mcIdx[i]>=nGenJets or Jet_mcIdx[i]<0 : continue
        if Jet_mcIdx[i]>=nGenJets or Jet_mcIdx[i]<0 or abs(tree.GenJet_wNuEta[Jet_mcIdx[i]])>2.6 : continue
        ndiff=abs(GenJet_wNuPt[Jet_mcIdx[i]]-Jet_pt[i])
        if ndiff>diff:
            idx=i
            diff=ndiff
    return int(idx)

def newPt(GenJet_wNuPt,Jet_pt,Jet_phi,met_pt,met_phi,function,cut):
    sign = (Jet_pt-GenJet_wNuPt)/abs(Jet_pt-GenJet_wNuPt)
    Jet_ptNew = Jet_pt
    met_ptx = met_pt * cos(met_phi)
    met_pty = met_pt * sin(met_phi)
    Jet_ptx = Jet_pt * cos(Jet_phi)
    Jet_pty = Jet_pt * sin(Jet_phi)
    metNoJet_ptx = met_ptx + Jet_ptx
    metNoJet_pty = met_pty + Jet_pty
    i=0
    newMet_pt_squared = met_pt**2
    count=1
    Jet_ptNew_min = Jet_ptNew
    Jet_ptNew_max = Jet_ptNew
    while(newMet_pt_squared < cut**2 and count<1E5):
        count+=1
        rdm = function.GetRandom()
#        while rdm*sign<0:
#            rdm = function.GetRandom()
        Jet_ptNew = GenJet_wNuPt + rdm
        if Jet_ptNew<Jet_ptNew_max and Jet_ptNew>Jet_ptNew_min: continue
        Jet_ptNew_min = min(Jet_ptNew_min,Jet_ptNew)
        Jet_ptNew_max = max(Jet_ptNew_max,Jet_ptNew)
        met_ptx = metNoJet_ptx - Jet_ptNew * cos(Jet_phi)
        met_pty = metNoJet_pty - Jet_ptNew * sin(Jet_phi)
        newMet_pt_squared = met_ptx**2+met_pty**2

    if count>1E4: print "count = ",count
    if Jet_ptNew<0: Jet_ptNew=0
    return Jet_ptNew,count

def correctMet(met_pt,met_phi,Jet_pt,Jet_phi,Jet_ptNew):
    met_ptx = met_pt * cos(met_phi)
    met_pty = met_pt * sin(met_phi)
    Jet_ptx = Jet_pt * cos(Jet_phi)
    Jet_pty = Jet_pt * sin(Jet_phi)
    JetNew_ptx = Jet_ptNew * cos(Jet_phi)
    JetNew_pty = Jet_ptNew * sin(Jet_phi)
    met_ptx = met_ptx + Jet_ptx - JetNew_ptx
    met_pty = met_pty + Jet_pty - JetNew_pty
    met_pt  = (met_ptx**2+met_pty**2)**0.5
    if met_ptx==0:
        if met_pty>0: met_phi=pi
        else: met_phi=-pi
    else:
        met_phi = atan(met_pty/met_ptx)
    if met_ptx<0: met_phi+=pi
    if met_phi>pi: met_phi-=2*pi
    if met_phi<-pi: met_phi+=2*pi
    return met_pt,met_phi

#file_ = TFile("tree_100_QCDHT300.root")

def doFile(fileName="tree_100_QCDHT700.root",outName="newTree.root",function=None):

    if function is None:
        c1              = TCanvas()
#        chainN          = fileName
        chainN          = fileName.split("/tree_")[0]+"/tree_*.root"
        chain           = TChain("tree")
        chain.Add(chainN)
        nEntries = chain.GetEntries()
        histo = TH1F("histo","histo",2000,-1000,+1000)
        for entry in range(0,nEntries):
            #print entry
#            if entry>1E5: break
            chain.GetEntry(entry)
            if chain.met_pt<precut: continue
            idx = getJetIdx(chain.nJet,chain.nGenJet,chain.Jet_pt,chain.Jet_mcIdx,chain.GenJet_wNuPt)
            if idx<0:
                print "X"
                continue
            if chain.Jet_mcIdx[idx]<0: continue
            histo.Fill((chain.Jet_pt[idx]-chain.GenJet_wNuPt[chain.Jet_mcIdx[idx]]))
        histo.Draw()
        print "Fitting function in: ",chainN
#        chain.Draw(" log(Jet_pt/GenJet_wNuPt[Jet_mcIdx])  >> histo(1000,-3,3)","Jet_mcIdx==0 && GenJet_wNuPt[Jet_mcIdx]>0 && abs(GenJet_wNuEta[Jet_mcIdx])<2.6 && met_pt>%d"%precut,"NORM")
#        histo = gDirectory.Get("histo")

#        default=(0.015,0.027,0.094,0.0060,-0.050,0.15,0.00015,-0.13,0.44)
#        function = smartFit(histo,default,"gaus(0)+gaus(3)+gaus(6)")

        import copy
        function = copy.deepcopy(histo)

        c1.SetLogy()
        c1.SaveAs(outName.replace(".root","_fit.png"))
        c1.SaveAs(outName.replace(".root","_fit.C"))
#        c1.SaveAs(outName.replace(".root","_fit.root"))
#        chain.Delete()

#    old_tree            = TChain("tree")
#    old_tree.Add(fileNames)
#    file_               = old_tree.GetFile()


    file_               = TFile(fileName)
    old_tree            = file_.Get("tree")
    old_Count           = file_.Get("Count")
    old_CountWeighted   = file_.Get("CountWeighted")
    old_CountPosWeight  = file_.Get("CountPosWeight")
    old_CountNegWeight  = file_.Get("CountNegWeight")


    fileNew = TFile(outName,"recreate")
    fileNew.cd()
    #tree.Write()

    #old_tree.Draw("(MaxIf$(abs(GenJet_wNuPt[Jet_mcIdx] - Jet_pt),Jet_mcIdx>=0 && GenJet_wNuPt[Jet_mcIdx]>0 && abs(GenJet_wNuEta[Jet_mcIdx])<2.6)) >> histo(1000,0,1000)","")
    #function = smartFit(histo,"(1+[4]+[5]*x**2)*(exp([0]+[1]*x)+exp([2]+[3]*x))")
    #1/0
    #tree = old_tree
    #return

    tree            = old_tree.CloneTree(0)
    #tree            = old_tree.CopyTree(1000,0)
    Count           = old_Count.Clone("Count")
    CountWeighted   = old_CountWeighted.Clone("CountWeighted")
    CountPosWeight  = old_CountPosWeight.Clone("CountPosWeight")
    CountNegWeight  = old_CountNegWeight.Clone("CountNegWeight")
    FakeMET_count   = old_CountNegWeight.Clone("FakeMET_count")
    FakeMET_count.SetBinContent(0,0)
    #file_.Close()

    Vtype = array('f',[0])
    tree.SetBranchAddress("Vtype",Vtype)

    nJet = array('I',[0])
    tree.SetBranchAddress("nJet",nJet)

    nhJCidx = array('I',[0])
    tree.SetBranchAddress("nhJCidx",nhJCidx)

    naJCidx = array('I',[0])
    tree.SetBranchAddress("naJCidx",naJCidx)

    HLT_BIT_HLT_PFMET90_PFMHT90_IDLoose_v = array('f',[0])
    tree.SetBranchAddress("HLT_BIT_HLT_PFMET90_PFMHT90_IDLoose_v",HLT_BIT_HLT_PFMET90_PFMHT90_IDLoose_v)

    HCSV_mass = array('f',[0])
    tree.SetBranchAddress("HCSV_mass",HCSV_mass)

    HCSV_pt = array('f',[0])
    tree.SetBranchAddress("HCSV_pt",HCSV_pt)

    HCSV_phi = array('f',[0])
    tree.SetBranchAddress("HCSV_phi",HCSV_phi)

    HCSV_eta = array('f',[0])
    tree.SetBranchAddress("HCSV_eta",HCSV_eta)

    met_pt = array('f',[0])
    tree.SetBranchAddress("met_pt",met_pt)

    met_phi = array('f',[0])
    tree.SetBranchAddress("met_phi",met_phi)

    mhtJet30 = array('f',[0])
    tree.SetBranchAddress("mhtJet30",mhtJet30)

    mhtPhiJet30 = array('f',[0])
    tree.SetBranchAddress("mhtPhiJet30",mhtPhiJet30)

    htJet30 = array('f',[0])
    tree.SetBranchAddress("htJet30",htJet30)

    FakeMET_met = array('f',[0])
    tree.Branch('FakeMET_met',FakeMET_met,'FakeMET_met/F')

    FakeMET_metPhi = array('f',[0])
    tree.Branch('FakeMET_metPhi',FakeMET_metPhi,'FakeMET_metPhi/F')

    FakeMET_jetPt = array('f',[0])
    tree.Branch('FakeMET_jetPt',FakeMET_jetPt,'FakeMET_jetPt/F')

    FakeMET_jetIdx = array('i',[0])
    tree.Branch('FakeMET_jetIdx',FakeMET_jetIdx,'FakeMET_jetIdx/I')

    nEntries = old_tree.GetEntries()

    for entry in range(0,nEntries):
        old_tree.GetEntry(entry)
#        print old_tree.nJet
#        print nJet[0]
#        print nJet
#        print
        if not old_tree.met_pt>precut: continue
    #    if entry>1000: break
    #    idx                     = getJetIdx(old_tree.nJet,old_tree.nGenJet,old_tree.Jet_pt,old_tree.Jet_mcIdx,old_tree.GenJet_wNuPt)
        idx = 0
        if idx>=old_tree.nJet or idx<0 or old_tree.Jet_mcIdx[idx]<0 or old_tree.Jet_mcIdx[idx]>=old_tree.nGenJet:
            print
            print idx
            print old_tree.nJet
            continue
        FakeMET_met[0]          = old_tree.met_pt
        FakeMET_metPhi[0]       = old_tree.met_phi
        FakeMET_jetPt[0]        = old_tree.Jet_pt[idx]
        FakeMET_jetIdx[0]       = idx

        nJet[0]    = old_tree.nJet
        nhJCidx[0] = old_tree.nhJCidx
        naJCidx[0] = old_tree.naJCidx

#        print "Before"
#        for i in range(nJet[0]):
#            print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]
#        print "CSV"
#        for i in old_tree.hJCidx:
#            print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]
#        for i in old_tree.aJCidx:
#            print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]

        newPt_,count            = newPt(old_tree.GenJet_wNuPt[old_tree.Jet_mcIdx[idx]],old_tree.Jet_pt[idx],old_tree.Jet_phi[idx],old_tree.met_pt,old_tree.met_phi,function,cut)
        newPt_15                = newPt_
        newPt_30                = newPt_
        if newPt_15<15: newPt_15=0
        if newPt_30<30: newPt_30=0
        (met_pt[0],met_phi[0])  = correctMet(old_tree.met_pt,old_tree.met_phi,old_tree.Jet_pt[idx],old_tree.Jet_phi[idx],newPt_)
        if old_tree.Jet_pt[idx]>30 and old_tree.Jet_puId[idx]==1 and abs(old_tree.Jet_eta[idx])<2.4:
            htJet30[0]  = old_tree.htJet30 - old_tree.Jet_pt[idx] + newPt_30
            (mhtJet30[0],mhtPhiJet30[0]) = correctMet(old_tree.mhtJet30,old_tree.mhtPhiJet30,old_tree.Jet_pt[idx],old_tree.Jet_phi[idx],newPt_30)

        old_tree.Jet_pt[idx]    = newPt_15
        Vtype[0]                   = 4
        HLT_BIT_HLT_PFMET90_PFMHT90_IDLoose_v[0] = 1

        redoHCSV_ = True
        if idx in old_tree.hJCidx: redoHCSV_ = True

        redoJetArray(old_tree,idx,nJet,nhJCidx,naJCidx)

#        if newPt_15==0:
#            print "X"*1000
#            print "After"
#            for i in range(nJet[0]):
#                print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]
#            print "CSV"
#            for i in old_tree.hJCidx:
#                print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]
#            for i in old_tree.aJCidx:
#                print old_tree.Jet_pt[i], old_tree.Jet_eta[i], old_tree.Jet_btagCSV[i]

        ## if the leading jet was in hJCidx and now pt<15 -> recalculate hJCidx
        if idx in old_tree.hJCidx and newPt_15==0: redohJCidx(old_tree)

        if redoHCSV_:    redoHCSV(old_tree,HCSV_pt,HCSV_eta,HCSV_phi,HCSV_mass)

        tree.Fill()

    FakeMET_count.SetBinContent(1,CountWeighted.GetBinContent(1))
    ratio = 1.*tree.Draw("","met_pt>%d"%cut)/(1E-9+tree.Draw("","FakeMET_met>%d"%cut))
    tree.AutoSave()

    Count.SetBinContent(1,ratio*Count.GetBinContent(1))
    CountWeighted.SetBinContent(1,ratio*CountWeighted.GetBinContent(1))
    CountPosWeight.SetBinContent(1,ratio*CountPosWeight.GetBinContent(1))
    CountNegWeight.SetBinContent(1,ratio*CountNegWeight.GetBinContent(1))

    Count.Write()
    CountWeighted.Write()
    CountPosWeight.Write()
    CountNegWeight.Write()
    FakeMET_count.Write()
    fileNew.Close()
    return function

if __name__ == "__main__":
    f       = TFile("newTree_fit.root")
    function = f.Get("c1").GetPrimitive("histo")
#    function = copy.copy(function)
    fileName="/gpfs/ddn/srm/cms/store/user/arizzi/VHBBHeppyV14//QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBB_HEPPY_V14_QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8__RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/151024_181957/0000/tree_1.root"
#    fileName="/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/ZvvHighPt_V15_QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#    fileName="/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/ZvvHighPt_V15_QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#    fileName="/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/ZvvHighPt_V15_QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#    fileName="/gpfs/ddn/srm/cms/store/user/arizzi/VHBBHeppyV14//QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/VHBB_HEPPY_V14_QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8__RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/151025_083609/0000/tree_1.root"
    outName="newTree.root"
    doFile(fileName,outName,function)


