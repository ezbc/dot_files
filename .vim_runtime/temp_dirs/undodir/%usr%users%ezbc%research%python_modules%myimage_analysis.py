Vim�UnDo� �X �Z=��U �<��6��>�T��c	��O_�  6   A                          (velocity_range[1, i] <= velocity_axis)  �   0      +       +   +   +    U'    _�                    $       ����                                                                                                                                                                                                                                                                                                                                                             T�N�     �  #  %  6      1    nh_image = 0.5 * (av_image / dgr - nhi_image)5�_�                   &       ����                                                                                                                                                                                                                                                                                                                                                             T�N�    �  %  '  6          return nh_image5�_�                   �   /    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Ub     �  �  �  6      F            indices = np.where((velocity_axis > velocity_range[0]) & \5�_�                   �   /    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uc     �  �  �  6      F                               (velocity_axis < velocity_range[1]))[0]5�_�                   y   <    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Ug     �  x  z  6      O                        indices = (velocity_range[0, i, j] < velocity_axis) & \5�_�                   z   <    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uh     �  y  {  6      K                                  (velocity_range[1, i, j] > velocity_axis)5�_�                   �   :    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uj     �  �  �  6      M                                (velocity_range[0, i, j] < velocity_axis) & \5�_�      	             �   :    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uj     �  �  �  6      I                                (velocity_range[1, i, j] > velocity_axis)5�_�      
           	  �   /    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uo     �  �  �  6      F            indices = np.where((velocity_axis > velocity_range[0]) & \5�_�   	              
  �   /    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Up     �  �  �  6      F                               (velocity_axis < velocity_range[1]))[0]5�_�   
                �   1    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Uq     �  �  �  6      D                indices = (velocity_range[0, i] < velocity_axis) & \5�_�                   �   1    ����                                                                                                                                                                                                                                                                                                                            5   C      �          v       Ur    �  �  �  6      @                          (velocity_range[1, i] > velocity_axis)5�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �   1       A         �           V        U#:    �  �  �  6      0        nhi_image_error = image_error * 1.823e-25�_�                   �   :    ����                                                                                                                                                                                                                                                                                                               �   9       A         �           V        U$=    �  �  �  6      :        nhi_image_error = image_error * 1.823e-2 * delta_v5�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �   /       A         �           V        U$A    �  �  �  6      0        nhi_image_error = image_error * 1.823e-25�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �   9       x          �   9       v   9    U&     �  �  �  6      E                indices = (velocity_range[0, i] <= velocity_axis) & \5�_�                   �   0    ����                                                                                                                                                                                                                                                                                                               �   9       x          �   9       v   9    U&     �  �  �  6      D                indices = (velocity_range[0, i] = velocity_axis) & \5�_�                   �        ����                                                                                                                                                                                                                                                                                                               �   9      {   @      y           v        U&A     �  �  �  6       5�_�                   �   @    ����                                                                                                                                                                                                                                                                                                               �   9      {   @      y           v        U&D     �  �  �  8    5�_�                   �        ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&V     �  �  �  9      P                        indices = (velocity_range[0, i, j] <= velocity_axis) & \   L                                  (velocity_range[1, i, j] >= velocity_axis)   A                        image[i, j] = np.sum(cube[indices, i, j])5�_�                   �       ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&X     �  �  �  9    5�_�                   �   1    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&`     �  �  �  :      H                indices = (velocity_range[0, i, j] <= velocity_axis) & \5�_�                   �   -    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&a     �  �  �  :      D                          (velocity_range[1, i, j] >= velocity_axis)5�_�                   �   -    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&b     �  �  �  :      C                          (velocity_range[1, , j] >= velocity_axis)5�_�                   �   -    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&b     �  �  �  :      B                          (velocity_range[1,  j] >= velocity_axis)5�_�                   �   -    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&b     �  �  �  :      A                          (velocity_range[1, j] >= velocity_axis)5�_�                   �   -    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&b     �  �  �  :      @                          (velocity_range[1, ] >= velocity_axis)5�_�                   �   4    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&e     �  �  �  :      9                image[i, j] = np.sum(cube[indices, i, j])5�_�                   �   4    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&e     �  �  �  :      8                image[i, j] = np.sum(cube[indices, i j])5�_�                   �   4    ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&e     �  �  �  :      7                image[i, j] = np.sum(cube[indices, ij])5�_�                    �       ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&h     �  �  �  :      6                image[i, j] = np.sum(cube[indices, i])5�_�      !              �       ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&h     �  �  �  :      5                image[i j] = np.sum(cube[indices, i])5�_�       "           !  �       ����                                                                                                                                                                                                                                                                                                               �   9      �         �          V       U&h    �  �  �  :      4                image[ij] = np.sum(cube[indices, i])5�_�   !   #           "  �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       U&�     �  �  �  :      E                indices = (velocity_range[0, i] <= velocity_axis) & \5�_�   "   $           #  �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       U&�     �  �  �  :      D                indices = (velocity_range[0, i] = velocity_axis) & \5�_�   #   %           $  �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       U&�     �  �  �  :      A                          (velocity_range[1, i] >= velocity_axis)5�_�   $   &           %  �   0    ����                                                                                                                                                                                                                                                                                                               �         �         �          V       U&�     �  �  �  :      @                          (velocity_range[1, i] = velocity_axis)5�_�   %   '           &  �        ����                                                                                                                                                                                                                                                                                                               �         �   0      �   0       V   0    U&�     �  �  �          E                indices = (velocity_range[0, i] <= velocity_axis) & \   A                          (velocity_range[1, i] >= velocity_axis)   3                image[i] = np.sum(cube[indices, i])5�_�   &   (           '  �        ����                                                                                                                                                                                                                                                                                                                          �   0      �   0       V   0    U&�    �  �  �           5�_�   '   )           (  �   0    ����                                                                                                                                                                                                                                                                                                               �         �   0      �   0       V   0    U'     �  �  �  6      E                indices = (velocity_range[0, i] >= velocity_axis) & \5�_�   (   *           )  �   0    ����                                                                                                                                                                                                                                                                                                               �         �   0      �   0       V   0    U'     �  �  �  6      D                indices = (velocity_range[0, i] = velocity_axis) & \5�_�   )   +           *  �   0    ����                                                                                                                                                                                                                                                                                                               �         �   0      �   0       V   0    U'     �  �  �  6      A                          (velocity_range[1, i] <= velocity_axis)5�_�   *               +  �   0    ����                                                                                                                                                                                                                                                                                                               �         �   0      �   0       V   0    U'    �  �  �  6      @                          (velocity_range[1, i] = velocity_axis)5��