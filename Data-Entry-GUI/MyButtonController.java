package sample;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.geometry.HPos;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class MyButtonController {

    public static boolean isNotEmptyAll(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree) {

        if (!nameOne.getText().isEmpty() && !nameTwo.getText().isEmpty() && !nameThree.getText().isEmpty() && !numberOne.getText().isEmpty() && !numberTwo.getText().isEmpty() && !numberThree.getText().isEmpty()) {
            return true;
        }

        else {
            return false;
        }

    }

    public static boolean isValidAll(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree) {

        if (MyNameValidator.isValidName(nameOne) && MyNameValidator.isValidName(nameTwo) && MyNameValidator.isValidName(nameThree) && MyNumberValidator.isValidNumber(numberOne) && MyNumberValidator.isValidNumber(numberTwo) && MyNumberValidator.isValidNumber(numberThree)) {
            return true;
        }

        else {
            return false;
        }

    }

    public static void addListenerAll(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree, Button createProfiles) {

        nameOne.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNameValidator.isValidName(nameOne)) {
                        nameOne.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        nameOne.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    nameOne.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

        nameTwo.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNameValidator.isValidName(nameTwo)) {
                        nameTwo.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        nameTwo.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    nameTwo.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

        nameThree.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNameValidator.isValidName(nameThree)) {
                        nameThree.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        nameThree.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    nameThree.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

        numberOne.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNumberValidator.isValidNumber(numberOne)) {
                        numberOne.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        numberOne.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    numberOne.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

        numberTwo.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNumberValidator.isValidNumber(numberTwo)) {
                        numberTwo.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        numberTwo.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    numberTwo.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

        numberThree.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNumberValidator.isValidNumber(numberThree)) {
                        numberThree.setStyle("-fx-text-inner-color: black;");
                    }

                    else {
                        numberThree.setStyle("-fx-text-inner-color: red;");
                    }
                }

                else {
                    numberThree.setStyle("-fx-text-inner-color: black;");
                }
            }
        });



        nameOne.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

        nameTwo.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

        nameThree.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

        numberOne.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

        numberTwo.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

        numberThree.textProperty().addListener((observable, oldValue, newValue) -> {

            if (isNotEmptyAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
                createProfiles.setDisable(false);
            }

            else {
                createProfiles.setDisable(true);
            }

        });

    }

    public static void buttonCheck(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree) {
        if (isValidAll(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree)) {
            validInputShow(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree);
        }

        else {
            invalidInputShow();
        }


    }

    public static String validInputShow(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree) {

        Stage stage = new Stage();
        Button close = new Button("Close");
        close.setOnAction(e->{
            stage.close();
        });

        GridPane successMessage = new GridPane();
        successMessage.setAlignment(Pos.CENTER);
        successMessage.add(close, 0, 1);
        successMessage.add(new Label("The profiles have been saved and added to the database."), 0, 0);
        successMessage.setHalignment(close, HPos.CENTER);
        lockTextFields(nameOne, nameTwo, nameThree, numberOne, numberTwo, numberThree);
        Scene scene = new Scene(successMessage, 480, 300);
        stage.setTitle("Data Saved");
        stage.setScene(scene);
        stage.show();

        return "Data Saved";

    }

    public static String invalidInputShow() {
        Stage stage = new Stage();
        Button close = new Button("Close");
        close.setOnAction(e->{
            stage.close();
        });

        GridPane errorMessage = new GridPane();
        errorMessage.setAlignment(Pos.CENTER);
        errorMessage.add(close, 0, 1);
        GridPane.setHalignment(close, HPos.CENTER);
        errorMessage.add(new Label("INVALID INPUT: you have attempted to provide one or more invalid input(s). \nPlease correct the information displayed in red and retry."),0, 0);
        Scene scene = new Scene(errorMessage, 480, 300);
        stage.setTitle("Invalid Error Input");
        stage.setScene(scene);
        stage.show();

        return "Invalid Error Input";
    }

    public static void lockTextFields(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree) {
        nameOne.setDisable(true);
        nameTwo.setDisable(true);
        nameThree.setDisable(true);
        numberOne.setDisable(true);
        numberTwo.setDisable(true);
        numberThree.setDisable(true);
    }


}
