keys = {
"title" : "Lord of the rings",
"release year" : 2001,
"duration" : 228,
"director" : "Peter Jackson"
}

keys["actors"] = ["Viggo Mortenson", "Orlando Bloom", "Elijah Wood"]

for key, value in keys.items():
	if key == "duration":
		print(f"{key} : {value} minutes")
	
	elif key == "actors":
		print(key + " : " + " , ".join(value))

	else:
		print(f"{key} : {value}")
		
	


