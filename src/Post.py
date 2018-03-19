
import sys
import pandas as pd
import hdfs
import os


def main():
    try:
        client =hdfs.InsecureClient('http://udltest1.cs.ucl.ac.uk:50075')
        status = client.status('dat/features')
        print(status)
    except Exception as e:
        print("ERROR")
        print(e)

if __name__ == "__main__":
    main()
