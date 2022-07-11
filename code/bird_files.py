import os
import pandas as pd

class Bird:
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_parquet(filename)

    @property
    def name(self):
        return os.path.splitext(os.path.basename(self.filename))[0]

    def save(self, path, prefix='', format='parquet'):
        if format == 'parquet':
            self.df.to_parquet(os.path.join(path, f"{prefix}{self.name}.parquet"), index=False)
        elif format == 'csv':
            self.df.to_csv(os.path.join(path, f"{prefix}{self.name}.csv"), index=False)
        else:
            raise ValueError(f'Wrong format={format}')