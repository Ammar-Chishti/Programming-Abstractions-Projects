package sample;

import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXMLLoader;
import javafx.geometry.HPos;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.StackPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class DataEntryGUI extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {

        GridPane profiles = new GridPane();
        profiles.setAlignment(Pos.CENTER);
        profiles.setHgap(10);
        profiles.setVgap(10);


        // Creating the text fields
        TextField row0col0 = new TextField();
        MyNameValidator.setGrayedOutTexttoName(row0col0);
        TextField row1col0 = new TextField();
        MyNameValidator.setGrayedOutTexttoName(row1col0);
        TextField row2col0 = new TextField();
        MyNameValidator.setGrayedOutTexttoName(row2col0);
        TextField row0col1 = new TextField();
        MyNumberValidator.setGrayedOutTexttoNumber(row0col1);
        TextField row1col1 = new TextField();
        MyNumberValidator.setGrayedOutTexttoNumber(row1col1);
        TextField row2col1 = new TextField();
        MyNumberValidator.setGrayedOutTexttoNumber(row2col1);

        profiles.add(row0col0, 0, 0);
        profiles.add(row1col0, 0, 1);
        profiles.add(row2col0, 0,2);
        profiles.add(row0col1, 1, 0);
        profiles.add(row1col1, 1, 1);
        profiles.add(row2col1, 1, 2);

        Button createProfiles = new Button("Create Profiles");
        createProfiles.setDisable(true);

        createProfiles.setOnAction(e->{
            MyButtonController.buttonCheck(row0col0, row1col0, row2col0, row0col1, row1col1, row2col1);
        });

        MyButtonController.addListenerAll(row0col0, row1col0, row2col0, row0col1, row1col1, row2col1, createProfiles);
        profiles.add(createProfiles,0,3,2,1);
        GridPane.setHalignment(createProfiles, HPos.CENTER);


        //Creating the scene to be displayed
        Scene scene = new Scene(profiles, 500, 500);

        //Ending the program and displaying
        primaryStage.setTitle("Data Entry GUI");
        primaryStage.setScene(scene);
        primaryStage.show();

    }


    public static void main(String[] args) {
        launch(args);
    }


}
