from .models import *
from fuzzywuzzy import process


#function to add entso_unit_id to Mappings table
def mapEntso():
	entso = Entso.objects.filter(mapped=False)
	for obj in entso:
		entso_unit_id = obj.entso_unit_id
		check = Mapping.objects.filter(entso_unit_id = entso_unit_id).first()
		if check:
			obj.mapped = True
			obj.save()
		else:
			new = Mapping()
			new.entso_unit_id = entso_unit_id
			new.save()

#function to map gppd_plant_id to entso_unit_id in Mappings table using fuzzy matches on plant_name
def mapGppd():
	#initial variable, lists, and dictionary
	results = {}
	matches = []
	entso_ids = []
	count = 0
	
	#create list from all Gppd Names that exist
	gppd_plant_names = Gppd.objects.filter(plant_name__isnull=False)
	names = []
	for i in gppd_plant_names:
		names.append(i.plant_name)

	#get all Entso objects with a plant name
	entso = Entso.objects.filter(plant_name__isnull=False)
	for obj in entso:
		name = obj.plant_name
		match = process.extractOne(name, names) #fuzzy match Entso against possible Gppd matches
		if match[1] >= 80: #hard set to greater than or equal to 80% likely match
			matches.append(match[0])
			entso_id = (obj.entso_unit_id, match[0])
			entso_ids.append(entso_id)
			count = count + 1
		else:
			matches.append(None)

	#for resulting matches, map entso_unit_id to gppd_plant_id
	for res in entso_ids:
		entso_id = res[0]
		gppd_name = res[1]
		gppd = Gppd.objects.filter(plant_name = gppd_name).first()
		if gppd:
			check = Mapping.objects.filter(entso_unit_id = entso_id, gppd_plant_id__isnull=True).first()
			if check:
				check.gppd_plant_id = gppd.gppd_plant_id
				check.save()

	return results

#function to map platt_unit_id to entso_unit_id in Mappings table using fuzzy matches on unit_name
def mapPlatts():
	#initial variable, lists, and dictionary
	results = {}
	matches = []
	entso_ids = []
	count = 0
	
	#create list from all Platt Names that exist
	platt_unit_names = Platt.objects.filter(unit_name__isnull=False)
	names = []
	for i in platt_unit_names:
		names.append(i.unit_name)

	#get all Entso objects with a plant name
	entso = Entso.objects.filter(unit_name__isnull=False)
	for obj in entso:
		name = obj.unit_name
		match = process.extractOne(name, names) #fuzzy match Entso against possible Platt matches
		if match[1] >= 80: #hard set to greater than or equal to 80% likely match
			matches.append(match[0])
			entso_id = (obj.entso_unit_id, match[0])
			entso_ids.append(entso_id)
			count = count + 1
		else:
			matches.append(None)

	#for resulting matches, map entso_unit_id to gppd_plant_id
	for res in entso_ids:
		entso_id = res[0]
		platt_name = res[1]
		platt = Platt.objects.filter(unit_name = platt_name).first()
		if platt:
			check = Mapping.objects.filter(entso_unit_id = entso_id, platts_unit_id__isnull=True).first()
			if check:
				check.platts_unit_id = platt.platts_unit_id
				check.save()

	return results

#quick reset
def reset():
	Entso.objects.all().delete()
	Mapping.objects.all().delete()


