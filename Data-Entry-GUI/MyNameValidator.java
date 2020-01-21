package sample;
import javafx.scene.control.TextField;
import javax.naming.Name;

public class MyNameValidator {

    public static void setGrayedOutTexttoName(TextField a) {
        a.setPromptText("Name");
    }

    public static boolean isValidName(TextField a) {

        // If the entire name is longer than 20 return false
        if (a.getText().length() > 20) {
            return false;
        }

        String inputText = a.getText().trim();

        // If there is more than one space, return false
        int count = 0;
        for (int i=0; i<inputText.length(); i++) {
            if (inputText.charAt(i) == ' ') {
                count += 1;
            }
        }
        if (count != 1) {
            return false;
        }

        //Check if each name starts with an uppercase
        if (Character.isLowerCase(inputText.charAt(0))) {
            return false;
        }
        int i = inputText.indexOf(" ");
        i += 1;
        if (Character.isLowerCase(inputText.charAt(i))) {
            return false;
        }
        // If there is more than 1 capital letter than at the beginning of the names
        for (int k = 0; k < inputText.length(); k++) {
            if (k == 0) {
                continue;
            }

            else if (k == i) {
                continue;
            }

            if (Character.isUpperCase(inputText.charAt(k))) {
                return false;
            }

        }

        //Check if all characters are letters
        inputText = inputText.replaceAll("\\s+","");
        for (int j = 0; j < inputText.length(); j++) {
            if (!((Character.isLowerCase(inputText.charAt(j))) || (Character.isUpperCase(inputText.charAt(j))))) {
                return false;
            }
        }

        return true;
    }

}
