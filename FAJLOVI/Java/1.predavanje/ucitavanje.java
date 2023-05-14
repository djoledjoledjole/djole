import java.util.Scanner;     //sam ucitava module, klikce se na crvenu klasu (Scanner ovde)

public class ucitavanje {
    public static void main(String[] args){
        int x;

        Scanner sc = new Scanner(System.in);     //system.in je input iz pajtona

        x = sc.nextInt();
        System.out.println(x);
        sc.close();
    }
}
