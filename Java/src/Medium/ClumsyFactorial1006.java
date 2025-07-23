package Medium;

import java.util.LinkedList;
import java.util.List;

public class ClumsyFactorial1006{

    public int clumsy(int n) {
        List<Integer> stack = new LinkedList<>();
        int ops = 0;

        for(int i=n; i > 0; i--){
            if(!stack.isEmpty()){
                int last;
                if(ops == 0){
                    last = stack.removeLast();
                    stack.addLast(last * i);
                }
                if(ops == 1){
                    last = stack.removeLast();
                    stack.addLast(last / i);
                }
                if(ops == 2){
                    last = stack.removeLast();
                    stack.addLast(last + i);
                }
                if(ops == 3){
                    stack.addLast(-i);
                }
                ops++;
                ops %= 4;
            }
            else{
                stack.addLast(i);
            }
        }

        int total = stack.getFirst();
        for(Integer num: stack.subList(1, stack.size())){
            // System.out.println(num);
            total += num;
        }

        return total;
    }


    public static void main(String[] args) {
        int c = 4;
        System.out.println(new ClumsyFactorial1006().clumsy(c));
        c = 10;
        System.out.println(new ClumsyFactorial1006().clumsy(c));
        c = 15;
        System.out.println(new ClumsyFactorial1006().clumsy(c));
    }
}