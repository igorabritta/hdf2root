# hdf2root
Some code to convert HDF5 images to root

* USAGE:
   * convert a list of h5 files:              `hdf2root.py Run720/run720*.h5 -o neutrons.root`

   * convert all the h5 files in a directory: `hdf2root.py -d Run720`  (by default will put TH2s into Run720.root)