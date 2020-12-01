import pygame
import random

#TILES
PRETO = 0
MAPA_01 = 1
MAPA_02 = 2
MAPA_03 = 3
MAPA_04 = 4
MAPA_05 = 5
MAPA_06 = 6
MAPA_07 = 7
MAPA_08 = 8
MAPA_09 = 9
MAPA_10 = 10
MAPA_11 = 11
MAPA_12 = 12
MAPA_13 = 13
MAPA_14 = 14
MAPA_15 = 15
MAPA_16 = 16
MAPA_17 = 17
MAPA_18 = 18
MAPA_19 = 19
MAPA_20 = 20
MAPA_21 = 21
MAPA_22 = 22
MAPA_23 = 23
MAPA_24 = 24
MAPA_25 = 25
MAPA_26 = 26
MAPA_27 = 27
MAPA_28 = 28
MAPA_29 = 29
MAPA_30 = 30
MAPA_31 = 31
MAPA_32 = 32
MAPA_33 = 33
MAPA_34 = 34
MAPA_35 = 35
MAPA_36 = 36
MAPA_37 = 37
MAPA_38 = 38
MAPA_39 = 39
MAPA_40 = 40
MAPA_41 = 41
MAPA_42 = 42
MAPA_43 = 43
MAPA_44 = 44
MAPA_45 = 45
MAPA_46 = 46
MAPA_47 = 47
MAPA_48 = 48
MAPA_49 = 49
MAPA_50 = 50
MAPA_51 = 51
MAPA_52 = 52
MAPA_53 = 53
MAPA_54 = 54
MAPA_55 = 55
MAPA_56 = 56
MAPA_57 = 57
MAPA_58 = 58
MAPA_59 = 59
MAPA_60 = 60
MAPA_61 = 61
MAPA_62 = 62
MAPA_63 = 63
MAPA_64 = 64
MAPA_65 = 65
MAPA_66 = 66
MAPA_67 = 67
MAPA_68 = 68
MAPA_69 = 69
MAPA_70 = 70
MAPA_71 = 71
MAPA_72 = 72
MAPA_73 = 73
MAPA_74 = 74
MAPA_75 = 75
MAPA_76 = 76
MAPA_77 = 77
MAPA_78 = 78
MAPA_79 = 79
MAPA_80 = 80
MAPA_81 = 81
MAPA_82 = 82
MAPA_83 = 83
MAPA_84 = 84
MAPA_85 = 85
MAPA_86 = 86
MAPA_87 = 87
MAPA_88 = 88
MAPA_89 = 89
MAPA_90 = 90
MAPA_91 = 91
MAPA_92 = 92
MAPA_93 = 93
MAPA_94 = 94
MAPA_95 = 95
MAPA_96 = 96
MAPA_97 = 97
MAPA_98 = 98
MAPA_99 = 99
MAPA_100 = 100
MAPA_101 = 101
MAPA_102 = 102
MAPA_103 = 103
MAPA_104 = 104
MAPA_105 = 105
MAPA_106 = 106
MAPA_107 = 107
MAPA_108 = 108
MAPA_109 = 109
MAPA_110 = 110
MAPA_111 = 111
MAPA_112 = 112
MAPA_113 = 113
MAPA_114 = 114
MAPA_115 = 115
MAPA_116 = 116
MAPA_117 = 117
MAPA_118 = 118
MAPA_119 = 119
MAPA_120 = 120
MAPA_121 = 121
MAPA_122 = 122
MAPA_123 = 123
MAPA_124 = 124
MAPA_125 = 125
MAPA_126 = 126
MAPA_127 = 127
MAPA_128 = 128
MAPA_129 = 129
MAPA_130 = 130
MAPA_131 = 131
MAPA_132 = 132
MAPA_133 = 133
MAPA_134 = 134
MAPA_135 = 135
MAPA_136 = 136
MAPA_137 = 137
MAPA_138 = 138
MAPA_139 = 139
MAPA_140 = 140
MAPA_141 = 141
MAPA_142 = 142
MAPA_143 = 143
MAPA_144 = 144
MAPA_145 = 145
MAPA_146 = 146
MAPA_147 = 147
MAPA_148 = 148
MAPA_149 = 149
MAPA_150 = 150
MAPA_151 = 151
MAPA_152 = 152
MAPA_153 = 153
MAPA_154 = 154
MAPA_155 = 155
MAPA_156 = 156
MAPA_157 = 157
MAPA_158 = 158
MAPA_159 = 159
MAPA_160 = 160
MAPA_161 = 161
MAPA_162 = 162
MAPA_163 = 163
MAPA_164 = 164
MAPA_165 = 165
MAPA_166 = 166
MAPA_167 = 167
MAPA_168 = 168
MAPA_169 = 169
MAPA_170 = 170
MAPA_171 = 171
MAPA_172 = 172
MAPA_173 = 173
MAPA_174 = 174
MAPA_175 = 175
MAPA_176 = 176
MAPA_177 = 177
MAPA_178 = 178
MAPA_179 = 179
MAPA_180 = 180
MAPA_181 = 181
MAPA_182 = 182
MAPA_183 = 183
MAPA_184 = 184
MAPA_185 = 185
MAPA_186 = 186
MAPA_187 = 187
MAPA_188 = 188
MAPA_189 = 189
MAPA_190 = 190
MAPA_191 = 191
MAPA_192 = 192
MAPA_193 = 193
MAPA_194 = 194
MAPA_195 = 195
MAPA_196 = 196
MAPA_197 = 197
MAPA_198 = 198
MAPA_199 = 199
MAPA_200 = 200
MAPA_201 = 201
MAPA_202 = 202
MAPA_203 = 203
MAPA_204 = 204
MAPA_205 = 205
MAPA_206 = 206
MAPA_207 = 207
MAPA_208 = 208
MAPA_209 = 209
MAPA_210 = 210

