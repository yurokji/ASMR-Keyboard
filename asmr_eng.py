# -*- coding: utf-8 -*-
import pyautogui as p
import time
import pygame
import time
import random
import numpy as np
from directkeys import *
import copy

from hangul_utils import split_syllables, join_jamos
lines =[]
with open('meditation.txt', encoding="utf-8") as f:
	lines = f.readlines()
# print(lines)
jamos = []
com_chars = {
 'ㅘ': ['ㅗ', 'ㅏ'],
 'ㅙ': ['ㅗ', 'ㅐ'],
 'ㅚ': ['ㅗ', 'ㅣ'],
 'ㅝ': ['ㅜ', 'ㅓ'],
 'ㅞ': ['ㅜ', 'ㅔ'],
 'ㅟ': ['ㅜ', 'ㅣ'],
 'ㅢ': ['ㅡ', 'ㅣ'],
 'ㄳ': ['ㄱ', 'ㅅ'],
 'ㄵ': ['ㄴ', 'ㅈ'],
 'ㄶ': ['ㄴ', 'ㅎ'],
 'ㄺ': ['ㄹ', 'ㄱ'],
 'ㄻ': ['ㄹ', 'ㅁ'],
 'ㄼ': ['ㄹ', 'ㅂ'],
 'ㄽ': ['ㄹ', 'ㅅ'],
 'ㄾ': ['ㄹ', 'ㅌ'],
 'ㄿ': ['ㄹ', 'ㅍ'],
 'ㅀ': ['ㄹ', 'ㅎ'],
 'ㅄ': ['ㅂ', 'ㅅ']
}

positions = []
for i, line in enumerate(lines):
	for j, x in enumerate(line):
		if x == "]":
			positions.append(len(line) - j -1)
			
proc_lines = []
for line in lines:
	
	jamo = split_syllables(line)
	my_str=""
	for x in jamo:
		if x in com_chars:
			for y in com_chars[x]:	
				my_str += y
		else:
			my_str += x
	proc_lines.append(my_str)

lines = copy.deepcopy(proc_lines)
proc_lines = []
words = []


for i, line in enumerate(lines):
	pline = ""
	is_emph_word = False
	word =""
	for j, x in enumerate(line):
		if x == "[":
			is_emph_word = True
			continue
		elif is_emph_word:
			if x == "]":
				if len(word) > 0:
					words.append([i, j-len(word), word])
				word = ""
				is_emph_word = False
				continue
			else:
				word += x
		else:
			pline += x
	proc_lines.append(pline)
			
print(proc_lines)

clock = pygame.time.Clock()
mu, sigma = 0, 0.1
key_sound = []
enter_sound = []
futuristic_sound = []
input_lines = {}
code_lines = []


def numFrontTabs(line):
	count = 0
	for j, x in enumerate(line):
		if line[j] == '\t':
			count+= 1
		else:
			return count

def playSound(key, duration):
	pygame.mixer.unpause()
	global enter_sound, key_sound
	if key == "\n":            
		sound_num = random.randint(0, 14)
		t= np.random.normal(0.3, 0.1)
		if t < 0.05:
			t = 0.05
		if t > 0.7:
			t = 0.7
		enter_sound[sound_num].set_volume(t)

		
		enter_sound[sound_num].play()
		pygame.mixer.fadeout(100)
	else:
		sound_num = random.randint(0, 43)
		t = np.random.normal(0.5, 0.12)
		if t < 0.1:
			t = 0.1
		if t > 0.85:
			t = 0.85
		key_sound[sound_num].set_volume(t)
		key_sound[sound_num].play()
		pygame.mixer.fadeout(100)

def playFuturisticSound(key):
	pygame.mixer.unpause()
	global futuristic_sound
	sound_num = random.randint(0, 68)
	futuristic_sound[sound_num].set_volume(0.3)
	futuristic_sound[sound_num].play()
	pygame.mixer.fadeout(100)

def pauseSound():
	if pygame.mixer.get_busy():
		pygame.mixer.pause()
	else:
		pygame.mixer.unpause()



pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

for i in range(69):
	futuristicKey_file = "c:/coding/autocoding/matrix_sound/key{:03d}.wav".format(i)
	futuristic_sound.append(pygame.mixer.Sound(futuristicKey_file))

for i in range(44):
	# print(i)
	spaceKey_file = "c:/coding/autocoding/sound/key{:03d}.wav".format(i)
	key_sound.append(pygame.mixer.Sound(spaceKey_file))
	# print(i)

for i in range(15):
	enterKey_file = "c:/coding/autocoding/sound/enter{:03d}.wav".format(i)
	enter_sound.append(pygame.mixer.Sound(enterKey_file))


begin_pos = [2700, 300]
exe_pos = [2485, 40]
del_pos = [2485, 400]
run = True


p.moveTo(begin_pos)
time.sleep(2)
p.click(begin_pos)
time.sleep(2)

sz_lines = len(proc_lines)

print("lines: ", sz_lines)
lnum = 0
mu, sigma = 0.003, 0.002

kor = False
for i  in range(sz_lines):
	for j, key in enumerate(proc_lines[i]):
		if kor and j == 0:
			continue
		t = np.random.normal(mu, sigma)
		if t < 0.003:
			t = 0.003

		playSound(key, t * 1000)
		typeKey(VKEYS[key], interval=t, randomized=True)
		rand_pause = random.randint(0, 100)
		if rand_pause > 97:
			time.sleep(random.randint(1,2)*0.2)