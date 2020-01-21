package sample;

import javafx.embed.swing.JFXPanel;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class MyButtonControllerTest {

    JFXPanel p;
    Button butt;

    @Before
    public void setUp() {
        this.p = new JFXPanel();
        this.butt = new Button();
    }

    @Test
    public void testListeners() {

        // Creating TextFields and Button
        butt = new Button();

        TextField a = new TextField();
        TextField b = new TextField();
        TextField c = new TextField();
        TextField d = new TextField();
        TextField e = new TextField();
        TextField f = new TextField();
        MyButtonController.addListenerAll(a, b, c, d, e, f, butt);

        a.setText("Not all are null");
        assertTrue(butt.isDisabled());
        b.setText("Not all are null");
        assertTrue(butt.isDisabled());
        c.setText("Not all are null");
        assertTrue(butt.isDisabled());
        d.setText("Not all are null");
        assertTrue(butt.isDisabled());
        e.setText("Not all are null");
        assertTrue(butt.isDisabled());
        f.setText("Not all are null");
        assertFalse(butt.isDisabled());
        f.setText("");
        assertTrue(butt.isDisabled());

    }

    @Test
    public void popUpWindowTest() {

        // Creating TextFields
        butt = new Button();

        TextField a = new TextField();
        TextField b = new TextField();
        TextField c = new TextField();
        TextField d = new TextField();
        TextField e = new TextField();
        TextField f = new TextField();

        assertEquals("Invalid Error Input", MyButtonController.invalidInputShow());


        assertFalse(a.isDisabled());
        assertFalse(b.isDisabled());
        assertFalse(c.isDisabled());
        assertFalse(d.isDisabled());
        assertFalse(e.isDisabled());
        assertFalse(f.isDisabled());

        a.setText("A C");
        b.setText("A C");
        c.setText("A C");
        d.setText("(333) 333-3333");
        e.setText("(333) 333-3333");
        f.setText("(333) 333-3333");

        assertEquals("Data Saved", MyButtonController.validInputShow(a, b, c, d, e, f));

        assertTrue(a.isDisabled());
        assertTrue(b.isDisabled());
        assertTrue(c.isDisabled());
        assertTrue(d.isDisabled());
        assertTrue(e.isDisabled());
        assertTrue(f.isDisabled());

    }










}
