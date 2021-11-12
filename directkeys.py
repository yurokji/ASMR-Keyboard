# direct inputs
# modified by Yurok Ji yurokji@gmail.com
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

from hangul_jamo import *
import ctypes
import time
import random
SendInput = ctypes.windll.user32.SendInput
DIK_ESCAPE =      0x01
DIK_1 =           0x02
DIK_2 =           0x03
DIK_3 =           0x04
DIK_4 =           0x05
DIK_5 =           0x06
DIK_6 =           0x07
DIK_7 =           0x08
DIK_8 =           0x09
DIK_9 =           0x0A
DIK_0 =           0x0B
DIK_MINUS =       0x0C   
DIK_EQUALS =      0x0D
DIK_BACK =        0x0E    
DIK_TAB =         0x0F
DIK_Q =           0x10
DIK_W =           0x11
DIK_E =           0x12
DIK_R =           0x13
DIK_T =           0x14
DIK_Y =           0x15
DIK_U =           0x16
DIK_I =           0x17
DIK_O =           0x18
DIK_P =           0x19
DIK_LBRACKET =    0x1A
DIK_RBRACKET =    0x1B
DIK_RETURN =      0x1C    
DIK_LCONTROL =    0x1D
DIK_A =           0x1E
DIK_S =           0x1F
DIK_D =           0x20
DIK_F =           0x21
DIK_G =           0x22
DIK_H =           0x23
DIK_J =           0x24
DIK_K =           0x25
DIK_L =           0x26
DIK_SEMICOLON =   0x27
DIK_APOSTROPHE =  0x28
DIK_GRAVE =       0x29    
DIK_LSHIFT =      0x2A
DIK_BACKSLASH =   0x2B
DIK_Z =           0x2C
DIK_X =           0x2D
DIK_C =           0x2E
DIK_V =           0x2F
DIK_B =           0x30
DIK_N =           0x31
DIK_M =           0x32
DIK_COMMA =       0x33
DIK_PERIOD =      0x34    
DIK_SLASH =       0x35    
DIK_RSHIFT =      0x36
DIK_MULTIPLY =    0x37    
DIK_LMENU =       0x38    
DIK_SPACE =       0x39
DIK_CAPITAL =     0x3A
DIK_F1 =          0x3B
DIK_F2 =          0x3C
DIK_F3 =          0x3D
DIK_F4 =          0x3E
DIK_F5 =          0x3F
DIK_F6 =          0x40
DIK_F7 =          0x41
DIK_F8 =          0x42
DIK_F9 =          0x43
DIK_F10 =         0x44
DIK_NUMLOCK =     0x45
DIK_SCROLL =      0x46    
DIK_NUMPAD7 =     0x47
DIK_NUMPAD8 =     0x48
DIK_NUMPAD9 =     0x49
DIK_SUBTRACT =    0x4A    
DIK_NUMPAD4 =     0x4B
DIK_NUMPAD5 =     0x4C
DIK_NUMPAD6 =     0x4D
DIK_ADD =         0x4E    
DIK_NUMPAD1 =     0x4F
DIK_NUMPAD2 =     0x50
DIK_NUMPAD3 =     0x51
DIK_NUMPAD0 =     0x52
DIK_DECIMAL =     0x53    
DIK_OEM_102 =     0x56    
DIK_F11 =         0x57
DIK_F12 =         0x58
DIK_F13 =         0x64    
DIK_F14 =         0x65    
DIK_F15 =         0x66    
DIK_KANA =        0x70    
DIK_ABNT_C1 =     0x73    
DIK_CONVERT =     0x79    
DIK_NOCONVERT =   0x7B    
DIK_YEN =         0x7D    
DIK_ABNT_C2 =     0x7E    
DIK_NUMPADEQUALS =  0x8D    
DIK_PREVTRACK =   0x90    
DIK_AT =          0x91    
DIK_COLON =       0x92    
DIK_UNDERLINE =   0x93    
DIK_KANJI =       0x94    
DIK_STOP =        0x95    
DIK_AX =          0x96    
DIK_UNLABELED =   0x97    
DIK_NEXTTRACK =   0x99    
DIK_NUMPADENTER =  0x9C    
DIK_RCONTROL =    0x9D
DIK_MUTE =        0xA0    
DIK_CALCULATOR =  0xA1    
DIK_PLAYPAUSE =   0xA2    
DIK_MEDIASTOP =   0xA4    
DIK_VOLUMEDOWN =  0xAE    
DIK_VOLUMEUP =    0xB0    
DIK_WEBHOME =     0xB2    
DIK_NUMPADCOMMA =  0xB3    
DIK_DIVIDE =      0xB5    
DIK_SYSRQ =       0xB7
DIK_RMENU =       0xB8    
DIK_PAUSE =       0xC5    
DIK_HOME =        0xC7    
DIK_UP =          0xC8    
DIK_PRIOR =       0xC9    
DIK_LEFT =        0xCB    
DIK_RIGHT =       0xCD    
DIK_END =         0xCF    
DIK_DOWN =        0xD0    
DIK_NEXT =        0xD1   
DIK_INSERT =      0xD2   
DIK_DELETE =      0xD3   
DIK_LWIN =        0xDB   
DIK_RWIN =        0xDC   
DIK_APPS =        0xDD    
DIK_POWER =       0xDE    
DIK_SLEEP =       0xDF    
DIK_WAKE =        0xE3    
DIK_WEBSEARCH =   0xE5    
DIK_WEBFAVORITES =  0xE6    
DIK_WEBREFRESH =  0xE7    
DIK_WEBSTOP =     0xE8    
DIK_WEBFORWARD =  0xE9    
DIK_WEBBACK =     0xEA    
DIK_MYCOMPUTER =  0xEB    
DIK_MAIL =        0xEC    
DIK_MEDIASELECT =  0xED    


