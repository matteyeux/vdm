import datetime

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


def handle_themes(data: dict) -> dict:
    """Set themes according to game."""
    if data['Game']['Nom'] == "Impot sur le revenu":
        first_theme = "Braquage"
        second_theme = "Stress"
    elif data['Game']['Nom'] == "Greve de la SNCF":
        first_theme = "Rapidité"
        second_theme = "Mythologique"
    elif data['Game']['Nom'] == "Interminable attente chez le medecin":
        first_theme = "Stratégie"
        second_theme = "Psychologique"
    elif data['Game']['Nom'] == "Soutenance finale":
        first_theme = "Stress"
        second_theme = "Rapidité"
    elif data['Game']['Nom'] == "Mon compte en banque en fin du mois":
        first_theme = "Mythologique"
        second_theme = "Braquage"
    elif data['Game']['Nom'] == "Mariage sans alcool":
        first_theme = "Santé"
        second_theme = "Amour"
    elif data['Game']['Nom'] == "Diner de famille insoutenable":
        first_theme = "Psychologique"
        second_theme = "Stratégie"
    elif data['Game']['Nom'] == "Plus de PQ dans les toilettes":
        first_theme = "Horreur"
        second_theme = "Santé"
    elif data['Game']['Nom'] == "En plein dans la Friendzone":
        first_theme = "Amour"
        second_theme = "Horreur"
    else:
        first_theme = None
        second_theme = None
    data['Game']['theme_pricipal'] = first_theme
    data['Game']['theme_secondaire'] = second_theme
    return data


def handle_datetime(data: dict) -> dict:
	"""Set fields CreatedAt."""
	data['CreatedAt'] = datetime.datetime.now()
	return data


def handle_utilities(data: dict) -> dict:
	"""Call each function to transform the data dict."""
	data_w_price = handle_prices(data)
	data_w_theme = handle_themes(data_w_price)
	data_w_date = handle_datetime(data_w_theme)
	return data_w_date
