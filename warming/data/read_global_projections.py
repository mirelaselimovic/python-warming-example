import pandas as pb

class sum_global_projections:
    def __init__(self):
        self._filepath = "./data/41558_2023_1605_MOESM2_ESM.xlsx"
        self._data = self.prepare_data()

    def prepare_data(self):
        data = pb.read_excel(self._filepath, sheet_name="Global Projections")
        data = data.set_index("Population Projection")
        return data[2:]

    def co2(self):
        """Returns the data of `CO2` values per capity per country.

        :return: The `CO2` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2"]

    def ch4(self):
        """Returns the data of `CH4C` values per capity per country.

        :return: The `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['CH4']

    def n2o(self):
        """Returns the data of `N2OC` values per capity per country.

        :return: The `N2OC` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['N2O']

    def xscale(self):
        return self._data["Year"]
