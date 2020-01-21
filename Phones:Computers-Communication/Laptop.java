package Homework1;

import java.util.HashSet;

public class Laptop implements Computer {

    private String owner;
    private String brand;
    private String hostname;
    private int screenSize;
    private int RAM;
    private int processorSpeed;
    private String gameName;
    State state;
    private HashSet<String> games = new HashSet<>();

    public Laptop(String o, String b, int scrnS, int ram, int pS, String state) {
        this.hostname = o + "'s " + b + " laptop";
        this.owner = o;
        this.brand = b;
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
                System.out.println("Sorry " + this.hostname + " already has 5 games and is full.");
                return;
            }

            System.out.println("Installing " + gameName + " on " + this.hostname() + ".");
            games.add(gameName);
        }

        else {
            System.out.println("Cannot install a game on " + this.hostname() + " since it's off.");
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
                System.out.println(this.hostname() + " is playing " + gameName + ". ");
            }

            else {
                System.out.println("Cannot play " + gameName + " on " + this.hostname() + ". Install it first.");
            }
        }

        else {
            System.out.println("Cannot play a game on " + this.hostname() + " since it's off.");
        }

    }

    public String hostname() {
        return this.hostname;
    }

    public String getBrand() { return this.brand; }

    public String getHostname() {
        return this.hostname;
    }

    public String toString() {
        return "screen size: " + this.getScreenSize() + ", brand name: " + this.getBrand() + ", RAM: " + this.getRAM();
    }







}
