from .checkers import checkout, PATH_ARC, PATH, PATH_EXTRACT, PATH_FILES, FILE1
import pytest




def test_temp_factory(make__tmp_base_folder):
    test = make__tmp_base_folder
    assert True

# @pytest.mark.exp
# def test_7z_a():
#     '''put files to arch'''
#     assert checkout(f'cd {PATH}/{PATH_FILES} && 7z - t a {PATH}/{PATH_ARC}/{FILE1}', 'Everything is Ok')
