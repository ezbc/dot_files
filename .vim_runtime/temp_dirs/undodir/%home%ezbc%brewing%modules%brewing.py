VimUnDoå K<Ž©źj­\¾čfŹT~7Ļ@šø-y   ø                 D       D   D   D    SĻ!E    _Š                     Z        ’’’’                                                                                                                                                                                                                                                                                                                                                            SĻI     õ   Y   ]          5_Š                    Z        ’’’’                                                                                                                                                                                                                                                                                                                                                            SĻN     õ   Z          õ   Z   [       5_Š                    [        ’’’’                                                                                                                                                                                                                                                                                                                           [                     V       SĻi     õ   Z   [       &   Adef calc_hop_bill(target_IBU=30., volume=5.5, gravity_boil=1.050,   6        boil_time=60.0, alpha_acid=0.06, pellet=True):           '''       volume in gallons   *    gravity_boil in specific gravity units       boil_time in minutes       alpha_acid as a fraction       +    returns the weight of the hop in ounces       '''       C    # Correction of high gravity worts which change the utilization       if gravity_boil > 1.050:   ?        gravity_correction = 1 + ((gravity_boil - 1.050) / 0.2)   	    else:            gravity_correction = 1.0           # Get utilization value   F    boil_data = np.array([0.0, 4.5, 14.5, 24.5, 37.0, 52.0, 67.0, 75])   9    util_whole = np.array([0, 5, 12, 15, 19, 22, 24, 27])   :    util_pellet = np.array([0, 6, 15, 19, 24, 27, 30, 34])           if pellet:           util_data = util_pellet   	    else:           util_data = util_whole       <    utilization = np.interp(boil_time, boil_data, util_data)           if utilization == 0.0:           return np.NaN           # page 81, hops in ounces   =    hop_weight = volume * gravity_correction * target_IBU / \   3                 (utilization * alpha_acid * 7489.)           return hop_weight5_Š                    ?        ’’’’                                                                                                                                                                                                                                                                                                                           [           [          V       SĻj     õ   >   B          5_Š                    @        ’’’’                                                                                                                                                                                                                                                                                                                           ]           ]          V       SĻk     õ   @   g       õ   @   A       5_Š                    ?        ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻl     õ   >   ?           5_Š                            ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻn     õ                 5_Š      	                      ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻo    õ                 5_Š      
           	           ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻ     õ                 5_Š   	              
   v       ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻĖ     õ   t   v   ³      ?    ax.text(0.5, 0.5, 'Target IBU = {:.1f}'.format(target_IBU),   )õ   u   w   ³                  )5_Š   
                        ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻ§     õ         ²      def update(e):5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                                                V       SĻ¬     õ         ²          return None5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                                      t           v   $    SĻÖ     õ         ²          ax.5_Š                    ­        ’’’’                                                                                                                                                                                                                                                                                                                                      t           v   $    SĻŚ     õ   ¬   ®   ²       5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                                      t           v   $    SĻŻ    õ         ²          IBU5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                                     t           v   $    SĻ*    õ         ²          IBU_text.val5_Š                    |       ’’’’                                                                                                                                                                                                                                                                                                                                     t           v   $    SĻ3    õ   {   }   ²          update.IBU_text = IBU_text5_Š                    |       ’’’’                                                                                                                                                                                                                                                                                                                |   
                  t           v   $    SĻ;    õ   {   }   ²      %    global update.IBU_text = IBU_text5_Š                    x        ’’’’                                                                                                                                                                                                                                                                                                                |                     t           v   $    SĻ\    õ   w   z   ²       5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                y                     t           v   $    SĻ    õ         ³          IBU_text = IBU_text.val5_Š                       
    ’’’’                                                                                                                                                                                                                                                                                                                   	                  t           v   $    SĻ    õ         “      
    draw()5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                                     t           v   $    SĻ^   	 õ         “          IBU_text = IBU_text.val5_Š                       B    ’’’’                                                                                                                                                                                                                                                                                                                                     t           v   $    SĻ   
 õ         “      B    ax = fig.add_axes([0.25, add_new_slider.count*0.1, 0.5, 0.05])5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                          z   !       z   J       v   J    SĻ“     õ         µ          IBU_text.set_text(s.val)õ         µ    5_Š                       @    ’’’’                                                                                                                                                                                                                                                                                                                          z   !       z   J       v   J    SĻµ     õ         µ      F    IBU_text.set_text('Current IBU = {:.1f}'.format(current_IBU)s.val)5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                             ?                 v       SĻĮ     õ         µ      E    IBU_text.set_text('Current IBU = {:.1f}'.format(current_IBU).val)5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                             ?                 v       SĻĀ     õ         µ          IBU_text.set_text(.val)5_Š                           ’’’’                                                                                                                                                                                                                                                                                                                             ?                 v       SĻĻ     õ         µ          IBU_text.set_text(s.val)õ         µ    5_Š                       @    ’’’’                                                                                                                                                                                                                                                                                                                             ?                 v       SĻŅ     õ         µ      F    IBU_text.set_text('Current IBU = {:.1f}'.format(current_IBU)s.val)5_Š                       :    ’’’’                                                                                                                                                                                                                                                                                                                             ?                 v       SĻÕ    õ         µ      :    IBU_text.set_text('Current IBU = {:.1f}'.format(s.val)5_Š                            ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻ     õ         µ          global s5_Š      #                      ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻ     õ         ¶          #global s    õ         ¶          õ         µ    5_Š       $   !       #   o       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻŗ     õ   n   p   µ      F    sliders = [add_new_slider(fig, hops, hop, update) for hop in hops]5_Š   #   %           $   y       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻĢ     õ   x   z   µ          global IBU_text5_Š   $   '           %   z       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻĪ     õ   y   {   µ      L    IBU_text = ax.text(0.5, 0.1, 'Current IBU = {:.1f}'.format(current_IBU),5_Š   %   (   &       '   y       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻŌ     õ   x   {   µ          #global IBU_text5_Š   '   )           (   {       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻÕ    õ   z   ~   ¶      S    update.IBU_text = ax.text(0.5, 0.1, 'Current IBU = {:.1f}'.format(current_IBU),                          )    5_Š   (   *           )   |       ’’’’                                                                                                                                                                                                                                                                                                                {                              V       SĻŁ     õ   z   |   ¶      6    update.IBU_text = ax.text(0.5, 0.1, 'Current IBU =   {:.1f}'.format(current_IBU),)õ   {   }   ¶      )            {:.1f}'.format(current_IBU),)5_Š   )   +           *   {   ?    ’’’’                                                                                                                                                                                                                                                                                                                {                              V       SĻŽ     õ   z   |   µ      T    update.IBU_text = ax.text(0.5, 0.1, 'Current IBU = {:.1f}'.format(current_IBU),)5_Š   *   ,           +   {   7    ’’’’                                                                                                                                                                                                                                                                                                                {                              V       SĻć    õ   z   }   µ      T    update.IBU_text = ax.text(0.5, 0.1, 'Current IBU = {:.1f}' format(current_IBU),)5_Š   +   -           ,   |   (    ’’’’                                                                                                                                                                                                                                                                                                                |                              V       SĻė    õ   {   }   ¶      *            '{:.1f}' format(current_IBU),)5_Š   ,   .           -   }        ’’’’                                                                                                                                                                                                                                                                                                                |   (       ~          }           V   (    SĻł    õ   |   }                  update.IBU_text = IBU_text5_Š   -   /           .   |       ’’’’                                                                                                                                                                                                                                                                                                                }           }          }           V   (    SĻ      õ   {   }   “      )            '{:.1f}' format(current_IBU))5_Š   .   0           /   |       ’’’’                                                                                                                                                                                                                                                                                                                }           }          }           V   (    SĻ 	    õ   {   }   “      (            '{:.1f}'format(current_IBU))5_Š   /   1           0          ’’’’                                                                                                                                                                                                                                                                                                                |          }          }           V   (    SĻ !    õ         “      ;    IBU_text.set_text('Current IBU = {:.1f}'.format(s.val))5_Š   0   2           1      ;    ’’’’                                                                                                                                                                                                                                                                                                                   
       }          }           V   (    SĻ )    õ         “      B    update.IBU_text.set_text('Current IBU = {:.1f}'.format(s.val))5_Š   1   3           2      C    ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ E     õ         “      I    update.IBU_text.set_text('Current IBU = {:.1f}'.format(update.s.val))5_Š   2   4           3      I    ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ P     õ         “      O    update.IBU_text.set_text('Current IBU = {:.1f}'.format(update.sliders.val))5_Š   3   5           4          ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ f     õ         “      def update(val):5_Š   4   6           5           ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ g     õ         ¶       5_Š   5   7           6          ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ ~     õ         ¶          5_Š   6   8           7           ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ      õ         ¶      !    IBU = get_IBU(update.sliders)5_Š   7   9           8           ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ      õ         ¶      !    IBU = get_IBU(update.sliders)5_Š   8   :           9      
    ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ      õ         ¶      !    IBU = get_IBU(update.sliders)5_Š   9   ;           :      "    ’’’’                                                                                                                                                                                                                                                                                                                   A       }          }           V   (    SĻ      õ         ¶      "    IBU = [get_IBU(update.sliders)5_Š   :   <           ;          ’’’’                                                                                                                                                                                                                                                                                                                   A                            v        SĻ ö     õ         ¶      #    IBU = [get_IBU(update.sliders) 5_Š   ;   =           <          ’’’’                                                                                                                                                                                                                                                                                                                   A                            v        SĻ ÷     õ         ¶          IBU = [get_IBU(update.) 5_Š   <   >           =          ’’’’                                                                                                                                                                                                                                                                                                                   A                            v        SĻ!     õ         ¶           IBU = [get_IBU(update.hops) 5_Š   =   ?           >           ’’’’                                                                                                                                                                                                                                                                                                                   A                            v        SĻ!     õ         ¶      !    IBU = [get_IBU(update.hops)  5_Š   >   @           ?      
    ’’’’                                                                                                                                                                                                                                                                                                                   A                            v        SĻ!     õ         ¶           IBU = [get_IBU(update.hops) 5_Š   ?   A           @           ’’’’                                                                                                                                                                                                                                                                                                                   
                            v        SĻ!	    õ                    IBU = get_IBU(update.hops) 5_Š   @   B           A      
    ’’’’                                                                                                                                                                                                                                                                                                                   
                            v        SĻ!     õ         ·          õ         ¶    5_Š   A   C           B          ’’’’                                                                                                                                                                                                                                                                                                                   
                           v       SĻ!@     õ         ø          for hop in hops:5_Š   B   D           C          ’’’’                                                                                                                                                                                                                                                                                                                   
                           v       SĻ!A     õ         ø      	    for :5_Š   C               D           ’’’’                                                                                                                                                                                                                                                                                                                   
                           v       SĻ!D    õ         ø       5_Š   %           '   &   z       ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻŅ     õ   x   }   µ      G    #global IBU_text update.IBU_text = ax.text(0.5, 0.1, 'Current IBU =   !    {:.1f}'.format(current_IBU),)    5_Š       "       #   !          ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻ     õ         µ      P    update.s = Slider(ax, hop_name, 0.0, 10.0, valinit=hops[hop_name]['weight'])5_Š   !               "          ’’’’                                                                                                                                                                                                                                                                                                                   :                           V       SĻ     õ         µ          update.s.on_changed(update)5ēŖ