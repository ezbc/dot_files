Vim�UnDo� hm]S�q�}��Xo�/�x�oT�j>���S+I�  �                                   S�3�    _�                              ����                                                                                                                                                                                                                                                                                                                                                             S�3�    �  �  �          A    with open(core_dir + 'taurus_core_properties.txt', 'w') as f:�  �  �          <            filename_base = region_dir + 'taurus_av_boxes_',�  �  �          A    with open(core_dir + 'taurus_core_properties.txt', 'r') as f:�  �  �          L    noise_cube_filename = 'taurus_hi_galfa_cube_regrid_planckres_noise.fits'�  �  �          =                'taurus_hi_galfa_cube_regrid_planckres.fits',�  �  �          6                'taurus_av_error_planck_5arcmin.fits',�  �  �          0                'taurus_av_planck_5arcmin.fits',�  �  �          F    region_dir = '/d/bip3/ezbc/taurus/data/python_output/ds9_regions/'�  �  �          H    core_dir = '/d/bip3/ezbc/taurus/data/python_output/core_properties/'�  �  �          +    co_dir = '/d/bip3/ezbc/taurus/data/co/'�  �  �          +    hi_dir = '/d/bip3/ezbc/taurus/data/hi/'�    �          +    av_dir = '/d/bip3/ezbc/taurus/data/av/'�  ~  �          5    figure_dir = '/d/bip3/ezbc/taurus/figures/cores/'�  }            A    output_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�  L  N          Ldef load_ds9_region(cores, filename_base = 'taurus_av_boxes_', header=None):�                I''' Calculates the N(HI) / Av correlation for the taurus molecular cloud.5��