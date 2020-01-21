package Homework1;

import java.util.*;

public class Landline extends OldLandline implements Phone {

    private MSG_STATUS[] msgstatuses = new MSG_STATUS[1000];
    private String[] messages = new String[1000];
    private int msgarraysize = 0;

    public enum MSG_STATUS {
        READ, UNREAD;
    }

    public Landline() {}

    public Landline(String o, long n) {
        super(o, n);
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

    /**
     * @preconditions
     * -An array that holds message statuses and messages has been created and currently stores the respective values
     * @postconditions
     * -Prints out all of the messages the person has on to the console
     * -Every message that was previously marked unread is now marked read
     * @throws
     * -Exception: Thrown if the person is in a call. Cannot read messages in a call
     * -Exception: Thrown if the person has no messages
     */
    public void readMessages() {

        if (this.msgarraysize == 0) {
            System.out.println(this.getOwner() + " currently has no messages right now. Please leave a message first.");
            return;
        }

        if (this.isBusy()) {
            System.out.println("Sorry, cannot read messages while in a call");
            return;
        }

        System.out.println("Reading all of " + this.getOwner() + "'s messages. Every message that is currently unread will be marked read after this.");
        for (int i = 0; i < this.msgarraysize; i++) {

            System.out.println("Message " + (i+1) + " (" + this.msgstatuses[i] + "): " + this.messages[i]);

            if (this.msgstatuses[i] == MSG_STATUS.UNREAD) {
                this.msgstatuses[i] = MSG_STATUS.READ;
            }

        }

    }

    /**
     * @param
     * -MSG_STATUS: Enum determining what type of messages to read
     * @preconditions
     * -An array that holds message statuses and messages has been created and currently stores the respective values
     * @postconditions
     * -Prints out every message of type MSG_STATUS
     * -Every message that was previously marked unread is now marked read
     * @throws
     * -Exception: Thrown if the person has no messages
     */
    public void readMessages(String messagestatus) {

        MSG_STATUS status;

        if (this.msgarraysize == 0) {
            System.out.println(this.getOwner() + " currently has no messages right now. Please leave a message first.");
            return;
        }

        if (this.isBusy()) {
            System.out.println("Sorry, cannot read messages while in a call");
            return;
        }

        if (messagestatus.equalsIgnoreCase(("read"))) {
            status = MSG_STATUS.READ;
        }

        else if (messagestatus.equalsIgnoreCase(("unread"))) {
            status = MSG_STATUS.UNREAD;
        }

        else {
            throw new IllegalArgumentException("Please enter in a valid message status.");
        }

        //Reading all of the unread messages
        if (status == MSG_STATUS.UNREAD) {
            System.out.println("Reading all of " + this.getOwner() + "'s unread messages. All of these messages will be marked read after.");
            for (int i = 0; i < this.msgarraysize; i++) {
                if (msgstatuses[i] == MSG_STATUS.UNREAD) {
                    System.out.println("Message " + (i+1) + " (" + this.msgstatuses[i] + "): " + this.messages[i]);
                    msgstatuses[i] = MSG_STATUS.READ;
                }
            }
        }

        //Reading all of the read messages
        if (status == MSG_STATUS.READ) {
            System.out.println("Reading all of " + this.getOwner() + "'s read messages.");
            for (int i = 0; i < this.msgarraysize; i++) {
                if (msgstatuses[i] == MSG_STATUS.READ) {
                    System.out.println("Message " + (i+1) + " (" + this.msgstatuses[i] + "): " + this.messages[i]);
                }
            }
        }



    }

    /**
     * @param
     * -String message: The message to be stored in a person's inbox
     * @preconditions
     * -An array that holds message statuses and messages has been created
     * @postconditions
     * -Loads the message and message status into the respective arrays
     * -Updates both of the arrays' size counter
     */
    public void updateMessage(String message) {

        this.msgstatuses[this.msgarraysize] = MSG_STATUS.UNREAD;
        this.messages[this.msgarraysize] = message;
        this.msgarraysize++;

    }

}
