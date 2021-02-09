from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
file = "<s3path>/<xml_file_name.xml>"
schema_path = "<s3path>/<xml_schame_name.xml>"
'''
xml schema -

'''

df_schema = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='<xml_tag_name>').load(schema_path)
df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='<xml_tag_name>').load(path,schema=df_schema.schema)
#display(df)
df.createOrReplaceTempView("temptable")
structured_df =sqlContext.sql("select * from temptable")
display(structured_df)