def formatNumberInt(number):
	if number < 1000:
		num_anno = str(int(number))
	elif number < 1000000:
		num_tmp = number/1000
		num_anno = str(int(num_tmp)) + " K"

	return num_anno


def formatNumberMoney(number):
	if number < 1000:
		num_anno = str(round(number, 2)).replace(".", ",") + " €"
	elif number < 1000000:
		num_tmp = number/1000
		num_anno = str(round(num_tmp, 2)).replace(".", ",") + " K €"

	return num_anno
