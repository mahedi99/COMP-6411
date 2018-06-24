import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Exchange {

    public static List<PeopleThread> peopleThreads;
    public static HashMap<String, PeopleThread> threadHM = new HashMap<>();
    public static HashMap<String, String> userHM = new HashMap<>();
    public static int threadFinishedCounter = 1;

    public static void main(String[] args) {
        List<String> userList = readData("calls.txt");
        peopleThreads = new ArrayList<>();
        if (userList.size() > 0){
            showCallsList(userList);

            List<String[]> tmpUsers = new ArrayList<>();
            for(String data : userList){

                String [] userArr = data.replaceAll("[.{}\\[\\]]","").split(" ");
                tmpUsers.add(userArr);

                String tmpUser = userArr[0].replace(",", "");

                PeopleThread tmpThread = new PeopleThread(tmpUser);
                threadHM.put(tmpUser, tmpThread);
                userHM.put(tmpUser, userArr[1]);
                tmpThread.start();
            }
        }
        else {
            System.out.println("Empty Data!");
        }
    }

    private static void showCallsList(List<String> userList) {
        System.out.println("\n** Calls to be made **");
        for (String data : userList) {
            String[] userArr = data.replaceAll("[.{}]", "").split(" ");
            System.out.println(userArr[0].replace(",", ": ") + userArr[1]);
        }
        System.out.println("\n");
    }

    private static List<String> readData (String file){
        List<String> dataList = new ArrayList<>();
        Scanner input = null;
        try {
            input = new Scanner(new File(file));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while (input.hasNextLine()) {
            String tmpData = input.nextLine();
            tmpData = tmpData.trim();
            if (tmpData != null && !tmpData.isEmpty()){
                dataList.add(tmpData);
            }
        }
        return dataList;
    }

    public void printIntroInMaster(String msg, long time) {
        System.out.println(msg + " [" + time + "]");
    }
    public void printReplyInMaster(String msg, long time) {
        System.out.println(msg + " [" + time + "]");
    }
    public void getNotifyInMaster(){
        System.out.println("\nMaster has received no replies for 1.5 seconds, ending...");
    }
}
