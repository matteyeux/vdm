def handle_prices(data: dict) -> dict:
	"""Set price according to rate."""
	for reservation in data['Reservation']:
		if reservation['Tarif'] == "Plein tarif":
			price = 10.00
		elif reservation['Tarif'] == "Tarif reduit":
			price = 8.00
		elif reservation['Tarif'] == "Senior":
			price = 7.00
		elif reservation['Tarif'] == "Tarif etudiant":
			price = 7.00
		else:
			price = None
		reservation['prix'] = price
	return data


def handle_prices(data: dict) -> dict:
	"""Set themes according to game."""
	for theme in data['Game']:
		if theme['Nom'] == "Impot sur le revenu":
			first_theme = "Braquage"
			second_theme = "Stress"
		elif theme['Nom'] == "Greve de la SNCF":
			first_theme = "Rapidité"
			second_theme = "Mythologique"
		elif theme['Nom'] == "Interminable attente chez le medecin":
			first_theme = "Stratégie"
			second_theme = "Psychologie"
		elif theme['Nom'] == "Soutenance finale":
			first_theme = "Stress"
			second_theme = "Rapidité"
		elif theme['Nom'] == "Mon compte en banque en fin du mois":
			first_theme = "Mythologique"
			second_theme = "Braquage"
		elif theme['Nom'] == "Mariage sans alcool":
			first_theme = "Santé"
			second_theme = "Amour"
		elif theme['Nom'] == "Diner de famille insoutenable":
			first_theme = "Psychologique"
			second_theme = "Stratégie"
		elif theme['Nom'] == "Plus de PQ dans les toilettes":
			first_theme = "Horreur"
			second_theme = "Santé"
		elif theme['Nom'] == "En plein dans la Friendzone":
			first_theme = "Amour"
			second_theme = "Horreur"
		else:
			first_theme = None
			second_theme = None
		theme['theme_pricipal'] = first_theme
		theme['theme_secondaire'] = second_theme
	return data
