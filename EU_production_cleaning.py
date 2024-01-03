import pandas as pd 

waste_production = pd.read_csv("produkce_odpadu.csv")

exclude_values = ["C10-C12", "C13-C15", "C16", "C17_C18", "C19", "C20-C22", "C23",
                  "C24_C25", "C26-C30", "C31-C33", "E36_E37_E39", "E38", "TOTAL_HH",
                  2004, 2006, 2008, "PRIM", "SEC", "TOTAL", "TOT_X_MIN", 
                  "W01-05", "W06", "W06_07A", "W077_08", "W10", "W12-13", "W126_127",
                  "W12A", "W12_X_127NH", "W13", "W09", "W091_092", "UK", "EU27_2020", 
                  "EU28"]

waste_production = waste_production[(waste_production["hazard"] != "HAZ_NHAZ") &
                                    (~waste_production["nace_r2"].isin(exclude_values)) &
                                    (~waste_production["TIME_PERIOD"].isin(exclude_values)) &
                                    (~waste_production["waste"].isin(exclude_values)) &
                                    (~waste_production["geo"].isin(exclude_values))]

waste_production.drop(
    labels=["DATAFLOW", "LAST UPDATE", "freq", "OBS_FLAG"], 
    axis=1,
    inplace=True)

waste_production.rename(columns={
    "hazard": "Typ",
    "unit": "Jednotky",
    "nace_r2": "Ekonomická aktivita",
    "waste": "Kategorie",
    "geo": "Stát",
    "TIME_PERIOD": "Rok",
    "OBS_VALUE": "Hodnota tuny (produkce)"
}, inplace=True)

hazard_dict = {
    "HAZ": "Nebezpečný",
    "NHAZ": "Ostatný"
}

economic_activity_dict = {
    "A": "Zemědělství, lesnictví a rybolov",
    "B": "Těžba nerostných surovin",
    "C": "Výroba",
    "D": "Energie",
    "E": "Vodní a odpadové hospodářství",
    "F": "Stavebnictví",
    "G-U_X_G4677": "Ostatní",
    "G4677": "Ostatní",
    "EP_HH": "Domácnosti"
}

waste_category_dict = {
    "W011": "Chemický odpad",
    "W012": "Chemický odpad",
    "W013": "Chemický odpad",
    "W02A": "Chemický odpad",
    "W032": "Chemický odpad",
    "W033": "Chemický odpad",
    "W05": "Chemický odpad",
    "W05": "Chemický odpad",
    "W061": "Recyklovatelný odpad",
    "W062": "Recyklovatelný odpad",
    "W063": "Recyklovatelný odpad",
    "W071": "Recyklovatelný odpad",
    "W072": "Recyklovatelný odpad",
    "W073": "Recyklovatelný odpad",
    "W074": "Recyklovatelný odpad",
    "W075": "Recyklovatelný odpad",
    "W076": "Recyklovatelný odpad",
    "W077": "Zařízení",
    "W08A": "Zařízení",
    "W081": "Zařízení",
    "W0841": "Zařízení",
    "W091": "Živočíšní a rostlinný odpad",
    "W092": "Živočíšní a rostlinný odpad",
    "W093": "Živočíšní a rostlinný odpad",
    "W101": "Směsný odpad",
    "W102": "Směsný odpad",
    "W103": "Směsný odpad",
    "W11": "Běžné kaly",
    "W121": "Velký minerální odpad",
    "W12B": "Velký minerální odpad",
    "W126": "Velký minerální odpad",
    "W127": "Velký minerální odpad",
    "W124": "Ostatní minerální odpad",
    "W128_13": "Ostatní minerální odpad",
}

country_dict_EU_2020 = {
    "AL": "Albánie",
    "AT": "Rakousko",
    "BA": "Bosna a Hercegovina",
    "BE": "Belgie",
    "BG": "Bulharsko",
    "CY": "Kypr",
    "CZ": "Česko",
    "DE": "Německo",
    "DK": "Dánsko",
    "EE": "Estónsko",
    "EL": "Řecko",
    "ES": "Španělsko",
    "FI": "Finsko",
    "FR": "Francie",
    "HR": "Chorvatsko",
    "HU": "Maďarsko",
    "IE": "Irsko",
    "IS": "Island",
    "IT": "Itálie",
    "LI": "Lichtenštajnsko",
    "LT": "Litva",
    "LU": "Lucembursko",
    "LV": "Lotyšsko",
    "ME": "Černá Hora",
    "MK": "Severní Makedonie",
    "MT": "Malta",
    "NL": "Nizozemsko",
    "NO": "Norsko",
    "PL": "Polsko",
    "PT": "Portugalsko",
    "RO": "Rumunsko",
    "RS": "Srbsko",
    "SE": "Švédsko",
    "SI": "Slovinsko",
    "SK": "Slovensko",
    "TR": "Turecko",
    "XK": "Kosovo"  
}

waste_production["Typ"] = waste_production["Typ"].replace(hazard_dict)
waste_production["Ekonomická aktivita"] = waste_production["Ekonomická aktivita"].replace(economic_activity_dict)
waste_production["Kategorie"] = waste_production["Kategorie"].replace(waste_category_dict)
waste_production["Stát"] = waste_production["Stát"].replace(country_dict_EU_2020)

waste_production.to_csv("cista_produkce_odpadu.csv", index=False, encoding="utf-8")

print(waste_production.head())
