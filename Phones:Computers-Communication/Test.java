package Homework1;
import java.util.*;

public class Test {

    public static void main(String[] args) {

        /**
         * Here starts the testing for the PhoneNumber Class
         */
        System.out.println("Testing out PhoneNumber Class\n");
        try {
            System.out.print("Testing out PhoneNumber that is longer than 10 digits: ");
            PhoneNumber one = new PhoneNumber(6319221983436L);
        }

        catch (IllegalArgumentException e) {
            System.out.println("Please enter in a valid phone number.");
        }

        try {
            System.out.print("Testing out PhoneNumber that is shorter than than 10 digits: ");
            PhoneNumber one = new PhoneNumber(631L);
        }

        catch (IllegalArgumentException e) {
            System.out.println("Please enter in a valid phone number.");
        }

        System.out.println("Creating a valid phone number.");
        PhoneNumber one = new PhoneNumber(6319221986L);

        System.out.print("\nPress enter to test out OldLandline Class: ");
        Scanner input = new Scanner(System.in);
        input.nextLine();


        /**
         * Here starts the testing for the OldLandline Class
         */
        System.out.println("Testing out OldLandline class\n");
        OldLandline Nick = new OldLandline("Nick", 6316248457L);
        OldLandline Harry = new OldLandline("Harry", 6315979657L);
        OldLandline Jack = new OldLandline("Jack", 6315592429L);
        OldLandline John = new OldLandline("John", 6316248457L);

        System.out.println("Nick calls Harry. Nick ends the call:");
        Nick.call(Harry);
        Nick.end();
        System.out.println();

        System.out.println("Nick calls Harry. Harry ends the call:");
        Nick.call(Harry);
        Harry.end();
        System.out.println();

        System.out.println("Nick calls Harry. Jack calls Harry. Harry is busy so Jack tries to leave a message " +
                "but Harry can't receive it:");
        Nick.call(Harry);
        Jack.call(Harry);
        System.out.println();

        System.out.println("While Nick is in a call with Harry, Nick tries to call Jack:");
        Nick.call(Jack);
        System.out.println();

        System.out.println("Resetting phone calls:");
        Nick.end();
        System.out.println();

        try {
            System.out.println("Nick tries to call himself:");
            Nick.call(Nick);
        }

        catch (IllegalArgumentException e) {
            System.out.println("Please call someone else. You cannot call yourself.");
            System.out.println();
        }

        System.out.println("Nick tries to call John who has the same number as him:");
        Nick.call(John);
        System.out.println();

        System.out.println("Nick ends the call when he was never in a call at all:");
        Nick.end();
        System.out.println();

        System.out.print("Press enter to test out Landline Class: ");
        input.nextLine();

        /**
         * Here starts the testing for the Landline Class
         */
        System.out.println("Testing out Landline class\n");

        Landline Douglas = new Landline("Douglas", 6316248457L);
        Landline Jackson = new Landline("Jackson", 6315979657L);
        Landline Joe = new Landline("Joe", 6315592429L);
        //OldLandline Jason = new OldLandline("Jason", 6316248457L);

        System.out.println("Calling a Landline and leaving messages:");
        Douglas.call(Jackson);
        Joe.call(Jackson);
        Joe.call(Jackson);
        Joe.call(Jackson);
        System.out.println();

        System.out.println("Attempting to read messages while in a call:");
        Jackson.readMessages();
        System.out.println();

        System.out.println("Reading messages:");
        Jackson.end();
        Jackson.readMessages();
        System.out.println();

        System.out.println("Adding more messages:");
        Jackson.call(Douglas);
        Joe.call(Jackson);
        Joe.call(Jackson);
        System.out.println();

        System.out.println("Reading read messages:");
        Jackson.end();
        Jackson.readMessages("read");
        System.out.println();

        System.out.println("Reading unread messages:");
        Jackson.readMessages("unread");
        System.out.println();

        System.out.println("Reading all messages:");
        Jackson.readMessages();
        System.out.println();

        try {
            System.out.println("Inputting incorrect parameter to readMessages:");
            Jackson.readMessages("Hello");
        }

        catch (IllegalArgumentException e) {
            System.out.println("Please enter in a valid message status.");
            System.out.println();
        }

        System.out.println("Reading a message when there are no messages:");
        Douglas.readMessages();
        System.out.println();

        System.out.print("Press enter to test out SmartPhone Class: ");
        input.nextLine();


        /**
         * Here starts the testing for the SmartPhone Class
         */
        System.out.println("Testing out SmartPhone class\n");

        SmartPhone Walter = new SmartPhone("Walter", 6319944825L, 50, 50, 50, "on");
        SmartPhone Adam = new SmartPhone("Adam", 6315426321L, 50, 50, 50, "on");
        SmartPhone Raymond = new SmartPhone("Raymond", 6317611624L, 50, 50, 50, "off");

        try {
            System.out.println("Setting state to something other than on or off:");
            Walter.setState("Hello");
        }

        catch (IllegalArgumentException e) {
            System.out.println("Please enter in a valid state.");
            System.out.println();
        }

        System.out.println("Installing and playing a game:");
        Walter.installGame("Fortnite");
        Walter.playGame("Fortnite");
        System.out.println();

        System.out.println("Installing a game that had already being installed:");
        Walter.installGame("Fortnite");
        System.out.println();

        System.out.println("Installing more than 5 games:");
        Walter.installGame("Minecraft");
        Walter.installGame("League of Legends");
        Walter.installGame("Apex Legends");
        Walter.installGame("Left 4 Dead 2");
        Walter.installGame("Planetside 2");
        System.out.println();

        System.out.println("Attempting to play a game that hasn't been installed");
        Walter.playGame("Fire Emblem");
        System.out.println();

        Walter.setState("off");

        System.out.println("Attempting to install a game when off:");
        Walter.installGame("Fire Emblem");
        System.out.println();

        System.out.println("Attempting to play a game when off:");
        Walter.playGame("Fire Emblem");
        System.out.println();

        System.out.println("Attempting to call someone when off:");
        Walter.call(Adam);
        System.out.println();

        System.out.println("Leaving a message for a phone that's off:");
        Adam.call(Walter);
        System.out.println();

        System.out.println("Attempting to read a message when off:");
        Walter.readMessages();
        System.out.println();

        System.out.print("Press enter to test out Laptop Class: ");
        input.nextLine();


        /**
         * Here starts the testing for the Laptop Class
         */
        System.out.println("Testing out Laptop class\n");

        Laptop Mark = new Laptop("Walter", "Dell", 50, 50, 50, "on");
        Laptop Marcus = new Laptop("Adam", "Apple", 50, 50, 50, "on");
        Laptop Jimmy = new Laptop("Raymond", "Samsung", 50, 50, 50, "off");

        System.out.println("Installing and playing a game:");
        Mark.installGame("Fortnite");
        Mark.playGame("Fortnite");
        System.out.println();

        System.out.println("Installing a game that had already being installed:");
        Mark.installGame("Fortnite");
        System.out.println();

        System.out.println("Installing more than 5 games:");
        Mark.installGame("Minecraft");
        Mark.installGame("League of Legends");
        Mark.installGame("Apex Legends");
        Mark.installGame("Left 4 Dead 2");
        Mark.installGame("Planetside 2");
        System.out.println();

        System.out.println("Attempting to play a game that hasn't been installed");
        Mark.playGame("Fire Emblem");
        System.out.println();

        Mark.setState("off");

        System.out.println("Attempting to install a game when off:");
        Mark.installGame("Fire Emblem");
        System.out.println();

        System.out.println("Attempting to play a game when off:");
        Mark.playGame("Fire Emblem");
        System.out.println();

        System.out.print("Press enter to test out Orderings: ");
        input.nextLine();


        /**
         * Here starts the testing for the Orderings Class
         */
        System.out.println("Testing out Orderings class\n");

        ArrayList<Phone> phones = new ArrayList<>();
        Phone Liam = new OldLandline("Liam", 6315967458L);
        Phone Noah = new OldLandline("Noah", 3679644242L);
        Phone William = new OldLandline("William", 8924715463L);
        Phone James = new OldLandline("James", 5697412542L);
        Phone Michael = new OldLandline("Michael", 7697944521L);
        phones.add(Liam);
        phones.add(Noah);
        phones.add(William);
        phones.add(James);
        phones.add(Michael);

        ArrayList<Computer> computers = new ArrayList<>();
        Computer Benjamin = new Laptop("Benjamin", "Dell", 20, 20, 20, "on");
        Computer Elijah = new Laptop("Elijah", "Apple", 50, 50, 50, "on");
        Computer Ethan = new Laptop("Ethan", "Samsung", 25, 25, 25, "on");
        SmartPhone Daniel = new SmartPhone("Daniel", 6315874687L, 15, 15, 15, "on");
        SmartPhone Matthew = new SmartPhone("Matthew", 6315789746L, 38, 38, 38, "on");
        computers.add(Benjamin);
        computers.add(Elijah);
        computers.add(Ethan);
        computers.add(Daniel);
        computers.add(Matthew);


        System.out.println("Before sorting phones: ");
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(phones.get(i));
        }
        System.out.println();

