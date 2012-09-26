def cm(dimensions):
	mm = str(10 * float(dimensions))
	newsy = newspaperify(mm)
	return '%(dimensions)s cm is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def inch(dimensions):
	mm = str(25.4 * float(dimensions))
	newsy = newspaperify(mm)
	return '%(dimensions)s inches is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def feet(dimensions):
	mm = str(25.4 * float(dimensions) / 12)
	newsy = newspaperify(mm)
	return '%(dimensions)s inches is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def miles(dimensions):
	mm = str(float(dimensions)* 1609 * 1000)
	newsy = newspaperify(mm)
	return '%(dimensions)s miles is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def m(dimensions):
	mm = str(1000 * float(dimensions))
	newsy = newspaperify(mm)
	return '%(dimensions)s metres is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def km(dimensions):
	mm = str(1000 * float(dimensions) * 1000)
	newsy = newspaperify(mm)
	return '%(dimensions)s km is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def mm(dimensions):
	mm = dimensions
	newsy = newspaperify(mm)
	return '%(dimensions)s mm is %(number)s %(description)s' % {'dimensions':dimensions,'mm':mm,'number':newsy[0],'description':newsy[1]}

def buses(mm):
	return '%s' % ( int(float(mm)/1000 / 13)),'buses'

def footballPitches(mm):
	return '%s' % ( int(float(mm)/1000 / 105)),'football pitches'

def tennisCourts(mm):
	return '%s' % ( int(float(mm)/1000 / 23.78)),'tennis courts'

def minis(mm):
	return '%s' % ( int(float(mm)/1000 / 3.05)),'minis'

def rulers(mm):
	return '%s' % ( int(float(mm)/300)),'rulers'

def pencils(mm):
	return '%s' % ( int(float(mm)/175)),'pencils'
			
def strings(mm):
	return '1','strings'

def moonTrips(mm):
	return '%s' % ( int(float(mm)/1000 / 384400000)), 'trips to moon'
	
def lightYears(mm):
	return '%s' % ( int(float(mm)/1000 / 9460730472580800)), 'light years'

def newspaperify(mm):
	for newspaperUnit in newspaperUnits:
		if (newspaperUnits[newspaperUnit](mm)[0] > '0'):
			return newspaperUnits[newspaperUnit](mm)

newspaperUnits = {
	0 : lightYears,
	1 : moonTrips,
	2 : footballPitches,
	3 : tennisCourts,
	4 : buses,
	5 : minis,
	6 : rulers,
	7 : pencils,
	8 : strings
}
options = {	
	'inch' : inch,
	'in' : inch,
	'"' : inch,
	'inches' : inch,
	'feet' :feet,
	"\'": feet,
	'ft': feet,
	'centimeter' : cm,
	'centimeters' : cm,
	'cm' : cm,
	'millimeter' : mm,
	'millimeters' : mm,
	'mm' : mm,
	'meter' : m,
	'meters' : m,
	'metres' : m,
	'metre' : m,
	'm' : m,
	
	'kilometer' : km,
	'kilometers' : km,
	'kilometres' : km,
	'kilometre' : km,
	'km' : km,
	
	'mile' : miles,
	'miles' : miles
}