import src.LinesSelector;


public class Main {

    /**
     * source file name
     */
    private final static String SOURCE_FILE = "rotowire.txt";
    /**
     * name of file where chosen lines are stored
     */
    private final static String TARGET_FILE = "chosen.txt";


    public static void main(String[] args){

        LinesSelector.selectLines(SOURCE_FILE,TARGET_FILE);

    }
}
