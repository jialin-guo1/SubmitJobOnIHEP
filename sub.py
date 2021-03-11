#this script will creat a .sh file and submit it

import sys, os, pwd, commands
import argparse
parser = argparse.ArgumentParser(description="A simple ttree plotter")
parser.add_argument("-n", "--jobname", dest="jobname", default="ControlRegin_SS", help="jobname also the codes file name")
parser.add_argument("-p", "--path", dest="path", default="/cms/user/guojl/CMSSW_10_6_12/src/HToZZ4lRepeat/ZplusX", help="codes file path")
parser.add_argument("-c", "--codename", dest="codename", default="ControlRegin_SS.py", help="excutable codes file name")
parser.add_argument("-v","--verbosity",dest="verbosity",default=True, help="True is data False is MC")
args = parser.parse_args()

# define function for processing the external os commands
def processCmd(cmd, quite = 0):
    #    print cmd
    status, output = commands.getstatusoutput(cmd)
    if (status !=0 and not quite):
        print 'Error in processing command:\n   ['+cmd+']'
        print 'Output:\n   ['+output+'] \n'
        return "ERROR!!! "+output
    else:
        return output
# using "with open as f" will close the file automatically
jobfile = args.jobname+".sh"
with open(jobfile,"w") as outSH:
    outSH.write("#!/bin/bash\n")
    outSH.write("/bin/hostname\n")
    outSH.write("gcc -v\n")
    outSH.write("pwd\n")
    outSH.write("cd {}\n".format(args.path)) #this is the path storing excutable codes
    #outSH.write("cd ~\n")
    outSH.write("python {0:s}{1:s}\n".format(args.jobname,".py"))
    #outSH.write("python {0:s}{1:s} -i WZ_2018.root -o WZ_2018.root -v False".format(args.jobname,".py"))
    #outSH.write("python {0:s}{1:s} -i 2018_noDuplicates.root -o 2018_noDuplicates.root ".format(args.jobname,".py"))
    #outSH.write("gfal-copy -r -v -T 999999 gsiftp://cmspn001.ihep.ac.cn/pnfs/ihep.ac.cn/data/cms/store/user/chenguan/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8   gsiftp://ccsrm.ihep.ac.cn/dpm/ihep.ac.cn/home/cms/store/user/guoj")


cmd = 'chmod 777 {}'.format(jobfile)
output = processCmd(cmd)
cmd = 'hep_sub {0:s} -wt mid -o /publicfs/cms/user/guojl/sub_out/{1:s}.log -e /publicfs/cms/user/guojl/sub_out/{2:s}.err'.format(jobfile,args.jobname,args.jobname)
#cmd = 'hep_sub {0:s}  -o /publicfs/cms/user/guojl/sub_out/{1:s}.log -e /publicfs/cms/user/guojl/sub_out/{2:s}.err'.format(jobfile,args.jobname,args.jobname)
output = processCmd(cmd)
print output
