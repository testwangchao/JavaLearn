package InterfaceClass;

import AbstractClass.Animal;

/**
 * Created by Administrator on 2017/7/6.
 */
public class TestMain extends Animal{
    //接口
    public void func() {
        System.out.println();
    }
    //抽象类
    @Override
    public void cry(){

    }
    public static void main(String args[]){
        Animal test = new TestMain();
        //test.func();
    }


}
