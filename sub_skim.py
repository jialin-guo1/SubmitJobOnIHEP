#this script will creat a .sh file and submit it

import sys, os, pwd, commands
import argparse
parser = argparse.ArgumentParser(description="A simple ttree plotter")
parser.add_argument("-n", "--jobname", dest="jobname", default="ControlRegin_SS", help="jobname also the codes file name")
parser.add_argument("-p", "--path", dest="path", default="/cms/user/guojl/CMSSW_10_6_12/src/HToZZ4lRepeat/", help="codes file path")
parser.add_argument("-c", "--codename", dest="codename", default="ControlRegin_SS.py", help="excutable codes file name")
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

jobfile = args.jobname+".sh"
with open(jobfile,"w") as outSH:
    outSH.write("#!/bin/bash\n")
    outSH.write("/bin/hostname\n")
    outSH.write("gcc -v\n")
    outSH.write("pwd\n")
    outSH.write("cd {}\n".format(args.path)) #this is the path storing excutable codes
    outSH.write("python DoReduceTree.py -i {0:s} -o {1:s}".format(args.jobname+".root",args.jobname+"_ZX.root"))
    #outSH.write("python reduceSSTree.py -i {0:s}".format(args.jobname))

cmd = 'chmod 777 {}'.format(jobfile)
output = processCmd(cmd)
cmd = 'hep_sub {0:s} -wt mid -o /publicfs/cms/user/guojl/sub_out/{1:s}.log -e /publicfs/cms/user/guojl/sub_out/{2:s}.err'.format(jobfile,args.jobname,args.jobname)
#cmd = 'hep_sub {0:s}  -o /publicfs/cms/user/guojl/sub_out/{1:s}.log -e /publicfs/cms/user/guojl/sub_out/{2:s}.err'.format(jobfile,args.jobname,args.jobname)
output = processCmd(cmd)
print output
