import pandas as pd
import numpy as np
from constants import AREA_DROP

class DataProcessor:
    def __init__(self):
        pass

    def load_dataset(self, path):
        self.path = path
        self.data = pd.read_csv(self.path)

    def process_data(self):
        emm_all = pd.DataFrame(self.data.loc[self.data['Element'] == 'Emissions (CH4)'])
        emm_all['Value'].fillna((emm_all['Value'].mean()), inplace=True)
        emm_df = emm_all.drop(columns='Note')

        emm_df["Area"].replace({"China, mainland": "China"}, inplace=True)

        all_area = list(emm_df['Area'].unique())

        dropped_cat = set(all_area).difference(AREA_DROP)
        dropped_cat2 = set(all_area).difference(dropped_cat)

        data_d = emm_df.set_index("Area")
        area_drop_df = data_d.drop(dropped_cat2, axis=0).reset_index()

        lastten = pd.DataFrame(
            self.data.loc[(self.data['Year'] > 2009) & (self.data['Year'] < 2030)])

        last_ten_years = lastten.copy()
        mean_ten_years = last_ten_years.groupby(['Area'])['Value'].mean()
        mean_ten_df = mean_ten_years.to_frame().reset_index()

        self.result = pd.DataFrame(mean_ten_df.nlargest(10, 'Value'))

    def get_processed_data(self):
        return self.result

