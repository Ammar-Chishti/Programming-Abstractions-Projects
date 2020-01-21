package Homework3;
import java.util.*;
import java.util.stream.*;
import java.lang.*;

public class FunctionalUtils {

    /**
     * @param strings: The input collection of <code>String</code>s.
     * @return         A collection of <code>String</code>s that start with a
     *                 capital letter (i.e., 'A' through 'Z').
     */
    public static Collection<String> capitalized(Collection<String> strings) {
        return strings.stream().filter(s -> !s.equals("") && Character.isUpperCase(s.charAt(0))).collect(Collectors.toList());
    }

    /**
     * Find and return the longest <code>String</code> in a given collection of <code>String</code>s.
     *
     * @param strings: The given collection of <code>String</code>s.
     * @param from_start: A <code>boolean</code> flag that decides how ties are broken.
     *                    If <code>true</code>, then the element encountered earlier in the
     *                    iteration is returned, otherwise the element encountered later is returned.
     *
     * @return            The longest <code>String</code> in the given collection, where ties are broken based on <code>from_start</code>.
     */
    public static String longest(Collection<String> strings, boolean from_start) {
        return strings.stream().reduce((one, two) -> one.length() > two.length() ? one : from_start && one.length() == two.length() ? one : two).orElse(null);
    }

    /**
     * Find and return the least element from a collection of given elements that are comparable
     *
     * @param items:        The given collection of elements
     * @param from_start:   a <code>boolean</code> flag that decides how ties are broken.
     *                      If <code>true</code>, then the element encountered earlier in the iteration is returned,
     *                      otherwise the element encountered later is returned.
     * @param <T>           The type parameter of the collection (i.e., the item are all of type T)
     * @return              The least element in <code>items</code>, where ties are broken based on <code>from_start</code>
     */
    public static <T extends Comparable<T>> T least(Collection<T> items, boolean from_start) {
        return items.stream().reduce((one, two) -> one.compareTo(two) < 0 ? one : from_start && one.compareTo(two) == 0 ? one : two).orElse(null);
    }

    /**
     * Flattens a map to a stream of <code>String</code>s, where each element of the list
     * is formatted as "key -> value"
     *
     * @param aMap:         The specified input map
     * @param <K>:          The type parameter of keys in <code>aMap</code>
     * @param <V>:          The type parameter of values in <code>aMap</code>
     * @return              The flattened list representation of <code>aMap</code>
     */
    public static <K, V> List<String> flatten(Map<K, V> aMap) {
        return aMap.entrySet().stream().map(kvEntry -> kvEntry.getKey().toString() + " -> " + kvEntry.getValue().toString()).collect(Collectors.toList());
    }

}
