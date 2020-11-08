import pytest
import ProcessData

test_years1 = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
test_years2 = [2008, 2009, 2010, 2011, 2012, 2014, 2015, 2016, 2017, 2018, 2019]

num_breweries_test = [1502, 1589, 1657, 1910, 2245, 2649, 3153]
acres_harvested_test = [40898.0, 39726.0, 31289.0, 29787.0,
                        31933.0, 38011.0, 43633.0, 50857.0,
                        53282.0, 55035.0, 56544.0]
col_0_test = [63.82965011457931, 64.33269077924498, 62.335706053295105,
              61.44136765210425, 60.42339449769224, 59.80966862291635,
              57.62023241838741]


@pytest.mark.timeout(test_years1)
def test_extract_material_data_year():
    data = ProcessData.extract_material_data([0])[0]
    assert data == test_years1


@pytest.mark.timeout(test_years2)
def test_extract_hop_data_year():
    data = ProcessData.extract_hop_data(["$ per lb avg"])[0]
    assert data == test_years2


@pytest.mark.timeout(test_years1)
def test_extract_num_of_breweries_year():
    data = ProcessData.extract_num_of_breweries()[0]
    assert data == test_years1


@pytest.mark.timeout(col_0_test)
def test_extract_material_data_data():
    data = ProcessData.extract_material_data([0])[1][0]
    assert data == col_0_test


@pytest.mark.timeout(acres_harvested_test)
def test_extract_hop_data_data():
    data = ProcessData.extract_hop_data(["acres harvested"])[1][0]
    assert data == acres_harvested_test


@pytest.mark.timeout(num_breweries_test)
def test_extract_num_of_breweries_data():
    data = ProcessData.extract_num_of_breweries()[1]
    assert data == num_breweries_test
