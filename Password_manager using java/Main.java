import java.util.Scanner;

public class Main{

    static String start(int size){

        if (size < 10){
            return "";
        }

        Passwords pass = new Passwords();
        String mypass = pass.generatePass(size);
        return mypass;

    }

    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        Passwords obj_pass = new Passwords();
        String my_password = start(12);
        System.out.println("Your password = "+my_password);
        obj_pass.copyPass(my_password);



    
        try{
       
            int choice = 0;
            while (choice != 9){
                System.out.print("check password strength\t(1) ");
                choice = sc.nextInt();
                if (choice == 1){
                    System.out.print("Enter your password: ");
                    obj_pass.checkStrength(sc.next());
                    }
                }
            } 

            catch (Exception e){
                System.out.println("Please enter valid option.");
            }
    }
}