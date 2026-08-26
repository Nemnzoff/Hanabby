# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TravelPack
import argparse

def main():
    parser = argparse.ArgumentParser(description="TravelPack CLI")
    subparsers = parser.add_subparsers(dest="command")

    cmd_list = subparsers.add_parser("list", help="List all trips")
    cmd_add = subparsers.add_parser("add", help="Add a new trip")
    cmd_add.add_argument("--name", required=True)
    cmd_del = subparsers.add_parser("delete", help="Delete a trip by ID")
    cmd_del.add_argument("--id", required=True)
    cmd_show = subparsers.add_parser("show", help="Show a trip by ID")
    cmd_show.add_argument("--id", required=True)

    args = parser.parse_args()
    if args.command == "list":
        print(list_all_trips())
    elif args.command == "add":
        add_trip(args.name)
    elif args.command == "delete":
        delete_trip(args.id)
    elif args.command == "show":
        show_trip(args.id)
    else:
        parser.print_help()
