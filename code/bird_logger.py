from contextlib import ContextDecorator
import os
import pandas as pd

class Logger:
    def __init__(self, folder, prefix=""):
        self.folder = folder
        self.prefix = prefix
        self.counters = pd.DataFrame(columns=["bird_file", "counter", "data"])
        self.operations = pd.DataFrame(columns=["bird_file", "operation", "shape_before", "shape_after"])

    def counter_info(self, bird_file:str, counter, data):
        rec = {
            "bird_file": bird_file,
            "counter": counter,
            "data": data
        }
        self.counters = self.counters.append(rec, ignore_index=True)

    def operation_info(self, bird_file:str, operation, shape_before, shape_after):
        rec = {
            "bird_file": bird_file,
            "operation": operation,
            "shape_before": shape_before,
            "shape_after": shape_after
        }
        self.operations = self.operations.append(rec, ignore_index=True)

    def info(self, message, bird_file:str=None):
        if bird_file:
            print(f"  {bird_file}: {message}")
        else:
            print(message)

    def flush(self):
        if self.counters.size:
            self.counters.to_csv(os.path.join(self.folder, self.prefix + "counters.csv"), index=False)
        if self.operations.size:
            self.operations.to_csv(os.path.join(self.folder, self.prefix + "operations.csv"), index=False)

class LogOperation(ContextDecorator):
    def __init__(self, log, bird, operation):
        self.log = log
        self.bird = bird        
        self.operation = operation

    def __enter__(self):
        self.shape_before = self.bird.df.shape

    def __exit__(self, type, value, traceback):
        self.shape_after = self.bird.df.shape
        self.log.operation_info(self.bird.name, self.operation, self.shape_before, self.shape_after)
