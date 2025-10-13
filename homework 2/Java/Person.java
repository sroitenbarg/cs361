public class Person {
    private int age;
    private String lastName, firstName;

    public Person(String firstName, String lastName, int age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public int compareTo(Person other) {
        return this.age - other.age;
    }
}