VKEYS = {}
VKEYS['esc'] = [DIK_ESCAPE ]

VKEYS['`'] = [DIK_GRAVE ] 
VKEYS['1'] = [DIK_1 ]
VKEYS['2'] = [DIK_2 ]
VKEYS['3'] = [DIK_3 ]
VKEYS['4'] = [DIK_4 ]
VKEYS['5'] = [DIK_5 ]
VKEYS['6'] = [DIK_6 ]
VKEYS['7'] = [DIK_7 ]
VKEYS['8'] = [DIK_8 ]
VKEYS['9'] = [DIK_9 ]
VKEYS['0'] = [DIK_0 ]
VKEYS['-'] = [DIK_MINUS ]   
VKEYS['='] = [DIK_EQUALS ]


VKEYS['~'] = [DIK_LSHIFT, DIK_GRAVE ] 
VKEYS['!'] = [DIK_LSHIFT, DIK_1 ]
VKEYS['@'] = [DIK_LSHIFT, DIK_2 ]
VKEYS['#'] = [DIK_LSHIFT, DIK_3 ]
VKEYS['$'] = [DIK_LSHIFT, DIK_4 ]
VKEYS['%'] = [DIK_LSHIFT, DIK_5 ]
VKEYS['^'] = [DIK_LSHIFT, DIK_6 ]
VKEYS['&'] = [DIK_LSHIFT, DIK_7 ]
VKEYS['*'] = [DIK_LSHIFT, DIK_8 ]
VKEYS['('] = [DIK_LSHIFT, DIK_9 ]
VKEYS[')'] = [DIK_LSHIFT, DIK_0 ]
VKEYS['_'] = [DIK_LSHIFT, DIK_MINUS ]   
VKEYS['+'] = [DIK_LSHIFT, DIK_EQUALS ]

