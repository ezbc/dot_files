Vim�UnDo� BA2j1SF�̉ޥ��=O'	�J(�$=_�7���  
�   )    main(av_data_type='planck', region=1)  
�   (                       U �Z    _�                             ����                                                                                                                                                                                                                                                                                                                                                             U �R     �  
�  
�          .                #        + ' of taurus Cores',�  
�  
�          M        fig_name_hivsav = 'taurus_hi_vs_av_panels_{0:s}'.format(av_data_type)�  
X  
Z          K        fig_name_hivsh = 'taurus_hi_vs_h_panels_{0:s}'.format(av_data_type)�  
,  
.          L        fig_name_rh2 = 'taurus_rh2_vs_hsd_panels_{0:s}'.format(av_data_type)�  
  

          E        with open(core_dir + 'taurus_core_properties.txt', 'w') as f:�  	�  	�          @                                             'taurus_%s' % core,�  	r  	t          L    region_vertices = properties['regions']['taurus']['poly_verts']['pixel']�  	i  	k          C                                            'taurus_av_poly_cores',�  	[  	]          A    with open(core_dir + 'taurus_core_properties.txt', 'r') as f:�  	P  	R          L    noise_cube_filename = 'taurus_hi_galfa_cube_regrid_planckres_noise.fits'�  	C  	E          0    # 'av/taurus_analysis_global_properties.txt'�  	:  	<          ;                'taurus_co_cfa_cube_regrid_planckres.fits',�  	6  	8          =                'taurus_hi_galfa_cube_regrid_planckres.fits',�  	2  	4          6                'taurus_av_error_planck_5arcmin.fits',�  	.  	0          0                'taurus_av_planck_5arcmin.fits',�  	(  	*          F    region_dir = '/d/bip3/ezbc/taurus/data/python_output/ds9_regions/'�  	'  	)          <    property_dir = '/d/bip3/ezbc/taurus/data/python_output/'�  	&  	(          H    core_dir = '/d/bip3/ezbc/taurus/data/python_output/core_properties/'�  	%  	'          +    co_dir = '/d/bip3/ezbc/taurus/data/co/'�  	$  	&          +    hi_dir = '/d/bip3/ezbc/taurus/data/hi/'�  	#  	%          +    av_dir = '/d/bip3/ezbc/taurus/data/av/'�  	"  	$          5    figure_dir = '/d/bip3/ezbc/taurus/figures/cores/'�  	!  	#          A    output_dir = '/d/bip3/ezbc/taurus/data/python_output/nhi_av/'�  �  	           C            global_property_filename.replace('taurus', region_name)�  �  �                  region_name = 'taurus'�  �  �                  region_name = 'taurus2'�  �  �                  region_name = 'taurus1'�  �  �          9    global_property_filename = 'taurus_global_properties'�  �  �          I            'monte_carlo_results/taurus_mc_results_' + av_data_type + '_'�  �  �          D    results_filename = '/d/bip3/ezbc/taurus/data/python_output/' + \�  �  �          )    av/taurus_analysis_av_load_regions.py�  �  �          J    hi/taurus_analysis_hi_av_core_likelihoods.py    Calculates HI velocity�  �  �          H    av/taurus_analysis_av_derive_core_boxes.py      Calculates box sizes�  �  �          J    hi/taurus_analysis_core_properties.py           Defines core positions�  m  o          Cdef load_ds9_core_region(cores, filename_base = 'taurus_av_boxes_',�  �  �          G            # the lower phi_cnm values than for taurus mean that taurus�                I''' Calculates the N(HI) / Av correlation for the taurus molecular cloud.5�_�                    
�   (    ����                                                                                                                                                                                                                                                                                                                                                             U �Y    �  
�  
�  
�      )    main(av_data_type='planck', region=1)5��