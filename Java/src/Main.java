import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.time.LocalDate;

// Abstract class for a person
abstract class Person {
    protected String name;
    protected int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

// Child class
class Child extends Person {
    private String group;
    private List<String> parentsContacts;
    private MedicalRecord medicalRecord;

    public Child(String name, int age, String group) {
        super(name, age);
        this.group = group;
        this.parentsContacts = new ArrayList<>();
        this.medicalRecord = new MedicalRecord();
    }

    public void addParentContact(String contact) {
        parentsContacts.add(contact);
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<String> getParentsContacts() {
        return parentsContacts;
    }

    public MedicalRecord getMedicalRecord() {
        return medicalRecord;
    }
}

// Employee class
class Employee extends Person {
    private String position;
    private double salary;

    public Employee(String name, int age, String position, double salary) {
        super(name, age);
        this.position = position;
        this.salary = salary;
    }

    public String getPosition() {
        return position;
    }

    public double getSalary() {
        return salary;
    }
}

// Medical record class
class MedicalRecord {
    private List<String> vaccinations;
    private List<String> allergies;

    public MedicalRecord() {
        this.vaccinations = new ArrayList<>();
        this.allergies = new ArrayList<>();
    }

    public void addVaccination(String vaccination) {
        vaccinations.add(vaccination);
    }

    public void addAllergy(String allergy) {
        allergies.add(allergy);
    }
}

// Singleton Kindergarten Registry
class KindergartenRegistry {
    private static KindergartenRegistry instance;
    private List<Child> children;
    private List<Employee> employees;

    private KindergartenRegistry() {
        children = new ArrayList<>();
        employees = new ArrayList<>();
    }

    public static synchronized KindergartenRegistry getInstance() {
        if (instance == null) {
            instance = new KindergartenRegistry();
        }
        return instance;
    }

    public void registerChild(Child child) {
        children.add(child);
    }

    public void registerEmployee(Employee employee) {
        employees.add(employee);
    }

    public int getTotalChildren() {
        return children.size();
    }

    public int getTotalEmployees() {
        return employees.size();
    }
}

// Prototype interface
public interface Prototype<T> {
    T clone();
}

// ChildProfile class implementing Prototype
public class ChildProfile implements Prototype<ChildProfile>, Cloneable {
    private String name;
    private int age;
    private String group;
    private List<String> parentsContacts;

    public ChildProfile(String name, int age, String group) {
        this.name = name;
        this.age = age;
        this.group = group;
        this.parentsContacts = new ArrayList<>();
    }

    @Override
    public ChildProfile clone() {
        try {
            ChildProfile clonedProfile = (ChildProfile) super.clone();
            clonedProfile.parentsContacts = new ArrayList<>(this.parentsContacts);
            return clonedProfile;
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException("Cloning error", e);
        }
    }

    public ChildProfile duplicateWithModifications(String newName, int newAge) {
        ChildProfile newProfile = this.clone();
        newProfile.name = newName;
        newProfile.age = newAge;
        return newProfile;
    }
}

// Enum for employee types
public enum EmployeeType {
    TEACHER, ASSISTANT, COOK, MEDICAL_STAFF
}

// Abstract Employee Factory
public abstract class EmployeeFactory {
    public abstract Employee createEmployee(String name, int age);

    public static Employee createEmployeeByType(EmployeeType type, String name, int age) {
        switch (type) {
            case TEACHER:
                return new Teacher(name, age);
            case ASSISTANT:
                return new Assistant(name, age);
            case COOK:
                return new Cook(name, age);
            case MEDICAL_STAFF:
                return new MedicalStaff(name, age);
            default:
                throw new IllegalArgumentException("Unknown employee type");
        }
    }
}

// Concrete Employee classes
class Teacher extends Employee {
    public Teacher(String name, int age) {
        super(name, age, "Teacher", 25000);
    }
}

class Assistant extends Employee {
    public Assistant(String name, int age) {
        super(name, age, "Assistant", 18000);
    }
}

class Cook extends Employee {
    public Cook(String name, int age) {
        super(name, age, "Cook", 20000);
    }
}

class MedicalStaff extends Employee {
    public MedicalStaff(String name, int age) {
        super(name, age, "Nurse", 22000);
    }
}

// Abstract Child Group class
public abstract class ChildGroup {
    protected List<Child> children = new ArrayList<>();
    protected int minAge;
    protected int maxAge;

    public void addChild(Child child) {
        if (child.getAge() >= minAge && child.getAge() <= maxAge) {
            children.add(child);
        }
    }
}

// Group factories
public class YoungGroupFactory implements GroupFactory {
    @Override
    public ChildGroup createGroup() {
        return new YoungGroup();
    }
}

public class MiddleGroupFactory implements GroupFactory {
    @Override
    public ChildGroup createGroup() {
        return new MiddleGroup();
    }
}

public class YoungGroup extends ChildGroup {
    public YoungGroup() {
        this.minAge = 2;
        this.maxAge = 3;
    }
}

public class MiddleGroup extends ChildGroup {
    public MiddleGroup() {
        this.minAge = 4;
        this.maxAge = 5;
    }
}

// Builder pattern for creating child objects
public class ChildBuilder {
    private String name;
    private int age;
    private String group;
    private List<String> parentsContacts;
    private MedicalRecord medicalRecord;

