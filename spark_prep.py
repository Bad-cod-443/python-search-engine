from pyspark.sql import SparkSession

# 1. Создаем Spark Session (это твоя точка входа в мир Big Data)
# master("local[*]") означает "использовать все доступные ядра процессора на моем компе"
spark = SparkSession.builder \
    .appName("RecSys_Data_Prep") \
    .master("local[*]") \
    .getOrCreate()

print("🚀 Spark успешно запущен!")

# 2. Читаем наш старый movies.csv
# header=True говорит, что первая строка — это названия колонок
# inferSchema=True заставляет Spark самому угадать типы данных (числа, строки)
movies_df = spark.read.csv("movies.csv", header=True, inferSchema=True)

# 3. Смотрим, что получилось
print("\n--- Схема данных (типы колонок) ---")
movies_df.printSchema()

print("\n--- Первые строки датасета ---")
movies_df.show(truncate=False)

# 4. Выключаем движок
spark.stop()