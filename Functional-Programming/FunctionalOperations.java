package Homework3;

import java.util.*;
import java.util.function.BiFunction;
import java.util.function.Function;


public class FunctionalOperations {

    public static NamedBiFunction add = new NamedBiFunction<Double, Double, Double>() {

        @Override
        public String name() {
            return "add";
        }

        @Override
        public Double apply(Double o, Double o2) {

            return o + o2;

        }

    };

    public static NamedBiFunction diff = new NamedBiFunction<Double, Double, Double>() {

        @Override
        public String name() {
            return "diff";
        }

        @Override
        public Double apply(Double o, Double o2) {
            return o - o2;
        }

    };

    public static NamedBiFunction mult = new NamedBiFunction<Double, Double, Double>() {

        @Override
        public String name() {
            return "mult";
        }

        @Override
        public Double apply(Double o, Double o2) {
            return o * o2;
        }

    };

    public static NamedBiFunction div = new NamedBiFunction<Double, Double, Double>() {

        @Override
        public String name() {
            return "div";
        }

        @Override
        public Double apply(Double o, Double o2) {

            if (o2 == 0) {
                throw new ArithmeticException();
            }

            else {
                return o / o2;
            }

        }

    };


    /**
     * Applies a given list of bifunctions -- functions that take two arguments of a
     * certain type, and produce a single instance of that type -- to a list of
     * arguments of that type. The functions are applied in an iterative manner, and
     * the result of each function is stored in the list in an iterative manner as
     * well, to be used by the next bifunction in the next iteration.
     * For example, given
     * List<Integer> args = [1,1,3,0,4], and
     * List<BiFunction<Double, Double, Double>> bfs = [add, multiply, add, divide],
     * <code>zip(args, bfs)</code> will proceed iteratively as follows:
     * - index 0: the result of add(1,1) is stored in args[1] to yield args = [1,2,3,0,4]
     * - index 1: the result of multiply(2,3) is stored in args[2] to yield args = [1,2,6,0,4]
     * - index 2: the result of add(6,0) is stored in args[3] to yield args = [1,2,6,6,4]
     * - index 3: the result of divide(6,4) is stored in args[4] to yield args = [1,2,6,6,1]
     *
     * @param args: the arguments over which <code>bifunctions</code> will be iteratively applied.
     * @param bifunctions: the given list of bifunctions that will iteratively be applied on the <code>args</code>.
     * @param <T>: the type parameter of the arguments (e.g., Integer, Double)
     * @return the last element in <code>args</code>, the final result of all the bifunctions being applied in sequence.
     */
    public static <T> T zip(List<T> args, List<NamedBiFunction<T, T, T>> bifunctions) {

        int i = 0;
        while (i < bifunctions.size()) {
            NamedBiFunction one = bifunctions.get(i);
            args.set(i+1, (T) one.apply(args.get(i), args.get(i+1)));
            i++;
        }
        return args.get(args.size() - 1);   //Returning the last element in args
    }


    static class FunctionComposition<T, U, V> {
        BiFunction<Function<T, U>, Function<U, V>, Function<T, V>> composition = (Function<T, U> one, Function<U, V> two) -> one.andThen(two);
    }


    public interface NamedBiFunction<T, U, R> extends BiFunction<T, U, R> {
        String name();
    }


}
