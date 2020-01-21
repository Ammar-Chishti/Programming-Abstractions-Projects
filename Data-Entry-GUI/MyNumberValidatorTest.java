package sample;

import javafx.embed.swing.JFXPanel;
import javafx.scene.control.TextField;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertFalse;

public class MyNumberValidatorTest {

    JFXPanel p;
    TextField numberText;

    @Before
    public void setUp() {
        this.p = new JFXPanel();
        this.numberText = new TextField();
    }

    @Test
    public void setGrayedOutTexttoNameTest() {
        MyNumberValidator.setGrayedOutTexttoNumber(numberText);
        assertEquals("Number", numberText.getPromptText());
    }

    @Test
    public void isValidNameTest() {
        // Cases that are true
        numberText.setText("(333) 333-3333");
        assertTrue(MyNumberValidator.isValidNumber(numberText));
        numberText.setText("(666) 666-6666");
        assertTrue(MyNumberValidator.isValidNumber(numberText));

        //Cases that are false
        numberText.setText("888 888-8888");
        assertFalse(MyNumberValidator.isValidNumber(numberText));
        numberText.setText("(555) 555 5555");
        assertFalse(MyNumberValidator.isValidNumber(numberText));
        numberText.setText("25");
        assertFalse(MyNumberValidator.isValidNumber(numberText));


    }





}
