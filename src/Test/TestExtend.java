package Test;

/**
 * Created by Administrator on 2017/7/6.
 * 继承
 */
class Graph{
    String name;
    public Graph(){}
    public Graph(String name){
        this.name=name;
    }
    public void show(){
        System.out.println("I'm a graph");
    }
    //返回name
    public String name(){
        return this.name;
    }
}
/*TestSon是Graph的子类
可以继承父类的所有构造方法及非private成员方法、及所有非private成员变量
 */
class TestSon extends Graph{
    int age;
    public TestSon(){
        //super表示对父类对象的引用，
        super();
    }
    public TestSon(int age){
        this.age=age;
    }
    public TestSon(String name,int age){
        this.age=age;
        //继承父类的name成员变量
        this.name=name;
        String str = "My name is %s,and my age is %d years old!";
        System.out.println(String.format(str,name,age ));
    }
    //方法覆盖：如果子类中有和父类中非private的同名方法，且返回类型和参数表也完全相同，就会覆盖从父类继承来的方法。
    public void show(){
        System.out.println("This is 方法覆盖");
    }
}
public class TestExtend {

    public static void main(String args[]){
        TestSon son = new TestSon();
        son.show();
    }
}
