Vim�UnDo� @Hg/gߣS�s��[׋���G���m�yeS,  �       regions = [None, 1, 2,]  `                          U�    _�                    �        ����                                                                                                                                                                                                                                                                                                                                                             U�     �  k  m          L        property_filename = property_filename.replace('taurus', region_name)�  j  l          D        property_filename = 'taurus_global_properties_planck_scaled'�  h  j          "            region_name = 'taurus'�  f  h          #            region_name = 'taurus2'�  d  f          #            region_name = 'taurus1'�  Y  [          9    property_filename = 'taurus_global_properties_planck'�  W  Y          B    final_property_dir = '/d/bip3/ezbc/taurus/data/python_output/'�  U  W          &        '/d/bip3/ezbc/taurus/figures/'�  S  U          L        '/d/bip3/ezbc/taurus/data/python_output/residual_parameter_results/'�  �  �          G                            'taurus_hi_galfa_cube_regrid_planckres' + \�  �  �          J                               'taurus_av_planck_5arcmin' + bin_string + \�  �  �          H                'taurus_av_error_planck_5arcmin' + bin_string + '.fits',�  �  �          N                            'taurus_av_planck_5arcmin' + bin_string + '.fits',�  �  �          J                         'taurus_hi_galfa_cube_regrid_planckres_bin.fits',�  �  �          K                          'taurus_hi_galfa_cube_regrid_planckres_bin.fits',�  �  �          L            fits.writeto(av_dir + 'taurus_av_error_planck_5arcmin_bin.fits',�  �  �          M        if not check_file(av_dir + 'taurus_av_error_planck_5arcmin_bin.fits',�  �  �          N            fits.writeto(av_dir + 'taurus_av_planck_5arcmin_bin_weights.fits',�  �  �          O        if not check_file(av_dir + 'taurus_av_planck_5arcmin_bin_weights.fits',�  �  �          F            fits.writeto(av_dir + 'taurus_av_planck_5arcmin_bin.fits',�  �  �          G        if not check_file(av_dir + 'taurus_av_planck_5arcmin_bin.fits',�  �  �          I                     'taurus_hi_galfa_cube_regrid_planckres_masked.fits',�  �  �          J                      'taurus_hi_galfa_cube_regrid_planckres_masked.fits',�  �  �          K        fits.writeto(av_dir + 'taurus_av_error_planck_5arcmin_masked.fits',�  �  �          L    if not check_file(av_dir + 'taurus_av_error_planck_5arcmin_masked.fits',�  �  �          E        fits.writeto(av_dir + 'taurus_av_planck_5arcmin_masked.fits',�  �  �          F    if not check_file(av_dir + 'taurus_av_planck_5arcmin_masked.fits',�  k  m          G                                              'taurus_residual_pdf.pdf'�              N    global_property_file = global_property_file.replace('taurus', region_name)�                       region_name = 'taurus'�  �                     region_name = 'taurus2'�  �  �                  region_name = 'taurus1'�  �  �          =                'taurus_hi_galfa_cube_regrid_planckres.fits',�  �  �          J                                    'taurus_av_error_planck_5arcmin.fits',�  �  �          J                                          'taurus_av_planck_5arcmin.fits',�  �  �          H                                  'taurus_av_k09_regrid_planckres.fits',�  �  �          I    results_filename = 'taurus_likelihood_{0:s}_bin'.format(av_data_type)�  �  �          L    likelihood_filename = 'taurus_likelihood_{0:s}_bin'.format(av_data_type)�  �  �          E    likelihood_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�  �  �          <    property_dir = '/d/bip3/ezbc/taurus/data/python_output/'�  �  �          H    core_dir = '/d/bip3/ezbc/taurus/data/python_output/core_properties/'�  �  �          +    co_dir = '/d/bip3/ezbc/taurus/data/co/'�  �  �          +    hi_dir = '/d/bip3/ezbc/taurus/data/hi/'�  �  �          +    av_dir = '/d/bip3/ezbc/taurus/data/av/'�  �  �          &        '/d/bip3/ezbc/taurus/figures/'�  �  �          A    output_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�  �  �          5    global_property_file = 'taurus_global_properties'�  �  �          G    noise_cube_filename = 'taurus_hi_galfa_cube_regrid_planckres_noise'5�_�                    `       ����                                                                                                                                                                                                                                                                                                                                                             U�    �  _  a  �          regions = [None, 1, 2,]5��