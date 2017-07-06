package Test;

/**
 * Created by Administrator on 2017/7/5.
 */
class Man {
    void test(){
        System.out.println("test");
    }
}
public class Demo {
    private int a;
    private String b;
    public Demo(){
        System.out.println("构造方法");
        this.a=10;
        this.b="测试";
        System.out.println(a+b);
    }
    public void setA(int a){
        this.a=a;
    }
    public int getA(){
        return this.a;
    }
        public static void main(String args[]) {
            Demo demo=new Demo();
            //demo.setA(5);
            //System.out.println(demo.getA());
            demo.setA(5);
        }
}

