package sample;

import javafx.embed.swing.JFXPanel;
import javafx.scene.control.TextField;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertFalse;

public class MyColorTest {

    JFXPanel p;
    TextField colorText;

    @Before
    public void setUp() {
        this.p = new JFXPanel();
        this.colorText = new TextField();
    }

    @Test
    public void colorChangeTest() {

        // Cases that have to do with name
        colorText.setText("Ammar Chishti");
        MyColor.colorChange(colorText, MyNameValidator.isValidName(colorText));
        assertEquals("-fx-text-inner-color: black;", colorText.getStyle());

        colorText.setText("Ammar");
        MyColor.colorChange(colorText, MyNameValidator.isValidName(colorText));
        assertEquals("-fx-text-inner-color: red;", colorText.getStyle());


        // Cases that have to do with number
        colorText.setText("(333) 333-3333");
        MyColor.colorChange(colorText, MyNumberValidator.isValidNumber(colorText));
        assertEquals("-fx-text-inner-color: black;", colorText.getStyle());

        colorText.setText("333");
        MyColor.colorChange(colorText, MyNumberValidator.isValidNumber(colorText));
        assertEquals("-fx-text-inner-color: red;", colorText.getStyle());

    }

}