TEXTURES = {
    PRETO: pygame.image.load('./sprites/textures/negao.png'),
    MAPA_01: pygame.image.load("./Image/images/mapa_01.png"),
    MAPA_02: pygame.image.load("./Image/images/mapa_02.png"),
    MAPA_03: pygame.image.load("./Image/images/mapa_03.png"),
    MAPA_04: pygame.image.load("./Image/images/mapa_04.png"),
    MAPA_05: pygame.image.load("./Image/images/mapa_05.png"),
    MAPA_06: pygame.image.load("./Image/images/mapa_06.png"),
    MAPA_07: pygame.image.load("./Image/images/mapa_07.png"),
    MAPA_08: pygame.image.load("./Image/images/mapa_08.png"),
    MAPA_09: pygame.image.load("./Image/images/mapa_09.png"),
    MAPA_10: pygame.image.load("./Image/images/mapa_10.png"),
    MAPA_11: pygame.image.load("./Image/images/mapa_11.png"),
    MAPA_12: pygame.image.load("./Image/images/mapa_12.png"),
    MAPA_13: pygame.image.load("./Image/images/mapa_13.png"),
    MAPA_14: pygame.image.load("./Image/images/mapa_14.png"),
    MAPA_15: pygame.image.load("./Image/images/mapa_15.png"),
    MAPA_16: pygame.image.load("./Image/images/mapa_16.png"),
    MAPA_17: pygame.image.load("./Image/images/mapa_17.png"),
    MAPA_18: pygame.image.load("./Image/images/mapa_18.png"),
    MAPA_19: pygame.image.load("./Image/images/mapa_19.png"),
    MAPA_20: pygame.image.load("./Image/images/mapa_20.png"),
    MAPA_21: pygame.image.load("./Image/images/mapa_21.png"),
    MAPA_22: pygame.image.load("./Image/images/mapa_22.png"),
    MAPA_23: pygame.image.load("./Image/images/mapa_23.png"),
    MAPA_24: pygame.image.load("./Image/images/mapa_24.png"),
    MAPA_25: pygame.image.load("./Image/images/mapa_25.png"),
    MAPA_26: pygame.image.load("./Image/images/mapa_26.png"),
    MAPA_27: pygame.image.load("./Image/images/mapa_27.png"),
    MAPA_28: pygame.image.load("./Image/images/mapa_28.png"),
    MAPA_29: pygame.image.load("./Image/images/mapa_29.png"),
    MAPA_30: pygame.image.load("./Image/images/mapa_30.png"),
    MAPA_31: pygame.image.load("./Image/images/mapa_31.png"),
    MAPA_32: pygame.image.load("./Image/images/mapa_32.png"),
    MAPA_33: pygame.image.load("./Image/images/mapa_33.png"),
    MAPA_34: pygame.image.load("./Image/images/mapa_34.png"),
    MAPA_35: pygame.image.load("./Image/images/mapa_35.png"),
    MAPA_36: pygame.image.load("./Image/images/mapa_36.png"),
    MAPA_37: pygame.image.load("./Image/images/mapa_37.png"),
    MAPA_38: pygame.image.load("./Image/images/mapa_38.png"),
    MAPA_39: pygame.image.load("./Image/images/mapa_39.png"),
    MAPA_40: pygame.image.load("./Image/images/mapa_40.png"),
    MAPA_41: pygame.image.load("./Image/images/mapa_41.png"),
    MAPA_42: pygame.image.load("./Image/images/mapa_42.png"),
    MAPA_43: pygame.image.load("./Image/images/mapa_43.png"),
    MAPA_44: pygame.image.load("./Image/images/mapa_44.png"),
    MAPA_45: pygame.image.load("./Image/images/mapa_45.png"),
    MAPA_46: pygame.image.load("./Image/images/mapa_46.png"),
    MAPA_47: pygame.image.load("./Image/images/mapa_47.png"),
    MAPA_48: pygame.image.load("./Image/images/mapa_48.png"),
    MAPA_49: pygame.image.load("./Image/images/mapa_49.png"),
    MAPA_50: pygame.image.load("./Image/images/mapa_50.png"),
    MAPA_51: pygame.image.load("./Image/images/mapa_51.png"),
    MAPA_52: pygame.image.load("./Image/images/mapa_52.png"),
    MAPA_53: pygame.image.load("./Image/images/mapa_53.png"),
    MAPA_54: pygame.image.load("./Image/images/mapa_54.png"),
    MAPA_55: pygame.image.load("./Image/images/mapa_55.png"),
    MAPA_56: pygame.image.load("./Image/images/mapa_56.png"),
    MAPA_57: pygame.image.load("./Image/images/mapa_57.png"),
    MAPA_58: pygame.image.load("./Image/images/mapa_58.png"),
    MAPA_59: pygame.image.load("./Image/images/mapa_59.png"),
    MAPA_60: pygame.image.load("./Image/images/mapa_60.png"),
    MAPA_61: pygame.image.load("./Image/images/mapa_61.png"),
    MAPA_62: pygame.image.load("./Image/images/mapa_62.png"),
    MAPA_63: pygame.image.load("./Image/images/mapa_63.png"),
    MAPA_64: pygame.image.load("./Image/images/mapa_64.png"),
    MAPA_65: pygame.image.load("./Image/images/mapa_65.png"),
    MAPA_66: pygame.image.load("./Image/images/mapa_66.png"),
    MAPA_67: pygame.image.load("./Image/images/mapa_67.png"),
    MAPA_68: pygame.image.load("./Image/images/mapa_68.png"),
    MAPA_69: pygame.image.load("./Image/images/mapa_69.png"),
    MAPA_70: pygame.image.load("./Image/images/mapa_70.png"),
    MAPA_71: pygame.image.load("./Image/images/mapa_71.png"),
    MAPA_72: pygame.image.load("./Image/images/mapa_72.png"),
    MAPA_73: pygame.image.load("./Image/images/mapa_73.png"),
    MAPA_74: pygame.image.load("./Image/images/mapa_74.png"),
    MAPA_75: pygame.image.load("./Image/images/mapa_75.png"),
    MAPA_76: pygame.image.load("./Image/images/mapa_76.png"),
    MAPA_77: pygame.image.load("./Image/images/mapa_77.png"),
    MAPA_78: pygame.image.load("./Image/images/mapa_78.png"),
    MAPA_79: pygame.image.load("./Image/images/mapa_79.png"),
    MAPA_80: pygame.image.load("./Image/images/mapa_80.png"),
    MAPA_81: pygame.image.load("./Image/images/mapa_81.png"),
    MAPA_82: pygame.image.load("./Image/images/mapa_82.png"),
    MAPA_83: pygame.image.load("./Image/images/mapa_83.png"),
    MAPA_84: pygame.image.load("./Image/images/mapa_84.png"),
    MAPA_85: pygame.image.load("./Image/images/mapa_85.png"),
    MAPA_86: pygame.image.load("./Image/images/mapa_86.png"),
    MAPA_87: pygame.image.load("./Image/images/mapa_87.png"),
    MAPA_88: pygame.image.load("./Image/images/mapa_88.png"),
    MAPA_89: pygame.image.load("./Image/images/mapa_89.png"),
    MAPA_90: pygame.image.load("./Image/images/mapa_90.png"),
    MAPA_91: pygame.image.load("./Image/images/mapa_91.png"),
    MAPA_92: pygame.image.load("./Image/images/mapa_92.png"),
    MAPA_93: pygame.image.load("./Image/images/mapa_93.png"),
    MAPA_94: pygame.image.load("./Image/images/mapa_94.png"),
    MAPA_95: pygame.image.load("./Image/images/mapa_95.png"),
    MAPA_96: pygame.image.load("./Image/images/mapa_96.png"),
    MAPA_97: pygame.image.load("./Image/images/mapa_97.png"),
    MAPA_98: pygame.image.load("./Image/images/mapa_98.png"),
    MAPA_99: pygame.image.load("./Image/images/mapa_99.png"),
    MAPA_100: pygame.image.load("./Image/images/mapa_100.png"),
    MAPA_101: pygame.image.load("./Image/images/mapa_101.png"),
    MAPA_102: pygame.image.load("./Image/images/mapa_102.png"),
    MAPA_103: pygame.image.load("./Image/images/mapa_103.png"),
    MAPA_104: pygame.image.load("./Image/images/mapa_104.png"),
    MAPA_105: pygame.image.load("./Image/images/mapa_105.png"),
    MAPA_106: pygame.image.load("./Image/images/mapa_106.png"),
    MAPA_107: pygame.image.load("./Image/images/mapa_107.png"),
    MAPA_108: pygame.image.load("./Image/images/mapa_108.png"),
    MAPA_109: pygame.image.load("./Image/images/mapa_109.png"),
    MAPA_110: pygame.image.load("./Image/images/mapa_110.png"),
    MAPA_111: pygame.image.load("./Image/images/mapa_111.png"),
    MAPA_112: pygame.image.load("./Image/images/mapa_112.png"),
    MAPA_113: pygame.image.load("./Image/images/mapa_113.png"),
    MAPA_114: pygame.image.load("./Image/images/mapa_114.png"),
    MAPA_115: pygame.image.load("./Image/images/mapa_115.png"),
    MAPA_116: pygame.image.load("./Image/images/mapa_116.png"),
    MAPA_117: pygame.image.load("./Image/images/mapa_117.png"),
    MAPA_118: pygame.image.load("./Image/images/mapa_118.png"),
    MAPA_119: pygame.image.load("./Image/images/mapa_119.png"),
    MAPA_120: pygame.image.load("./Image/images/mapa_120.png"),
    MAPA_121: pygame.image.load("./Image/images/mapa_121.png"),
    MAPA_122: pygame.image.load("./Image/images/mapa_122.png"),
    MAPA_123: pygame.image.load("./Image/images/mapa_123.png"),
    MAPA_124: pygame.image.load("./Image/images/mapa_124.png"),
    MAPA_125: pygame.image.load("./Image/images/mapa_125.png"),
    MAPA_126: pygame.image.load("./Image/images/mapa_126.png"),
    MAPA_127: pygame.image.load("./Image/images/mapa_127.png"),
    MAPA_128: pygame.image.load("./Image/images/mapa_128.png"),
    MAPA_129: pygame.image.load("./Image/images/mapa_129.png"),
    MAPA_130: pygame.image.load("./Image/images/mapa_130.png"),
    MAPA_131: pygame.image.load("./Image/images/mapa_131.png"),
    MAPA_132: pygame.image.load("./Image/images/mapa_132.png"),
    MAPA_133: pygame.image.load("./Image/images/mapa_133.png"),
    MAPA_134: pygame.image.load("./Image/images/mapa_134.png"),
    MAPA_135: pygame.image.load("./Image/images/mapa_135.png"),
    MAPA_136: pygame.image.load("./Image/images/mapa_136.png"),
    MAPA_137: pygame.image.load("./Image/images/mapa_137.png"),
    MAPA_138: pygame.image.load("./Image/images/mapa_138.png"),
    MAPA_139: pygame.image.load("./Image/images/mapa_139.png"),
    MAPA_140: pygame.image.load("./Image/images/mapa_140.png"),
    MAPA_141: pygame.image.load("./Image/images/mapa_141.png"),
    MAPA_142: pygame.image.load("./Image/images/mapa_142.png"),
    MAPA_143: pygame.image.load("./Image/images/mapa_143.png"),
    MAPA_144: pygame.image.load("./Image/images/mapa_144.png"),
    MAPA_145: pygame.image.load("./Image/images/mapa_145.png"),
    MAPA_146: pygame.image.load("./Image/images/mapa_146.png"),
    MAPA_147: pygame.image.load("./Image/images/mapa_147.png"),
    MAPA_148: pygame.image.load("./Image/images/mapa_148.png"),
    MAPA_149: pygame.image.load("./Image/images/mapa_149.png"),
    MAPA_150: pygame.image.load("./Image/images/mapa_150.png"),
    MAPA_151: pygame.image.load("./Image/images/mapa_151.png"),
    MAPA_152: pygame.image.load("./Image/images/mapa_152.png"),
    MAPA_153: pygame.image.load("./Image/images/mapa_153.png"),
    MAPA_154: pygame.image.load("./Image/images/mapa_154.png"),
    MAPA_155: pygame.image.load("./Image/images/mapa_155.png"),
    MAPA_156: pygame.image.load("./Image/images/mapa_156.png"),
    MAPA_157: pygame.image.load("./Image/images/mapa_157.png"),
    MAPA_158: pygame.image.load("./Image/images/mapa_158.png"),
    MAPA_159: pygame.image.load("./Image/images/mapa_159.png"),
    MAPA_160: pygame.image.load("./Image/images/mapa_160.png"),
    MAPA_161: pygame.image.load("./Image/images/mapa_161.png"),
    MAPA_162: pygame.image.load("./Image/images/mapa_162.png"),
    MAPA_163: pygame.image.load("./Image/images/mapa_163.png"),
    MAPA_164: pygame.image.load("./Image/images/mapa_164.png"),
    MAPA_165: pygame.image.load("./Image/images/mapa_165.png"),
    MAPA_166: pygame.image.load("./Image/images/mapa_166.png"),
    MAPA_167: pygame.image.load("./Image/images/mapa_167.png"),
    MAPA_168: pygame.image.load("./Image/images/mapa_168.png"),
    MAPA_169: pygame.image.load("./Image/images/mapa_169.png"),
    MAPA_170: pygame.image.load("./Image/images/mapa_170.png"),
    MAPA_171: pygame.image.load("./Image/images/mapa_171.png"),
    MAPA_172: pygame.image.load("./Image/images/mapa_172.png"),
    MAPA_173: pygame.image.load("./Image/images/mapa_173.png"),
    MAPA_174: pygame.image.load("./Image/images/mapa_174.png"),
    MAPA_175: pygame.image.load("./Image/images/mapa_175.png"),
    MAPA_176: pygame.image.load("./Image/images/mapa_176.png"),
    MAPA_177: pygame.image.load("./Image/images/mapa_177.png"),
    MAPA_178: pygame.image.load("./Image/images/mapa_178.png"),
    MAPA_179: pygame.image.load("./Image/images/mapa_179.png"),
    MAPA_180: pygame.image.load("./Image/images/mapa_180.png"),
    MAPA_181: pygame.image.load("./Image/images/mapa_181.png"),
    MAPA_182: pygame.image.load("./Image/images/mapa_182.png"),
    MAPA_183: pygame.image.load("./Image/images/mapa_183.png"),
    MAPA_184: pygame.image.load("./Image/images/mapa_184.png"),
    MAPA_185: pygame.image.load("./Image/images/mapa_185.png"),
    MAPA_186: pygame.image.load("./Image/images/mapa_186.png"),
    MAPA_187: pygame.image.load("./Image/images/mapa_187.png"),
    MAPA_188: pygame.image.load("./Image/images/mapa_188.png"),
    MAPA_189: pygame.image.load("./Image/images/mapa_189.png"),
    MAPA_190: pygame.image.load("./Image/images/mapa_190.png"),
    MAPA_191: pygame.image.load("./Image/images/mapa_191.png"),
    MAPA_192: pygame.image.load("./Image/images/mapa_192.png"),
    MAPA_193: pygame.image.load("./Image/images/mapa_193.png"),
    MAPA_194: pygame.image.load("./Image/images/mapa_194.png"),
    MAPA_195: pygame.image.load("./Image/images/mapa_195.png"),
    MAPA_196: pygame.image.load("./Image/images/mapa_196.png"),
    MAPA_197: pygame.image.load("./Image/images/mapa_197.png"),
    MAPA_198: pygame.image.load("./Image/images/mapa_198.png"),
    MAPA_199: pygame.image.load("./Image/images/mapa_199.png"),
    MAPA_200: pygame.image.load("./Image/images/mapa_200.png"),
    MAPA_201: pygame.image.load("./Image/images/mapa_201.png"),
    MAPA_202: pygame.image.load("./Image/images/mapa_202.png"),
    MAPA_203: pygame.image.load("./Image/images/mapa_203.png"),
    MAPA_204: pygame.image.load("./Image/images/mapa_204.png"),
    MAPA_205: pygame.image.load("./Image/images/mapa_205.png"),
    MAPA_206: pygame.image.load("./Image/images/mapa_206.png"),
    MAPA_207: pygame.image.load("./Image/images/mapa_207.png"),
    MAPA_208: pygame.image.load("./Image/images/mapa_208.png"),
    MAPA_209: pygame.image.load("./Image/images/mapa_209.png"),
    MAPA_210: pygame.image.load("./Image/images/mapa_210.png")
}

