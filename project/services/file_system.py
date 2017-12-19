from unipath import Path
import glob
import os

class FileSystem(object):

    def __init__(self, work_dir):
        self.base_dir   = work_dir
        self.media_dir  = self.base_dir.child('static','media')
        self.identified_path = '{}/identified'.format(self.media_dir)
        self.upload_path = '{}/upload'.format(self.media_dir)

        self.noimage_url = 'https://dummyimage.com/300.png/09f/fff'

    def save_file(self, temp_file):
        temp_file.save(self.media_dir.child('upload',temp_file.filename))

    def upload_path_of(self, temp_file):
        return "{}/{}".format(self.upload_path,temp_file.filename)
    
    def identified_path_of(self, temp_file):
        return '{}/{}'.format(self.identified_path,temp_file.filename)

    def last_identified_paths(self):
        files_path = os.path.join(self.identified_path+'/', '*')
        files = sorted(
            glob.iglob(files_path), key=os.path.getctime, reverse=True) 
        files_count = len(files)
        last_files = []
        for index in range(5):
            if index <= (files_count-1):
                file_name = files[index].split('/').pop()
                last_files.append('static/media/identified/{}'.format(file_name))
            else:
                last_files.append(self.noimage_url)
            
        return last_files


