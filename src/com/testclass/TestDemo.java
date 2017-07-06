package com.testclass;

/**
 * Created by Administrator on 2017/7/5.
 */
public class TestDemo {
    //实例变量（有默认值、可以通过构造方法改变）
    int var=5;
    //构造方法
    public TestDemo(int a){
        this.var=a;
    }
    public void testDemoA(){
        //var = 100;
        System.out.println(var);
    }
    public static void main(String args[]){
        TestDemo demo = new TestDemo(55);
        demo.testDemoA();
    }
}
