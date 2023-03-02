#!/usr/bin/python3
'''Creating cmd console'''
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''cmd console class'''
    prompt = '(hbnb) '
    def do_quit(self, *args):
        '''write quit to exit'''
        return True

    def do_EOF(self, line):
        '''write EOF to exit'''
        return True
    
    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything"""
        if self.lastcmd:
            pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''
        line = BaseModel()
        if not line:
            print('** class name missing **')
            return
        line.save()
        print(line.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
