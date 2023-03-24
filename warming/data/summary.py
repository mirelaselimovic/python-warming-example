import pandas as pb

class Summary:

    def __init__(self):
        self._filepath = "./data/41558_2023_1605_MOESM2_ESM.xlsx"
        self._data = self.prepare_data()

    def prepare_data(self):
        data = pb.read_excel(self._filepath, sheet_name="Country Summaries")
        data = data.set_index("Country Name")
        return data[2:]

    def countries(self):
        """Returns an index of the countries available in the dataset.

        :return: Returns an index of countries of the dataset.
        :rtype: pandas.core.indexes.base.Index
        """
        return self._data.keys()

    def co2(self):
        """Returns the data of `CO2` values per capity per country.

        :return: The `CO2` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2C"]

    def ch4(self):
        """Returns the data of `CH4C` values per capity per country.

        :return: The `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['CH4C']

    def n2o(self):
        """Returns the data of `N2OC` values per capity per country.

        :return: The `N2OC` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['N2OC']

    def co2_year(self):
        """Returns the data of `CO2` values per capity per country.

        :return: The `CO2` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2Y"]

    def ch4_year(self):
        """Returns the data of `CH4C` values per capity per country.

        :return: The `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['CH4Y']

    def n2o_year(self):
        """Returns the data of `N2OC` values per capity per country.

        :return: The `N2OC` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data['N2OY']