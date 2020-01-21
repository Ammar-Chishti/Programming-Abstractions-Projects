package sample;

import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class MyColor {

    public static void addListenerAll(TextField nameOne, TextField nameTwo, TextField nameThree, TextField numberOne, TextField numberTwo, TextField numberThree, Button createProfiles) {

        nameOne.focusedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable, Boolean oldValue, Boolean newValue) {

                if (!newValue) {
                    if (MyNameValidator.isValidName(nameOne)) {
                        nameOne.setStyle("-fx-text-inner-color: black;");
                    } else {
                        nameOne.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
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
                    } else {
                        nameTwo.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
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
                    } else {
                        nameThree.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
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
                    } else {
                        numberOne.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
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
                    } else {
                        numberTwo.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
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
                    } else {
                        numberThree.setStyle("-fx-text-inner-color: red;");
                    }
                } else {
                    numberThree.setStyle("-fx-text-inner-color: black;");
                }
            }
        });

    }

    public static void colorChange(TextField nameOne, boolean f) {
        if (f) {
            nameOne.setStyle("-fx-text-inner-color: black;");
        } else {
            nameOne.setStyle("-fx-text-inner-color: red;");
        }
    }




}