VKEYS['a'] = [DIK_A ]
VKEYS['b'] = [DIK_B ]
VKEYS['c'] = [DIK_C ]
VKEYS['d'] = [DIK_D ]
VKEYS['e'] = [DIK_E ]
VKEYS['f'] = [DIK_F ]
VKEYS['g'] = [DIK_G ]
VKEYS['h'] = [DIK_H ]
VKEYS['i'] = [DIK_I ]
VKEYS['j'] = [DIK_J ]
VKEYS['k'] = [DIK_K ]
VKEYS['l'] = [DIK_L ]
VKEYS['m'] = [DIK_M ]
VKEYS['n'] = [DIK_N ]
VKEYS['o'] = [DIK_O ]
VKEYS['p'] = [DIK_P ]
VKEYS['q'] = [DIK_Q ]
VKEYS['r'] = [DIK_R ]
VKEYS['s'] = [DIK_S ]
VKEYS['t'] = [DIK_T ]
VKEYS['u'] = [DIK_U ]
VKEYS['v'] = [DIK_V ]
VKEYS['w'] = [DIK_W ]
VKEYS['x'] = [DIK_X ]
VKEYS['y'] = [DIK_Y ]
VKEYS['z'] = [DIK_Z ]

VKEYS['A'] = [DIK_LSHIFT, DIK_A ]
VKEYS['B'] = [DIK_LSHIFT, DIK_B ]
VKEYS['C'] = [DIK_LSHIFT, DIK_C ]
VKEYS['D'] = [DIK_LSHIFT, DIK_D ]
VKEYS['E'] = [DIK_LSHIFT, DIK_E ]
VKEYS['F'] = [DIK_LSHIFT, DIK_F ]
VKEYS['G'] = [DIK_LSHIFT, DIK_G ]
VKEYS['H'] = [DIK_LSHIFT, DIK_H ]
VKEYS['I'] = [DIK_LSHIFT, DIK_I ]
VKEYS['J'] = [DIK_LSHIFT, DIK_J ]
VKEYS['K'] = [DIK_LSHIFT, DIK_K ]
VKEYS['L'] = [DIK_LSHIFT, DIK_L ]
VKEYS['M'] = [DIK_LSHIFT, DIK_M ]
VKEYS['N'] = [DIK_LSHIFT, DIK_N ]
VKEYS['O'] = [DIK_LSHIFT, DIK_O ]
VKEYS['P'] = [DIK_LSHIFT, DIK_P ]
VKEYS['Q'] = [DIK_LSHIFT, DIK_Q ]
VKEYS['R'] = [DIK_LSHIFT, DIK_R ]
VKEYS['S'] = [DIK_LSHIFT, DIK_S ]
VKEYS['T'] = [DIK_LSHIFT, DIK_T ]
VKEYS['U'] = [DIK_LSHIFT, DIK_U ]
VKEYS['V'] = [DIK_LSHIFT, DIK_V ]
VKEYS['W'] = [DIK_LSHIFT, DIK_W ]
VKEYS['X'] = [DIK_LSHIFT, DIK_X ]
VKEYS['Y'] = [DIK_LSHIFT, DIK_Y ]
VKEYS['Z'] = [DIK_LSHIFT, DIK_Z ]


VKEYS['\\'] = [DIK_BACKSLASH ]
VKEYS['|'] = [DIK_LSHIFT, DIK_BACKSLASH ]
VKEYS['['] = [DIK_LBRACKET ]
VKEYS[']'] = [DIK_RBRACKET ]
VKEYS['{'] = [DIK_LSHIFT, DIK_LBRACKET ]
VKEYS['}'] = [DIK_LSHIFT, DIK_RBRACKET ]
VKEYS[';'] = [DIK_SEMICOLON ]
VKEYS['\''] = [DIK_APOSTROPHE ]
VKEYS[':'] = [DIK_LSHIFT, DIK_SEMICOLON ]
VKEYS['\"'] = [DIK_LSHIFT, DIK_APOSTROPHE ]
VKEYS[','] = [DIK_COMMA ]
VKEYS['.'] = [DIK_PERIOD ]    
VKEYS['/'] = [DIK_SLASH ]   
VKEYS['<'] = [DIK_LSHIFT, DIK_COMMA ]
VKEYS['>'] = [DIK_LSHIFT, DIK_PERIOD ]    
VKEYS['?'] = [DIK_LSHIFT, DIK_SLASH ]   

