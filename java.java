/*
Code by Jacob

Commended by MushroomEnder :ok_hand:
:)
*/

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello from Java! Type something to continue.");
        menu();
    }
    private static void menu(){
      Scanner scan = new Scanner(System.in);
      String input;
      String inputL;
      do{
        input = scan.nextLine();
        inputL = input.toLowerCase();

        if (inputL.equals("broken")){
          System.out.println("With the power of IFIXIT it shall be fixed");
        }else if (inputL.equals("hello")){
          System.out.println("Yes you exist. Now get on to something fun.");
        } else if (inputL.contains("snuggles") || inputL.contains("cuddles") || inputL.contains("cuddle") || inputL.contains("snuggle")) {
            System.out.println("If I try, I will get coffee on you :/");
        } else {
            System.out.println("I don't understand :/");
        }
        
      }while (!inputL.equals("exit"));
    }
}