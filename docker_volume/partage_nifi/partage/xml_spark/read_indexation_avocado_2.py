# Importation 
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format

# Ouverture d'une session
spark = SparkSession.builder.appName("AvocadoToElastic").getOrCreate()

# Lire le fichier CSV
df = spark.read.csv(f'/projet_elasticsearch_kibana/raw_avocado/avocado_2.csv', header=True, inferSchema=True)
df.show()

# Ajouter les colonnes 'jour' et 'mois'
df = df.withColumn('jour', date_format(col('Date'), 'd'))
df = df.withColumn('mois', date_format(col('Date'), 'M'))

# Écrire le résultat dans un fichier CSV avec le numéro du fichier
df.write.csv(r'/projet_elasticsearch_kibana/stagging_avocado/avocado_cleaned_2.csv', header=True)

# Chargement pour indexer
df_index = spark.read.option("header", True) \
.option("inferSchema" , "true").csv(f"/projet_elasticsearch_kibana/stagging_avocado/avocado_cleaned_2.csv")

# Indexer les données dans ElasticSearch
df_index.write.format("org.elasticsearch.spark.sql") \
.option("es.net.http.auth.user", "groupe10") \
.option("es.net.http.auth.pass", "groupe10") \
.option("es.nodes", "http://elasticsearch:9200") \
.option("es.nodes.discovery", "false") \
.option("es.nodes.wan.only", "true") \
.option("es.index.auto.create", "true") \
.mode("append") \
.save("avocado")

# Afficher un message pour indiquer que le traitement est terminé
print("Traitement terminé pour tous les fichiers !")

spark.stop()