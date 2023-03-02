#!/usr/bin/python3
'''Creating cmd console'''
import cmd
from models.base_model import BaseModel
class_dict = {'BaseModel': BaseModel}

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
        if not line:
            print('** class name missing **')
            return
        if line not in class_dict.keys():
            print("** class doesn't exist **")
            return
        inst_to_create = class_dict.get(line, None)()
        inst_to_create.save()
        print(inst_to_create.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
