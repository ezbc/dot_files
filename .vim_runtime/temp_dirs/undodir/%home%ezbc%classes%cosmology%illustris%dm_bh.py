Vim�UnDo� 1���k�\�e���Cf�_�ؼ�jl���      import readsnapHDF5 as rs!            	       	   	   	    TA�D    _�                             ����                                                                                                                                                                                                                                                                                                                                                             TAf     �                   5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             TA�     �                 
basedir = �               �                 import matplotlib.pyplot5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             TA�     �               *basedir = /d/sierra3/astro735/Illustris-3/5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             TA�     �               +basedir = /d/sierra3/astro735/Illustris-3/'5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             TA�    �   	               �   
            �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                   #       	                      v        TA�@     �                �             5�_�      	                     ����                                                                                                                                                                                                                                                                                                                   #       	                      v        TA�A     �               import readsnapHDF5 as rs!5�_�                  	          ����                                                                                                                                                                                                                                                                                                                   #       
                      v        TA�C    �               import readsnapHDF5 as rs!5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             TA�     �                 �                  �              �                rimport numpy as np!import matplotlib.pyplot as plt!import readsnapHDF5 as rs!!# Header!basedir = "/usr/users/ciro/training/astroph/snaps/Illustris/Illustris-3"!snapnum = 135!fname = basedir + "/snapdir_" + str(snapnum).zfill(3) + "/snap_" + \ !! !  str(snapnum).zfill(3)!!header = rs.snapshot_header(fname) !print 'Box size = %f kpc' % (header.boxsize / header.hubble)!!5��