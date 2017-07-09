package Test;

/**
 * Created by wangchao88 on 2017/7/6.
 */
public class test1 {
    public static void main(String args[]){
        Integer i1=128;
        Integer i2=128;
        System.out.println(i1==i2);
        System.out.println(i1.equals(i2));
        Integer i3=127;
        Integer i4=127;
        System.out.println(i3==i4);
        System.out.println(i1.equals(i2));
    }
}
