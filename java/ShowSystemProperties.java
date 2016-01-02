class ShowSystemProperties {
    public static void main(String[] args) {
        System.getProperties().list(System.out);
    }
}

/* Example output

-- listing properties --
java.runtime.name=Java(TM) SE Runtime Environment
sun.boot.library.path=C:\Program Files\Java\jre1.8.0_66\bin
java.vm.version=25.66-b18
java.vm.vendor=Oracle Corporation
java.vendor.url=http://java.oracle.com/
path.separator=;
java.vm.name=Java HotSpot(TM) 64-Bit Server VM
file.encoding.pkg=sun.io
user.script=
user.country=US
sun.java.launcher=SUN_STANDARD
sun.os.patch.level=
java.vm.specification.name=Java Virtual Machine Specification
user.dir=D:\workspace\Cookbook\java
java.runtime.version=1.8.0_66-b18
java.awt.graphicsenv=sun.awt.Win32GraphicsEnvironment
java.endorsed.dirs=C:\Program Files\Java\jre1.8.0_66\lib...
os.arch=amd64
java.io.tmpdir=C:\Users\dtron\AppData\Local\Temp\
line.separator=

java.vm.specification.vendor=Oracle Corporation
user.variant=
os.name=Windows 10
sun.jnu.encoding=Cp1252
java.library.path=C:\ProgramData\Oracle\Java\javapath;C...
java.specification.name=Java Platform API Specification
java.class.version=52.0
sun.management.compiler=HotSpot 64-Bit Tiered Compilers
os.version=10.0
user.home=C:\Users\dtron
user.timezone=
java.awt.printerjob=sun.awt.windows.WPrinterJob
file.encoding=Cp1252
java.specification.version=1.8
user.name=dtron
java.class.path=.
java.vm.specification.version=1.8
sun.arch.data.model=64
java.home=C:\Program Files\Java\jre1.8.0_66
sun.java.command=ShowSystemProperties
java.specification.vendor=Oracle Corporation
user.language=en
awt.toolkit=sun.awt.windows.WToolkit
java.vm.info=mixed mode
java.version=1.8.0_66
java.ext.dirs=C:\Program Files\Java\jre1.8.0_66\lib...
sun.boot.class.path=C:\Program Files\Java\jre1.8.0_66\lib...
sun.stderr.encoding=cp437
java.vendor=Oracle Corporation
file.separator=\
java.vendor.url.bug=http://bugreport.sun.com/bugreport/
sun.cpu.endian=little
sun.io.unicode.encoding=UnicodeLittle
sun.stdout.encoding=cp437
sun.desktop=windows
sun.cpu.isalist=amd64

*/