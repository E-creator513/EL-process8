FROM apache/airflow:2.8.1

USER root

# Копируем entrypoint и ставим права
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Меняем пользователя на airflow
USER airflow

# Устанавливаем pip пакеты
RUN pip install --no-cache-dir pymongo psycopg2-binary

ENTRYPOINT ["/entrypoint.sh"]
CMD ["standalone"]
