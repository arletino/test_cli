import pytest
import yaml


@pytest.fixture(scope='class')
def atype(request, load_config_yml):
    '''Put type archive to classTest'''
    if load_config_yml['archive_type'] is not None:
        request.cls.atype = f'-t{load_config_yml['archive_type']}'
    else:
        request.cls.atype = ''
        
@pytest.fixture(scope='class')
def load_config_yml():
    '''Load config from yaml file'''
    with open('config.yml') as f:
        '''Read YAML config'''
        test_data = yaml.safe_load(f)
    return test_data


