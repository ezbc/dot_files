Vim�UnDo� �G	oj}����4R�&_¿Xh�̣�h��  Y                   vmax=0.5,  �         ?       ?   ?   ?    T�mB    _�                           ����                                                                                                                                                                                                                                                                                                                                                             T�f�    �      )                       axes_pad=0.4,5�_�                   1        ����                                                                                                                                                                                                                                                                                                                                                          T�g      �  0  >  )       5�_�                   1       ����                                                                                                                                                                                                                                                                                                                        =         1          V       T�g     �  0  >  5      6            ax.annotate(spectra_names[i].capitalize(),   +                        xytext=(0.96, 0.9),   '                        xy=(0.96, 0.9),   3                        textcoords='axes fraction',   1                        xycoords='axes fraction',   (                        size=font_scale,   "                        color='k',   4                        bbox=dict(boxstyle='square',   0                                  facecolor='w',   +                                  alpha=1),   4                        horizontalalignment='right',   0                        verticalalignment='top',                           )5�_�                   1   -    ����                                                                                                                                                                                                                                                                                                                        =         1          V       T�g     �  0  2  5      .    ax.annotate(spectra_names[i].capitalize(),5�_�                   1       ����                                                                                                                                                                                                                                                                                                                        0         0          v       T�g     �  0  2  5          ax.annotate(,5�_�                   0       ����                                                                                                                                                                                                                                                                                                                        0         0          v       T�g    �  /  1  5           ax.set_title(r'Model $A_V$')5�_�                   =       ����                                                                                                                                                                                                                                                                                                               0         0         0          v       T�g    �  =  ?  5    5�_�      	             ;   %    ����                                                                                                                                                                                                                                                                                                               >          ;   %      ;   )       v   )    T�g     �  :  <  6      ,                horizontalalignment='right',5�_�      
           	  ;   %    ����                                                                                                                                                                                                                                                                                                               >          ;   %      ;   )       v   )    T�g     �  :  <  6      '                horizontalalignment='',5�_�   	              
  2       ����                                                                                                                                                                                                                                                                                                               >          ;   %      ;   )       v   )    T�g      �  1  3  6      #                xytext=(0.96, 0.9),5�_�   
                3       ����                                                                                                                                                                                                                                                                                                               >          ;   %      ;   )       v   )    T�g"    �  2  4  6                      xy=(0.96, 0.9),5�_�                    �        ����                                                                                                                                                                                                                                                                                                               3          �          �           v        T�g3     �   �   �  6           params = {#'backend': .pdf',   +              'axes.labelsize': font_scale,   +              'axes.titlesize': font_scale,   *              'text.fontsize': font_scale,   0              'legend.fontsize': font_scale*3/4,   ,              'xtick.labelsize': font_scale,   ,              'ytick.labelsize': font_scale,   !              'font.weight': 500,   &              'axes.labelweight': 500,   #              'text.usetex': False,   (              'figure.figsize': figsize,   ,              'figure.titlesize': font_scale   J              #'axes.color_cycle': color_cycle # colors of different plots                }       plt.rcParams.update(params)5�_�                    �        ����                                                                                                                                                                                                                                                                                                               %          �          �           v        T�g:     �   �   �  (       5�_�                    �   2    ����                                                                                                                                                                                                                                                                                                               <          �          �           v        T�g=    �   �   �  ?      3              'figure.figsize': (7.3/2.0, 7.3/1.5),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                �   &       �          �           v        T�gI    �   �   �  ?    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                �           �          �           v        T�gN    �   �   �  @          colormap = plt.cm.gist_ncar5�_�                   �        ����                                                                                                                                                                                                                                                                                                                �         G         ;           v        T�gr     �  �  �  @       5�_�                   �       ����                                                                                                                                                                                                                                                                                                                �         �         �          V       T�gu     �  �  �  L          ax.annotate(r'Model $A_V$',   #                xytext=(0.05, 0.9),                   xy=(0.05, 0.9),   +                textcoords='axes fraction',   )                xycoords='axes fraction',                    size=font_scale,                   color='k',   ,                bbox=dict(boxstyle='square',   (                          facecolor='w',   #                          alpha=1),   +                horizontalalignment='left',   (                verticalalignment='top',                   )5�_�                   �       ����                                                                                                                                                                                                                                                                                                                �         �         �          V       T�gx   	 �  �  �  L      #        ax.annotate(r'Model $A_V$',5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �         �         �          V       T�g�   
 �  �  �  L      '        ax.set_title(r'Observed $A_V$')5�_�                    �       ����                                                                                                                                                                                                                                                                                                               �         �         �          V       T�g�    �   �   �  L          colormap = plt.cm.gnuplot5�_�                   �        ����                                                                                                                                                                                                                                                                                                                �         �         �           v        T�g�     �  �  �  L       5�_�                   �       ����                                                                                                                                                                                                                                                                                                                �         �         �           v        T�g�    �  �  �  X      &        ax.annotate(r'Observed $A_V$',5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �         �         �           v        T�g�    �  �  �  X      '        ax.set_title(r'Residual $A_V$')5�_�                   �   %    ����                                                                                                                                                                                                                                                                                                               �                             v   =    T�g�     �  �  �  X      &        ax.annotate(r'Residual $A_V$',5�_�                   �   '    ����                                                                                                                                                                                                                                                                                                               �                             v   =    T�g�     �  �  �  X      )        ax.annotate(r'Residual $A_V$' [],5�_�                   �   $    ����                                                                                                                                                                                                                                                                                                               �                             v   =    T�h    �  �  �  X      &        ax.annotate(r'Residual $A_V$',5�_�                   �   $    ����                                                                                                                                                                                                                                                                                                               �   )                          v   =    T�h     �  �  �  X      &        ax.annotate(r'Observed $A_V$',5�_�                   ;       ����                                                                                                                                                                                                                                                                                                               �   )                          v   =    T�h    �  :  <  X          ax.annotate(r'Model $A_V$',5�_�                   4       ����                                                                                                                                                                                                                                                                                                               4                             v   =    T�hC    �  4  5  Y          main(av_data_type='planck')�  2  4  X    5�_�                    
        ����                                                                                                                                                                                                                                                                                                               3         
   .         !       V   7    T�h�     �  	  
          /        plot_av_model(av_image=av_image_masked,   /                      av_model=av_model_masked,   '                      header=av_header,   $                      results=props,   G                      limits=props['plot_limit' + bin_string]['pixel'],   =                      savedir=figure_dir + 'maps/av_models/',   <                      filename=filename + '.' + figure_type,   !                      show=False)5�_�      !              �        ����                                                                                                                                                                                                                                                                                                               +         
   .      
   !       V   7    T�h�     �  �     P    5�_�       "           !  �       ����                                                                                                                                                                                                                                                                                                               3            .         !       V   7    T�h�     �  �  �  X      /        plot_av_model(av_image=av_image_masked,5�_�   !   #           "  �        ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�h�    �  �  �                  5�_�   "   $           #  �       ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�h�     �  �  �  Y      #    figure_types = ['png',]# 'pdf']5�_�   #   %           $  �       ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�h�    �  �  �  Y      "    figure_types = ['png',# 'pdf']5�_�   $   &           %  ,   ;    ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�h�     �  +  -  Y      <        plt.savefig(savedir + filename, bbox_inches='tight')5�_�   %   '           &  ,   D    ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�h�    �  +  -  Y      F        plt.savefig(savedir + filename, bbox_inches='tight', dpi=4004)5�_�   &   (           '   �       ����                                                                                                                                                                                                                                                                                                               ,   D         .         !       V   7    T�i;     �   �   �  Y                  figsize = (7, 4)5�_�   '   )           (   �       ����                                                                                                                                                                                                                                                                                                               ,   D         .         !       V   7    T�iA     �   �   �  Y                  figsize = (3.3, 4)5�_�   (   *           )   �       ����                                                                                                                                                                                                                                                                                                               ,   D         .         !       V   7    T�iD    �   �   �  Y                  figsize = (3.3, )5�_�   )   +           *         ����                                                                                                                                                                                                                                                                                                                �            .         !       V   7    T�iR     �      Y                        cbar_size='3%',5�_�   *   ,           +         ����                                                                                                                                                                                                                                                                                                                �            .         !       V   7    T�iT    �      Y                       cbar_size='%',5�_�   +   -           ,  7   #    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�is     �  6  8  Y      -    ax.set_xlabel('Right Ascension (J2000)',)5�_�   ,   .           -  7   #    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�is     �  6  8  Y      ,    ax.set_xlabel('Right Ascension J2000)',)5�_�   -   /           .  7   )    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iu     �  6  8  Y      -    ax.set_xlabel('Right Ascension [J2000)',)5�_�   .   0           /  7   )    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iu     �  6  8  Y      ,    ax.set_xlabel('Right Ascension [J2000',)5�_�   /   1           0  8   %    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iw     �  7  9  Y      )    ax.set_ylabel('Declination (J2000)',)5�_�   0   2           1  8   %    ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iw     �  7  9  Y      (    ax.set_ylabel('Declination (J2000',)5�_�   1   3           2  8       ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iy     �  7  9  Y      )    ax.set_ylabel('Declination (J2000]',)5�_�   2   4           3  8       ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�iy     �  7  9  Y      (    ax.set_ylabel('Declination J2000]',)5�_�   3   5           4   _        ����                                                                                                                                                                                                                                                                                                                           .         !       V   7    T�i�    �  �  �          -        ax.set_ylabel('Declination (J2000)',)�  �  �          1        ax.set_xlabel('Right Ascension (J2000)',)�  �  �          -        ax.set_ylabel('Declination (J2000)',)�  �  �          1        ax.set_xlabel('Right Ascension (J2000)',)�   �   �          -        ax.set_ylabel('Declination (J2000)',)�   �   �          1        ax.set_xlabel('Right Ascension (J2000)',)�   _   a          )    ax.set_ylabel('Declination (J2000)',)�   ^   `          -    ax.set_xlabel('Right Ascension (J2000)',)5�_�   4   6           5         ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�i�     �      Y              nrows_ncols=(1,3)5�_�   5   7           6         ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�i�     �      Y              nrows_ncols=(,3)5�_�   6   8           7         ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�i�     �      Y              nrows_ncols=(3,3)5�_�   7   9           8         ����                                                                                                                                                                                                                                                                                                               �            .         !       V   7    T�i�    �      Y              nrows_ncols=(3,)5�_�   8   :           9  $        ����                                                                                                                                                                                                                                                                                                                        $         $          V       T�i�    �  #  $              cmap = cm.Greys # colormap5�_�   9   ;           :           ����                                                                                                                                                                                                                                                                                                               $         $         $          V       T�j#     �       Y              �       X    5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                               $                             V       T�j)    �    !  Y      !        if not use_binned_images:   3            plot_av_model(av_image=av_image_masked,   3                          av_model=av_model_masked,   +                          header=av_header,   (                          results=props,   9                          hi_velocity_axis=velocity_axis,   .                          vel_range=vel_range,   2                          hi_spectrum=hi_spectrum,   7                          #hi_limits=[-15, 25, -1, 10],   :                          hi_limits=[-15, 25, None, None],   2                          co_spectrum=co_spectrum,   <                          co_velocity_axis=co_velocity_axis,   K                          limits=props['plot_limit' + bin_string]['pixel'],   A                          savedir=figure_dir + 'maps/av_models/',   M                          filename=filename + '_spectra' + '.' + figure_type,   %                          show=False)           ,        plot_avmod_vs_av((av_model_masked,),   #                (av_image_masked,),   -                av_errors=(av_error_masked,),   :                #limits=[10**-1, 10**1.9, 10**0, 10**1.7],   %                limits=[0,1.5,0,1.5],   +                savedir=figure_dir + 'av/',   !                gridsize=(10,10),   &                #scale=('log', 'log'),   ,                #scale=('linear', 'linear'),   O                filename='taurus_avmod_vs_av%s.%s' % (bin_string, figure_type),                   show = False,                   std=0.22,                   )5�_�   ;   =           <  �       ����                                                                                                                                                                                                                                                                                                                                            V       T�m.    �  �  �  Y                      vmin=-0.25,5�_�   <   >           =  �       ����                                                                                                                                                                                                                                                                                                               �                             V       T�m>     �  �  �  Y                      vmin=-0.5,5�_�   =   ?           >  �       ����                                                                                                                                                                                                                                                                                                               �                             V       T�m?     �  �  �  Y                      vmin=-0.,5�_�   >               ?  �       ����                                                                                                                                                                                                                                                                                                               �                             V       T�mA    �  �  �  Y                      vmax=0.5,5��