#!/usr/bin/python3
'''Creating cmd console'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
class_dict = {'BaseModel': BaseModel}
all_data = storage.all()


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

    def do_show(self, line):
        '''Prints the string representation of
         an instance based on the class name and id'''
        if not line:
            print('** class name missing **')
            return
        
        args = line.split()

        if args[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        
        obj = args[0] + '.' + args[1]

        for k, v in all_data.items():
            if k == obj:
                print(v)
                return    
        print('** no instance found **')

        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
