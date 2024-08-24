from db_config import DBFunctions
import pandas as pd
import matplotlib.pyplot as plt

class Report:

    def weekly_report():
        sql = 'SELECT * FROM meals WHERE date >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
        with DBFunctions.get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['id', 'filename', 'ingredients', 'nutrition', 'date'])

                # Generate visualization
                plt.figure(figsize=(10, 6))
                df['nutrition'].apply(lambda x: pd.Series(eval(x))).sum().plot(kind='bar')
                plt.title('Weekly Nutrition Report')
                plt.savefig('static/reports/weekly_report.png')