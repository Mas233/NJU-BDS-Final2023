package src;

import java.io.*;

import java.util.ArrayList;


public class LinesSelector {
    /**
     * temporary storage for the lines of the file
     */
    private final static ArrayList<String> lines= new ArrayList<>();

    /**
     * number of lines to be stored
     */
    private final static int COUNT=30;


     public static void selectLines(String src,String target) {
         readToLines(src);
         //lines.forEach(System.out::println);
         writeToDest(target);

     }
     /**
      * read lines from the source file and sort them by length
      * save sorted lines in *lines*
      * @param src source file name
     */

     private static void readToLines(String src){
         try{
             FileReader fileReader = new FileReader(src);
             BufferedReader bufferedReader= new BufferedReader(fileReader);
             String line;
             while ((line = bufferedReader.readLine()) != null) {
                 if(lines.isEmpty())lines.add(line);
                 else{
                     int i=lines.size();
                     while(i>0){
                         if(line.length()>lines.get(i-1).length()){
                             lines.add(i,line);
                             break;
                         }
                         i--;
                     }
                 }
             }
         } catch (IOException e) {
             System.err.println("Error reading the file: " + e.getMessage());
         }
     }

    /**
     * write the last COUNT lines of the file to the target file
     * @param target target file name
     */
     private static void writeToDest(String target){
         try {
             /*clear file*/
             FileWriter fileWriter = new FileWriter(target, false);
             fileWriter.write("");
             fileWriter.close();

             fileWriter = new FileWriter(target, true);
             BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

             String line;
             for (int i = 1; i <= COUNT; i++) {
                 line = lines.get(lines.size() - i);
                 bufferedWriter.write(line);
                 bufferedWriter.newLine();

                 bufferedWriter.flush();
                 //System.out.println("Line "+i+" written: "+line);
             }


         } catch (IOException e) {
             System.err.println("Error writing to the file: " + e.getMessage());
         }
     }


}
