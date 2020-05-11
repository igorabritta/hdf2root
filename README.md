# Converting images to ROOT files

## hdf2root
Code to convert HDF5 images to root

* USAGE:
   * convert a list of h5 files:              `hdf2root.py Run720/run720*.h5 -o neutrons.root`

   * convert all the h5 files in a directory: `hdf2root.py -d Run720`  (by default will put TH2s into Run720.root)
   
   
## tif2root
Code to convert TIF images to root

* USAGE:
   * convert a TIF with more some images:              `hdf2root.py -o histograms_Run02353.root -i 2356.tif`
      
      -o is the name of the output file
      
      -i is the location of the input file
      
Obs.: For now the input file and the algorithm should be in the same directory
