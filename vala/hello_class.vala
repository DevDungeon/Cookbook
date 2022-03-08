// compile with `valac hello_class.vala`
class Demo.HelloWorld : GLib.Object {

    public static int main(string[] args) {

        stdout.printf("Hello, World\n");

        return 0;
    }
}
