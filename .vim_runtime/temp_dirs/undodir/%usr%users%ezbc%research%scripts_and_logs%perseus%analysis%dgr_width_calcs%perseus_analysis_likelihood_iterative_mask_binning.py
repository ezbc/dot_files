Vim�UnDo� 0*�7Ud=o:�~�����S�gh�_���ZW�F  �       vel_range = (0, 20)  1                          T��    _�                            ����                                                                                                                                                                                                                                                                                                               �                                           T���    �  `  b          G                            'taurus_hi_galfa_cube_regrid_planckres' + \�  \  ^          J                               'taurus_av_planck_5arcmin' + bin_string + \�  X  Z          H                'taurus_av_error_planck_5arcmin' + bin_string + '.fits',�  T  V          N                            'taurus_av_planck_5arcmin' + bin_string + '.fits',�  D  F          J                         'taurus_hi_galfa_cube_regrid_planckres_bin.fits',�  A  C          K                          'taurus_hi_galfa_cube_regrid_planckres_bin.fits',�  5  7          L            fits.writeto(av_dir + 'taurus_av_error_planck_5arcmin_bin.fits',�  3  5          M        if not check_file(av_dir + 'taurus_av_error_planck_5arcmin_bin.fits',�  #  %          N            fits.writeto(av_dir + 'taurus_av_planck_5arcmin_bin_weights.fits',�  !  #          O        if not check_file(av_dir + 'taurus_av_planck_5arcmin_bin_weights.fits',�               F            fits.writeto(av_dir + 'taurus_av_planck_5arcmin_bin.fits',�              G        if not check_file(av_dir + 'taurus_av_planck_5arcmin_bin.fits',�  	            I                     'taurus_hi_galfa_cube_regrid_planckres_masked.fits',�              J                      'taurus_hi_galfa_cube_regrid_planckres_masked.fits',�              K        fits.writeto(av_dir + 'taurus_av_error_planck_5arcmin_masked.fits',�  �            L    if not check_file(av_dir + 'taurus_av_error_planck_5arcmin_masked.fits',�  �  �          E        fits.writeto(av_dir + 'taurus_av_planck_5arcmin_masked.fits',�  �  �          F    if not check_file(av_dir + 'taurus_av_planck_5arcmin_masked.fits',�  �  �          G                                              'taurus_residual_pdf.pdf'�  s  u          N    global_property_file = global_property_file.replace('taurus', region_name)�  r  t                  region_name = 'taurus'�  p  r                  region_name = 'taurus2'�  n  p                  region_name = 'taurus1'�  c  e          =                'taurus_hi_galfa_cube_regrid_planckres.fits',�  _  a          J                                    'taurus_av_error_planck_5arcmin.fits',�  [  ]          J                                          'taurus_av_planck_5arcmin.fits',�  U  W          H                                  'taurus_av_k09_regrid_planckres.fits',�  P  R          I    results_filename = 'taurus_likelihood_{0:s}_bin'.format(av_data_type)�  O  Q          L    likelihood_filename = 'taurus_likelihood_{0:s}_bin'.format(av_data_type)�  I  K          E    likelihood_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�  G  I          <    property_dir = '/d/bip3/ezbc/taurus/data/python_output/'�  F  H          H    core_dir = '/d/bip3/ezbc/taurus/data/python_output/core_properties/'�  E  G          +    co_dir = '/d/bip3/ezbc/taurus/data/co/'�  D  F          +    hi_dir = '/d/bip3/ezbc/taurus/data/hi/'�  C  E          +    av_dir = '/d/bip3/ezbc/taurus/data/av/'�  B  D          &        '/d/bip3/ezbc/taurus/figures/'�  @  B          A    output_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�               5    global_property_file = 'taurus_global_properties'�              G    noise_cube_filename = 'taurus_hi_galfa_cube_regrid_planckres_noise'5�_�                   1       ����                                                                                                                                                                                                                                                                                                               1                                           T��    �  1  2  �          vel_range = (1.7,7.7)�  /  1  �    5�_�                   1       ����                                                                                                                                                                                                                                                                                                               0                                           T��     �  0  2  �          vel_range = (0, 20)5�_�                   1       ����                                                                                                                                                                                                                                                                                                               0                                           T��     �  0  2  �          vel_range = (-5, 20)5�_�                   1       ����                                                                                                                                                                                                                                                                                                               0                                           T��     �  0  2  �          vel_range = (-5, 0)5�_�                    1       ����                                                                                                                                                                                                                                                                                                               0                                           T��    �  0  2  �          vel_range = (-5, )5��