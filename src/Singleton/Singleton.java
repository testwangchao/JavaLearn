package Singleton;

/**
 * Created by wangchao88 on 2017/7/9.
 */
public class Singleton {
    //私有构造函数
    private Singleton(){}
    //创建Singleton的对象
    private static Singleton instance = new Singleton();
    //得到唯一可用Singleton对象
    public static Singleton getInstance(){
        return instance;
    }
    public void show(){
        System.out.println("单例模式测试");
    }
}
class TestSingleton{

    public static void main(String args[]){
        Singleton test=Singleton.getInstance();
        test.show();
    }
}