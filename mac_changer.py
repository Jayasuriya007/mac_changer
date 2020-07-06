import subprocess
import optparse

def get_options():
    parser=optparse.OptionParser()
    parser.add_option("-i",dest="interface",help="used to select interface")
    parser.add_option("-m",dest="new_mac",help="used to change mac_address")
    (options,arguments)=parser.parse_args()

    if not options.interface :
        print(".........please enter select your interface.........")           #CODE BY SURIYA
    elif not options.new_mac:
        print("...............Please select your mac_id..............")
    else:
        return options

def mac_changer(interface,new_mac):
    print(".........Your Mac_address Is Changed To...........",new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])


(options)=get_options()
mac_changer(options.interface,options.new_mac)
