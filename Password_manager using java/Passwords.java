

import java.security.SecureRandom;
import java.util.HashMap;
import java.util.Map;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Passwords{


    String generatePass(int size){

        SecureRandom secureRandom = new SecureRandom();
    
        StringBuffer pass = new StringBuffer(getRandomName());
        String uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lowercase = uppercase.toLowerCase();
        String specials = "!@#$%^&*()";
        String numbers = "0123456789";

        

        while (pass.length() <= size){
            pass.append(specials.charAt(secureRandom.nextInt(10)));
            pass.append(numbers.charAt(secureRandom.nextInt(10)));
            pass.append(getRandomName());
        }

        return (pass.substring(0, size));
    }


    String suffleString(String s){

        SecureRandom secureRandom = new SecureRandom();
        StringBuffer pass = new StringBuffer(s);
        
        int counter = 1;
        while (counter <= 13){

            int index = secureRandom.nextInt(pass.length());
            char element = pass.charAt(index);

            int index2 = secureRandom.nextInt(pass.length());
            char element2 = pass.charAt(index2);

            pass.setCharAt(index, element2);
            pass.setCharAt(index2, element);

            counter++;
        }

        return pass.toString();
    }


    int checkStrength(String pass){

        int score = 0;
        if (pass.length()  >= 12){
            score += 1;
        }

        else{
            System.out.println("--Suggested to increse length of password by 12.");
        }

        if (pass.matches(".*\\d.*")){
            score += 1;
        }

        else{
            System.out.println("--Suggested to add numbers in password");

        }

        if (pass.matches(".*[!@#$%^&*()].*")){
            score += 1;
        }

        else{
            System.out.println("--Suggested to add special characters in password.");
        }

        if (pass.matches(".*[a-z].*")){
            score += 1;
        }

        else{
            System.out.println("--Suggested to add lowercase characters.");
        }

        if (pass.matches(".*[A-Z].*")){
            score +=1;
        }

        else{
            System.out.println("--Suggested to add uppercase characters.");
        }


        if (score == 5){
            System.out.println("Excellent password");
            System.out.println("There is no suggestion on this password.");
        }

        return score;

    }




    void copyPass(String pass){
        Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
        StringSelection selection = new StringSelection(pass);
        System.out.println("Password Copied");
        clipboard.setContents(selection, null);
    }
    



    String getRandomName(){


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
                        return (value);
                    }
                }

                randomNum--;
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "";
    }

}