import pandas as pd
from xml_parser import FinancialStatementParser

def add_multiple_columns(df: pd.DataFrame, column_names: list, values: list):
    for index in range(0, len(column_names)):
        df[column_names[index]] = values[index]
    return df


if __name__ == "__main__":
    columns_names = ["id", "line_name", "value_a", "value_b"]
    parser = FinancialStatementParser("data/raw/Test_XML.xml")
    income_data = parser.get_income_statement()
    balance_sheet_data = parser.get_balance_sheet()
    df_income  = pd.DataFrame(income_data, columns=columns_names)
    df_balance = pd.DataFrame(balance_sheet_data, columns=columns_names)
    general_data = parser.get_general_info()

    appended_df = pd.concat([df_balance, df_income]).reset_index()
    general_columns = ["nip", "krs", "date_from", "date_to"]
    final_df = add_multiple_columns(appended_df, general_columns, general_data)
    final_df.to_csv("test.csv")
