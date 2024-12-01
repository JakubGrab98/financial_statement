xml_namespaces = {
    'tns': "http://www.mf.gov.pl/schematy/SF/DefinicjeTypySprawozdaniaFinansowe/2018/07/09/JednostkaInnaWTysiacach",
    'dtsf': "http://www.mf.gov.pl/schematy/SF/DefinicjeTypySprawozdaniaFinansowe/2018/07/09/DefinicjeTypySprawozdaniaFinansowe/",
    'jin': "http://www.mf.gov.pl/schematy/SF/DefinicjeTypySprawozdaniaFinansowe/2018/07/09/JednostkaInnaStruktury"
}

BALANCE_TAG = 'tns:Bilans'
INCOME_TAG = 'tns:RZiS'
ASSETS_TAG = 'jin:Aktywa'
LIABILITIES_TAG = 'jin:Pasywa'
PNL_TAG = "jin:RZiSKalk"
AMOUNT_CY = 'dtsf:KwotaA'
AMOUNT_PY = 'dtsf:KwotaB'


balance_sheet_mapping = {
    "jin:Aktywa_A": {        
        "jin:Aktywa_A_I": "Wartości niematerialne i prawne",
        "jin:Aktywa_A_II": "Rzeczowe aktywa trwałe ",
        "jin:Aktywa_A_III": "Należności długoterminowe",
        "jin:Aktywa_A_IV": "Inwestycje długoterminowe",
        "jin:Aktywa_A_V": "Długoterminowe rozliczenia międzyokresowe",
    },
    "jin:Aktywa_B": {
        "jin:Aktywa_B_I": "Zapasy",
        "jin:Aktywa_B_II": "Należności krótkoterminowe",
        "jin:Aktywa_B_III": "Inwestycje krótkoterminowe",
        "jin:Aktywa_B_IV": "Krótkoterminowe rozliczenia międzyokresowe",
    },
    "jin:Pasywa_A": {        
        "jin:Pasywa_A_I": "Kapitał podstawowy",
        "jin:Pasywa_A_II": "Kapitał zapasowy",
        "jin:Pasywa_A_III": "Zysk netto",
    },
    "jin:Pasywa_B": {
        "jin:Pasywa_B_I": "Rezerwy na zobowiązania",
        "jin:Pasywa_B_II": "Zobowiązania długoterminowe",
        "jin:Pasywa_B_III": "Zobowiązania krótkoterminowe",
        "jin:Pasywa_B_IV": "Rozliczenia międzyokresowe",
    },
}

income_statement_mapping = {
    "jin:A": "Przychody netto ze sprzedaży",
    "jin:B": "Koszty sprzedanych produktów",
    "jin:C": "Zysk (strata) brutto ze sprzedaży",
    "jin:D": "Koszty sprzedaży",
    "jin:E": "Koszty ogólnego zarządu",
    "jin:F": "Zysk (strata) ze sprzedaży",
    "jin:G": "Pozostałe przychody operacyjne",
    "jin:H": "Pozostałe koszty operacyjne",
    "jin:I": "Zysk (strata) z działalności operacyjnej (F+G–H)",
    "jin:J": "Przychody finansowe",
    "jin:K": "Koszty finansowe",
    "jin:L": "Zysk (strata) brutto",
    "jin:M": "Podatek dochodowy",
    "jin:N": "Pozostałe obowiązkowe zmniejszenia zysku (zwiększenia straty)",
    "jin:O": "Zysk (strata) netto",
}
