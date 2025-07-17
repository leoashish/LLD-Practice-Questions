package UnixFileSearchSystem.src.Models;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class FileSearch{

    public FileSearch(){

    }
    public List<File> Search(File root,
    FileSearchCriteria fileSearchCriteria){
        Deque<File> fileDeque = new ArrayDeque<>();
        fileDeque.addLast(root);
        List<File> result = new ArrayList<>();

        for(;!fileDeque.isEmpty();){
            File front = fileDeque.pop();
            if(fileSearchCriteria.isMatch(front)){
                result.add(front);
            }

            for(var entry:front.getEntries()){
                fileDeque.addLast(entry);
            }
        }

        return result;
    }
}