    public ChildBuilder() {
        this.parentsContacts = new ArrayList<>();
        this.medicalRecord = new MedicalRecord();
    }

    public ChildBuilder name(String name) {
        this.name = name;
        return this;
    }

    public ChildBuilder age(int age) {
        this.age = age;
        return this;
    }

    public ChildBuilder group(String group) {
        this.group = group;
        return this;
    }

    public ChildBuilder addParentContact(String contact) {
        this.parentsContacts.add(contact);
        return this;
    }

    public ChildBuilder addVaccination(String vaccination) {
        this.medicalRecord.addVaccination(vaccination);
        return this;
    }

    public Child build() {
        Child child = new Child(name, age, group);
        parentsContacts.forEach(child::addParentContact);
        return child;
    }
}

// Director for building standard child
public class ChildDirector {
    public Child createStandardChild(String name, int age) {
        return new ChildBuilder()
                .name(name)
                .age(age)
                .group("Middle Group")
                .addParentContact("Parent's Phone")
                .addVaccination("BCG")
                .build();
    }
}

// Resource Pool pattern for managing resources
public class ResourcePool {
    private List<Resource> available = new ArrayList<>();
    private List<Resource> inUse = new ArrayList<>();
    private int maxPoolSize;

    public ResourcePool(int initialSize, int maxPoolSize) {
        this.maxPoolSize = maxPoolSize;
        for (int i = 0; i < initialSize; i++) {
            available.add(createResource());
        }
    }

    private Resource createResource() {
        return new Resource(available.size() + inUse.size());
    }

    public synchronized Resource acquireResource() {
        if (available.isEmpty()) {
            if (inUse.size() < maxPoolSize) {
                available.add(createResource());
            } else {
                throw new RuntimeException("Max pool size exceeded");
            }
        }

        Resource resource = available.remove(0);
        inUse.add(resource);
        return resource;
    }

    public synchronized void releaseResource(Resource resource) {
        inUse.remove(resource);
        available.add(resource);
    }

    public static class Resource {
        private int id;
        private boolean inUse;

        public Resource(int id) {
            this.id = id;
            this.inUse = false;
        }

        public int getId() {
            return id;
        }
    }
}

// Adapter for External Medical System
public class ExternalMedicalSystem {
    public Map<String, Object> getChildMedicalHistory(String childId) {
        Map<String, Object> medicalHistory = new HashMap<>();
        medicalHistory.put("vaccinations", List.of("BCG", "Polio"));
        medicalHistory.put("allergies", List.of("Nuts"));
        return medicalHistory;
    }
}

public class MedicalRecordAdapter {
    private ExternalMedicalSystem externalSystem;

    public MedicalRecordAdapter(ExternalMedicalSystem externalSystem) {
        this.externalSystem = externalSystem;
    }

    public MedicalRecord getMedicalRecords(String childId) {
        Map<String, Object> externalRecords = externalSystem.getChildMedicalHistory(childId);
        MedicalRecord record = new MedicalRecord();
        List<String> vaccinations = (List<String>) externalRecords.get("vaccinations");
        List<String> allergies = (List<String>) externalRecords.get("allergies");

        vaccinations.forEach(record::addVaccination);
        allergies.forEach(record::addAllergy);
        return record;
    }
}

// Main application example
public class KindergartenApp {
    public static void main(String[] args) {
        KindergartenRegistry registry = KindergartenRegistry.getInstance();

        // Using the Builder pattern
        Child child1 = new ChildBuilder()
                .name("Alice")
                .age(3)
                .group("Young Group")
                .addParentContact("123-456-7890")
                .addVaccination("BCG")
                .build();

        registry.registerChild(child1);

        // Using the Prototype pattern
        ChildProfile profile = new ChildProfile("Bob", 4, "Middle Group");
        ChildProfile clonedProfile = profile.clone();
        System.out.println("Cloned Profile Name: " + clonedProfile.getName());

        // Using the Factory pattern
        Employee teacher = EmployeeFactory.createEmployeeByType(EmployeeType.TEACHER, "John", 30);
        registry.registerEmployee(teacher);

        // Demonstrating the use of Adapter pattern
        ExternalMedicalSystem externalSystem = new ExternalMedicalSystem();
        MedicalRecordAdapter adapter = new MedicalRecordAdapter(externalSystem);
        MedicalRecord medicalRecord = adapter.getMedicalRecords("Alice");
        System.out.println("Medical Record for Alice: " + medicalRecord);
    }
}
