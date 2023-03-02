#!/usr/bin/python3
'''Creating cmd console'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''cmd console class'''
    prompt = '(hbnb)'
    def do_quit(self, *args):
        '''write quit to exit'''
        return True

    def do_EOF(self, line):
        '''write EOF to exit'''
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()