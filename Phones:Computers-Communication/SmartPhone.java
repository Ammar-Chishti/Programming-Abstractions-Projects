package Homework1;

import java.util.HashSet;
import java.util.Scanner;

public class SmartPhone extends Landline implements Computer {

    private int screenSize;
    private int RAM;
    private int processorSpeed;
    private String gameName;
    State state;
    private HashSet<String> games = new HashSet<>();

    public SmartPhone() {}

    public SmartPhone(String o, long n, int scrnS, int ram, int pS, String state) {

        super(o, n);

        this.screenSize = scrnS;
        this.RAM = ram;
        this.processorSpeed = pS;

        if (state.equalsIgnoreCase("on")) {
            this.state = State.ON;
        }

        else if (state.equalsIgnoreCase("off")) {
            this.state = State.OFF;
        }

        else {
            throw new IllegalArgumentException("Please enter in a valid state.");
        }

    }

    /**
     * @param
     * -phone: The class, that implements interface Phone, you are calling
     * @preconditions
     * -The class you are calling is instantiated
     * @postconditions
     * -connectPhone is referenced to the phone parameter
     * -isBusy is set to true
     * -Invoke the receive(Phone from) method where from is the
     * -If this class is currently busy, print out that call did not go through and exit
     * @throws
     * -IllegalArgumentException: Thrown if you call yourself
     */
    @Override
    public void call(Phone phone) {

        if (this.getState().equals(State.OFF)) {
            System.out.println("Cannot make a call since " + this.getOwner() + " is off right now.");
            callFailed++;
            return;
        }

        if (phone.equals(this)) {
            throw new IllegalArgumentException("Please call someone else. You cannot call yourself.");
        }

        this.tempPhone = phone;

        if (this.number().getNumber() == tempPhone.number().getNumber()) {
            System.out.println("Cannot call someone with the same number. Call someone else.");
            return;
        }

        if (this.isBusy()) {
            System.out.println(this.getOwner() + " is unable to call " + tempPhone.getOwner() +
                    " since " + this.getOwner() + " is in a phone call already.");
            return;
        }

        this.connectPhone = phone;
        callFailed = 0;
        phone.receive(this);

        if (callFailed == 1) {
            this.connectPhone = null;
            return;
        }

        this.setBusy(true);
        System.out.println(this.getOwner() + " is on the phone with " + connectPhone.getOwner() + ". ");

    }

    /**
     * @param
     * -from: The class that implements phone is calling you
     * @preconditions
     * -The class that is calling you is instantiated
     * @postconditions
     * -connectPhone is referenced to class that is calling this class
     * -isBusy is set to true
     * -If a call is successfully made, print call successful statement
     * -If this phone is busy and a call can go through, allow the from phone to leave a message
     * -Save the message status in a message status array and save the message in another array
     */
    public void receive(Phone from) {

        if (this.getState().equals(State.OFF)) {

            tempPhone = from;

            System.out.print(tempPhone.getOwner() + " is unable to call " + this.getOwner() +
                    " because it is currently off right now. ");
            System.out.print("Does " + tempPhone.getOwner() + " want to leave a message? [y/n]: ");

            Scanner input = new Scanner(System.in);
            String decision = input.next();

            if (decision.equalsIgnoreCase("y")) {
                System.out.print("Leave message here: ");
                input.nextLine();
                String message = input.nextLine();

                if (this.getClass().equals(OldLandline.class)) {
                    System.out.println(this.getOwner() + " is an OldLandline and did not receive the message.");
                    tempPhone = null;
                    callFailed++;
                    return;
                }

                else if ((this.getClass().equals(Landline.class)) || (this.getClass().equals(SmartPhone.class))) {
                    System.out.println(tempPhone.getOwner() + " successfully left a message for " + this.getOwner() + ". ");
                    this.updateMessage(message);
                    tempPhone = null;
                    callFailed++;
                    return;
                }

            }

            else if (decision.equalsIgnoreCase("n")) {
                callFailed++;
                return;
            }

            else {
                System.out.println("Enter in a valid input next time");
                callFailed++;
                return;
            }


        }

        else if (this.isBusy()) {

            tempPhone = from;

            System.out.print(tempPhone.getOwner() + " is unable to call " + this.getOwner() +
                    ". Line is busy. ");
            System.out.print("Does " + tempPhone.getOwner() + " want to leave a message? [y/n]: ");

            Scanner input = new Scanner(System.in);
            String decision = input.next();

            if (decision.equalsIgnoreCase("y")) {
                System.out.print("Leave message here: ");
                input.nextLine();
                String message = input.nextLine();

                if (this.getClass().equals(OldLandline.class)) {
                    System.out.println(this.getOwner() + " is an OldLandline and did not receive the message.");
                    tempPhone = null;
                    callFailed++;
                    return;
                }

                else if (this.getClass().equals(Landline.class)) {
                    System.out.println(tempPhone.getOwner() + " successfully left a message for " + this.getOwner() + ". ");
                    this.updateMessage(message);
                    tempPhone = null;
                    callFailed++;
                    return;
                }
            }

            else if (decision.equalsIgnoreCase("n")) {
                callFailed++;
                return;
            }

            else {
                System.out.println("Enter in a valid input next time");
                callFailed++;
                return;
            }


        }

        connectPhone = from;
        this.setBusy(true);

    }

