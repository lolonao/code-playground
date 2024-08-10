import os
import csv
import sqlitet3
import pandas as pd
import plotly.express as px

# Procedure that renames a table column
def my_procedure(table_name, old_column_name, new_column_name):
    cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name}")
    return pd.read_sql(f"SELECT * FROM {table_name}", conn)


def my_function(table_name, crimes):
    df = pd.read_sql(f"SELECT * FROM {table_name} WHERE Crimes >= {crimes}", conn)
    return df

def main():
    # csvファイルをpandasデータフレームに読み込む
    # df = pd.read_csv( '.\data.csv' )

    # SQLite データベースを作成
    conn = sqlite3.connect( 'database.db' )
    cursor = conn.cursor()

    # テーブル定義
    create_table = '''CREATE TABLE IF NOT EXISTS crimesSonora(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Year datetime NOT NULL,
                    amount_executed INTEGER NOT NULL,
                    Municipality VARCHAR(40) NOT NULL,
                    number_crimes INTEGER NOT NULL);
                    '''

    # データベースにテーブルを作成する
    cursor.execute(create_table)

    # DataFrame のデータを SQLite テーブルに挿入します
    df.to_sql( 'crimesSonora' , conn, if_exists= 'replace' , index = False )

    # pandas データフレームを印刷します
    pd.read_sql( '''SELECT * FROM crimesSonora''' , conn)

    # Renaming two columns
    my_procedure('crimesSonora', 'amount_executed', 'Budget_executed')
    my_procedure('crimesSonora', 'number_crimes', 'Crimes')
    df_function_test = my_function('crimesSonora', 1500)
    df_function_test.head(10)

    # Creating view of table
    cursor.execute("CREATE VIEW IF NOT EXISTS crimesHermosilloView AS SELECT Year, Budget_executed, Municipality, Crimes FROM crimesSonora WHERE Municipality = 'Hermosillo'")

    # Printing with pandas the content of the view created
    pd.read_sql('''SELECT * FROM crimesHermosilloView''', conn)

    # Get the column names
    cursor.execute("PRAGMA table_info(crimesSonora)")

    # Fetch all column names and store them in a list
    columns = cursor.fetchall()

    # Print each column name
    for column in columns:
        print(column[1])

    # Dropping column
    cursor.execute("ALTER TABLE crimesSonora DROP COLUMN 'Unnamed: 0'")

    # Printing resulting table
    pd.read_sql('''SELECT * FROM crimesSonora''', conn)

    # Creating pandas dataframe with the content from crimesSonora table
    df = pd.read_sql('''SELECT * FROM crimesSonora''', conn)

    # Creting dataframe of San Javier Municipality
    df_SanJavier = pd.read_sql('''SELECT * FROM crimesSonora WHERE Municipality="San Javier"''', conn)

    # Creating dataframe where crimes > 1000
    df_crimes_more_1000 = pd.read_sql('''SELECT * FROM crimesSonora WHERE Crimes>1000''', conn)
    df_crimes_more_1000.head(10)

    fig = px.line(df, x='Year', y='Budget_executed', title='Amount of money executed to public education in Sonora over the years', width=1000, height=400)
    fig.show()

    # drop the table
    conn.execute('DROP TABLE crimesSonora')
    # commit the changes and close the connection
    conn.commit()
    # close the connection
    conn.close()
    # delete the file "database.db"
    os.remove('.\database.db')

if __name__ == '__main__':
    main()
