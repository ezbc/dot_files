Vim�UnDo� �>XxЖW�>�5�w�*��R�V'�4���4  '                 )       )   )   )    U�3    _�                     �        ����                                                                                                                                                                                                                                                                                                                                                             U�`      �   �     �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �   K       V        U�`!     �   �   �       -   def main():   ,    av_dir = '/d/bip3/ezbc/perseus/data/av/'   4    planck_dir = '/d/bip3/ezbc/perseus/data/planck/'       	    if 0:       	# Color excess maps           # -----------------   :        (data, header) = extract_data(datatype = 'tau353')   K        write_data(data, header, planck_dir + 'perseus_planck_tau353.fits')   4        (data, header) = tau353_to_ebv(data, header)   H        write_data(data, header, planck_dir + 'perseus_planck_ebv.fits')   -        (data, header) = ebv2av(data, header)   C        write_data(data, header, av_dir + 'perseus_av_planck.fits')       =        (data, header) = extract_data(datatype = 'tau353err')   Q        write_data(data, header, planck_dir + 'perseus_planck_tau353_error.fits')   4        (data, header) = tau353_to_ebv(data, header)   N        write_data(data, header, planck_dir + 'perseus_planck_ebv_error.fits')   -        (data, header) = ebv2av(data, header)   I        write_data(data, header, av_dir + 'perseus_av_error_planck.fits')       	    if 1:   7        (data, header) = extract_data(datatype = 'ebv')   Q        write_data(data, header, planck_dir + 'perseus_planck_radiance_ebv.fits')   -        (data, header) = ebv2av(data, header)   L        write_data(data, header, av_dir + 'perseus_av_planck_radiance.fits')       ;        (data, header) = extract_data(datatype = 'ebv_err')            write_data(data, header,   F                planck_dir + 'perseus_planck_radiance_ebv_error.fits')   -        (data, header) = ebv2av(data, header)            write_data(data, header,   A                av_dir + 'perseus_av_error_planck_radiance.fits')   	    if 1:               # Band maps           # ---------   7        (data, header) = extract_data(datatype = '857')   K        write_data(data, header, planck_dir + 'perseus_planck_857ghz.fits')       7        (data, header) = extract_data(datatype = '545')   K        write_data(data, header, planck_dir + 'perseus_planck_545ghz.fits')       7        (data, header) = extract_data(datatype = '353')   K        write_data(data, header, planck_dir + 'perseus_planck_353ghz.fits')5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �   K       V        U�`"     �   �   �           5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �   K       V        U�`"     �   �   �           5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �   K       V        U�`*    �   �   �          H        write_data(data, header, co_dir + 'taurus_co_error_planck.fits')�   �   �          B        write_data(data, header, co_dir + 'taurus_co_planck.fits')�   �   �          L        write_data(data, header, co_dir + 'taurus_co_3-2_error_planck.fits')�   �   �          F        write_data(data, header, co_dir + 'taurus_co_3-2_planck.fits')�   �   �          L        write_data(data, header, co_dir + 'taurus_co_2-1_error_planck.fits')�   �   �          F        write_data(data, header, co_dir + 'taurus_co_2-1_planck.fits')�   �   �          L        write_data(data, header, co_dir + 'taurus_co_1-0_error_planck.fits')�   �   �          F        write_data(data, header, co_dir + 'taurus_co_1-0_planck.fits')�   �   �          J        write_data(data, header, planck_dir + 'taurus_planck_353ghz.fits')�   �   �          J        write_data(data, header, planck_dir + 'taurus_planck_545ghz.fits')�   �   �          J        write_data(data, header, planck_dir + 'taurus_planck_857ghz.fits')�   �   �          :                   av_dir + 'taurus_av_error_planck.fits')�   �   �          4                   av_dir + 'taurus_av_planck.fits')�   �   �          =                   av_dir + 'taurus_av_planck_radiance.fits')�   �   �          B                   planck_dir + 'taurus_ebv_planck_radiance.fits')�   �   �          L        write_data(data, header, planck_dir + 'taurus_planck_radiance.fits')�   �   �          H        write_data(data, header, av_dir + 'taurus_av_error_planck.fits')�   �   �          M        write_data(data, header, planck_dir + 'taurus_planck_ebv_error.fits')�   �   �          P        write_data(data, header, planck_dir + 'taurus_planck_tau353_error.fits')�   �   �          ;                   av_dir + 'taurus_av_planck_tau353.fits')�   �   �          @                   planck_dir + 'taurus_ebv_planck_tau353.fits')�   �   �          J        write_data(data, header, planck_dir + 'taurus_planck_tau353.fits')�   �   �          3    planck_dir = '/d/bip3/ezbc/taurus/data/planck/'�   �   �          +    co_dir = '/d/bip3/ezbc/taurus/data/co/'�   �   �          +    av_dir = '/d/bip3/ezbc/taurus/data/av/'5�_�                    �        ����                                                                                                                                                                                                                                                                                                                �          �           �   K       V        U�`     �   �   �   �       �   �   �   �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                �          �           �   K       V        U�`�     �   �   �   �    5�_�      	              ]        ����                                                                                                                                                                                                                                                                                                               +          �           ]           V        U�`�     �   \   ]       %   'def write_data(data, header, filename):           pf.writeto(filename,               data,               header = header,               clobber = True,   "            output_verify = 'fix')       def ebv2av(data, header):   4    # Av=E(B-V) x 3.05263, 152 in Tielens' ISM book.           data *= 3.05363       header['BUNIT'] = 'mag'           return (data, header)        def tau353_to_ebv(data, header):           '''       ,    The dust emission maps are derived from:   C    Planck 2013 results. XI. All-sky model of thermal dust emission       O    Whereby they fit for the dust optical depth at 353 GHz, and then calibrated   H    the conversion of the optical depth to color excess using background       quasars.       F    E(B-V) can be calculated from the dust optical depth at 353 GHz by   $    (E(B - V)/tau 353 = 1.49 x 10**4           '''           data *= 1.49e4       header['BUNIT'] = 'mag'           return (data, header)    5�_�      
           	   \        ����                                                                                                                                                                                                                                                                                                                         ]           ]           V        U�`�    �   [   \           5�_�   	              
   �        ����                                                                                                                                                                                                                                                                                                                \           \           \           V        U�`�    �   �   �           5�_�   
                �        ����                                                                                                                                                                                                                                                                                                                           %   @                  v        U���     �   �   �  
       5�_�                    �   	    ����                                                                                                                                                                                                                                                                                                                            �          �   	       V       U���     �   �   �          	    if 1:           # Color excess maps           # -----------------           # tau_353   :        (data, header) = extract_data(datatype = 'tau353')   K        write_data(data, header, planck_dir + 'perseus_planck_tau353.fits')       ?        (data_ebv_tau353, header) = tau353_to_ebv(data, header)   +        write_data(data_ebv_tau353, header,   A                   planck_dir + 'perseus_ebv_planck_tau353.fits')       B        (data_av_tau353, header) = ebv2av(data_ebv_tau353, header)   *        write_data(data_av_tau353, header,   <                   av_dir + 'perseus_av_planck_tau353.fits')               # tau 353 error   =        (data, header) = extract_data(datatype = 'tau353err')   Q        write_data(data, header, planck_dir + 'perseus_planck_tau353_error.fits')       4        (data, header) = tau353_to_ebv(data, header)   N        write_data(data, header, planck_dir + 'perseus_planck_ebv_error.fits')       -        (data, header) = ebv2av(data, header)   I        write_data(data, header, av_dir + 'perseus_av_error_planck.fits')5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �   	       V       U��     �   �   �          A                   av_dir + 'taurus_av_error_planck_tau353.fits')�   �   �          F                   planck_dir + 'taurus_ebv_error_planck_tau353.fits')�   �   �          P        write_data(data, header, planck_dir + 'taurus_planck_tau353_error.fits')�   �   �          ;                   av_dir + 'taurus_av_planck_tau353.fits')�   �   �          @                   planck_dir + 'taurus_ebv_planck_tau353.fits')�   �   �          J        write_data(data, header, planck_dir + 'taurus_planck_tau353.fits')5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            ]           d           v        U��     �   	               dec_range = (25, 35)5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            ]           d           v        U��	     �   	               dec_range = (23, 35)5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            ]           d           v        U��	    �   	               dec_range = (23, 3)5�_�                           ����                                                                                                                                                                                                                                                                                                                
          ]           d           v        U��    �   
               ra_range = (40, 65)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��[     �   
               ra_range = (40, 65)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��[     �   
               ra_range = (0, 65)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��\     �   
               ra_range = (, 65)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��^     �   
               ra_range = (35, 65)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��^     �   
               ra_range = (35, 5)5�_�                           ����                                                                                                                                                                                                                                                                                                                          ]           d           v        U��_   
 �   
               ra_range = (35, )5�_�                    
       ����                                                                                                                                                                                                                                                                                                                   "                                        U��t     �   	               dec_range = (23, 38)5�_�                    
       ����                                                                                                                                                                                                                                                                                                                   "                                        U��u     �   	               dec_range = (2, 38)5�_�                           ����                                                                                                                                                                                                                                                                                                                   "                                        U��    �   
               ra_range = (35, 70)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                           U�2�     �          5�_�                     �        ����                                                                                                                                                                                                                                                                                                                                                           U�2�     �   �   �         5�_�      !               �        ����                                                                                                                                                                                                                                                                                                                                                           U�2�     �   �           5�_�       "           !   �        ����                                                                                                                                                                                                                                                                                                                                                           U�2�     �   �   �  �    5�_�   !   #           "   d        ����                                                                                                                                                                                                                                                                                                                          �          d           V        U�2�     �   c   d       :       def ebv2av(data, header):   4    # Av=E(B-V) x 3.05263, 152 in Tielens' ISM book.           data *= 3.05363       header['BUNIT'] = 'mag'           return (data, header)        def tau353_to_ebv(data, header):           '''       ,    The dust emission maps are derived from:   C    Planck 2013 results. XI. All-sky model of thermal dust emission       O    Whereby they fit for the dust optical depth at 353 GHz, and then calibrated   H    the conversion of the optical depth to color excess using background       quasars.       F    E(B-V) can be calculated from the dust optical depth at 353 GHz by   $    (E(B - V)/tau 353 = 1.49 x 10**4           '''           data *= 1.49e4       header['BUNIT'] = 'mag'           return (data, header)       "def radiance_to_ebv(data, header):           '''       ,    The dust emission maps are derived from:   C    Planck 2013 results. XI. All-sky model of thermal dust emission       L    Whereby they fit for the radiance, and then calibrated the conversion of   :    the radiance to color excess using background quasars.       6    E(B-V) can be calculated from the dust radiance by   %    (E(B - V)/radiance = 5.40 x 10**5           '''           data *= 5.40e5       header['BUNIT'] = 'mag'           return (data, header)       2def combine_ebv(ebv_radiance, ebv_tau353, Rv=3.1):       (    ebv_combined = np.copy(ebv_radiance)   1    ebv_combined[ebv_combined > 0.3] = ebv_tau353           av = ebv_combined * Rv           return av5�_�   "   $           #   �        ����                                                                                                                                                                                                                                                                                                                          d          d           V        U�2�     �   �   �           5�_�   #   %           $   �        ����                                                                                                                                                                                                                                                                                                                          d          d           V        U�2�     �   �   �           5�_�   $   &           %   �        ����                                                                                                                                                                                                                                                                                                                          d          d           V        U�2�     �   �   �           5�_�   %   '           &   �        ����                                                                                                                                                                                                                                                                                                                          d          d           V        U�2�     �   �   �           5�_�   &   (           '   �        ����                                                                                                                                                                                                                                                                                                                          �                   V       U�2�    �   �   �       ,   def main():           '''       8    Information on the CO data products can be found at:       9        http://adsabs.harvard.edu/abs/2013arXiv1303.5073P       G        Planck Collaboration, Ade, P.~A.~R., Aghanim, N., et al.\ 2013,           arXiv:1303.5073               '''       ,    av_dir = '/d/bip3/ezbc/perseus/data/av/'   ,    co_dir = '/d/bip3/ezbc/perseus/data/co/'   4    planck_dir = '/d/bip3/ezbc/perseus/data/planck/'       	    if 1:           # Color excess maps           # -----------------           # tau_353   :        (data, header) = extract_data(datatype = 'tau353')   K        write_data(data, header, planck_dir + 'perseus_planck_tau353.fits')       ?        (data_ebv_tau353, header) = tau353_to_ebv(data, header)   +        write_data(data_ebv_tau353, header,   A                   planck_dir + 'perseus_ebv_planck_tau353.fits')       B        (data_av_tau353, header) = ebv2av(data_ebv_tau353, header)   *        write_data(data_av_tau353, header,   <                   av_dir + 'perseus_av_planck_tau353.fits')               # tau 353 error   =        (data, header) = extract_data(datatype = 'tau353err')   Q        write_data(data, header, planck_dir + 'perseus_planck_tau353_error.fits')       E        (data_ebv_tau353_error, header) = tau353_to_ebv(data, header)   +        write_data(data_ebv_tau353, header,   G                   planck_dir + 'perseus_ebv_error_planck_tau353.fits')       N        (data_av_tau353_error, header) = ebv2av(data_ebv_tau353_error, header)   0        write_data(data_av_tau353_error, header,   B                   av_dir + 'perseus_av_error_planck_tau353.fits')5�_�   '   )           (   �        ����                                                                                                                                                                                                                                                                                                                �          �          �          V       U�2�    �   �   �          E                   av_dir + 'california_av_error_planck_tau353.fits')�   �   �          J                   planck_dir + 'california_ebv_error_planck_tau353.fits')�   �   �          F                   planck_dir + 'california_planck_tau353_error.fits')�   �   �          ?                   av_dir + 'california_av_planck_tau353.fits')�   �   �          D                   planck_dir + 'california_ebv_planck_tau353.fits')�   �   �          @                   planck_dir + 'california_planck_tau353.fits')�   �   �          7    planck_dir = '/d/bip3/ezbc/california/data/planck/'�   �   �          /    co_dir = '/d/bip3/ezbc/california/data/co/'�   �   �          /    av_dir = '/d/bip3/ezbc/california/data/av/'5�_�   (               )           ����                                                                                                                                                                                                                                                                                                                �                                           U�3    �        '       �        &    5�_�   
                   !    ����                                                                                                                                                                                                                                                                                                                �           \           \           V        U�`�     �        
      =def extract_data(datatype = 'ebv', ra_range, dec_range=None):5�_�                       +    ����                                                                                                                                                                                                                                                                                                                �           
                     V   /    U�`�     �        
      Bdef extract_data(datatype = 'ebv', ra_range=None, dec_range=None):5�_�                     
        ����                                                                                                                                                                                                                                                                                                                �           
          
           V   /    U�`�     �   	           5��