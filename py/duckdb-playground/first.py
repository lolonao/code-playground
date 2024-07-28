# Get the top-3 busiest train stations
import duckdb

# duckdb.sql("""
#     SELECT station, count(*) AS num_services
#     FROM train_services
#     GROUP BY ALL
#     ORDER BY num_services DESC
#     LIMIT 3;
#     """)
#

# duckdb.sql("SELECT 42").show()

r1 = duckdb.sql("SELECT 42 AS i")
duckdb.sql("SELECT i * 2 AS k FROM r1").show()

