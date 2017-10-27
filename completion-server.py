import os
import sys
import threading
from epc.server import EPCServer
from collections import namedtuple

if os.environ.get("TERM", '') != "dumb":
    print "WARNING : terminal is not dumb (not running on emacs)."
    
class EPCCompletionServer(EPCServer):
    def __init__(self, address='localhost', port=0, *args, **kargs):
        EPCServer.__init__(self, (address, port), *args, **kargs)
        
        def complete(*cargs, **ckargs):
            return self.complete(*cargs, **ckargs)
        self.register_function(complete)
        
    def print_port(self, stream=None):
        if stream is None:
            stream=sys.stdout
        stream.write("___EPCCompletionServer_PORT=")
        EPCServer.print_port(self, stream)
            
class MyCompletionServer(EPCCompletionServer):
    def complete(self, *to_complete):
        to_complete = ''.join(to_complete)
        # print'trying to complete ' + to_complete
        completions = ('firstcompletion', 'second')
        # print "Return completions for ", to_complete, ":", completions
        return tuple(completions)


rpc_complete_server = MyCompletionServer()
rpc_complete_server.print_port()  # needed for Emacs client
rpc_complete_thread = threading.Thread(
    target=rpc_complete_server.serve_forever,
    name="MyCompletionServer")
rpc_complete_thread.setDaemon(True)
rpc_complete_thread.start()

inp = None
while inp!='q':
    inp=raw_input('what do you want? ')
