package Homework1;

import java.util.Comparator;

public class Ordering {

    static class PhoneNumberComparator implements Comparator<Phone> {

        public int compare(Phone one, Phone two) {

            if (one.number().getNumber() > two.number().getNumber()) {
                return 1;
            }

            else if (one.number().getNumber() < two.number().getNumber()) {
                return -1;
            }

            else {
                return 0;
            }

        }

    }

    static class PhoneNameComparator implements Comparator<Phone> {

        public int compare(Phone one, Phone two) {

            if (one.getOwner().compareToIgnoreCase(two.getOwner()) > 0) {
                return 1;
            }

            else if ((one.getOwner().compareToIgnoreCase(two.getOwner()) < 0)) {
                return -1;
            }

            else {
                return 0;
            }
        }

    }

    static class ComputerScreenComparator implements Comparator<Computer> {

        public int compare(Computer one, Computer two) {

            if (one.getScreenSize() > two.getScreenSize()) {
                return 1;
            } else if (one.getScreenSize() < two.getScreenSize()) {
                return -1;
            } else {
                return 0;
            }

        }
    }

    static class ComputerBrandComparator implements Comparator<Computer> {

        public int compare(Computer one, Computer two) {

            if ((one instanceof SmartPhone) && (two instanceof SmartPhone)) {
                return 0;
            }

            else if ((one instanceof SmartPhone) || (two instanceof SmartPhone)) {
                if (one.getClass().equals(SmartPhone.class)) {
                    return 1;
                }

                else if (two.getClass().equals(SmartPhone.class)) {
                    return -1;
                }
            }

            else if ((one instanceof Laptop) && (two instanceof Laptop)) {

                if (((Laptop) one).getBrand().compareToIgnoreCase(((Laptop) two).getBrand()) > 0) {
                    return 1;
                }

                else if (((Laptop) one).getBrand().compareToIgnoreCase(((Laptop) two).getBrand()) < 0) {
                    return -1;
                }

                else {
                    return 0;
                }
            }
        return 0;

        }

    }

    static class ComputerRAMComparator implements Comparator<Computer> {

        public int compare(Computer one, Computer two) {

            if (one.getRAM() > two.getRAM()) {
                return 1;
            }

            else if (one.getRAM() < two.getRAM()) {
                return -1;
            }

            else {
                return 0;
            }

        }

    }

}