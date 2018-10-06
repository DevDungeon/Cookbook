Creating and Using Packages
===========================

# Creating

The package names relate directly to the directory structure. Dots in the 

# Call directly

    new com.devdungeon.packagename.MyClass()

# Importing and then calling

    import com.devdungeon.packagename.MyClass
    
    new MyClass();

# or the whole package. It will only include what is needed at compile time

    import com.devdungeon.packagename.*

    new MyClass()


# When compiling a program that imports package, the location of the packages
# must be set in the Class-Path. This can be set as a command line argument 

    javac -cp /path/to/dir:/or/to/Ajar.jar MyProgram.java

# Or the classpath can be set as an environment variable

    CLASSPATH=/path1/:/path/to/Some.jar:/path/to/dir/of/jars/*

# Reference:

- https://en.wikipedia.org/wiki/Classpath_(Java)