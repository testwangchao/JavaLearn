package Test;

/**
 * Created by Administrator on 2017/7/5.
 * this的使用方法
 */
class Student{
    private String name;
    private int age;
    public void getInfo(){
        //this表示调用该函数的对象，对象=类的实例化
        System.out.println(this.name+this.age);
    }
    Student(String name,int age){
        this.name=name;
        this.age=age;
    }
    Student(String sex){
        //调用有参数的构造方法
        this("One",10);
        System.out.println("This is >>>>"+this);
    }
}
public class learnThis {

    public static void main(String args[]){
        Student stu1 = new Student("女");
        stu1.getInfo();
    }
}