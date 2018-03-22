import hdfs


def main():
    try:
        client = hdfs.InsecureClient("hdfs://udltest3.cs.ucl.ac.uk:8020")
        content = client.list('/user/tflETL')
        print(content)
    except Exception as e:
        print("ERROR")
        print(e)


if __name__ == "__main__":
    main()
