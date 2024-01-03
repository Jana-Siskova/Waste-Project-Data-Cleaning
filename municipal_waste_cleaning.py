import pandas as pd 

def thousands_of_tones(row):
    if row["Jednotka"] == "THS_T":
        return row["Hodnota - komunálny odpad"] * 1000
    else: 
        return row["Hodnota - komunálny odpad"]

municipal_waste = pd.read_csv("komunalny_odpad.csv")

exclude_values = ["UK", "EU27_2020", "EU28", "CH", "TRT", "DSP_I_RCV_E", 
                  "RCY", "PRP_REU"]

municipal_waste = municipal_waste[(~municipal_waste["geo"].isin(exclude_values)) &
                                (~municipal_waste["wst_oper"].isin(exclude_values))]

municipal_waste.drop(
    labels=["DATAFLOW", "LAST UPDATE", "freq", "OBS_FLAG"], 
    axis=1,
    inplace=True)

municipal_waste.rename(columns={
    "wst_oper": "Metoda",
    "unit": "Jednotka",
    "geo": "Stát",
    "TIME_PERIOD": "Rok",
    "OBS_VALUE": "Hodnota - komunálny odpad"
}, inplace=True)

waste_operations_dict = {
    "GEN": "Produkce",
    "DSP_L_OTH" : "Likvidace: Skládkování a ostatní",
    "DSP_I": "Likvidace: Spalování",
    "RCV_E": "Rekuperace energie",
    "RCY_M": "Recyklace: Materiál",
    "RCY_C_D": "Recyklace: Kompostování"
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
    "LI": "Lichtenštejnsko",
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

municipal_waste["Metoda"] = municipal_waste["Metoda"].replace(waste_operations_dict)
municipal_waste["Stát"] = municipal_waste["Stát"].replace(country_dict_EU_2020)

municipal_waste["Hodnota - komunálny odpad"] = municipal_waste.apply(thousands_of_tones, axis=1)


municipal_waste.to_csv("cisty_komunalny_odpad.csv", index=False, encoding="utf-8")

print(municipal_waste.head())