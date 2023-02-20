import java.util.Arrays;

public class time_calculator {
    public String addTime(String startTime, String durationTime, String startingDay) {
        // Separate the start time into hours and minutes
        String[] startPieces = startTime.split(" ");
        String[] startParts = startPieces[0].split(":");
        int startHour = Integer.parseInt(startParts[0]);
        int startMinute = Integer.parseInt(startParts[1]);
        String end = startPieces[1];
    
        // Calculate 24-hour clock format
        if (end.equals("PM")) {
            startHour += 12;
        }
    
        // Separate the duration time into hours and minutes
        String[] durationParts = durationTime.split(":");
        int durationHour = Integer.parseInt(durationParts[0]);
        int durationMinute = Integer.parseInt(durationParts[1]);
    
        // Add hours and minutes
        int newHour = startHour + durationHour;
        int newMinute = startMinute + durationMinute;
    
        // Handle minute overflow
        if (newMinute >= 60) {
            int hoursAdd = newMinute / 60;
            newMinute -= hoursAdd * 60;
            newHour += hoursAdd;
        }
    
        // Handle hour overflow
        int daysAdd = 0;
        if (newHour >= 24) {
            daysAdd = newHour / 24;
            newHour -= daysAdd * 24;
        }
    
        // Determine AM or PM and return to 12-hour clock format
        if (newHour < 12) {
            end = "AM";
        } else {
            end = "PM";
            newHour -= 12;
        }
    
        // Handle 12:00 edge case
        if (newHour == 0) {
            newHour = 12;
        }
    
        // Handle next day or days later
        String daysLater = "";
        if (daysAdd > 0) {
            if (daysAdd == 1) {
                daysLater = " (next day)";
            } else {
                daysLater = " (" + daysAdd + " days later)";
            }
        }
    
        // Get day of the week if startingDay is provided
        String day = "";
        if (startingDay != null && !startingDay.isEmpty()) {
            String[] weekDays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
            int startDay = Arrays.asList(weekDays).indexOf(startingDay.toLowerCase().substring(0, 1).toUpperCase() + startingDay.toLowerCase().substring(1));
            int newDay = (startDay + daysAdd) % 7;
            day = ", " + weekDays[newDay];
        }
    
        // Format and return new time string
        return String.format("%d:%02d %s%s%s", newHour, newMinute, end, day, daysLater);
    }
    
}