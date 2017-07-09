package AbstractClass;

import javax.print.attribute.standard.Destination;

/**
 * Created by Administrator on 2017/7/6.
 */
public class Inner {
    private String name;
    private int age;
    private static String sex;
    //设置成员变量
    public void setName(String name,int age,String sex){
        this.name=name;
        this.age=age;
        this.sex=sex;
    }
    //获取成员变量name的值
    public String getName(){
        return this.name;
    }
    //获取age的值
    public int getAge(){
        return this.age;
    }
    //获取成员内部类
    public InnerClass getInnerClass(){
        return new InnerClass();
    }
    //创建成员内部类InnerClass
    public class InnerClass{
        public InnerClass(){
        }
        //内部类的方法，可以调用外部类的方法及变量
        public void display(){
            //通过Inner.this访问外部类的方法
            System.out.println(getName());
            System.out.println("name："+getName()+" ,age："+getAge());
        }
    }
    //局部内部类
    //定义在方法内
    public void func(){
        class TestInner{
            public void innerFunc(){
                System.out.println("这是一个使用方法实现的局部类");
            }
        }
        new TestInner().innerFunc();
    }
    //静态内部类
    static class TestStatic{
        //静态内部类可以存在静态成员，其它非静态类不能存在
        static String testName="静态变量";
        static String sex2;
        //静态方法
        public static void func(){
            //只能访问外部类静态的方法或变量
            sex2=Inner.sex;
            System.out.println(sex2+testName);
        }

    }
    //匿名内部类的实现方法
    public void anonymousClass(){
        //匿名内部类（父类为抽象类）
        new Animal(){
            @Override
            public void cry(){
                System.out.println("匿名内部类");
            }
        }.cry();
    }
    public void anonymousClass2(){
        //父类为普通类
        Cat cat =new Cat(){
          public void normalFunc(){
              System.out.println("重写父类方法");
          }
        };
        cat.normalFunc();
    }
    public static void main(String args[]){
        Inner inner = new Inner();
        inner.setName("Test",10,"男");
        /*引用内部类的方法：
         1、指明这个对象的类型Inner.InnerClass
         2、利用外部类的对象通过new来创建内部类inner.new InnerClass()
         */
        Inner.InnerClass innerClass = inner.new InnerClass();
        innerClass.display();
        //通过get构造内部类的对象
        Inner.InnerClass innerClass1 = inner.getInnerClass();
        innerClass1.display();
        //调用局部类
        inner.func();
        //调用静态内部类
        Inner.TestStatic.func();
        //调用匿名内部类
        inner.anonymousClass();
        inner.anonymousClass2();
    }
}
