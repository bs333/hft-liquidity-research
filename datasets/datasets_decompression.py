"""
The following Python script decompresses the `.gz` files for the LOB and TAQ datasets.

Created by Siddharth Bhatia ('24 BSQF, '25 MSML, '25 MFE) on May 31st, 2023.

@author: Sid Bhatia
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

    # Initialize lists for each ticker and type for these CSVs.
    ticker_list = ['CVX', 'GME', 'JPM', 'XOM']
    type_list = ['LOB', 'TAQ']

    # Initialize the date for March 14th, 2022
    date = '20220314'

    # Iterate for each ticker and type of data set to result in 8 CSV files.
    for ticker in ticker_list:
        for type in type_list:
            # Use f-string to easily format the file name.
            file_name = f'{ticker}_{type}_{date}.csv.gz'
            # Use `with...as` to simplify filestream and open `.gz` files.
            with gzip.open(filename = file_name, mode = 'rt') as gz_file:
                # Read compressed data.
                data = gz_file.read()
                # Write decompressed data as CSV and index to retrieve precise file name.
                with open(file = file_name[:-3], mode = 'wt') as out_file:
                    out_file.write(data)

if __name__ == '__main__':
    decompress()

