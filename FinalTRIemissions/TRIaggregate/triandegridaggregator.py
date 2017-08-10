# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 12:09:09 2017

@author: tghosh
"""


import pandas as pd
import numpy as np

#Reading the tri and Egrid files for matching
tri = pd.read_csv("tri3.csv", header=0, error_bad_lines=False)
egrid = pd.read_csv("egrid.csv", header=0, error_bad_lines=False)


egrid = egrid.rename(columns={"DOE/EIA ORIS plant or facility code": "EGRID ID"})

'''
egrid = egrid.rename(columns={"Plant annual NOx total output emission rate (kg/MWh)" : "nox"})
egrid = egrid.rename(columns={"Plant annual SO2 total output emission rate (kg/MWh)" : "so2"})
egrid = egrid.rename(columns={"Plant annual CO2 total output emission rate (kg/MWh)" : "co2"})
egrid = egrid.rename(columns={"Plant annual CH4 total output emission rate (kg/MWh)" : "ch4"})
egrid = egrid.rename(columns={"Plant annual N2O total output emission rate (kg/MWh)" : "n2o"})

#print(egrid.columns.tolist())
egrid['nox'] = pd.to_numeric(egrid['nox'],errors = 'coerce')
egrid['so2'] = pd.to_numeric(egrid['so2'],errors = 'coerce')
egrid['co2'] = pd.to_numeric(egrid['co2'],errors = 'coerce')
egrid['ch4'] = pd.to_numeric(egrid['ch4'],errors = 'coerce')
egrid['n2o'] = pd.to_numeric(egrid['n2o'],errors = 'coerce')

egrid = egrid[egrid[' eGRID subregion acronym '] != ""]
egrid = egrid[egrid[' Plant primary fuel '] != ""]
#ascombnoa = ascomb[ascomb.Discipline == ""]
#Trying to Just compile EGRID  for emissions based on Regions fuel sources first
chk1 = egrid[[' eGRID subregion acronym ', ' Plant primary fuel ', 'nox', 'so2', 'co2', 'ch4', 'n2o']].groupby([' eGRID subregion acronym ',' Plant primary fuel ']).mean()
chk2 = egrid[[' eGRID subregion acronym ', ' Plant primary coal/oil/gas/ other fossil fuel category ', 'nox', 'so2', 'co2', 'ch4', 'n2o']].groupby([' eGRID subregion acronym ',' Plant primary coal/oil/gas/ other fossil fuel category ']).mean()
chk1.reset_index( drop=False, inplace=True)
chk2.reset_index( drop=False, inplace=True)

#Trying to Just compile EGRID  for emissions based on Regions fuel sources first

chk1.to_csv('Aggregated_LCI1.csv')
chk2.to_csv('Aggregated_LCI2.csv')
'''

#Worked Perfectly. It matched with the method that I developed earlier with the other python code where you had to change the
#Fuel source for every run. Just one thing that cant be done using this code is the emissions from SOlar PV and Geothermal.
#DUe to too much Prime mover information. Its best to do that with the old Python Code
#The values over here match perfectly with the results obtained earlier. Hence we can use either of these. Take Solar and GEO from old files. 

#Lessthan10% avg file is from old Python Code. 


#Starting Bridge with tri now
triegrd = pd.merge(tri,egrid,left_on = ['EGRID ID'], right_on = ['EGRID ID'])
print(triegrd.columns.tolist())


triegrd[['1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].apply(pd.to_numeric, errors='coerce')

triegrd[' Plant annual net generation (MWh) '] = pd.to_numeric(triegrd[' Plant annual net generation (MWh) '],errors = 'coerce')


#Dividing by generation
triegrd[['1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']] = triegrd[['1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].div(triegrd[' Plant annual net generation (MWh) '], axis=0)


triegrd.to_csv('temp.csv')

#Averaging based on regions and fuel sources ( SOlar and Geothermal not done)
chk1 = triegrd[[' eGRID subregion acronym ', ' Plant primary fuel ', '1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].groupby([' eGRID subregion acronym ',' Plant primary fuel ']).mean()
chk2 = triegrd[[' eGRID subregion acronym ', ' Plant primary coal/oil/gas/ other fossil fuel category ', '1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].groupby([' eGRID subregion acronym ',' Plant primary coal/oil/gas/ other fossil fuel category ']).mean()
chk1.reset_index( drop=False, inplace=True)
chk2.reset_index( drop=False, inplace=True)




chk1.to_csv('Aggregated_tri1.csv')
chk2.to_csv('Aggregated_tri2.csv')


#Exclusive averaging for SOlar and Geothermal
sLength = len(triegrd['EGRID ID'])
triegrd['Solar type'] = pd.Series(np.random.randn(sLength), index=triegrd.index)
triegrd['Geo type'] = pd.Series(np.random.randn(sLength), index=triegrd.index)
triegrd['Solar type'] = None
triegrd['Geo type'] = None
triegrd['Solar type'][(triegrd[' Plant primary coal/oil/gas/ other fossil fuel category '].str.strip().str.lower() == 'solar') & (triegrd[' Prime Mover '].str.strip().str.lower() == 'pv')] = "SOLAR PV"
triegrd['Solar type'][(triegrd[' Plant primary coal/oil/gas/ other fossil fuel category '].str.strip().str.lower() == 'solar') & (triegrd[' Prime Mover '].str.strip().str.lower() != 'pv')] = "SOLAR THERMAL"
triegrd['Geo type'][(triegrd[' Plant primary coal/oil/gas/ other fossil fuel category '].str.strip().str.lower() == 'geothermal') & (triegrd[' Prime Mover '].str.strip().str.lower() == 'bt')] = "GEOTHERMAL BT"
triegrd['Geo type'][(triegrd[' Plant primary coal/oil/gas/ other fossil fuel category '].str.strip().str.lower() == 'geothermal') & (triegrd[' Prime Mover '].str.strip().str.lower() != 'bt')] = "GEOTHERMAL FT"


chk1 = triegrd[[' eGRID subregion acronym ', 'Solar type', '1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].groupby([' eGRID subregion acronym ', 'Solar type']).mean()
chk2 = triegrd[[' eGRID subregion acronym ', 'Geo type', '1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium']].groupby([' eGRID subregion acronym ','Geo type']).mean()
chk1.reset_index( drop=False, inplace=True)
chk2.reset_index( drop=False, inplace=True)

chk1.to_csv('Aggregated_tri3.csv')
chk2.to_csv('Aggregated_tri4.csv')


#'1,2,4-trimethylbenzene', '1,4-DIOXANE', '1-Methyl-2-pyrrolidinone', '2,2-BIS(4-HYDROXY-3,5-DIBROMOPHENYL)PROPANE', '2,3-DICHLOROPROPENE', '2,4/2,6-toluenediisocyanate (mixture)', '2-PHENYLPHENOL', '4-Methyl-2-pentanone', 'ACRYLAMIDE', 'ALUMINUM OXIDE', 'AMMONIA', 'ANTIMONY COMPOUNDS', 'ARSENIC COMPOUNDS', 'Acetaldehyde', 'Acetonitrile', 'Acetophenone', 'Acrolein', 'Acrylic acid', 'Acrylonitrile', 'Aluminum', 'Aniline', 'Anthracene', 'Asbestos', 'BARIUM COMPOUNDS', 'BERYLLIUM COMPOUNDS', 'BUTYL ACRYLATE', 'Benzene, ethyl-', 'Benzene, hexachloro-', 'Benzene, pentachloro-', 'Benzo(g,h,i)perylene', 'Benzyl chloride', 'Biphenyl', 'Bisphenol A', 'Butadiene', 'Butanol', 'CADMIUM COMPOUNDS', 'CATECHOL', 'CHLORINE', 'CHROMIUM COMPOUNDS(EXCEPT CHROMITE ORE MINED IN THE TRANSVAAL REGION)', 'COBALT COMPOUNDS', 'COPPER COMPOUNDS', 'CYANIDE COMPOUNDS', 'Cadmium', 'Chloroform', 'Cobalt', 'Creosol', 'Cresol', 'Cumene hydroperoxide', 'Cyanide', 'DIAMINOTOLUENES', 'DIETHANOLAMINE', 'Dibenzofuran', 'Dimethyl sulfate', 'Dimethylamine', 'Dinitrotoluene, technical grade (2,4 (77%)- and 2,6 (19%)-)', 'Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin', 'ETHENE', 'Epichlorohydrin', 'Ethane, 1,1,1-trichloro-, HCFC-140', 'Ethane, 1,2-dichloro-', 'Ethene, tetrachloro-', 'Ethene, trichloro-', 'Ethylene glycol', 'Ethylene glycol monoethyl ether', 'Formaldehyde', 'Formic acid', 'HYDROFLUORIC ACID', 'HYDROGEN SULFIDE', 'HYDROQUINONE', 'Hexane', 'LEAD COMPOUNDS', 'MALEIC ANHYDRIDE', 'MANGANESE COMPOUNDS', 'MERCURY COMPOUNDS', 'METHYL BROMIDE', 'MOLYBDENUM(VI)', 'Methane, dichloro-, HCC-30', 'Methane, monochloro-, R-40', 'Methane, tetrachloro-, R-10', 'Methyl acrylate', 'Methyl methacrylate', 'N-(3-CHLORALLYL) HEXAMINIUM CHLORIDE', 'NICKEL COMPOUNDS', 'NICOTINE', 'NITRATE', 'NITRATE COMPOUNDS', 'NITRIC ACID', 'NITROGLYCERIN', 'Naphthalene', 'Nitrobenzene', 'PERACETIC ACID', 'PHTHALIC ANHYDRIDE', 'PYRIDINE', 'Phenanthrene', 'Phenol', 'Phenol, 2,4-dichloro', 'Phosphorus', 'Phthalate, dibutyl-', 'Phthalate, dimethyl-', 'Phthalate, dioctyl-', 'Polychlorinated biphenyls', 'Propene', 'Propene, 1,3-dichloro-', 'Propylene oxide', 'QUINOLINE', 'SEC-BUTYL ALCOHOL', 'SELENIUM COMPOUNDS', 'SELENIUM(IV)', 'SILVER COMPOUNDS', 'TERT-BUTYL ALCOHOL', 'THALLIUM COMPOUNDS', 'Thiram', 'Triethyl amine', 'VANADIUM COMPOUNDS', 'Vinyl acetate', 'Xylene', 'ZINC COMPOUNDS', 'Zinc', 'antimony', 'arsenic', 'barium', 'benzene', 'chromium', 'copper', 'cumene', 'cyclohexane', 'dicyclopentadiene', 'dimethyl formamide', 'isobutyraldehyde', 'lead', 'manganese', 'mercury', 'methanol', 'nickel', 'o-xylene', 'propargyl alcohol', 'silver', 'styrene', 'toluene', 'vanadium'
