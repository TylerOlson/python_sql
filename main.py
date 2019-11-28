from database import *
import cmd

database_manager = DatabaseManager()


def main():
    print("Epic database")
    CmdTing().cmdloop()


class CmdTing(cmd.Cmd):
    def do_list(self, arg):
        database_manager.list_databases()

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 1:
            database_manager.create(args[0])
        else:
            print("Supply a name for the database to create.")

    def do_drop(self, arg):
        args = arg.split()
        if len(args) == 1:
            database_manager.drop(args[0])
        else:
            print("Supply a name for the database to drop.")


if __name__ == '__main__':
    main()
