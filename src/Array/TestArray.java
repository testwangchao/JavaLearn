package Array;
import java.util.Arrays;
/**
 * Created by wangchao88 on 2017/7/6.
 */
public class TestArray {
    public void testArray(){
        //创建数组对象
        int[] array=new int[]{1,3,45,6};
        for (int i=0;i<=array.length-1;i++){
            System.out.println(String.format("arr[%d]=%d", i,array[i]));
        }
    }
    //创建一个数组容器，但不确定具体数据
    public void testArray2(){
        int[] array = new int[3];
        array[0]=2;
        System.out.println(array[0]);
    }
    //取出数组最大值和最小值
    public int testArray3(int[] arr){

        int a=arr[0];
        for (int i=1;i<=arr.length-1;i++){
            if (arr[i]>a){
            a=arr[i];
            }
        }
        return a;
        }
    //最小值
    public int testArray4(int[] arr){
        int min=0;
        for (int i=0;i<arr.length;i++){
            if (arr[i]<arr[min+1]){
                min=i;
            }
        }
        return arr[min];
    }
    //冒泡排序
    public int[] testArray5(int[] arr){
        //表示从第一个数字开始比较
        int temp;
        for(int i=0;i<arr.length-1;i++){
            //表示第一个数字与剩余的数字比较
            for (int k=i+1;k<arr.length;k++){
                if (arr[i]>arr[k]){
                    temp=arr[i];
                    arr[i]=arr[k];
                    arr[k]=temp;
                }
            }
        }
        return arr;
    }
    public static void main(String args[]){
        TestArray testArray=new TestArray();
        //testArray.testArray();
        //testArray.testArray2();
        int[] array={-1,4,-45,8};
        System.out.println(array);
        System.out.println(Arrays.toString(testArray.testArray5(array)));
        }

    }
