import java.util.ArrayList;
import java.util.List;

public class App {

    public static void temp(List<Integer> h){
        System.out.println(System.identityHashCode(h));
        System.out.println(h);
        h.add(4);
    }
    public static void main(String[] args) throws Exception {
        List<Integer> h = new ArrayList<>();
        h.add(3);
        h.add(5);
        System.out.println(System.identityHashCode(h));
        System.out.println(h);
        temp(new ArrayList<>(h));
        System.out.println(System.identityHashCode(h));
        System.out.println(h);
    }
}
