package Test;

/**
 * Created by Administrator on 2017/7/6.
 * final修饰符
 */
public class TestFinal {
    private String title;
    private String text;
    private static int count=0;
    //final修饰的变量无法被改变
    public final static String DEFAULT_Text="什么内容有没有！";
    public TestFinal(){
        count++;
    }
    //final修饰的方法无法被子类进行覆盖
    public final static int getCount(){
        return count;
    }
    public static void main(String args[]){

    }
}
class Test2 extends TestFinal{
    /*子类覆盖getCount方法会报错
    public int getCount(){

    }
    */
}