VKEYS[' '] = [DIK_SPACE ]
VKEYS['\n'] = [DIK_RETURN ] 
VKEYS['\t'] = [DIK_TAB ]
VKEYS['\b'] = [DIK_BACK ] 



VKEYS['lctrl'] = [DIK_LCONTROL ]
VKEYS['lshift'] = [DIK_LSHIFT ]
VKEYS['rshift'] = [DIK_RSHIFT ]
VKEYS['lmenu'] = [DIK_LMENU ]    
VKEYS['cap'] = [DIK_CAPITAL ]
VKEYS['numlck'] = [DIK_NUMLOCK ]
VKEYS['scrl'] = [DIK_SCROLL ]    
VKEYS['rctrl'] = [DIK_RCONTROL ]

VKEYS['ins'] = [DIK_INSERT ]   
VKEYS['home'] = [DIK_LSHIFT, DIK_HOME ]  
VKEYS['pgup'] = [DIK_LSHIFT, DIK_PRIOR ]  
VKEYS['del'] = [DIK_DELETE ]  
VKEYS['end'] = [DIK_LSHIFT, DIK_END ]    
VKEYS['pgdn'] = [DIK_LSHIFT, DIK_NEXT ]  

VKEYS['up'] = [DIK_LSHIFT, DIK_UP ]
VKEYS['left'] = [DIK_LSHIFT, DIK_LEFT ]    
VKEYS['right'] = [DIK_LSHIFT, DIK_RIGHT ]    
VKEYS['down'] = [DIK_LSHIFT, DIK_DOWN ] 



VKEYS['f1'] = [DIK_F1 ]
VKEYS['f2'] = [DIK_F2 ]
VKEYS['f3'] = [DIK_F3 ]
VKEYS['f4'] = [DIK_F4 ]
VKEYS['f5'] = [DIK_F5 ]
VKEYS['f6'] = [DIK_F6 ]
VKEYS['f7'] = [DIK_F7 ]
VKEYS['f8'] = [DIK_F8 ]
VKEYS['f9'] = [DIK_F9 ]
VKEYS['f10'] = [DIK_F10 ]
VKEYS['f11'] = [DIK_F11 ]
VKEYS['f12'] = [DIK_F12 ]
VKEYS['f13'] = [DIK_F13 ]    
VKEYS['f14'] = [DIK_F14 ]    
VKEYS['f15'] = [DIK_F15 ]    



VKEYS['n_1'] = [DIK_NUMPAD1 ]
VKEYS['n_2'] = [DIK_NUMPAD2 ]
VKEYS['n_3'] = [DIK_NUMPAD3 ]
VKEYS['n4'] = [DIK_NUMPAD4 ]
VKEYS['n5'] = [DIK_NUMPAD5 ]
VKEYS['n6'] = [DIK_NUMPAD6 ]
VKEYS['n_7'] = [DIK_NUMPAD7 ]
VKEYS['n_8'] = [DIK_NUMPAD8 ]
VKEYS['n_9'] = [DIK_NUMPAD9 ]
VKEYS['n_0'] = [DIK_NUMPAD0 ]
VKEYS['n_eq'] = [DIK_NUMPADEQUALS ]  
VKEYS['n_ent'] = [DIK_NUMPADENTER ]    

