"""Provides easy access to paths and credentials used in the project.
Meant to be used as an imported module.

Example
-------

import config
path = config.output_dir
path

## The config YAML should look something like this:
# config.yml

default:
    data_dir: "C:/My Documents/data/misc_project"
    private_data_dir: "D:/My Documents/private_data/misc_project"
    output_dir: "C:/Users/jdoe/GitRepositories/misc_project/output"
    wrds_username: "jdoe"

AWS:
    data_dir: "/data/awshomes/jdoe/data/misc_project"
    private_data_dir: "/data/awshomes/jdoe/private_data/misc_project"
    output_dir: "/data/awshomes/jdoe/GitRepositories/INT_misc_project/output"

"""
import yaml
from pathlib import Path

with open("../config.yml") as f:
    config = yaml.safe_load(f)

def _read_config_entry(upper_key, lower_key):
    entry = config[upper_key][lower_key]
    if entry is None:
        p = None
    else:
        p = Path(entry)
    return p

def switch_to(pathset_name='default'):
    global data_dir
    global private_data_dir
    global output_dir
    global pathset

    data_dir = _read_config_entry(pathset_name, "data_dir")
    private_data_dir = _read_config_entry(pathset_name, "private_data_dir")
    output_dir = _read_config_entry(pathset_name, "output_dir")
    pathset = pathset_name

def read(key):
    upper_key = pathset
    value = config[upper_key][key]
    return value

switch_to(pathset_name='default')

if __name__ == "__main__":
    pass
    

