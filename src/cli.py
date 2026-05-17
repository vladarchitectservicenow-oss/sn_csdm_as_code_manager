#!/usr/bin/env python3
import argparse, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.engine import Engine

def main():
    p = argparse.ArgumentParser(description="$name")
    p.add_argument("--sn-url", required=True)
    p.add_argument("--sn-user", required=True)
    p.add_argument("--sn-pass", required=True)
    p.add_argument("--table", default="incident")
    p.add_argument("--output", default="report")
    args = p.parse_args()
    Engine(args.sn_url, args.sn_user, args.sn_pass).run(args.table, args.output)
    print("Report generated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
