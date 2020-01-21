package sample;

import javafx.embed.swing.JFXPanel;
import javafx.scene.control.TextField;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class MyNameValidatorTest {

    JFXPanel p;
    TextField nameText;

    @Before
    public void setUp() {
        this.p = new JFXPanel();
        this.nameText = new TextField();
    }

    @Test
    public void setGrayedOutTexttoNameTest() {
        MyNameValidator.setGrayedOutTexttoName(nameText);
        assertEquals("Name", nameText.getPromptText());
    }

    @Test
    public void isValidNameTest() {
        // Cases that are true
        nameText.setText("Ammar Chishti");
        assertTrue(MyNameValidator.isValidName(nameText));
        nameText.setText("A C");
        assertTrue(MyNameValidator.isValidName(nameText));

        //Cases that are false
        nameText.setText("Ammar Chishti Man");
        assertFalse(MyNameValidator.isValidName(nameText));
        nameText.setText("Ammar");
        assertFalse(MyNameValidator.isValidName(nameText));
        nameText.setText("Ammar ChiShti");
        assertFalse(MyNameValidator.isValidName(nameText));

    }


}
