package Homework1;

public class PhoneNumber {

    private long number;

    //Constructor that takes in a 10 digit long (64 bit) number
    public PhoneNumber(long l) {
        if (l >= 1000000000L && l <= 9999999999L) {
            this.number = l;
        }

        else {
            throw new IllegalArgumentException("Please enter in a valid 10 digit number");
        }
    }

    //Getter for number member variable
    public long getNumber() {
        return this.number;
    }



}
