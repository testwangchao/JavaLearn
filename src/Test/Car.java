package Test;

/**
 * Created by Administrator on 2017/7/6.
 */
public class Car {
    private int color;
    private int speed;
    private Engine engine;
    public Car(int color,int speed){
        this.color=color;
        this.speed=speed;
    }
    public Car(int color,int speed,Engine engine){
        this.color=color;
        this.speed=speed;
        this.engine=engine;
    }
    public void startup(){
        System.out.println("启动");
    }
    public void run(){
        int speed=this.speed;
        this.startup();
        System.out.println("速度："+ speed);
    }
    public static void main(String args[]){
        /*
        Car car = new Car(0xffffff,100);
        System.out.println(car);
        car.run();
        */
        new Car(0xffffff,100).run();
    }
}

