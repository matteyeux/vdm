<?php

use EscapeGame\Database;

require_once 'lib/autoload.php';

$faker = Faker\Factory::create();
$escapegame = new Database();

if (empty($argv[1]) == true) {
    $timer = 100000;
} else {
    $timer = $argv[1]*1000;
}

$j = 0;

# create dir if it does not exist
if (!is_dir("jsons")) {
	mkdir("jsons");
}

# delete all jsons before generating more crap
$files = glob('jsons/*');
foreach($files as $file) {
  if(is_file($file))
    unlink($file);
}

while (true) {
    usleep($timer);
    $firstAge = $escapegame->getAge();
    $nbTickets = $escapegame->getNbTickets();
    $firstCivility = $escapegame->getGender(false);
    $firstNom = $faker->firstName;
    $firstPrenom = $faker->firstName;
    $firstEmail = $firstNom . '.' . $firstPrenom . '@' . $escapegame->getSuffixEmail();
    $firstPersonType = $escapegame->getPersonType($firstAge);

    $result['Acheteur']['Civilite'] = $firstCivility;
    $result['Acheteur']['Nom'] = $firstNom;
    $result['Acheteur']['Prenom'] = $firstPrenom;
    $result['Acheteur']['Age'] = $firstAge;
    $result['Acheteur']['Email'] = strtolower($firstEmail);
    $result['Game']['Nom'] = $escapegame->getEscapeGameName();
    $result['Game']['Jour'] = $escapegame->getReservationDate();
    $result['Game']['Horaire'] = $escapegame->getReservationHour();
    $result['Game']['VR'] = $escapegame->useVirtualReality();
    for ($i = 0; $i < $nbTickets; $i++) {
        if ($i == 0) {
            $result['Reservation'][$i]['Spectateur']['Civilite'] = $firstCivility;
            $result['Reservation'][$i]['Spectateur']['Nom'] = $firstNom;
            $result['Reservation'][$i]['Spectateur']['Prenom'] = $firstPrenom;
            $result['Reservation'][$i]['Spectateur']['Age'] = $firstAge;
            $result['Reservation'][$i]['Tarif'] = $firstPersonType;
        } else {
            $otherAge = $escapegame->getAge();
            $otherCivility = $escapegame->getGender(false);
            $otherNom = $faker->firstName;
            $otherPrenom = $faker->firstName;
            $otherPersonType = $escapegame->getPersonType($otherAge);

            $result['Reservation'][$i]['Spectateur']['Civilite'] = $otherCivility;
            $result['Reservation'][$i]['Spectateur']['Nom'] = $otherNom;
            $result['Reservation'][$i]['Spectateur']['Prenom'] = $otherPrenom;
            $result['Reservation'][$i]['Spectateur']['Age'] = $otherAge;
            $result['Reservation'][$i]['Tarif'] = $otherPersonType;
        }
    }

	$date = date("YdjHis");
    $json_file = $date . "_". $j . ".json";

	$file = fopen("jsons/" . $json_file, 'w');
	fwrite($file, json_encode($result));
	fclose($file);

	$j++;
    echo PHP_EOL;
}
