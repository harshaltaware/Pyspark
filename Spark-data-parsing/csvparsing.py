import pyspark
from pyspark.sql.functions import *
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql import DataFrame
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
file = "<s3path>/<csv_file_name.csv>"
schema = StructType([StructField("column1", StringType(), True),StructField("column2", StringType(), True),
                         StructField("column2", StringType(), True),StructField("column4", StringType(), True),
                         StructField("column5", StringType(), True),StructField("column6", StringType(), True),
                         ])
df = spark.read.format('csv').option('header','false').option('multiline','True').\
                            option('delimiter',',').option('quoteAll','True').option('ignoreTrailingWhiteSpace','True').\
                            option('escape','"').schema(schema).load(file)

#display(df)
df.createOrReplaceTempView("temptable")
structured_df =spark.sql("select * from temptable")
display(structured_df)

