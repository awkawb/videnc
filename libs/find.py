#!/usr/bin/end python3

import os
import re

def find(root, name='.*', type_='*'):
    find_regex = re.compile(name)
    found_paths = []

    if os.path.isdir(root):
        if type_ == 'f':
            add_files = True
            add_dirs = False
    
        elif type_ == 'd':
            add_files = False
            add_dirs = True
    
        elif type_ == '*':
            add_files = True
            add_dirs = True
    
        else:
            raise ValueError('Called with invalid type_ file type.')

        for path, dirs_list, files_list in os.walk(root):
            if add_dirs and find_regex.match(path):
                    found_paths.append(path)
                
            if add_files:
                for cur_file in files_list:
                    cur_file_path = os.path.join(path, cur_file)
    
                    if find_regex.match(cur_file_path):
                        found_paths.append(cur_file_path)
    
        return found_paths

    else:
        raise NotADirectoryError('Called with invalid root directory.')

