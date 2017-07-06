package AbstractClass;
/**
 * Created by Administrator on 2017/7/6.
 * 抽象类
 */
//抽象动物类，需要具体的动物去实现抽象类的方法
public abstract class Animal implements InterfaceClass{
    //抽象方法,子类实现抽象方法时，参数、及方法类型必须与父类一致
    public abstract void cry();
    public int test(){
        return 1;
    }
    //接口类
    @Override
    public void func(){
        System.out.println("这是一个接口类的调用");
    }
}
