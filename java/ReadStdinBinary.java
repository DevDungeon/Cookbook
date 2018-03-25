class ReadStdinBinary
{
    public static void main(String[] args)
    {
        byte singleByte;

        singleByte = System.in.read();

        System.out.println(singleByte);
    }

}