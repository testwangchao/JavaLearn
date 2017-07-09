package AbstractClass;

/**
 * Created by wangchao88 on 2017/7/9.
 */
public class Base {
    public void show(){
        System.out.println("这是show方法");
    }
}
class TestClass extends Base{
    public void show(Base a){
        if (a instanceof TestClass){}
    }
    public static void main(String args[]){
        Base test1 =new Base();
        test1.show();
        System.out.println(test1);
    }
}
