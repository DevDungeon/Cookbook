module com.devdungeon.mavenjavaexample {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.devdungeon.mavenjavaexample to javafx.fxml;
    exports com.devdungeon.mavenjavaexample;
}
