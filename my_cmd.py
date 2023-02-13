#!/usr/bin/python3
import cmd

class MyCmd(cmd.Cmd):
    """Simple command processor example."""
    intro = "welcome to the console"
    prompt = "$"
    
    def do_greet(self, line):
        print ("hello")
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()
