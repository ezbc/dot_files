Vim�UnDo� 7u&����	���� �ՏA�@���j�Pa�\  C   P                filename = 'perseus_hi_vs_h_panels_lee12_planck_reproduce.%s' %\  -   ,      -       -   -   -    S�   
 _�                   �       ����                                                                                                                                                                                                                                                                                                                                                             SƦ#     �  �  �      5�_�                  �        ����                                                                                                                                                                                                                                                                                                               �         �          �           V        S���    �  �  �               nhi_image = image * 1.823e-25�_�                   �        ����                                                                                                                                                                                                                                                                                                               �                                            S�
�     �  �  �         5�_�      	             �        ����                                                                                                                                                                                                                                                                                                               �                                            S�
�     �  �  �           5�_�      
           	  �        ����                                                                                                                                                                                                                                                                                                               �          E         �           V       S�
�     �  �  �       �   %def krumholz_eq(h_sd, phi_CNM = None,           Z = 1.0, # metallicity           a = 0.2, # ?   A        f_diss = 0.1, # fraction of absorbing H2 which disociates   0        phi_mol = 10.0, # molecular gas fraction   2        mu_H = 2.3e-24, # molecular weight of H, g           return_fractions=False   
        ):       '''       Krumholz et al. 2008       '''           # Constants   %    c = 3.0e10 # speed of light, cm/s           # solar values   @    sigma_d_solar = 1e-21 # solar dust grain cross section, cm^2   2    R_d_solar = 10**-16.5 # solar cloud radius, cm   /    E_0_solar = 7.5e-4 # Radiation field, erg/s           # cloud values   @    sigma_d = sigma_d_solar * Z # dust grain cross section, cm^2   *    R_d = R_d_solar * Z # cloud radius, cm       /    # normalized radiation field strength, EQ 7   5    chi = ((f_diss * sigma_d_solar * c * E_0_solar) \   )            * (1.0 + (3.1 * Z**0.365))) \   *            / (31.0 * phi_CNM * R_d_solar)       *    # dust-adjusted radiation field, EQ 10   2    psi = chi * (2.5 + chi) / (2.5 + (chi * np.e))            # cloud optical depth, EQ 21   D    tau_c = (3.0 * h_sd * sigma_d) / (4.0 * (3.1 * Z**0.365) * mu_H)            # cloud optical depth, EQ 21       tau_c = 0.067 * Z * h_sd       +    f_H2_sub1 = (3.0 * psi) / (3.0 * tau_c)   N    f_H2_sub2 = (4.0 * a * psi * phi_mol) / ((4.0 * tau_c) + (3.0 * (phi_mol \               - 1.0) * psi))   0    f_H2 = 1.0 - (f_H2_sub1 / (1.0 + f_H2_sub2))       f_HI = 1.0 - f_H2       7    # Keep fractions within real fractional value range       f_HI[f_HI > 1] = 1.0       f_HI[f_HI < 0] = 0.0       f_H2[f_H2 > 1] = 1.0       f_H2[f_H2 < 0] = 0.0       B    # ratio of molecular to atomic fraction, EQ 17 Lee et al. 2012   "    R_H2 = 4 * tau_c / (3 * psi) \   '            * (1+ 0.8 * psi * phi_mol \   ;                / (4 * tau_c + 3 * (phi_mol - 1) * psi)) -1           R_H2 = f_H2 / f_HI           if not return_fractions:           return R_H2       elif return_fractions:           return R_H2, f_H2, f_HI       Adef krumholz_eq_simple(h_sd, phi_CNM, Z, return_fractions=False):       ,   return krumholz_eq(h_sd, phi_CNM=phi_CNM,           Z=1.0, # metallicity           a=0.2, # ?   ?        f_diss=0.1, # fraction of absorbing H2 which disociates   .        phi_mol=10.0, # molecular gas fraction   0        mu_H=2.3e-24, # molecular weight of H, g   *        return_fractions=return_fractions,   	        )       Hdef fit_krumholz(h_sd, rh2, h_sd_extent, p0 = 10, return_params = False,   D        return_fractions=False, return_chisq=False, rh2_error=None):           '''       Parameters       ----------       h_sd : array-like   E        Hydrogen surface density in units of solar mass per parsec**2       rh2 : array-like   ;        Ratio between molecular and atomic hydrogen masses.       h_sd_extent : tuple   I        Lower and upper bound of hydrogen surface densities with which to   %        build the output model array.   ,    p0 : None, scalar, or M-length sequence.   G        Initial guess for the parameters. See scipy.optimize.curve_fit.       return_params : bool   #        Return parameters from fit?       return_fractions : bool           Return f_H2 and f_HI?       return_chisq : bool   /        Return the chi^2 statistic and p-value?       rh2_error : bool   J        Error in rh2 parameter. Calculates a more accurate chi^2 statistic           Returns       -------       rh2_fit : array-like   A        Model ratio between molecular and atomic hydrogen masses.       h_sd_extended : array-like   L        Model hydrogen surface density in units of solar mass per parsec**2.   )    rh2_fit_params : array-like, optional           Model parameter fits.   %    f_H2, f_HI : array-like, optional   2        f_H2 = mass fraction of molecular hydrogen   /        f_HI = mass fraction of atomic hydrogen   ,    chisq_reduced, p_value : float, optional   2        Reduced chi squared statistic and p-value.           '''       (    from scipy.optimize import curve_fit       from scipy import stats       H    # fit the krumholz model, choose first element of tuple = parameters   =    rh2_fit_params = curve_fit(krumholz_eq_simple, h_sd, rh2,   =            maxfev=10000000, p0 = p0, sigma=1.0/rh2_error)[0]            # Create large array of h_sd   O    h_sd_extended = np.linspace(h_sd_extent[0], h_sd_extent[1], h_sd_extent[2])           if not return_fractions:   C        rh2_fit = krumholz_eq_simple(h_sd_extended, rh2_fit_params)       elif return_fractions:   ?        rh2_fit, f_H2, f_HI = krumholz_eq_simple(h_sd_extended,   A                                                 *rh2_fit_params,   G                                                 return_fractions=True)           if return_chisq:           dof = len(rh2) - 1   @        rh2_fit_grid = krumholz_eq_simple(h_sd, *rh2_fit_params)   ?        #chisq = np.sum((rh2 - rh2_fit_grid)**2 / rh2_fit_grid)   >        chisq = np.sum((rh2 - rh2_fit_grid)**2 / rh2_error**2)   "        #if rh2_error is not None:   *        #    chisq /= np.sum(rh2_error**2)   2        p_value = 1.0 - stats.chi2.cdf(chisq, dof)   #        chisq_reduced = chisq / dof       $    print('pvalue = %.2f' % p_value)       print('dof = %.2f' % dof)        print('chi2 = %.2f' % chisq)       %    output = [rh2_fit, h_sd_extended]           if return_params:   $        for param in rh2_fit_params:                output.append(param)       if return_fractions:           output.append(f_H2)           output.append(f_HI)       if return_chisq:   $        output.append(chisq_reduced)           output.append(p_value)           return output5�_�   	              
  �        ����                                                                                                                                                                                                                                                                                                               �          �         �           V       S�
