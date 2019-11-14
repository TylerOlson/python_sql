from database import *

database_manager = DatabaseManager()

def main():
    print("Epic database")

    listener()


def listener():
    args = input().split()
    args_length = len(args)

    if args[0] == "exit":
        return

    if args[0] == "CREATE":
        if (args_length > 1):
            if args[1] == "DATABASE":
                if (args_length == 3):
                    database_manager.create(args[2])

    if args[0] == "list_databases":
        database_manager.list_databases()

    listener()



if __name__ == '__main__':
    main()