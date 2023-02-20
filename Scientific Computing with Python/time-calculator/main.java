public class main {
    public static void main(String[] args) {
        time_calculator obj = new time_calculator();
        String startTime = "3:30 PM";
        String durationTime = "2:15";
        String startingDay = "Monday";
    
        String newTime = obj.addTime(startTime, durationTime, startingDay);
        System.out.println(newTime);
    }
    
}
