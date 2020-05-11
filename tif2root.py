#!/usr/bin/env python
# Tool to convert TIF array of images in to a ROOT TH2D
# USAGE:
# convert a list of h5 files:              hdf2root.py Run720/run720*.h5 -o neutrons.root
# convert all the h5 files in a directory: hdf2root.py -d Run720  (will put TH2s into Run720.root)
# -*- coding: utf-8 -*-
import re,sys,os,glob
import numpy as np
import ROOT
from libtiff import TIFF

def read_h5_write_root(fileH5, fileROOT, ev, run, option='recreate'):
    
    image = fileH5
    tf = ROOT.TFile.Open(fileROOT,option)
    (nx,ny) = image.shape
    title = "pic_run%5d_%d" % run,ev
    h2 = ROOT.TH2D(title,title,nx,0,nx,ny,0,ny)
    h2.GetXaxis().SetTitle('x')
    h2.GetYaxis().SetTitle('y')
    [h2.SetBinContent(bx,by,image[bx,by]) for bx in xrange(nx) for by in xrange(ny)]
    h2.Write()
    tf.Close()
    return

def tif2root_array(args,tiffiles,rfname,run):
    tif = TIFF.open(tiffiles)
    i=-1
    for image in tif.iter_images():
        i=i+1
        option = 'recreate' if i==0 else 'update'
        print "Saving image %d into file %s" % (i,rfname)
        read_tif_write_root(image, rfname, i, run, option)
            
if __name__ == '__main__':

    from optparse import OptionParser
    parser = OptionParser(usage='%prog tifFile [opts] ')
    parser.add_option('-o', '--outputfile', dest='outputFile', default='image.root', type='string', help='name of the output ROOT file')
    parser.add_option('-i', '--inputfile', dest='inputFile', default=None, type='string', help='name of the input TIF file')
    (options, args) = parser.parse_args()
    

    if len(args)>0:
        print "you should specify just input file and output file"
        exit(0)
    else:
        if options.outputFile==None:
            print "You need to specify a name for the output root file. Exiting."
            exit(0)
        elif options.inputFile==None:
            print "You need to specify the file name where the files are. Exiting."
            exit(0)
        else:
            run = options.inputFile.split('.')[0].split('-')[0]
            outputFile = options.outputFile
            inputFile = options.inputFile
            print "Converting TIF files into ", outputFile
            tif2root_array(args,inputFile,outputFile,run)