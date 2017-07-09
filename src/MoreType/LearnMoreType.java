package MoreType;

/**
 * Created by wangchao88 on 2017/7/9.
 * 多态学习
 * 1、覆盖只发生在函数上，与变量没关系
 * 一、成员函数
 * 编译时：参考引用型变量所属的类中是否有调用的函数，有：编译通过 没有：编译失败
 * 运行时：参考的是对象所属的类中是否有调用的函数
 * 注意：上述只针对非静态方法
 *      静态方法不需要对象可以直接用所属类进行调用，对象是哪个引用类的，就运行该类的方法
 * 二、成员变量
 * 编译时：参考引用型变量所属的类中是否有调用的成员变量，有：编译通过 没有：编译失败
 * 运行时：参考引用型变量所属的类中是否有调用的成员变量，并运行该所属类中的成员变量
 *
 */
//父类
abstract class Animal{
    int age=8;
    abstract void eat();
    void baseFunc(){
        System.out.println("Animal的方法");
    }
}
//子类
class Dog extends Animal{
    @Override
    void eat(){
        System.out.println("狗啃骨头");
    }
    void lookHome(){
        System.out.println("狗看家");
    }
}
//子类
class Cat extends Animal{
    int age=10;
    @Override
    void eat(){
        System.out.println("猫吃鱼");
    }
    void catchMouse(){
        System.out.println("猫抓老鼠");
    }
}
//接口类多态
interface Test1{
    void test1();
}
//
class Test2 implements Test1{
    @Override
    public void test1(){
        System.out.println("这是test1");
    }
}
public class LearnMoreType {
    public static void main(String args[]){
        Cat cat1=new Cat();
        Cat cat2=new Cat();
        Cat cat3=new Cat();
        catFunc(cat1);
        Dog dog1=new Dog();
        Dog dog2=new Dog();
        Dog dog3=new Dog();
        //自助类型提升,猫对象提升了动物类型，但是猫的特有方法无法访问,限制对特有功能的访问（向上转型）
        Animal cat=new Cat();
        System.out.println((cat.age)); //转化为动物类型，使用的成员变量为父类的成员变量
        //如果要使用猫的特有方法，向下转型
        Cat cat4=(Cat)cat;
        cat4.catchMouse();
        //cat.baseFunc();Animal cat=new Cat();这样定义的是猫的对象，无法使用Animal的方法
        //要想使用Animal的方法，可以向上转型
        Animal cat5=(Animal)cat;
        cat.baseFunc();
        //接口类型的引用
        Test1 test1=new Test2();
        useTest2(test1);

    }
    public static void catFunc(Animal a){   //声明a为Animal类型，即a = new (子类)
        a.eat();
        if (a instanceof Cat){
            ((Cat) a).catchMouse();
        }
        else if (a instanceof Dog){
            ((Dog) a).lookHome();
        }
        }
    //
    public static void useTest2(Test1 a){ //Test2 a = new (子类)
        a.test1();
    }
    }