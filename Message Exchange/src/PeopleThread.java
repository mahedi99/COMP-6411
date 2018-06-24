import java.util.Random;

public class PeopleThread extends Thread {
    Exchange master = new Exchange();
    public PeopleThread(String threadName){
        super(threadName);
    }


    public void getIntroMsg(PeopleThread sender){
        long currentTime = System.nanoTime();
        master.printIntroInMaster(this.getName() + " got intro message from " + sender.getName(), currentTime);
        try {
            sender.sleep(new Random().nextInt(100) + 1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        sender.sendReply(this, currentTime);
    }

    public void sendReply(PeopleThread sender, long time){
        master.printReplyInMaster(this.getName() + " got reply message from " + sender.getName(), time);
    }


    @Override
    public void run() {
        synchronized (this) {
            try {
                sleep(new Random().nextInt(100) + 1);
            } catch (InterruptedException e) { }

            String[] receivers = master.userHM.get(getName()).split(",");
            for (String receiver : receivers) {
                master.threadHM.get(receiver).getIntroMsg(this);
            }

            terminateThread();
        }
    }

    public void terminateThread(){
        if(master.threadFinishedCounter < master.threadHM.size()) {
            master.threadFinishedCounter ++;
            synchronized (master.threadHM) {
                try {
                    master.threadHM.wait();
                    System.out.println("\nProcess " + getName() + " has received no calls for 1 second, ending...");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
        else {
            synchronized (master.threadHM){
                try {
                    sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("\nProcess " + getName() + " has received no calls for 1 second, ending...");
                master.threadHM.notifyAll();
            }
            try {
                sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            master.getNotifyInMaster();
        }
    }
}
