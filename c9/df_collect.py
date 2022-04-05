from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType
from pyspark.sql.functions import collect_list,collect_set
if __name__ == '__main__':
    spark = SparkSession.builder.appName("MyApp").master("local[*]").getOrCreate()
    data = [("Saif", "Sales", 3000),
            ("Ram", "Sales", 4600),
            ("Aniket", "Sales", 4100),
            ("Mitali", "Finance", 3000),
            ("Saif", "Sales", 3000),
            ("Sandeep", "Finance", 3300),
            ("John", "Finance", 3900),
            ("Jeff", "Marketing", 3000),
            ("Sagar", "Marketing", 2000),
            ("Swaroop", "Sales", 4100)]
    myschema = StructType([
        StructField('Name',StringType(),True),
        StructField('Dept', StringType(), True),
        StructField('Salary', StringType(), True)
    ])
    df = spark.createDataFrame(data,myschema)
    df.show()
    #Gives column values as a list with duplicates
    df1 = df.select(collect_list(df.Salary))
    df1.show(truncate=False)
    # Gives column value as list without duplicates
    df2 = df.select(collect_set(df.Salary))
    df2.show(truncate=False)