GRID = [
    [MAPA_01, MAPA_02, MAPA_03, MAPA_04, MAPA_05, MAPA_06, MAPA_07, MAPA_08, MAPA_09, MAPA_10, MAPA_11, MAPA_12, MAPA_13, MAPA_14, MAPA_15, MAPA_16, MAPA_17, MAPA_18, MAPA_19, MAPA_20, MAPA_21], 
    [MAPA_22, MAPA_23, MAPA_24, MAPA_25, MAPA_26, MAPA_27, MAPA_28, MAPA_29, MAPA_30, MAPA_31, MAPA_32, MAPA_33, MAPA_34, MAPA_35, MAPA_36, MAPA_37, MAPA_38, MAPA_39, MAPA_40, MAPA_41, MAPA_42], 
    [MAPA_43, MAPA_44, MAPA_45, MAPA_46, MAPA_47, MAPA_48, MAPA_49, MAPA_50, MAPA_51, MAPA_52, MAPA_53, MAPA_54, MAPA_55, MAPA_56, MAPA_57, MAPA_58, MAPA_59, MAPA_60, MAPA_61, MAPA_62, MAPA_63], 
    [MAPA_64, MAPA_65, MAPA_66, MAPA_67, MAPA_68, MAPA_69, MAPA_70, MAPA_71, MAPA_72, MAPA_73, MAPA_74, MAPA_75, MAPA_76, MAPA_77, MAPA_78, MAPA_79, MAPA_80, MAPA_81, MAPA_82, MAPA_83, MAPA_84], 
    [MAPA_85, MAPA_86, MAPA_87, MAPA_88, MAPA_89, MAPA_90, MAPA_91, MAPA_92, MAPA_93, MAPA_94, MAPA_95, MAPA_96, MAPA_97, MAPA_98, MAPA_99, MAPA_100, MAPA_101, MAPA_102, MAPA_103, MAPA_104, MAPA_105],
    [MAPA_106, MAPA_107, MAPA_108, MAPA_109, MAPA_110, MAPA_111, MAPA_112, MAPA_113, MAPA_114, MAPA_115, MAPA_116, MAPA_117, MAPA_118, MAPA_119, MAPA_120, MAPA_121, MAPA_122, MAPA_123, MAPA_124, MAPA_125, MAPA_126],
    [MAPA_127, MAPA_128, MAPA_129, MAPA_130, MAPA_131, MAPA_132, MAPA_133, MAPA_134, MAPA_135, MAPA_136, MAPA_137, MAPA_138, MAPA_139, MAPA_140, MAPA_141, MAPA_142, MAPA_143, MAPA_144, MAPA_145, MAPA_146, MAPA_147],
    [MAPA_148, MAPA_149, MAPA_150, MAPA_151, MAPA_152, MAPA_153, MAPA_154, MAPA_155, MAPA_156, MAPA_157, MAPA_158, MAPA_159, MAPA_160, MAPA_161, MAPA_162, MAPA_163, MAPA_164, MAPA_165, MAPA_166, MAPA_167, MAPA_168],
    [MAPA_169, MAPA_170, MAPA_171, MAPA_172, MAPA_173, MAPA_174, MAPA_175, MAPA_176, MAPA_177, MAPA_178, MAPA_179, MAPA_180, MAPA_181, MAPA_182, MAPA_183, MAPA_184, MAPA_185, MAPA_186, MAPA_187, MAPA_188, MAPA_189],
    [MAPA_190, MAPA_191, MAPA_192, MAPA_193, MAPA_194, MAPA_195, MAPA_196, MAPA_197, MAPA_198, MAPA_199, MAPA_200, MAPA_201, MAPA_202, MAPA_203, MAPA_204, MAPA_205, MAPA_206, MAPA_207, MAPA_208, MAPA_209, MAPA_210]
]

TILESIZE = 60
MAPWIDTH = 21
MAPHEIGHT = 10
pygame.init()
pygame.display.set_caption('Adventure Student')

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
