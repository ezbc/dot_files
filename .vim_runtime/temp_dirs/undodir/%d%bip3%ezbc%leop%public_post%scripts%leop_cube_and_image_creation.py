Vim�UnDo� g[�9<�'�P���.3g��:ewI[j��ѵvc  u   fitsDir = './'   '         L       L   L   L    S�E�    _�                     /        ����                                                                                                                                                                                                                                                                                                                                                             S��     �   .   /           5�_�                    �        ����                                                                                                                                                                                                                                                                                                                /                                            S��    �   �   �          $# blank the cube at threshold*sigma �   �   �          #	   For a x beam: �   �   �          7#	Here, units of images are Jy/Bm m/s; cellsize = 2"; 	5�_�                    #        ����                                                                                                                                                                                                                                                                                                                /           #          &   	       V       S�(     �   "   #          lappy = False   cosmos = True   # located on the laptop at:   	if lappy:5�_�                    $        ����                                                                                                                                                                                                                                                                                                                +           $          &          V       S�*     �   #   $          elif cosmos:   N    fitsDirOrig = '/d/bip3/ezbc/leop/data/hi/casa/fitsImages/fluxRescale/' + \                 'originalCubes/'5�_�                    $        ����                                                                                                                                                                                                                                                                                                                (           $           $           V        S�-     �   #   $          	if lappy:5�_�                    %        ����                                                                                                                                                                                                                                                                                                                '           %          &          V       S�.     �   $   %          elif cosmos:   F    fitsDir = '/d/bip3/ezbc/leop/data/hi/casa/fitsImages/fluxRescale/'5�_�                    &        ����                                                                                                                                                                                                                                                                                                                %           &           &           V        S�/     �   %   &          	if lappy:5�_�      	              %        ����                                                                                                                                                                                                                                                                                                                %           &           &           V        S�0     �   $   %           5�_�      
           	   &        ����                                                                                                                                                                                                                                                                                                                            &          '          V       S�1     �   %   &          elif cosmos:   <    chdir('/d/bip3/ezbc/leop/data/hi/casa/images/vla.gmrt/')5�_�   	              
   #        ����                                                                                                                                                                                                                                                                                                                            #           %                 S�5    �   "   &  ~      H    fitsDirOrig = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'   D    fitsDir = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'   @    chdir('/home/elijah/research/leop/data/vla.gmrt/casaImages')5�_�   
                %   <    ����                                                                                                                                                                                                                                                                                                                %           $          #          V       S� Q     �   $   (  ~      <chdir('/home/elijah/research/leop/data/vla.gmrt/casaImages')5�_�                           ����                                                                                                                                                                                                                                                                                                                %           $          #          V       S� l    �        �      import pyfits as pf5�_�                    1   )    ����                                                                                                                                                                                                                                                                                                                          >   )       1   )       V   )    S� �     �   0   1          0# add reference frame information to all headers   K# CASA task imhead changed the spectral values when the header info changed   # f-ing CASA   (for j, basename in enumerate(basenames):       images = []   0    for i, resolution in enumerate(resolutions):   "        images.append(basename + \   <                      str(resolution) + extension + '.fits')   A        f = pf.open(fitsDirOrig + 'noRefFrameCubes/' + images[i])   ,        h, d = f[0].header, f[0].data[:,:,:]   "        h.update('specsys','LSRK')   +        hdu = pyfits.PrimaryHDU(d,header=h)   '        hdulist = pyfits.HDUList([hdu])   0        hdulist.writeto(fitsDirOrig + images[i])5�_�                    0        ����                                                                                                                                                                                                                                                                                                                          1   )       1   )       V   )    S� �     �   /   0           5�_�                    0        ����                                                                                                                                                                                                                                                                                                                          0   )       0   )       V   )    S� �    �   /   0           5�_�                    ~       ����                                                                                                                                                                                                                                                                                                                0           ~          ~   G       v   G    S� �     �   }     q      I    dummyMS = '/d/bip3/ezbc/leop/data/hi/casa/uvdata/leopVLAc.contsub.ms'5�_�                            ����                                                                                                                                                                                                                                                                                                                0              
       �          V       S� �     �   ~             elif lappy:   F    dummyMS = '/home/elijah/research/leop/data/vla/c_config/casa/' + \   (              'reductionFiles/dataRR.ms'5�_�                    }        ����                                                                                                                                                                                                                                                                                                                0              
                 V       S� �     �   |   ~  n      
if cosmos:5�_�                    }        ����                                                                                                                                                                                                                                                                                                                0           }           }           V        S� �     �   |   }          	f cosmos:5�_�                    }       ����                                                                                                                                                                                                                                                                                                                0           }           }           V        S� �    �   |   ~  m          dummyMS = ''5�_�                    &       ����                                                                                                                                                                                                                                                                                                                �           &          &   9       v   9    S�!     �   %   '  m      <chdir('/home/elijah/research/leop/data/vla.gmrt/casaImages')5�_�                    &       ����                                                                                                                                                                                                                                                                                                                �           &          &   9       v   9    S�!    �   $   &          @fitsDir = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'�   %   '  m      	chdir('')5�_�                    (       ����                                                                                                                                                                                                                                                                                                                %   !       &          &   9       v   9    S�!'     �   '   )  m      fitsDirOrig = ''5�_�                    (       ����                                                                                                                                                                                                                                                                                                                %   !       &          &   9       v   9    S�!,     �   '   *  m      fitsDirOrig = '../original/'5�_�                    )       ����                                                                                                                                                                                                                                                                                                                %   !       &          &   9       v   9    S�!7   	 �   (   *  n      fitsDir = ''5�_�                     $       ����                                                                                                                                                                                                                                                                                                                )          %          $          V       S�!;    �   #   $          DfitsDirOrig = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'   @fitsDir = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'5�_�      !               4       ����                                                                                                                                                                                                                                                                                                                �          6   7       5          v       S�"�     �   3   7  l              # import fits image5�_�       "           !   5        ����                                                                                                                                                                                                                                                                                                                �          8   7       7          v       S�"�     �   4   6  n       5�_�   !   #           "   5       ����                                                                                                                                                                                                                                                                                                                �          8   7       7          v       S�"�    �   4   7  n              print 5�_�   "   $           #   5   %    ����                                                                                                                                                                                                                                                                                                                5          7           5   %       V   %    S�"�    �   4   5          (        print fitsDirOrig + basename + \   8                   str(resolution) + extension + '.fits'    5�_�   #   %           $   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../original/'5�_�   $   &           %   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../riginal/'5�_�   %   '           &   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../iginal/'5�_�   &   (           '   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../ginal/'5�_�   '   )           (   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../inal/'5�_�   (   *           )   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../nal/'5�_�   )   +           *   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../al/'5�_�   *   ,           +   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '../l/'5�_�   +   -           ,   &       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   %   '  l      fitsDirOrig = '..//'5�_�   ,   .           -   2       ����                                                                                                                                                                                                                                                                                                                5          5           5   %       V   %    S�#�     �   1   4  l          images = []5�_�   -   /           .   3       ����                                                                                                                                                                                                                                                                                                                6          6           6   %       V   %    S�#�     �   2   5  m          if basename == ''5�_�   .   0           /   4       ����                                                                                                                                                                                                                                                                                                                7          7           7   %       V   %    S�#�     �   3   6  n          	fitsDirOrig = ''5�_�   /   1           0   5       ����                                                                                                                                                                                                                                                                                                                8          8           8   %       V   %    S�$     �   4   7  o          elif basename == ''5�_�   0   2           1   6       ����                                                                                                                                                                                                                                                                                                                9          9           9   %       V   %    S�$    �   5   8  p              fitsDirOrigin = ''5�_�   1   3           2   7        ����                                                                                                                                                                                                                                                                                                                7           :           :   %       V   %    S�$3     �   6   8  q       5�_�   2   4           3   7        ����                                                                                                                                                                                                                                                                                                                7           ;   7       :          v       S�$>     �   6   9  q       5�_�   3   5           4   7        ����                                                                                                                                                                                                                                                                                                                7           <   7       ;          v       S�$>     �   6   8           �   6   9  r       5�_�   4   6           5   8   
    ����                                                                                                                                                                                                                                                                                                                7           =   7       <          v       S�$A     �   6   8          Z≡jedi=0, ≡         (*value*, ..., sep = ' ', end = '\n', file = sys.stdout) ≡jedi≡�   7   9  s          print()5�_�   5   7           6   8   
    ����                                                                                                                                                                                                                                                                                                                7           =   7       <          v       S�$C    �   7   :  s          print(f)5�_�   6   8           7   $       ����                                                                                                                                                                                                                                                                                                                9   8       $   !       $          v       S�$U    �   #   %  t      $chdir('../data/cubes/flux_rescale/')5�_�   7   9           8   6       ����                                                                                                                                                                                                                                                                                                                $          $   !       $          v       S�$c     �   5   7  t      '        fitsDirOrigin = 'flux_rescale/'5�_�   8   :           9   6       ����                                                                                                                                                                                                                                                                                                                $          $   !       $          v       S�$d    �   5   7  t      &        fitsDirOrign = 'flux_rescale/'5�_�   9   ;           :   5   !    ����                                                                                                                                                                                                                                                                                                                6          $   !       $          v       S�$�    �   4   6  t      *    elif basename == 'leop.flux_rescale.':5�_�   :   <           ;   8   
    ����                                                                                                                                                                                                                                                                                                                5          $   !       $          v       S�$�    �   6   8           �   7   9  t      $    print(fitsDirOrig + basename + \5�_�   ;   =           <   �        ����                                                                                                                                                                                                                                                                                                                8          $   !       $          v       S�%&     �   �   �  t       5�_�   <   >           =   �        ����                                                                                                                                                                                                                                                                                                                8          $   !       $          v       S�%'    �   �   �  u      dummyMS = ''    �   �   �  v           �   �   �  v       5�_�   =   ?           >   8        ����                                                                                                                                                                                                                                                                                                                8          :           8           V        S�%     �   7   8          1    print('Loading ' + fitsDirOrig + basename + \   9                   str(resolution) + extension + '.fits')    5�_�   >   @           ?   K        ����                                                                                                                                                                                                                                                                                                                           8           8           V        S�%�     �   J   N  q    5�_�   ?   A           @   J       ����                                                                                                                                                                                                                                                                                                                           8           8           V        S�%�     �   I   L  t              ia.close()5�_�   @   B           A   L        ����                                                                                                                                                                                                                                                                                                                           L          M          V       S�%�    �   K   N  u      1    print('Loading ' + fitsDirOrig + basename + \   9                   str(resolution) + extension + '.fits')5�_�   A   C           B   p        ����                                                                                                                                                                                                                                                                                                                L          L          M          V       S�%�     �   o   s  u       5�_�   B   D           C   q        ����                                                                                                                                                                                                                                                                                                                L          L          M          V       S�%�     �   o   q           �   p   r  w       5�_�   C   E           D   q       ����                                                                                                                                                                                                                                                                                                                L          L          M          V       S�%�     �   o   q          V≡jedi=0, ≡     (*value*, ..., sep = ' ', end = '\n', file = sys.stdout) ≡jedi≡�   p   r  w      print()5�_�   D   F           E   q       ����                                                                                                                                                                                                                                                                                                                L          L          M          V       S�%�    �   o   q           �   p   r  w      print(image)5�_�   E   G           F   q        ����                                                                                                                                                                                                                                                                                                                q          q          q          V       S�%�     �   p   q          print(images)5�_�   F   H           G   q        ����                                                                                                                                                                                                                                                                                                                           q          q          V       S�%�    �   p   q           5�_�   G   I           H   �       ����                                                                                                                                                                                                                                                                                                                �   #       q          q          V       S�(�    �   �   �          &for i, image in enumerate(images[4:]):�   �   �  u                    dummyMS=dummyMS,5�_�   H   J           I   �       ����                                                                                                                                                                                                                                                                                                                �          �           �           v        S�)    �   �   �  u                    #dummyMS=dummyMS,5�_�   I   K           J   �       ����                                                                                                                                                                                                                                                                                                                �          �           �           v        S�*�    �   �   �  u      dummyMS = ''5�_�   J   L           K   '       ����                                                                                                                                                                                                                                                                                                                �          �           �           v        S�E�     �   &   (  u      fitsDir = './'5�_�   K               L   '       ����                                                                                                                                                                                                                                                                                                                �          �           �           v        S�E�    �   &   (  u      fitsDir = '../'5�_�   
                #   C    ����                                                                                                                                                                                                                                                                                                                                                             S� <     �   "   $  ~      fitsDirOrig = ''5�_�                    #       ����                                                                                                                                                                                                                                                                                                                            #          #          V       S� A     �   "   %        5�_�                    #        ����                                                                                                                                                                                                                                                                                                                            #          #          V       S� B     �   #   $  |      fitsDirOrig = ''   @fitsDir = '/home/elijah/research/leop/data/vla.gmrt/fitsImages/'5�_�                    $        ����                                                                                                                                                                                                                                                                                                                            "           "           V        S� C     �   #   %  ~          fitsDirOrig = ''5�_�                     "        ����                                                                                                                                                                                                                                                                                                                            "           "           V        S� D    �   !   #        5��