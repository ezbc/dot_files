VimUnDoå ī9ā;ŹAąźåŖ wHd±\ŲėHĄ¦vhŁĮņ&   ­   ax.legend(loc=1)            :       :   :   :    S±    _Š                     X   ?    ’’’’                                                                                                                                                                                                                                                                                                                O   M                                        S    õ   V   X          (    if not os.path.exists(archive_file):õ   W   Y         ?        print ("- computing bootstrapped luminosity function ",5_Š                    X   ?    ’’’’                                                                                                                                                                                                                                                                                                                X   @                                        S    õ   V   X          (    if not os.path.exists(archive_file):õ   W   Y         A        print ("- computing bootstrapped luminosity function ", \5_Š                    X       ’’’’                                                                                                                                                                                                                                                                                                                X   A                                        S    õ   W   Y         B        print ("- computing bootstrapped luminosity function " + \5_Š                    w       ’’’’                                                                                                                                                                                                                                                                                                                X                                           S	     õ   v   x          fig = plt.figure(figsize=(5, 5))5_Š                    w       ’’’’                                                                                                                                                                                                                                                                                                                X                                           S     õ   u   w          .# Perform the computation and plot the resultsõ   v   x         fig = plt.figure(figsize=(, 5))5_Š                    w       ’’’’                                                                                                                                                                                                                                                                                                                X                                           S     õ   v   x          fig = plt.figure(figsize=(8, 5))5_Š                    w       ’’’’                                                                                                                                                                                                                                                                                                                X                                           S    õ   u   w          .# Perform the computation and plot the resultsõ   v   x         fig = plt.figure(figsize=(8, ))5_Š      	                  (    ’’’’                                                                                                                                                                                                                                                                                                                w                                           S    õ                 -from astroML.plotting import setup_text_plotsõ      !         )setup_text_plots(fontsize=8, usetex=True)5_Š      
           	   2       ’’’’                                                                                                                                                                                                                                                                                                                    (                                        S(    õ   1   3         flag_blue = ~flag_red5_Š   	              
   L       ’’’’                                                                                                                                                                                                                                                                                                                2   *                    -       v   -    S     õ   K   M         7archive_files = ['lumfunc_red.npz', 'lumfunc_blue.npz']5_Š   
                 L   :    ’’’’                                                                                                                                                                                                                                                                                                                2   *                    -       v   -    S    õ   K   M         @archive_files = ['lumfunc_red_freedman.npz', 'lumfunc_blue.npz']5_Š                    O   L    ’’’’                                                                                                                                                                                                                                                                                                                L   B                    -       v   -    S     õ   N   Q         Ndef compute_luminosity_function(z, m, M, m_max, archive_file, Nbootstraps=20):5_Š                    P       ’’’’                                                                                                                                                                                                                                                                                                                L   B                    -       v   -    S      õ   O   Q                 bin_type=''):5_Š                    \       ’’’’                                                                                                                                                                                                                                                                                                                L   B       ]          \          V       S§     õ   [   \          +        zbins = np.linspace(0.08, 0.12, 21)   +        Mbins = np.linspace(-24, -20.2, 21)5_Š                    \        ’’’’                                                                                                                                                                                                                                                                                                                L   B       \          \          V       SØ     õ   [   ]          5_Š                    \       ’’’’                                                                                                                                                                                                                                                                                                                L   B       \          \          V       S¬     õ   [   ]                 if bin_type == ''5_Š                    ]        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ]   !       ^   !       V   !    S±     õ   \   _         9        zbin_width, zbins = free_bin(z, return_bins=True)   9        Mbin_width, Mbins = free_bin(M, return_bins=True)5_Š                    _        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ]   !       ^   !       V   !    S²     õ   ^   b          5_Š                    _        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ]   !       ^   !       V   !    S³     õ   ^   `          5_Š                    _       ’’’’                                                                                                                                                                                                                                                                                                                L   B       ]   !       ^   !       V   !    S·     õ   ^   a                 elif bin_type == ''5_Š                    _       ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       S¼     õ   _   b       5_Š                    `        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       Sæ     õ   _   a          =            zbin_width, zbins = free_bin(z, return_bins=True)5_Š                    `        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       Sæ     õ   _   a          <            zbin_width, zbins = ree_bin(z, return_bins=True)5_Š                    `        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       Sæ     õ   _   a          ;            zbin_width, zbins = ee_bin(z, return_bins=True)5_Š                    `        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       Sæ     õ   _   a          :            zbin_width, zbins = e_bin(z, return_bins=True)5_Š                    `        ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       Sæ     õ   _   a          9            zbin_width, zbins = _bin(z, return_bins=True)5_Š                    a   $    ’’’’                                                                                                                                                                                                                                                                                                                L   B       ^          ]          V       SĮ   	 õ   `   b          =            Mbin_width, Mbins = free_bin(M, return_bins=True)5_Š                    b        ’’’’                                                                                                                                                                                                                                                                                                                a   $       ^          ]          V       SÅ     õ   a   b           5_Š                    b        ’’’’                                                                                                                                                                                                                                                                                                                a   $       ^          ]          V       SĘ   
 õ   a   b           5_Š                    M        ’’’’                                                                                                                                                                                                                                                                                                                b           ^          ]          V       Sč     õ   L   N              5_Š                     M        ’’’’                                                                                                                                                                                                                                                                                                                a           ]          \          V       Sč     õ   L   N             Mdef compute_luminosity_function(z, m, M, m_max, archive_file, Nbootstraps=20,5_Š      !               M        ’’’’                                                                                                                                                                                                                                                                                                                `           \          [          V       Sķ    õ   L   O         Mdef compute_luminosity_function(z, m, M, m_max, archive_file, Nbootstraps=20,5_Š       "           !      D    ’’’’                                                                                                                                                                                                                                                                                                                N           ]          \          V       S     õ                2    zbins, dist_z, err_z, Mbins, dist_M, err_M = \õ               E        compute_luminosity_function(z, m, M, m_max, archive_files[i])5_Š   !   #           "      D    ’’’’                                                                                                                                                                                                                                                                                                                N           ]          \          V       S
     õ                2    zbins, dist_z, err_z, Mbins, dist_M, err_M = \õ               E        compute_luminosity_function(z, m, M, m_max, archive_files[i])5_Š   "   $           #          ’’’’                                                                                                                                                                                                                                                                                                                N           ]          \          V       S     õ                    zbins, dist_z, err_z, Mbins, dā”jedi=0, ist_M, err_M = \ā” (z, m, M, m_max, archive_file, *Nbootstraps = 20*, bin_type = 'freedman') ā”jediā”õ                               bin_type='')5_Š   #   %           $   L        ’’’’                                                                                                                                                                                                                                                                                                                N           L          L          V       S     õ   L   N       5_Š   $   &           %   M   C    ’’’’                                                                                                                                                                                                                                                                                                                O           L          L          V       S     õ   L   N         Iarchive_files = ['lumfunc_red_freedman.npz', 'lumfunc_blue_freedman.npz']5_Š   %   '           &   M   &    ’’’’                                                                                                                                                                                                                                                                                                                O           L          L          V       S    õ   L   N         Farchive_files = ['lumfunc_red_freedman.npz', 'lumfunc_blue_scott.npz']5_Š   &   (           '           ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Sj     õ                5_Š   '   )           (      !    ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Sl     õ         „      !                bin_type='scott')5_Š   (   *           )          ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Sp     õ         ¦      "    ax2 = fig.add_subplot(2, 2, 2)5_Š   )   +           *          ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Sq     õ         ¦      !    ax2 = fig.add_subplot(, 2, 2)5_Š   *   ,           +           ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Ss     õ         ¦      "    ax2 = fig.add_subplot(1, 2, 2)5_Š   +   -           ,           ’’’’                                                                                                                                                                                                                                                                                                                M   "       E          E          v       Ss    õ         ¦      !    ax2 = fig.add_subplot(1, 2, )5_Š   ,   .           -          ’’’’                                                                                                                                                                                                                                                                                                                           E          E          v       Sz     õ         ¦      +    ax = fig.add_subplot(111, yscale='log')5_Š   -   /           .          ’’’’                                                                                                                                                                                                                                                                                                                           E          E          v       Sz     õ         ¦      *    ax = fig.add_subplot(11, yscale='log')5_Š   .   0           /          ’’’’                                                                                                                                                                                                                                                                                                                           E          E          v       S{     õ         ¦      +    ax = fig.add_subplot(121, yscale='log')5_Š   /   1           0          ’’’’                                                                                                                                                                                                                                                                                                                           E          E          v       S{    õ         ¦      *    ax = fig.add_subplot(12, yscale='log')5_Š   0   2           1          ’’’’                                                                                                                                                                                                                                                                                                                   %       E          E          v       S     õ         ¦      +    ax = fig.add_subplot(122, yscale='log')5_Š   1   3           2          ’’’’                                                                                                                                                                                                                                                                                                                   %       E          E          v       S     õ         ¦      >    ax.errorbar(0.5 * (Mbins[1:] + Mbins[:-1]), dist_M, err_M,5_Š   2   4           3          ’’’’                                                                                                                                                                                                                                                                                                                   %                                   S     õ         ¦      axlegend(loc=3)õ      ”   ¦      ax.legend(loc=3)   4ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))   ax.set_xlabel(r'$M$')   ax.set_ylabel(r'$\Phi(M)$')   ax.set_xlim(-20, -23.5)   ax.set_ylim(1E-5, 2)5_Š   3   5           4          ’’’’                                                                                                                                                                                                                                                                                                                   %                                   S     õ         ¦      "    ax2 = fig.add_subplot(1, 2, 1)5_Š   4   6           5          ’’’’                                                                                                                                                                                                                                                                                                                   %                                   S     õ         ¦      !    ax = fig.add_subplot(1, 2, 1)5_Š   5   7           6          ’’’’                                                                                                                                                                                                                                                                                                                   %                                   S     õ         ¦      0    ax2.errorbar(0.5 * (zbins[1:] + zbins[:-1]),5_Š   6   8           7          ’’’’                                                                                                                                                                                                                                                                                                                   %                                   S    õ         ¦      /    ax.errorbar(0.5 * (zbins[1:] + zbins[:-1]),5_Š   7   9           8          ’’’’                                                                                                                                                                                                                                                                                                                                                      S©     õ      ”   ¦      # set labels and limits5_Š   8   :           9          ’’’’                                                                                                                                                                                                                                                                                                                          ”          ¦                 S­     õ         ¬      (# set labels and limitsax2.legend(loc=1)5_Š   9               :          ’’’’                                                                                                                                                                                                                                                                                                                                                      S°    õ         ­      ax.legend(loc=1)õ      ”   ­      ax2.legend(loc=1)   6ax2.xaxis.set_major_locator(plt.MultipleLocator(0.01))   ax2.set_xlabel(r'$z$')   +ax2.set_ylabel(r'$\rho(z) / [z / 0.08]^2$')   ax2.set_xlim(0.075, 0.125)   ax2.set_ylim(10, 25)5ēŖ