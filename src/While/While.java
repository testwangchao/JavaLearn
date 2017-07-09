package While;

/**
 * Created by wangchao88 on 2017/7/4.
 */
public class While {
    //while
    public void whileDemo(){
        int i = 1;
        int sum=0;
        while (i<=10){
            sum+=i;
            i+=1;
        }
    System.out.println(sum);
    }
    //do while,不满足条件也会执行一次
    public void doDemo(int i){
        do {
            i++;
            System.out.println(i);
            System.out.println("Hello world");
        }while (i <=0);
    }
    //打印1-10数字的和
    public void forDemo(){
        int sum=0;
        for (int i=1;i<=10;i++){
            sum+=i;
            //System.out.println(i);
        }
        System.out.println(sum);
    }
    //九九乘法表
    public void nineTable(){
        for (int k=1;k<=9;k++){
            for (int i=1;i<=k;i++){
                System.out.print(i+"×"+k+"="+i*k+"\t");
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        While whileTest = new While();
        //whileTest.whileDemo();
        whileTest.nineTable();
    }
}
