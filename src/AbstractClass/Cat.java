package AbstractClass;

/**
 * Created by Administrator on 2017/7/6.
 * 子类cat实现父类Animal的抽象方法
 */
public class Cat extends Animal {
    @Override
    public void cry(){
        System.out.println("This s a cat");

    }
    public void normalFunc(){
        System.out.println("普通方法");
    }
}
