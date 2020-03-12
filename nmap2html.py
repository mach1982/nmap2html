import os 
import sys

nmap_options=' '.join(sys.argv[1:-2])+" " +" -oX "
#nmap_options="-A -T4 -p- "+" -oX "
ip_address = sys.argv[-2]
fn = sys.argv[-1]

if sys.argv[1] == '-h':
    print("Usage python3 nmap2html.py <ip_address> <flie_name>")

else:
    #os.system('nmap -A -T4 -p- -oX '+ os.getcwd()+'/'+fn+'.xml '+ip_address)
    os.system('nmap '+nmap_options + os.getcwd()+'/'+fn+'.xml '+ip_address)
    os.system('xsltproc '+fn+'.xml -o '+fn+'.html')
    os.remove(os.getcwd()+'/'+fn+'.xml')



#-A -T4 -p- -o
