package UnixFileSearchSystem.src;
import java.util.List;
import UnixFileSearchSystem.src.Models.File;
import UnixFileSearchSystem.src.Models.FileSearch;
import UnixFileSearchSystem.src.Models.EqualsOperator;
import UnixFileSearchSystem.src.Models.FileSearchCriteria;
import UnixFileSearchSystem.src.Models.AndPredicate;
import UnixFileSearchSystem.src.Models.RegexMatchOperator;
import UnixFileSearchSystem.src.Models.SimplePredicate;
import UnixFileSearchSystem.src.Models.FileAttribute;
import UnixFileSearchSystem.src.Models.LessThanOperator;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        File root = new File(0,
                "adam",
                "root",
                true);

        File a = new File(0,
                "adam",
                "a",
                false);

        File b = new File(0,
                "george",
                "b",
                false);

        root.addEntry(a);
        root.addEntry(b);

        final FileSearchCriteria criteria = new FileSearchCriteria(new AndPredicate(List.of(
                new SimplePredicate<>(FileAttribute.IS_DIRECTORY,
                        new EqualsOperator<>(), false)
                ,
                new SimplePredicate<>(FileAttribute.OWNER,
                        new RegexMatchOperator<>(), "ad.*"),
                new SimplePredicate<>(FileAttribute.SIZE,
                        new LessThanOperator<>(), 1)
        )));

        final FileSearch fileSearch = new FileSearch();
        final List<File> result = fileSearch.Search(root, criteria);

        System.out.println(result.size());
    }
}