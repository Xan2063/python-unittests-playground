
import mock
import pytest

import src
    
@mock.patch('src.sut.os')
def test_filesystem(mock_os):
    src.sut.dofilesystem('any path')
    mock_os.remove.assert_called_with('any path')


@mock.patch('src.sut.logging')
@mock.patch('src.sut.pd')
def test_rm(mock_pandas, mock_log):
    mock_pandas.DataFrame.return_value.__getitem__.return_value.mean.return_value=5
    a = src.sut.dopandas()
    mock_log.warn.assert_called_with('test')
    assert a== 5 

