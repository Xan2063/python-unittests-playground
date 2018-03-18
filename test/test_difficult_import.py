import pytest
import mock
import sys

influxMock = mock.Mock()
sys.modules["influxdb"] = influxMock
import src.difficult_import

@pytest.fixture
def influx():
    influxMock.reset_mock()
    return influxMock


def testconnection(influx):
    print influx.DataFrameClient.return_value
    influx.DataFrameClient.return_value.query.return_value = True
    target = src.difficult_import.DBAdapter()
    print(target)
    db = target.openDB()
    print db
    result = False
    result = target.getValueFromDB()
    influx.DataFrameClient.return_value.query.assert_called_once()
    assert result
    assert isinstance(db,mock.Mock )

def testconnection2(influx):
    print influx.DataFrameClient.return_value
    influx.DataFrameClient.return_value.query.return_value = True
    target = src.difficult_import.DBAdapter()
    print(target)
    db = target.openDB()
    print db
    result = False
    result = target.getValueFromDB()
    influx.DataFrameClient.return_value.query.assert_called_once()
    assert result
    assert isinstance(db,mock.Mock )

