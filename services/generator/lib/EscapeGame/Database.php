<?php

namespace EscapeGame;

/**
 * Class Database
 * @package EscapeGame
 */
class Database
{
    /**
     * @return string
     */
    public function getEscapeGameName($rand = false)
    {
        $movies = [
            'Impot sur le revenu',
            'Greve de la SNCF',
            'Interminable attente chez le medecin',
            'Soutenance finale',
            'Mon compte en banque en fin du mois',
            'Mariage sans alcool',
            'Diner de famille insoutenable',
            'Plus de PQ dans les toilettes',
            'En plein dans la Friendzone',
        ];

        if ($rand == false) {
            $rand = rand(0, 8);
        }

        return $movies[$rand];
    }

    /**
     * @param $age
     * @return mixed
     */
    public function getPersonType($age)
    {
        $rand = rand(1, 100);

        if ($age < 18) {
            return 'Tarif etudiant';
        } else if ($age >= 55) {
            return 'Senior';
        } else {
            if ($rand < 70) {
                return 'Plein tarif';
            } else if ($rand >= 70 && $rand <= 89) {
                return 'Tarif etudiant';
            } else {
                return 'Tarif reduit';
            }
        }
    }

    /**
     * @return mixed
     */
    public function getNbTickets($rand = false)
    {
        $rand = rand(1, 100);

        if ($rand >= 50) {
            return 1;
        } else if ($rand < 50 && $rand >= 30) {
            return 2;
        } else if ($rand < 30 && $rand >= 15) {
            return 3;
        } else {
            return 4;
        }
    }

    public function getReservationHour($rand = false)
    {
        $hour = [
            '08:00',
            '10:00',
            '12:30',
            '16:00',
            '18:30',
            '21:30',
            '00:00',
            '03:00',
            '05:30',
        ];

        if ($rand == false) {
            $rand = rand(0, 8);
        }

        return $hour[$rand];
    }

    /**
     * @return string
     */
    public function useVirtualReality($rand = false)
    {
        $rand = rand(0, 1);

        if ($rand == 0) {
            return 'Oui';
        } else {
            return 'Non';
        }
    }

    /**
     * @return string
     */
    public function getGender($rand = false)
    {
        $gender = [
            'Monsieur',
            'Madame',
        ];

        $rand = rand(0, 1);

        return $gender[$rand];
    }

    /**
     * @return int
     */
    public function getAge($rand = false)
    {
        if ($rand == false) {
            $rand = rand(5, 65);
        }
        return $rand;
    }

    public function getSuffixEmail($rand = false)
    {
        $suffix = [
            'gogole.com',
            'coldmail.com',
            'inlook.com',
            'youhou.com',
            'gcloud.com',
            'outbox.com'
        ];

        if ($rand = false) {
            $rand = rand(0, 5);
        }

        return $suffix[$rand];
    }

    public function getReservationDate()
    {
        $rand = rand(1, 100);

        if ($rand <= 80) {
            $date = new \DateTime('now');

            return $date->format('Y-m-d');
        } else if ($rand > 80 && $rand <= 95) {
            $date = new \DateTime('tomorrow');

            return $date->format('Y-m-d');
        } else {
            $date = new \DateTime('now');

            return $date->modify('+2 day')->format('Y-m-d');
        }
    }
}
