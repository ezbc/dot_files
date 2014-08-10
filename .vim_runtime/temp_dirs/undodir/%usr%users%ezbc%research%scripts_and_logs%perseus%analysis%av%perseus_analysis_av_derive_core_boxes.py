Vim�UnDo� @���\ag���w/�6���x��:���P             G                       Sƍ�    _�                             ����                                                                                                                                                                                                                                                                                                                                                          S��@    �  �  �          9                filename='california_av_cores_map.%s' % \�  �  �          H                title=r'california: A$_V$ map with core boxed-regions.',�  �  �          E    with open(core_dir + 'california_core_properties.txt', 'w') as f:�  �  �          @            filename_base = region_dir + 'california_av_boxes_',�  �  �          E    with open(core_dir + 'california_core_properties.txt', 'r') as f:�  �  �          :                'california_av_error_planck_5arcmin.fits',�  �  �          4                'california_av_planck_5arcmin.fits',�  �  �          J    region_dir = '/d/bip3/ezbc/california/data/python_output/ds9_regions/'�  �  �          L    core_dir = '/d/bip3/ezbc/california/data/python_output/core_properties/'�  �  �          /    co_dir = '/d/bip3/ezbc/california/data/co/'�  �  �          /    hi_dir = '/d/bip3/ezbc/california/data/hi/'�  �  �          /    av_dir = '/d/bip3/ezbc/california/data/av/'�  �  �          8    figure_dir = '/d/bip3/ezbc/california/figures/maps/'�  �  �          E    output_dir = '/d/bip3/ezbc/california/data/python_output/nhi_av/'�  �  �          Pdef load_ds9_region(cores, filename_base = 'california_av_boxes_', header=None):�                M''' Calculates the N(HI) / Av correlation for the california molecular cloud.5�_�                   �        ����                                                                                                                                                                                                                                                                                                               �                                           S���     �  �  �      5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �                                           S���     �  �  �            # parameters used in script5�_�                   �        ����                                                                                                                                                                                                                                                                                                                                                           S���     �  �  �         5�_�                   �       ����                                                                                                                                                                                                                                                                                                                                                           S���     �  �  �            box_width = ()5�_�                   �        ����                                                                                                                                                                                                                                                                                                                         �         �          V       S���     �  �  �      5�_�                   �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_width = 10 # in pixels5�_�      	             �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_idth = 10 # in pixels5�_�      
           	  �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_dth = 10 # in pixels5�_�   	              
  �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_th = 10 # in pixels5�_�   
                �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_h = 10 # in pixels5�_�                   �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_ = 10 # in pixels5�_�                   �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_height = 10 # in pixels5�_�                   �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���     �  �  �  	          box_height = 0 # in pixels5�_�                   �       ����                                                                                                                                                                                                                                                                                                                        �         �          V       S���    �  �  �  	          box_height =  # in pixels5�_�                   �        ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���     �  �  �           5�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���     �  �  �        H    box_dict = derive_ideal_box(av_data, cores, 8, 20, core_rel_pos=0.1,5�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���     �  �  �           �  �  �        G    box_dict = derive_ideal_box(av_data, cores, , 20, core_rel_pos=0.1,5�_�                   �   ;    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���     �  �  �        P    box_dict = derive_ideal_box(av_data, cores, box_width, 20, core_rel_pos=0.1,5�_�                   �   ;    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���     �  �  �        O    box_dict = derive_ideal_box(av_data, cores, box_width, 0, core_rel_pos=0.1,5�_�                   �   ;    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S���    �  �  �           �  �  �        N    box_dict = derive_ideal_box(av_data, cores, box_width, , core_rel_pos=0.1,5�_�                   �   D    ����                                                                                                                                                                                                                                                                                                               �   D      �         �          V       S���    �  �  �        X    box_dict = derive_ideal_box(av_data, cores, box_width, box_height, core_rel_pos=0.1,   8            angle_res=10., av_image_error=av_error_data)    5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �   D      �         �          V       S���     �  �  �            box_height = 60 # in pixels5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �   D      �         �          V       S���    �  �  �            box_height = 0 # in pixels5�_�                   :   G    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       S�&^    �  9  ;        G                                                     header=header)[:2]5�_�                    (        ����                                                                                                                                                                                                                                                                                                               :   O                  �          V       Sƍ�    �  '  (           5��