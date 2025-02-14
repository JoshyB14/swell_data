import duckdb

con = duckdb.connect('swell_data.duckdb')
#con.sql("drop table swell")
con.sql("select * from swell;").show()
con.close()