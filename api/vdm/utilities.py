def handle_prices(data: dict) -> dict:
    """Set price according to rate."""
    for reservation in data['Reservation']:
        if reservation['Tarif'] == "Plein tarif":
            price = 9.40
        elif reservation['Tarif'] == "Tarif reduit":
            price = 7.40
        elif reservation['Tarif'] == "Senior":
            price = 6.80
        elif reservation['Tarif'] == "Tarif etudiant":
            price = 6.80
        else:
            price = None
        reservation['prix'] = price
    return data