    //Checking to see if the SmartPhone is off. If it is, refuse to read the messages.
    public void readMessages() {

        if (this.getState().equals(State.OFF)) {
            System.out.println("Cannot read messages since " + this.getOwner() + " is off right now.");
        }

        else {
            super.readMessages();
        }
    }

    public void readMessages(String messagestatus) {

        if (this.getState().equals(State.OFF)) {
            System.out.println("Cannot read messages since " + this.getOwner() + " is off right now.");
        }

        else {
            super.readMessages(messagestatus);
        }
    }



    /**
     * @preconditions
     * -int screenSize has been declared
     * @return
     * -this.screenSize
     */
    public int getScreenSize() {
        return this.screenSize;
    }

    /**
     * @preconditions
     * -int RAM has been declared
     * @return
     * -this.RAM
     */
    public int getRAM() {
        return this.RAM;
    }

    /**
     * @preconditions
     * -int processorSpeed has been declared
     * @return
     * -this.processorSpeed
     */
    public int getProcessorSpeeed() {
        return this.processorSpeed;
    }

    /**
     * @preconditions
     * -Enum State class has been created
     * @return
     * -this.state
     */
    public State getState() {
        return this.state;
    }

    /**
     * @param
     * -String to: The state you want to set this class to
     * @preconditions
     * -Enum State class has been created
     * @postconditions
     * -State has been initialized to ON or OFF based on the parameter
     * @throws
     * -IllegalargumentException: Thrown if String to is not "on" or "off" (equalsignorecase)
     */
    public void setState(String to) {

        if (to.equalsIgnoreCase("on")) {
            this.state = State.ON;
        }

        else if (to.equalsIgnoreCase("off")) {
            this.state = State.OFF;
        }

        else {
            throw new IllegalArgumentException("Please enter in a valid state.");
        }


    }

    /**
     * @param
     * -String gameName: The name of the game you want to install
     * @preconditions
     * -HashSet has been declared
     * -HashSet is not full
     * @postconditions
     * -gameName has been added to HashSet
     * @throws
     * -Exception: If the size of HashSet is full (5 or more games installed)
     */
    public void installGame(String gameName) {

        if (this.state == State.ON) {

            if (hasGame(gameName)) {
                return;
            }

            if (games.size() >= 5) {
                System.out.println("Sorry, SmartPhone already has 5 games and is full.");
                return;
            }

            System.out.println("Installing " + gameName + " on " + this.getOwner() + "'s smart phone.");
            games.add(gameName);
        }

        else {
            System.out.println("Cannot install a game on " + this.getOwner() + "'s smart phone since it's off.");
        }
    }

    /**
     * @param
     * -String gameName: The name of the game you want to check for
     * @preconditions
     * -HashSet has been declared
     * -HashSet is not full
     * @return
     * -boolean true if game is in HashSet or false if not
     */
    public boolean hasGame(String gameName) {

        if (games.contains(gameName)) {
            return true;
        }

        else {
            return false;
        }

    }

    /**
     * @param
     * -String gameName: The name of the game you want to play
     * @preconditions
     * -HashSet contains the game you want to play
     * @postconditions
     * -Print out the game that is being played
     * @throws
     * -Exception: Thrown when trying to play a game that hasn't been installed (not in the HashSet)
     */
    public void playGame(String gameName) {

        if (this.state == State.ON) {
            if (hasGame(gameName)) {
                System.out.println(this.getOwner() + " is playing " + gameName + ". ");
            }

            else {
                System.out.println("Cannot play " + gameName + " on " + this.getOwner() + "'s smart phone. Install it first.");
            }
        }

        else {
            System.out.println("Cannot play a game on " + this.getOwner() + "'s smart phone since it's off.");
        }

    }

    public String toString() {
        return "screen size: " + this.getScreenSize() + ", name: " + this.getOwner() + ", RAM: " + this.getRAM();
    }


}
