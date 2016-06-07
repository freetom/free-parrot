import math
import sys

# 27.55 is the coefficient of open space (not into a building), different propagation pattern
# ( db, Mhz) -> m
def calculateDistance(signalLevelInDb, freqInMHz):
	if signalLevelInDb<0:
		signalLevelInDb*=-1
	exp = (27.55 - (20 * math.log10(freqInMHz)) + signalLevelInDb) / 20.0;
	return math.pow(10.0, exp);

