#!/usr/bin/python
import psycopg2
import sys
import pandas as pd
import hdfs

import os


def main():
    try:
        client = hdfs.client.Client("hdfs://udltest3.cs.ucl.ac.uk:8020")
        print(client)
        print(client.content('/'))
    except Exception as e:
        print("ERROR")
        print(e)

if __name__ == "__main__":
    main()
