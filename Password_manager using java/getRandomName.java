import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.security.SecureRandom;


public class getRandomName {
    public static void main(String[] args) {
        String csvFile = "names.csv";
        String line = "";
        String csvDelimiter = ",";
        SecureRandom secureRandom = new SecureRandom();
        int randomNum = secureRandom.nextInt(200);

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                String[] data = line.split(csvDelimiter);

                for (String value : data) {
                    if (randomNum == 0){
                        System.out.println(value);
                        break;
                    }
                }

                randomNum--;
            }

            } catch (IOException e) {
                e.printStackTrace();
            }
    }
}