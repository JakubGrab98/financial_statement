import xml.etree.ElementTree as ET
import pandas as pd
import const as ct
from xml_parser import FinancialStatementParser


if __name__ == "__main__":
    parser = FinancialStatementParser("data/raw/Test_XML.xml")
    data = parser.get_income_statement()
    df  = pd.DataFrame(data, columns=["id", "line_name", "value_a", "value_b"])
    print(df)
    