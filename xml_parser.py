"""Module responsible for retrieving financial data from XML files"""
import xml.etree.ElementTree as ET
import const as ct


class FinancialStatementParser:
    """Class parses XML files"""
    def __init__(self, xml_file):
        """Initializes FinancialStatement Parser class."""
        self.xml_file = xml_file
        self.root = self.get_xml_root()
        self.income_statement = self.root.find(ct.INCOME_TAG, ct.xml_namespaces)

    def get_xml_root(self) -> ET.Element:
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        return root

    def get_balance_sheet(self) -> list[tuple] | None:
        """Retrieves balance sheet data from xml file"""
        try:
            balance_sheet_root = self.root.find(ct.BALANCE_TAG, ct.xml_namespaces)
            assets = balance_sheet_root.find(ct.ASSETS_TAG, ct.xml_namespaces)
            liabilities = balance_sheet_root.find(ct.LIABILITIES_TAG, ct.xml_namespaces)

            assets_data = self.loop_balance_sheet_tree(assets)
            liabilities_data = self.loop_balance_sheet_tree(liabilities)
            balance_sheet = assets_data + liabilities_data

            return balance_sheet
        except AttributeError as e:
            print("Cannot find balance sheet attribute")

    def get_income_statement(self):
        statement = self.income_statement.find(ct.PNL_TAG, ct.xml_namespaces)
        data = []
        for key, value in ct.income_statement_mapping.items():
            lines = statement.findall(key, ct.xml_namespaces)
            for line in lines:
                record = (
                    key,
                    value,
                    line.find(ct.AMOUNT_CY, ct.xml_namespaces).text,
                    line.find(ct.AMOUNT_PY, ct.xml_namespaces).text,
                )
                data.append(record)
        return data

    @staticmethod
    def loop_balance_sheet_tree(parent_root):
        data = []
        for key, sub_dict in ct.balance_sheet_mapping.items():
            sub_dict: dict
            sublines = parent_root.find(key, ct.xml_namespaces)
            for sub_key, sub_value in sub_dict.items():
                for line in sublines.findall(sub_key, ct.xml_namespaces):
                    record = (
                        sub_key,
                        sub_value,
                        line.find(ct.AMOUNT_CY, ct.xml_namespaces).text,
                        line.find(ct.AMOUNT_PY, ct.xml_namespaces).text,
                    )
                    data.append(record)
        return data
