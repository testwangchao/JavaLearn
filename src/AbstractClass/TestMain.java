package AbstractClass;

/**
 * Created by Administrator on 2017/7/6.
 */
public class TestMain {
    public static void main(String args[]){
        //抽象类Animal不能被实例化，应由子类进行实例化，它只需要一个引用
        Animal cat = new Cat();
        cat.cry();
        System.out.println(cat.test());
    }
}
