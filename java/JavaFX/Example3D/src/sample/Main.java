package sample;
// https://www.developer.com/java/data/3d-graphics-in-javafx.html
import javafx.application.Application;
import javafx.scene.*;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.Box;
import javafx.scene.shape.Sphere;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{

        // Create some shapes
        Box box = new Box();
        Sphere sphere = new Sphere(100);
        PhongMaterial material1 = new PhongMaterial();
        material1.setDiffuseColor(Color.BLUE);
        material1.setSpecularColor(Color.LIGHTBLUE);
        material1.setSpecularPower(10.0);
        sphere.setMaterial(material1);

        AmbientLight light=new AmbientLight(Color.AQUA);
        light.setTranslateX(-180);
        light.setTranslateY(-90);
        light.setTranslateZ(-120);
        light.getScope().addAll(box,sphere);

        PointLight light2=new PointLight(Color.RED);
        light2.setTranslateX(180);
        light2.setTranslateY(190);
        light2.setTranslateZ(180);
        light2.getScope().addAll(box,sphere);

        // Group things together
        Group group = new Group(sphere, box);
        group.getChildren().addAll(light,light2);

        // Create the scene with all the objects
        Scene scene = new Scene(group, 600, 600);

        // Setup camera
        scene.setFill(Color.BLACK);
        PerspectiveCamera camera =
                new PerspectiveCamera(true);
        camera.setNearClip(0.1);
        camera.setFarClip(1000.0);
        camera.setTranslateZ(-1000);
        scene.setCamera(camera);

        // Setup stage (window)
        primaryStage.setTitle("3D Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
