# completion-epc
Using epc+python epc to send completions over back to emacs.

# Usage:

Put this code in your application:
[code]
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
[/code]

To make your own completions:
[code]
class MyCompletionServer(EPCCompletionServer):
    def complete(self, *to_complete):
        to_complete = ''.join(to_complete)
        # print('trying to complete ' + to_complete)
        return ('firstcompletion', 'second')
[/code]

You can send back whatever completions you have. emacs takes care on which completions to show you.

# Examples:
See frida-python:
https://github.com/frida/frida-python
on path:
frida-python/src/frida/repl.py

# Installation:
Just put in init.el:
[code]
(require 'completion-epc)
[/code]

# Requirements:
https://github.com/kiwanami/emacs-epc
https://github.com/tkf/python-epc
