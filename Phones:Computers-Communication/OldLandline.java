package Homework1;
import java.util.*;

public class OldLandline implements Phone {

    private String owner;
    private boolean isBusy = false;
    private PhoneNumber number;
    public Phone connectPhone; //To connect to the phone you are calling
    public Phone tempPhone; //To reference the phone that is calling but you don't want to connect to in receive method
    static int callFailed = 0;

    public OldLandline() {}

    public OldLandline(String o, long n) {
        this.owner = o;
        this.number = new PhoneNumber(n);
    }

    /**
     * @preconditions
     * -String owner is declared and initialized
     * @return
     * -String owner of this instantiation
     */
    @Override
    public String getOwner() {
        return this.owner;
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
     * @preconditions
     * -Two classes that implement phone are instantiated and are linked to each other via a phone call
     * -This class and the phone this class is connected to is busy
     * @postconditions
     * -Set this.isBusy to false
     * -invoke receiveEndSignal(Phone from)
     * -Print the message that the call was ended successfully
     * -Set this.connectedPhone reference to null
     * @throws
     * -Exception: Thrown if this class is not currently in a call
     */
    @Override
    public void end() {

        if (this.connectPhone == null) {
            System.out.println("Please call someone. You can't end a call that doesn't exist.");
            return;
        }

        if ((!this.isBusy()) || (!connectPhone.isBusy())) {
            System.out.println("Please try again. " + this.getOwner() + " is not in a call.");
            return;
        }

        connectPhone.receiveEndSignal(this);

        System.out.println(this.getOwner() + " has ended the call to " + connectPhone.getOwner() + ". ");
        this.setBusy(false);
        this.connectPhone = null;

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
     */
    @Override
    public void receive(Phone from) {

        if (this.isBusy()) {

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

    /**
     * @preconditions
     * -Boolean isBusy is declared and initialized
     * @return
     * -Boolean isBusy
     */
    @Override
    public boolean isBusy() {
        return this.isBusy;
    }

    /**
     * @preconditions
     * -From: The class, which implements phone, that is calling you
     * @postconditions
     * -Set this.isBusy to false
     * -Set this.connectedPhone reference to null
     */
    public void receiveEndSignal(Phone from) {
        this.setBusy(false);
        this.connectPhone = null;
    }

    /**
     * @return
     * -this.number of type PhoneNumber
     */
    @Override
    public PhoneNumber number() {
        return this.number;
    }


    /**
     * @param
     * -b: Boolean value to set this.isBusy to
     * @preconditions
     * -Boolean isBusy is declared and initialized
     * @postconditions
     * -isBusy is set to value b
     */
    public void setBusy(boolean b) {
        this.isBusy = b;
    }

    public String toString() {
        return "name: " + this.getOwner() + ", number: " + this.number().getNumber();
    }



}
