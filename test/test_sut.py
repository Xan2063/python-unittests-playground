import src

import mock
import unittest


class RmTestCase(unittest.TestCase):
    @mock.patch('src.sut.pd')
    @mock.patch('src.sut.os')
    @mock.patch('src.sut.logging')
    def test_rm(self, mock_log, mock_os,mock_pandas):
        mock_pandas.DataFrame.return_value.__getitem__.return_value.mean.return_value=5
        a = src.sut.remove("any path")
        assert a== 5 
        # mock_mean=mock.Mock()
        # mock_mean = mock_pndas.__getitem__.return_value
        # self.assertEqual(a, mock_mean)
        # test that rm called os.remove wimth the right parameters
        print("lalala")
        print(a)
        print("alalal")
        # assert(mock_log.warn.called)
        mock_log.warn.assert_called_with("test")
        # mock_os.remove.assert_called_with("any path")