�     �  �    |       5�_�   
                        ����                                                                                                                                                                                                                                                                                                               �                              V       S�
�     �               5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �                              V       S�
�     �  �  �  �      '''5�_�                   u        ����                                                                                                                                                                                                                                                                                                               �          &         u           V       S�
�     �  t  u       �   Cdef calculate_nhi(cube=None, velocity_axis=None, velocity_range=[],   /        return_nhi_error=True, noise_cube=None,   =        velocity_noise_range=[90,100], Tsys=30., header=None,   D        fits_filename=None, fits_error_filename=None, verbose=True):       H    ''' Calculates an N(HI) image given a velocity range within which to   (    include a SpectralGrid's components.           Parameters       ----------       cube : array-like, optional   L        Three dimensional array with velocity axis as 0th axis. Must specify   (        a velocity_axis if cube is used.   (    velocity_axis : array-like, optional   D        One dimensional array containing velocities corresponding to       fits_filename : str   N        If specified, and a header is provided, the nhi image will be written.       header : pyfits.Header           Header from cube.           '''           import numpy as np       $    # Calculate NHI from cube if set   6    if cube is not None and velocity_axis is not None:   (        image = np.empty((cube.shape[1],   )                          cube.shape[2]))           image[:,:] = np.NaN   B        indices = np.where((velocity_axis > velocity_range[0]) & \   7                (velocity_axis < velocity_range[1]))[0]   2        image[:,:] = cube[indices,:,:].sum(axis=0)           # Calculate image error           if return_nhi_error:   2            image_error = np.empty((cube.shape[1],   -                              cube.shape[2]))   %            image_error[:,:] = np.NaN   L            image_error[:,:] = (noise_cube[indices,:,:]**2).sum(axis=0)**0.5            # NHI in units of 1e20 cm^-2   B    nhi_image = np.ma.array(image,mask=np.isnan(image)) * 1.823e-2   3    delta_v = velocity_axis[-1] - velocity_axis[-2]   C    #nhi_image = np.ma.array(image,mask=np.isnan(image)) * 1.823e-2   *    nhi_image = image * 1.823e-2 * delta_v       8    if fits_filename is not None and header is not None:           if verbose:   H            print('Writing N(HI) image to FITS file %s' % fits_filename)   &        header['BUNIT'] = '1e20 cm^-2'           header.remove('CDELT3')           header.remove('CRVAL3')           header.remove('CRPIX3')           header.remove('CTYPE3')           header.remove('NAXIS3')           header['NAXIS'] = 2       L        pf.writeto(fits_filename, image*1.823e-2, header = header, clobber =   ,                True, output_verify = 'fix')       >    if fits_error_filename is not None and header is not None:           if verbose:   N            print('Writing N(HI) error image to FITS file %s' % fits_filename)       H        pf.writeto(fits_error_filename, image_error * 1.823e-2, header =   >                header, clobber = True, output_verify = 'fix')           if return_nhi_error:   2        nhi_image_error = np.ma.array(image_error,   6                mask=np.isnan(image_error)) * 1.823e-2   0        nhi_image_error = image_error * 1.823e-2   )        return nhi_image, nhi_image_error   	    else:           return nhi_image       7def calculate_noise_cube(cube=None, velocity_axis=None,   J            velocity_noise_range=[-110,-90,90,110], header=None, Tsys=30.,               filename=None):       :    """ Calcuates noise envelopes for each pixel in a cube       """           import numpy as np       import pyfits as pf       %    noise_cube = np.zeros(cube.shape)   "    for i in range(cube.shape[1]):   &        for j in range(cube.shape[2]):   !            profile = cube[:,i,j]   ;            noise = calculate_noise(profile, velocity_axis,   )                    velocity_noise_range)   7            #noise = 0.1 # measured in line free region   ;            noise_cube[:,i,j] = calculate_noise_scale(Tsys,   )                    profile, noise=noise)           if filename is not None:   7        pf.writeto(filename, noise_cube, header=header)           return noise_cube       <def calculate_noise(profile, velocity_axis, velocity_range):   C    """ Calculates rms noise of Tile profile given velocity ranges.       """       import numpy as np           std = 0       1    # calculate noises for each individual region   ,    for i in range(len(velocity_range) / 2):   (        velMin = velocity_range[2*i + 0]   (        velMax = velocity_range[2*i + 1]       =        noise_region = np.where((velocity_axis >= velMin) & \   2                        (velocity_axis <= velMax))       ,        std += np.std(profile[noise_region])       "    std /= len(velocity_range) / 2       return std       5def calculate_noise_scale(Tsys, profile, noise=None):   D    """ Creates an array for scaling the noise by (Tsys + Tb) / Tsys       """       import numpy as np       n = np.zeros(len(profile))   '    n = (Tsys + profile) / Tsys * noise           return n       *def calculate_sd(image, sd_factor=1/1.25):       N    ''' Calculates a surface density image given a velocity range within which   +    to include a SpectralGrid's components.           Parameters       ----------       cube : array-like, optional   L        Three dimensional array with velocity axis as 0th axis. Must specify   (        a velocity_axis if cube is used.   (    velocity_axis : array-like, optional   H        One dimensional array containing velocities corresponding to '''           import numpy as np            # NHI in units of 1e20 cm^-2        sd_image = image * sd_factor           return sd_image       Cdef calculate_nh2(nhi_image = None, av_image = None, dgr = 1.1e-1):       F    ''' Calculates the total gas column density given N(HI), A_v and a       dust-to-gas ratio.           Parameters       ----------       '''           import numpy as np       1    nh_image = 0.5 * (av_image / dgr - nhi_image)           return nh_image       Odef calculate_nh2_error(nhi_image_error=None, av_image_error=None, dgr=1.1e-1):       F    ''' Calculates the total gas column density given N(HI), A_v and a       dust-to-gas ratio.           Parameters       ----------       '''           import numpy as np       :    nh2_image_error = 0.5 * ((av_image_error / dgr)**2 - \   $            nhi_image_error**2)**0.5           return nh2_image_error5�_�                   t        ����                                                                                                                                                                                                                                                                                                                           u         u           V       S�
�    �  s  t           5�_�                       9    ����                                                                                                                                                                                                                                                                                                               t          t         t           V       S�
�    �    !  6      I                filename = 'perseus_hi_vs_h_panels_lee12_reproduce.%s' %\5�_�                   .   4    ����                                                                                                                                                                                                                                                                                                                   ?          ?          9       v   9    S�     �  -  /  6      F                filename='perseus_av_cores_map_lee12_reproduce.%s' % \5�_�                          ����                                                                                                                                                                                                                                                                                                                   ?          ?          9       v   9    S�    �      6      ;                        'lee12_reproduce.%s' % figure_type,5�_�                  4   4    ����                                                                                                                                                                                                                                                                                                               �   &          ?          9       v   9    S�B     �  3  5  6      9    params.add('Z', value=1.0, min=0.1, max=5, vary=True)5�_�                   4   4    ����                                                                                                                                                                                                                                                                                                               �   &          ?          9       v   9    S�B     �  3  5  6      8    params.add('Z', value=1.0, min=0.1, max=5, vary=rue)5�_�                   4   4    ����                                                                                                                                                                                                                                                                                                               �   &          ?          9       v   9    S�C     �  3  5  6      7    params.add('Z', value=1.0, min=0.1, max=5, vary=ue)5�_�                   4   4    ����                                                                                                                                                                                                                                                                                                               �   &          ?          9       v   9    S�C     �  3  5  6      6    params.add('Z', value=1.0, min=0.1, max=5, vary=e)5�_�                   4   4    ����                                                                                                                                                                                                                                                                                                               �   &          ?          9       v   9    S�C    �  3  5  6      5    params.add('Z', value=1.0, min=0.1, max=5, vary=)5�_�                   e       ����                                                                                                                                                                                                                                                                                                               4   8          ?          9       v   9    S�i     �  e  g  6    5�_�                   �   #    ����                                                                                                                                                                                                                                                                                                               4   8      !   ?      !   9       v   9    S�v     �  �  �  7    5�_�                      *    ����                                                                                                                                                                                                                                                                                                               4   8      "   ?      "   9       v   9    S��     �      8      *                p_value_list=p_value_list,5�_�                          ����                                                                                                                                                                                                                                                                                                               4   8                         v       S��     �      9                      5�_�                   �        ����                                                                                                                                                                                                                                                                                                               4   8      �                    V       S��     �  �  �       �   Fdef plot_rh2_vs_h_grid(rh2_images, h_sd_images, rh2_error_images=None,   K        h_sd_error_images=None, rh2_fits = None, h_sd_fits = None, limits =   O        None, fit = True, savedir = './', filename = None, show = True, scale =   ?        'linear', title = '', core_names='', phi_cnm_list=None,   ,        chisq_list=None, p_value_list=None):           # Import external modules       import numpy as np       import math       import pyfits as pf   #    import matplotlib.pyplot as plt       import matplotlib   1    from mpl_toolkits.axes_grid1 import ImageGrid           # Set up plot aesthetics       plt.clf()       plt.rcdefaults()       colormap = plt.cm.gist_ncar   M    #color_cycle = [colormap(i) for i in np.linspace(0, 0.9, len(flux_list))]       fontScale = 12        params = {#'backend': .pdf',   *              'axes.labelsize': fontScale,   *              'axes.titlesize': fontScale,   )              'text.fontsize': fontScale,   /              'legend.fontsize': fontScale*3/4,   +              'xtick.labelsize': fontScale,   +              'ytick.labelsize': fontScale,   !              'font.weight': 500,   &              'axes.labelweight': 500,   #              'text.usetex': False,   )              'figure.figsize': (10, 10),   J              #'axes.color_cycle': color_cycle # colors of different plots                }       plt.rcParams.update(params)           # Create figure instance       fig = plt.figure()       *    n = int(np.ceil(len(rh2_images)**0.5))       '    imagegrid = ImageGrid(fig, (1,1,1),   $                 nrows_ncols=(n, n),   (                 ngrids=len(rh2_images),                    axes_pad=0.25,                    aspect=False,                     label_mode='L',                     share_all=True)           # Cycle through lists   %    for i in xrange(len(rh2_images)):           rh2 = rh2_images[i]           h_sd = h_sd_images[i]   '        rh2_error = rh2_error_images[i]   )        h_sd_error = h_sd_error_images[i]           rh2_fit = rh2_fits[i]           h_sd_fit = h_sd_fits[i]   $        if phi_cnm_list is not None:   %            phi_cnm = phi_cnm_list[i]   "        if chisq_list is not None:   !            chisq = chisq_list[i]   $        if p_value_list is not None:   %            p_value = p_value_list[i]       '        # Drop the NaNs from the images   $        if type(rh2_error) is float:   .            indices = np.where((rh2 == rh2) &\   /                               (h_sd == h_sd)&\   ,                               (h_sd > 0) &\   )                               (rh2 > 0))       -        if type(rh2_error) is np.ndarray or \   >                type(rh2_error) is np.ma.core.MaskedArray or \   3                type(h_sd_error) is np.ndarray or \   ;                type(h_sd_error) is np.ma.core.MaskedArray:   .            indices = np.where((rh2 == rh2) &\   0                               (h_sd == h_sd) &\   <                               (h_sd_error == h_sd_error) &\   :                               (rh2_error == rh2_error) &\   ,                               (h_sd > 0) &\   )                               (rh2 > 0))       !        rh2_nonans = rh2[indices]   #        h_sd_nonans = h_sd[indices]       )        if type(rh2_error) is np.ndarray:   1            rh2_error_nonans = rh2_error[indices]           else:   ;            rh2_error_nonans = np.array(rh2_error[indices])       .        if type(h_sd_error) is np.ndarray or \   ;                type(h_sd_error) is np.ma.core.MaskedArray:   3            h_sd_error_nonans = h_sd_error[indices]           else:   .            h_sd_error_nonans = h_sd_error * \   0                    np.ones(h_sd[indices].shape)                       # Create plot           ax = imagegrid[i]       0        image = ax.errorbar(h_sd_nonans.ravel(),   #                rh2_nonans.ravel(),   1                xerr=(h_sd_error_nonans.ravel()),   0                yerr=(rh2_error_nonans.ravel()),                   alpha=0.5,                   color='k',   7                marker='^',ecolor='k',linestyle='none',                   markersize=4                   )               if rh2_fit is not None:   &            ax.plot(h_sd_fit, rh2_fit,                        color = 'r')       $        if phi_cnm_list is not None:   3            ax.annotate(r'$\phi$ = %.2f' % phi_cnm,   &                    xytext=(0.6, 0.1),   "                    xy=(0.6, 0.1),   /                    textcoords='axes fraction',   -                    xycoords='axes fraction',                       color='k'                       )   "        if chisq_list is not None:   )            conf = (1.0 - p_value) * 100.   2            ax.annotate(r'$\chi^2/\nu$ = %.2f' % \                       chisq,   '                    xytext=(0.48, 0.2),   #                    xy=(0.48, 0.2),   /                    textcoords='axes fraction',   -                    xycoords='axes fraction',                       color='k'                       )       1        ax.set_xscale(scale[0], nonposx = 'clip')   1        ax.set_yscale(scale[1], nonposy = 'clip')               if limits is not None:   ,            ax.set_xlim(limits[0],limits[1])   ,            ax.set_ylim(limits[2],limits[3])               # Adjust asthetics   L        ax.set_xlabel('$\Sigma_{HI}$ + $\Sigma_{H2}$ (M$_\odot$ / pc$^2$)',)   #        ax.set_ylabel(r'R$_{H2}$',)   #        ax.set_title(core_names[i])           ax.grid(True)           if title is not None:   3        fig.suptitle(title, fontsize=fontScale*1.5)       if filename is not None:   ?        plt.savefig(savedir + filename) #, bbox_inches='tight')       if show:           fig.show()5�_�                   �        ����                                                                                                                                                                                                                                                                                                               �   8      �          �          V       S��    �  �  "  �    5�_�                       5    ����                                                                                                                                                                                                                                                                                                               "          "          "          V       S��   	 �      C      9                filename = 'perseus_rh2_vs_hsd_panels' +\5�_�      !                 /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      :                filename = 'perseus_rh2_vs_hsd_panels_' +\5�_�       "           !     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      9                filename = 'perseus_rh2_vs_hsd_anels_' +\5�_�   !   #           "     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      8                filename = 'perseus_rh2_vs_hsd_nels_' +\5�_�   "   $           #     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      7                filename = 'perseus_rh2_vs_hsd_els_' +\5�_�   #   %           $     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      6                filename = 'perseus_rh2_vs_hsd_ls_' +\5�_�   $   &           %     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      5                filename = 'perseus_rh2_vs_hsd_s_' +\5�_�   %   '           &     /    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S��     �      C      4                filename = 'perseus_rh2_vs_hsd__' +\5�_�   &   (           '  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      P                filename = 'perseus_hi_vs_h_panels_lee12_planck_reproduce.%s' %\5�_�   '   )           (  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      O                filename = 'perseus_hi_vs_h_anels_lee12_planck_reproduce.%s' %\5�_�   (   *           )  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      N                filename = 'perseus_hi_vs_h_nels_lee12_planck_reproduce.%s' %\5�_�   )   +           *  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      M                filename = 'perseus_hi_vs_h_els_lee12_planck_reproduce.%s' %\5�_�   *   ,           +  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      L                filename = 'perseus_hi_vs_h_ls_lee12_planck_reproduce.%s' %\5�_�   +   -           ,  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�     �  ,  .  C      K                filename = 'perseus_hi_vs_h_s_lee12_planck_reproduce.%s' %\5�_�   ,               -  -   ,    ����                                                                                                                                                                                                                                                                                                                  5      "          "          V       S�   
 �  ,  .  C      J                filename = 'perseus_hi_vs_h__lee12_planck_reproduce.%s' %\5�_�                  �   &    ����                                                                                                                                                                                                                                                                                                                         �   &      �   &       v   &    S�1     �  �  �  6      9        hi_sd_image_error_sub = hi_sd_mage_error[indices]5�_�                    �        ����                                                                                                                                                                                                                                                                                                                          �          �           v        S�2     �  �  �        5�_�                  �        ����                                                                                                                                                                                                                                                                                                                           �   	      �   	       V   	    SƦ'     �  �  �        5�_�                   �        ����                                                                                                                                                                                                                                                                                                                                                             SƦ(    �  �  �        5�_�                    �        ����                                                                                                                                                                                                                                                                                                               �                                           S��}     �  �  �        Bd                        ef calculate_sd(image, sd_factor=1/1.25):5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             SƦ      �  �  �        3    delta_v = velocity_axis[-1] - velocity_axis[-2]   C    #nhi_image = np.ma.array(image,mask=np.isnan(image)) * 1.823e-2   *    nhi_image = image * 1.823e-2 * delta_v5��