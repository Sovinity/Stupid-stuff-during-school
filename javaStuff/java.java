/*
Code by Jacob

Commended by MushroomEnder :ok_hand:
*/

import java.util.Scanner;
import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class java {
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
        } else if (inputL.equals("gui")){
          gui();
        } else if (inputL.equals("city")){
          
        } else if (inputL.equals("exit")) {
            System.exit(0);
        } else {
            System.out.println("I'm not programmed to understand :/");
        }
        
      }while (true);
    }
    private static void gui(){
      JFrame win = new JFrame("windoooow");
      win.setBounds(20, 20, 1000, 800);
      win.setLayout(null);
      win.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
      win.setVisible(true);

      Random rand = new Random();

      for (int i = 0; i < 5; i++) {
          win.add(new Rectangley(100+i*50, 60+i*30, 40, 40, new Color(rand.nextInt(255), rand.nextInt(255), rand.nextInt(255))), 0);
      }
    }
}