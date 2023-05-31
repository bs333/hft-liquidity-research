"""
The following Python script decompresses the `.gz` files for the LOB and TAQ datasets.

Created by Siddharth Bhatia ('24 BSQF, '25 MSML, '25 MFE) on May 31st, 2023.

@author: Sid
"""

# Import `gzip` to open and write `.gz` files.
import gzip

## DECOMPRESSION SCRIPT

def decompress():
    """
    Decompresses the LOB and TAQ .gz datasets.

    Args:
        N/A
    
    Returns:
        {ticker}_{type}_{date}: CSV
            CSV files which contains financial data (date, bid price, bid size,
            ask price, ask size) for each respective ticker.
    """

    ticker_list = ['CVX', 'GME', 'JPM', 'XOM']
    type_list = ['LOB', 'TAQ']

    # Iterate for each ticker and type of data set to result in 8 CSV files.
    for ticker in ticker_list:
        for type in type_list:
            pass
