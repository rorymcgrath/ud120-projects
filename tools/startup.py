#!/usr/bin/python
import sys

print()
print("checking for nltk")
try:
    import nltk
except ImportError:
    print("you should install nltk before continuing")

print("checking for numpy")
try:
    import numpy
except ImportError:
    print("you should install numpy before continuing")

print("checking for scipy")
try:
    import scipy
except:
    print("you should install scipy before continuing")

print("checking for sklearn")
try:
    import sklearn
except:
    print("you should install sklearn before continuing")

print()
print("downloading the Enron dataset (this may take a while)")
print("to check on progress, you can cd up one level, then execute <ls -lthr>")
print("Enron dataset should be last item on the list, along with its current size")
print("download will complete at about 423 MB")
from tqdm import tqdm

url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"

if sys.version_info.major < 3:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve


class TqdmUrlHook(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""
    def update_to(self, count=1, block_size=1, total_size=None):
        """
        count  : int, optional
            Number of blocks transferred so far [default: 1].
        block_size  : int, optional
            Size of each block (in tqdm units) [default: 1].
        total_size  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if total_size is not None:
            self.total = total_size
        self.update(count * block_size - self.n)

with TqdmUrlHook(unit='B', unit_scale=True, miniters=1) as t:
    urlretrieve(url,filename="../enron_mail_20150507.tar.gz",reporthook=t.update_to)

print("download complete!")

print()
print("unzipping Enron dataset (this may take a while)")
import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print("you're ready to go!")
