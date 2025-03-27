from pyspark.sql import Row, SparkSession
from databricks.connect import DatabricksSession
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

host_name = os.getenv('DATABRICKS_HOST')
token = os.getenv('DATABRICKS_TOKEN')
cluster_id = os.getenv('DATABRICKS_CLUSTER_ID')

# Start DB Conenct session with Serverless
spark = DatabricksSession.builder.serverless(True).getOrCreate()

# tart DB Conenct session with classic compute
#spark = DatabricksSession.builder.remote(
#   f"sc://{host_name}:443/;token={token};x-databricks-cluster-id={cluster_id}"
#).getOrCreate()

from ..cleaning_utils import *

def test_lowercase_all_columns():
    # ARRANGE
    test_data = [
        {
            "ID": 1,
            "First_Name": "Bob",
            "Last_Name": "Builder",
            "Age": 24
        },
        {
            "ID": 2,
            "First_Name": "Sam",
            "Last_Name": "Smith",
            "Age": 41
        }
    ]

    test_df = spark.createDataFrame(map(lambda x: Row(**x), test_data))

    # ACT 
    output_df = lowercase_all_column_names(test_df)

    output_df_as_pd = output_df.toPandas()

    expected_output_df = pd.DataFrame({
        "id": [1, 2],
        "first_name": ["Bob", "Sam"],
        "last_name": ["Builder", "Smith"],
        "age": [24, 41]
    })
    # ASSERT
    pd.testing.assert_frame_equal(left=expected_output_df,right=output_df_as_pd, check_exact=True)