VKEYS['dcm'] = [DIK_DECIMAL ]    
VKEYS['oem102'] = [DIK_OEM_102 ]    
VKEYS['kana'] = [DIK_KANA ]    
VKEYS['abc1'] = [DIK_ABNT_C1 ]    
VKEYS['conv'] = [DIK_CONVERT ]    
VKEYS['nconv'] = [DIK_NOCONVERT ]    
VKEYS['yen'] = [DIK_YEN ]    
VKEYS['abc2'] = [DIK_ABNT_C2 ]    
VKEYS['prev_track'] = [DIK_PREVTRACK ]    
VKEYS['at'] = [DIK_AT ]    
VKEYS['kanji'] = [DIK_KANJI ]    
VKEYS['stop'] = [DIK_STOP ]    
VKEYS['ax'] = [DIK_AX ]    
VKEYS['unlabeled'] = [DIK_UNLABELED ]    
VKEYS['next_track'] = [DIK_NEXTTRACK ]    
VKEYS['mute'] = [DIK_MUTE ]    
VKEYS['calc'] = [DIK_CALCULATOR ]    
VKEYS['playpause'] = [DIK_PLAYPAUSE ]    
VKEYS['media_stop'] = [DIK_MEDIASTOP ]    
VKEYS['vol_down'] = [DIK_VOLUMEDOWN ]    
VKEYS['vol_up'] = [DIK_VOLUMEUP ]    
VKEYS['web_home'] = [DIK_WEBHOME ]    
VKEYS['n_comma'] = [DIK_NUMPADCOMMA ]    
VKEYS['div'] = [DIK_DIVIDE ]    
VKEYS['sysrq'] = [DIK_SYSRQ ]
VKEYS['rmenu'] = [DIK_RMENU ]    
VKEYS['pause'] = [DIK_PAUSE ]    
VKEYS['kor_eng'] = [ DIK_LSHIFT, DIK_SPACE]   
  
 
VKEYS['lwin'] = [DIK_LWIN ]   
VKEYS['rwin'] = [DIK_RWIN ]   
VKEYS['apps'] = [DIK_APPS ]    
VKEYS['power'] = [DIK_POWER ]    
VKEYS['sleep'] = [DIK_SLEEP ]    
VKEYS['wake'] = [DIK_WAKE ]    
VKEYS['web_search'] = [DIK_WEBSEARCH ]    
VKEYS['web_favorite'] = [DIK_WEBFAVORITES ]    
VKEYS['web_refresh'] = [DIK_WEBREFRESH ]    
VKEYS['web_stop'] = [DIK_WEBSTOP ]    
VKEYS['web_forward'] = [DIK_WEBFORWARD ]    
VKEYS['web_back'] = [DIK_WEBBACK ]    
VKEYS['web_mycom'] = [DIK_MYCOMPUTER ]    
VKEYS['mail'] = [DIK_MAIL ]    
VKEYS['media_sel'] = [DIK_MEDIASELECT ]    


VKEYS[''] = [DIK_LSHIFT, DIK_A ]



# c struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
				("wScan", ctypes.c_ushort),
				("dwFlags", ctypes.c_ulong),
				("time", ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
				("wParamL", ctypes.c_short),
				("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
				("dy", ctypes.c_long),
				("mouseData", ctypes.c_ulong),
				("dwFlags", ctypes.c_ulong),
				("time",ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
				 ("mi", MouseInput),
				 ("hi", HardwareInput)]

class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
				("ii", Input_I)]

def typeKey(codeList, repeat=1, interval=0.02, randomized=False):
	pauseTime = 0
	print(codeList)
	if randomized:
		interval = interval + interval * random.random()
	for i in range(repeat):
		PressCombKey(codeList, interval)	
		ReleaseCombKey(codeList, interval) 

# Actuals Functions
def PressCombKey(codeList, interval):
	for code in codeList:
		PressKey(code)
		time.sleep(interval)

def ReleaseCombKey(codeList, interval):
	for code in reversed(codeList):
		ReleaseKey(code)
		time.sleep(interval)


def PressKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
	PressKey(0x11)
	time.sleep(1)
	ReleaseKey(0x11)
	time.sleep(1)