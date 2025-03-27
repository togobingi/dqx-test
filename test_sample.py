from pyspark import SparkConf as spark


def logic_1(df):
    # your logic 1 code here
    return df 

def logic_2(df):
    # your logic 2 code here
    return df 

def logic_3(df):
    # your logic 3 code here
    return df 

def application_code():
    df = spark.read.format("csv").path("input_file.csv")
    df = logic_1(df)
    df = logic_2(df)
    df = logic_3(df)
    df.write.csv("transformed_table.csv")


