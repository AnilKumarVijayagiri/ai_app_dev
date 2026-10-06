//STUDENT RESULT MANAGEMNET SYSTEM
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String name,course;
        int age,marks1,marks2,marks3,total;
        double average;
        char grade;
        boolean running=true;
        System.out.println("Enter student name: ");
        name=sc.nextLine();
        System.out.println("Enter age: ");
        age=sc.nextInt();
        sc.nextLine();
        System.out.println("ENter course: ");
        course=sc.nextLine();
        displayStudent(name,age,course);
        System.out.println("Enter Java marks: ");
        marks1=sc.nextInt();
        System.out.println("Enter SQL marks: ");
        marks2=sc.nextInt();
        System.out.println("Enter Dev marks: ");
        marks3=sc.nextInt();

        total=calculateTotal(marks1,marks2,marks3);
        average=calculateAverage(total);
        grade=calculateGrade(average);
        System.out.println("\n--Result");
        System.out.println("Total marks:"+total);
        System.out.println("Average: "+average);
        checkResult(marks1,marks2,marks3);
        System.out.println("Grade: "+grade);
        while(running)
            System.out.println("\n--Menu---");
            System.out.println("1. Display Student");
            System.out.println("2.Check age eleigibility");
            System.out.println("3.Exit");
    
            System.out.println("Enter your choice: ");
            int choice=sc.nextInt();
            if(choice==1){
                displayStudent(name,age,course);
            }
            else if (choice==2){
                if (age>=18){
                    System.out.println("Eligible: Adult");
                }
                    else{
                        System.out.println("Not eligible : Minor");
                    }
            }
            else if(choice==3){
                running=false;
                System.out.println("Thank you");
            }
            else{
                System.out.println("Invalid choice");
            }
        
    }
    public static void displayStudent(String name,int age,String course){
        System.out.println("\n--STudent Details--");
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
        System.out.println("COurse: "+course);
    }
    static int calculateTotal(int marks1,int marks2,int marks3){
        int total=marks1+marks2+marks3;
        return total;
    }
    static double calculateAverage(int total){
        double average=total/3.0;
        return average;
    }
    static void checkResult(int marks1,int marks2,int marks3){
        if(marks1>=35 && marks2>=35 && marks3>=35){
            System.out.println("Result:PASS");
        }
        else{
            System.out.println("Result:FAIL");
        }
    }
    static char calculateGrade(double average){
        if (average>=90){
            return 'A';
        }
        else if(average>=75){
            return 'B';
        }
        else if(average>=60){
            return 'C';
        }
        else if(average>=35){
            return 'D';
        }
        else{
            return 'F';
        }
    }
    






    
}