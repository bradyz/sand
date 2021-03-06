import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FileOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Map.Entry;

public class EffectsTest { public static void main(String args[]) {

    ArrayList<File> fileList = new ArrayList<File>();
    Map<Integer, Map<String, Integer>> colorVals = new HashMap<Integer, Map<String, Integer>>();
    int numInputs;
    int len = 0;
    int width = 0;
    String fileName = "";
    Scanner fileInput;
    Scanner keyboard = new Scanner(System.in); 

    System.out.println("Enter number of input files: ");
    numInputs = keyboard.nextInt();

    keyboard.nextLine();

    for(int n = 0; n < numInputs; n++) {
      System.out.println("Enter a file name: ");
      fileName = keyboard.nextLine();

      File f = new File(fileName);
      fileList.add(f);
    }

    for(int n = 0; n < fileList.size(); n++)
    {
      try {
        fileInput = new Scanner(new FileReader(fileList.get(n)));
        fileInput.nextLine();
        len = fileInput.nextInt();
        width = fileInput.nextInt();
        fileInput.nextLine();
        String range = fileInput.nextLine();

        int val = 0;
        String line = "";

        while(fileInput.hasNextLine())
        {
          Map<String, Integer> tmpEntry = new HashMap<String, Integer>();
          line = fileInput.nextLine();
          if(!colorVals.containsKey(val)) {
            tmpEntry = new HashMap<String, Integer>();
            tmpEntry.put(line, 1);
          }
          else {
            tmpEntry = colorVals.get(val);
            if(!tmpEntry.containsKey(line)) {
              tmpEntry.put(line, 1);
            }
            else {
              tmpEntry.put(line, tmpEntry.get(line) + 1);
            }
          }
          colorVals.put(val, tmpEntry);
          val++;
        }
      } 
      catch (Exception ex) {
        //solid exception handling right here
        ex.printStackTrace();
      }
    }

    System.out.println("Output File: ");
    String writeFile = keyboard.nextLine();

    try {
      FileWriter fw = new FileWriter(writeFile);

      fw.write("P3\n");
      fw.write(len + " " + width + "\n");
      fw.write("255\n");

      int pos = 0;
      String correct = "";
      /* for all animals */
      /* int count = 4; */
      int count = 0;

      Map<String, Integer> tmp = new HashMap<String, Integer>();

      for(Entry<Integer, Map<String,Integer>> posVal : colorVals.entrySet()) {
        pos = posVal.getKey();
        tmp = posVal.getValue();

        for(Entry<String, Integer> valCount : tmp.entrySet()) {

          if(valCount.getValue() > count) {
            correct = valCount.getKey();
            count = valCount.getValue();
          }
        }

        fw.write(correct + "\n");
        /* fw.write(new StringBuilder(correct).reverse().toString() + "\n"); */
        /* for all animals */
        /* count = 4; */
        count = 0;
      }

      fw.close();
    } catch (Exception ex) {
      ex.printStackTrace();
    }
  }
}
