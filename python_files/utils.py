"""
##### DATA CLEANING #####

This module contains our utility functions & information

"""

import pandas as pd
import numpy as n


class DCMetroInfo():
    
    def __init__(self, df_dcmetro_final):
    
        dcmetro_median_pct_private_schools = df_dcmetro_final['PercentPrivateSchools'].median()
        dcmetro_median_house_price = df_dcmetro_final['MedianHousePrice'].median()

        dcmetro_house_price_is_low = df_dcmetro_final['MedianHousePrice'] <= dcmetro_median_house_price
        dcmetro_house_price_is_high = df_dcmetro_final['MedianHousePrice'] > dcmetro_median_house_price

        dcmetro_pct_private_schools_is_low = df_dcmetro_final['PercentPrivateSchools'] <= dcmetro_median_pct_private_schools
        dcmetro_pct_private_schools_is_high = df_dcmetro_final['PercentPrivateSchools'] > dcmetro_median_pct_private_schools

        self.dcmetro_low_price_low_pct_private_schools = df_dcmetro_final.loc[dcmetro_house_price_is_low & dcmetro_pct_private_schools_is_low]
        self.dcmetro_low_price_high_pct_private_schools = df_dcmetro_final.loc[dcmetro_house_price_is_low & dcmetro_pct_private_schools_is_high]
        self.dcmetro_high_price_low_pct_private_schools = df_dcmetro_final.loc[dcmetro_house_price_is_high & dcmetro_pct_private_schools_is_low]
        self.dcmetro_high_price_high_pct_private_schools = df_dcmetro_final.loc[dcmetro_house_price_is_high & dcmetro_pct_private_schools_is_high]


        self.dcmetro_low_price_counties = df_dcmetro_final.loc[dcmetro_house_price_is_low]
        self.dcmetro_high_price_counties = df_dcmetro_final.loc[dcmetro_house_price_is_high]
        
    
    


