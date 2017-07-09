package Switch;
import java.util.Scanner;
/**
 * Created by wangchao88 on 2017/7/4.
 */
public class Switch {
    public void ifDemo() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number:");
        int number = input.nextInt();
        if (number == 0){
            System.out.println("This number is 0");
        }
        else if (number ==1){
            System.out.println("This number is 1");
        }
        else {
            System.out.println("非0非1");
        }
    }
    /*
    如果没有break，条件满足，会一直执行下面的内容，直到遇到break
    * */
    public void switchDemo(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a number:");
        int number = input.nextInt();
        switch (number){
            case 1:
                System.out.println("number 1");
                break;
            case 2:
                System.out.println("number 2");
            case 3:
                System.out.println("number 3");
            //default可有可无
            default:
                System.out.println("This is default");
        }
    }
    public static void main(String args[]) {
        /*
        char grade = '1';

        switch(grade)
        {
            case 'A' :
            case 'B' :
            case 'C' :
                System.out.println("良好");
                break;
            case 'D' :
                System.out.println("及格");
            case 'F' :
                System.out.println("你需要再努力努力");
                break;
            //default :
              //  System.out.println("未知等级");
        }
        System.out.println("你的等级是 " + grade);
    }
    */
        Switch sc = new Switch();
        sc.switchDemo();
    }
}