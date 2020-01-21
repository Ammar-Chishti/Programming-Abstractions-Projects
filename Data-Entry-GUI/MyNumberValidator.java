package sample;
import javafx.scene.control.TextField;

public class MyNumberValidator {

    public static void setGrayedOutTexttoNumber(TextField a) {
        a.setPromptText("Number");
    }

    public static boolean isValidNumber(TextField a) {
        String inputNumber = a.getText().trim();

        if (inputNumber.length() != 14) {
            return false;
        }

        if ( (inputNumber.charAt(0) != '(') || (inputNumber.charAt(4) != ')') || (inputNumber.charAt(5) != ' ') || (inputNumber.charAt(9) != '-')) {
            return false;
        }

        inputNumber = inputNumber.replaceAll("[^\\d.]", "");
        for (int i = 0; i < inputNumber.length(); i++) {
            if (!(Character.isDigit(inputNumber.charAt(i)))) {
                return false;
            }
        }
        return true;
    }

}