        System.out.println("After sorting phones by their numbers:");
        Collections.sort(phones, new Ordering.PhoneNumberComparator());
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(phones.get(i));
        }
        System.out.println();

        System.out.println("After sorting phones by their names:");
        Collections.sort(phones, new Ordering.PhoneNameComparator());
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(phones.get(i));
        }
        System.out.println();

        System.out.println("Before sorting computers: ");
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(computers.get(i));
        }
        System.out.println();

        System.out.println("After sorting computers by their screen size: ");
        Collections.sort(computers, new Ordering.ComputerScreenComparator());
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(computers.get(i));
        }
        System.out.println();

        System.out.println("After sorting computers by their brand names: ");
        Collections.sort(computers, new Ordering.ComputerBrandComparator());
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(computers.get(i));
        }
        System.out.println();


        System.out.println("After sorting computers by their amount of RAM: ");
        Collections.sort(computers, new Ordering.ComputerRAMComparator());
        for (int i = 0; i < phones.size(); i++) {
            System.out.println(computers.get(i));
        }
        System.out.println();

        System.out.print("Press enter to test out difference between real and apparent types when phones and computers are different: ");
        input.nextLine();


        /**
        * Here starts the testing for the Phone class in the difference between real and apparent types
        */
        System.out.println("Testing out Phone and Computer real vs apparent types\n");

        OldLandline Samuel = new Landline("Samuel", 6316248457L);
        Landline David = new Landline("David", 6315979657L);
        OldLandline Ryan = new OldLandline("Ryan", 6315487459L);

        System.out.println("Testing out calling and leaving a message to a class whose apparent type is OldLandline but actualy type is Landline:");
        Ryan.call(Samuel);
        David.call(Samuel);
        Samuel.end();
        ((Landline) Samuel).readMessages();
        System.out.println("Functionality works but Samuel must be casted to Landline before using Landline methods.");
        System.out.println();

        OldLandline Jonathon = new SmartPhone("Jonathon", 6316248457L, 50, 50, 50, "on");
        Computer Connor = new Laptop("Connor", "Dell", 100, 100, 100, "off");

        System.out.println("Installing and playing a game with Jonathon: ");
        ((SmartPhone) Jonathon).installGame("Fornite");
        ((SmartPhone) Jonathon).playGame("Fortnite");
        System.out.println();

        System.out.println("Getting the Host name of Connor");
        ((Laptop) Connor).getHostname();
        System.out.println("Same as above. Functionality works but classes need to be casted.");

    }



}
