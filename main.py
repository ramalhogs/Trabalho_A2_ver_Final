# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:12:56 2021

@author: eborn
"""

"""
Este módulo contém as funções principais responsáveis pelo funcionamento do jogo.
"""

# Módulos importados
import pygame
import os
import time
import random

# Função que abilita o uso de diferentes fontes do pygame;
pygame.font.init() 

# Função que abilita os efeitos sonoros do pygame;
pygame.mixer.init()

"""
Várias como nome em caixa alta não serão alteradas ao londo do nosso programa.
"""

# Tamanho da tela
WIDTH, HEIGHT = 750, 750

# A variável WIN recebe o display do nosso jogo;
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

# Efeitos Sonoros - Música de fundo;
music = pygame.mixer.music.load('futurama_theme.mp3')

# O parâmento -1 da função play() faz com que a música toque em loop no jogo;
pygame.mixer.music.play(-1)

# Efeitos Sonoros - Som do laser;
# Esse som será usado na nave do jogador;
laser_sound = pygame.mixer.Sound('laser_wrath.wav')

# Volume do som do laser do jogador;
laser_sound.set_volume(0.1)

# Efeitos Sonoros - Larger explosion sound;
# Esse som será usado quando o jogador perder todas as vidas ou saúde;
larger_explosion_sound = pygame.mixer.Sound('larger_explosion.wav')

# Volume do som da explosão "maior" (larger)
larger_explosion_sound.set_volume(0.2)  

# Efeitos Sonoros - Smaller explosion sound
# Esse som será usado quando o jogador sofrer algum dano e perder saúde;
smaller_explosion_sound = pygame.mixer.Sound('smaller_explosion.wav')

# Volume do som da explosão "menor" (smaller)
smaller_explosion_sound.set_volume(0.2) 

# Preparando as fontes que serão usadas
pygame.font.init()