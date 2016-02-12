from ROOT import *
from array import *
from math import *

gROOT.SetBatch()
preselection = "AntiSoftLetponDecay && (!Jet_over[0] && !Jet_overMC[0] && Sum$((Jet_under||Jet_underMC) * (Jet_pt>25) * (abs(TVector2::Phi_mpi_pi ( Jet_phi-met_phi ))<0.785))==0)"

def fixCountFile(fileName="tree_100_QCDHT700.root",outName="newTree.root"):

    file_               = TFile(fileName)
    old_tree            = file_.Get("tree")
    old_Count           = file_.Get("Count")
    old_CountWeighted   = file_.Get("CountWeighted")
    old_CountPosWeight  = file_.Get("CountPosWeight")
    old_CountNegWeight  = file_.Get("CountNegWeight")
    old_FakeMET_count  = file_.Get("FakeMET_count")

    fileNew = TFile(outName,"recreate")
    fileNew.cd()

#    tree            = old_tree.CopyTree("")
#    Count           = old_Count.Clone("Count")
    tree            = old_tree.CloneTree()
    Count           = old_Count.Clone("Count")
    CountWeighted   = old_CountWeighted.Clone("CountWeighted")
    CountPosWeight  = old_CountPosWeight.Clone("CountPosWeight")
    CountNegWeight  = old_CountNegWeight.Clone("CountNegWeight")
    FakeMET_count   = old_FakeMET_count.Clone("FakeMET_count")

    newcount        = old_Count.GetBinContent(1)
    count           = old_FakeMET_count.GetBinContent(1)
    events          = 1.*old_tree.Draw("",preselection)
    eventsOriginal  = 1.*old_tree.Draw("","(FakeMET_met==met_pt)&&"+preselection)
    if eventsOriginal!=0:
        oldcount        = newcount
        newcount        = count*events/eventsOriginal
        print "eventsTrue:",eventsOriginal
        print "eventsFake(including true):",events
        print "count original:",count
        print "count fake (old):",oldcount
        print "count fake (new):",newcount


    Count.SetBinContent(1,newcount)
    CountWeighted.SetBinContent(1,newcount)
    CountPosWeight.SetBinContent(1,newcount)
    CountNegWeight.SetBinContent(1,0)

#    tree.AutoSave()
    tree.Write()
    Count.Write()
    CountWeighted.Write()
    CountPosWeight.Write()
    CountNegWeight.Write()
    FakeMET_count.Write()
    fileNew.Close()

if __name__ == "__main__":

    dirIn       = "/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/syst/"
    dirOut       = "/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/syst/"

    files = [
        'ZvvHighPt_V15_FakeQCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
       'ZvvHighPt_V15_FakeQCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
        'ZvvHighPt_V15_FakeQCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
    ]

    import os
    for file_ in files:
        pathIn = dirIn + file_
        pathOut = dirIn + file_.replace(".root","_old.root")
        print "Moving ",pathIn," in ",pathOut
        os.rename(pathIn, pathOut)
        print "Launching ",pathOut," to ",pathIn
        fixCountFile(pathOut,pathIn)
#
#    fileName="/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/syst/MVAout_v0.0.0/ZvvHighPt_V15_FakeQCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#    outName="/scratch/sdonato/VHbbRun2/V14_forPreApproval/CMSSW_7_1_5/src/Xbb/env/syst/MVAout_v0.0.0/ZvvHighPt_V15_FakeQCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_corr.root"
#    fixCountFile(fileName,outName)

